from pyrilog import multiplier
from pyrilog.core.wire import Wire


def create(width, size, cpa=True, signed=True):
    # Generate all the partial products
    inputs, partials, entities = [], [], []

    for i in range(size):
        multiplier_in = [Wire() for _ in range(width)]
        multiplicand_in = [Wire() for _ in range(width)]

        inputs += [multiplier_in, multiplicand_in]

        product_partial, product_entities = multiplier._create_partial_products(
            multiplier_in,
            multiplicand_in,
        )

        partials += product_partial
        entities += product_entities

    # Reduce partials
    penultimate, reduction_entities = multiplier._reduce_partial_products(partials)

    # Carry Propagate Adder
    if cpa:
        output, cpa_entities = multiplier._carry_propagate(penultimate)

    return inputs, output, entities + reduction_entities + cpa_entities
