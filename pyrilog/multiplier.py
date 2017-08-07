from pyrilog.core.full_adder import FullAdder
from pyrilog.core.half_adder import HalfAdder
from pyrilog.core.wire import Wire
from pyrilog.core.gates import And, Not
from pyrilog.utils import chunks, result_bit_width


def create(multiplier, multiplicand, width, signed=True):
    """
    Creates a tree multiplier with a Wallace Partial Product Reduction
    Tree (PPRT).

    :type width: Int
    :type signed: Bool
    :rtype: List[List[Wire]], List[Entity]
    """
    partials, input_entities = _create_partial_products(multiplier, multiplicand)
    penultimate, reduction_entities = _reduce_partial_products(partials)
    output, cpa_entities = _carry_propagate(penultimate)

    return output, input_entities + reduction_entities + cpa_entities


def _create_partial_products(multiplier, multiplicand):
    """
    Combine the multiplier and multiplicand into partial products in separate
    layers in order to group them together with our Wallace strategy later.

    The handling of signed multiplication is in this step, where we utilize
    Modified Baugh-Wooley method to compensate for the negatively weighted
    bits in the PPRT.

    :type multiplier: List[Wire]
    :type multiplicand: List[Wire]
    :rtype: List[List[Wire]], List[Entity]
    """

    # We assume that one is longer than the other
    assert len(multiplier) == len(multiplicand)

    entities = []
    wires = [[] for _ in range(len(multiplier) * 2)]
    compensation = [[] for _ in range(len(multiplier) * 2)]

    # 'AND' related bits together
    for col_x, x in enumerate(multiplier[:-1]):
        for col_a, a in enumerate(multiplicand):
            label = 'a{}x{}'.format(col_a, col_x)
            out = Wire(label=label)

            # Negate the last product
            if col_a == len(multiplicand) - 1:
                out2 = Wire(label=label)
                product = And(a, x, out)
                negate = Not(out, None, out2)

                # Compensate for negating one bit
                compensation[col_x + col_a] += [-1]

                entities += [product, negate]
                wires[col_x + col_a] += [out2]
            else:
                entities += [And(a, x, out)]
                wires[col_x + col_a] += [out]

    # The final layer has every partial product negated except for the
    # last
    for col_a, a in enumerate(multiplicand):
        label = 'a{}x{}'.format(col_a, len(multiplier) - 1)

        out = Wire(label=label)

        if col_a == len(multiplicand) - 1:
            entities += [And(a, multiplier[-1], out)]
            wires[col_a + len(multiplier) - 1] += [out]
        else:
            out2 = Wire(label=label)
            product = And(a, multiplier[-1], out)
            negate = Not(out, None, out2)

            # Compensate for negating the bit
            compensation[col_a + len(multiplier) - 1] += [-1]

            entities += [product, negate]
            wires[col_a + len(multiplier) - 1] += [out2]

    return wires, entities, compensation


def compensate(wires, compensation):
    """
    Compensate negatively weighted bits in 2s complement representation
    of the partial products.
    """

    # Group compensation bits together by moving them one column up
    # until all the way to the left
    for idx, col in enumerate(compensation):
        for chunk in chunks(col, 2):
            # The last column does not need to be negated again
            if idx < len(compensation) - 1:
                compensation[idx + 1] += [-1]

            if len(chunk) == 1:
                wires[idx] += [Wire(value=1, label='1')]

    return wires


def _reduce_partial_products(partials):
    """
    Reduce our partial products into a list of entities. We group every
    column's bit in chunks of 3 / 2 bits at a time.

    :type partials: List[List[Wire]]
    :rtype: List[List[Wire]], List[Entity]
    """

    bit_width = len(partials)
    result_width = result_bit_width(max(map(len, partials)), bit_width)
    entities = []

    # Transform the partial products
    while max(map(len, partials)) > 2:
        next_layer = [[] for _ in range(result_width)]

        for idx, column in enumerate(partials):
            bits = [item for item in column if item != None]
            # Group chunks of bits into a full adder
            for chunk in chunks(bits, 3):
                if len(chunk) == 1:
                    next_layer[idx] += chunk
                    continue

                s = Wire()
                c = Wire()

                if len(chunk) == 3:
                    in_1, in_2, in_3 = chunk

                    fa = FullAdder(in_1, in_2, in_3, s, c)
                    entities += [fa]
                elif len(chunk) == 2:
                    in_1, in_2 = chunk
                    ha = HalfAdder(in_1, in_2, s, c)
                    entities += [ha]

                next_layer[idx] += [s]
                if idx < result_width - 1:
                    next_layer[idx + 1] += [c]

        partials = next_layer

    return partials, entities


def _carry_propagate(columns):
    """
    Creates the Carry Propagate Adder at the end of the partial product
    reduction tree given 2 layers.

    :type columns: List[List[Wire]]
    :rtype: List[Wire], List[Entity]
    """

    # We assume that the max number of bits in each column is 2.
    assert max(map(len, columns)) == 2

    res, entities = [], []

    carry = None
    for column in columns:
        if len(column) == 0:
            continue

        if carry:
            s, c = Wire(), Wire()
            if len(column) == 2: # Combine 2 bits and carry with FA
                adder = FullAdder(column[0], column[1], carry, s, c)
            else: # Combine 1 bit and carry with HA
                adder = HalfAdder(column[0], carry, s, c)
            res += [s]
            entities += [adder]
            carry = c
        else:
            if len(column) == 2: # Combine two bits into with a single HA
                s, c = Wire(), Wire()
                adder = HalfAdder(column[0], column[1], s, c)
                entities += [adder]
                carry = c
                res += [s]
            else: # Add the wire into result
                res += [column[0]]

    return res, entities
