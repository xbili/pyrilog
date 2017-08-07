from math import log2, floor

def chunks(l, n):
    """
    Yields chunks from a list of size n.

    Reference:
    https://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks
    """
    for i in range(0, len(l), n):
        yield l[i:i + n]

def result_bit_width(k, n):
    """Returns the result bit width for k n-bit operands."""
    return n + floor(log2(k))
