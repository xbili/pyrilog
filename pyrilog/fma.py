from pyrilog import multiplier
from pyrilog.core.wire import Wire
from pyrilog.utils import result_bit_width


def create(width, size, cpa=True, signed=True):
    # Generate all the partial products
    inputs, entities = [], []

    res_width = result_bit_width(size, width * 2)
    partials = [[] for _ in range(res_width)]
    compensation = [[] for _ in range(res_width)]

    for i in range(size):
        multiplier_in = [Wire(label='a{}{}'.format(i, j)) for j in range(width)]
        multiplicand_in = [Wire(label='b{}{}'.format(i, j)) for j in range(width)]

        inputs += [multiplier_in, multiplicand_in]

        product_partial, product_entities, product_compensation =\
            multiplier._create_partial_products(
                multiplier_in,
                multiplicand_in,
            )

        for idx, col in enumerate(product_partial):
            partials[idx] += col
        for idx, col in enumerate(product_compensation):
            compensation[idx] += col
        entities += product_entities

    # Compensate negatively weighted bits
    partials = multiplier.compensate(partials, compensation)

    # Reduce partials
    penultimate, reduction_entities = multiplier._reduce_partial_products(partials)

    output, cpa_entities = multiplier._carry_propagate(penultimate)

    return inputs, output, entities + reduction_entities + cpa_entities
