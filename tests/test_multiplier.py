from pprint import pprint

from nose import with_setup

from pyrilog.core.wire import Wire
from pyrilog.multiplier import (
    create,
    _create_partial_products,
    _reduce_partial_products,
)

from .test_utils import reset_counts


@with_setup(reset_counts,)
def test_4x4_partial_products():
    assert_NxN_partial_products(4)


@with_setup(reset_counts,)
def test_16x16_partial_products():
    assert_NxN_partial_products(16)


@with_setup(reset_counts,)
def test_32x32_partial_products():
    assert_NxN_partial_products(32)


@with_setup(reset_counts,)
def test_4x4_pprt():
    assert_NxN_pprt(4)


@with_setup(reset_counts,)
def test_create():
    wires, entities = create(4)

    # TODO: Figure out the test case for this.


def assert_NxN_pprt(width):
    multiplier = [Wire()] * width
    multiplicand = [Wire()] * width

    wires, entities = _create_partial_products(multiplier, multiplicand)
    pprt_wires, pprt_entities = _reduce_partial_products(wires)

    # TODO: Figure out the test case for this.


def assert_NxN_partial_products(width):
    multiplier = [Wire()] * width
    multiplicand = [Wire()] * width

    wires, entities = _create_partial_products(multiplier, multiplicand)

    _assert_multiplier(width, wires, entities)


def _assert_multiplier(width, wires, entities):
    expected_wire_count = [width for _ in range(width)]
    expected_wire_count[0] += 1
    expected_wire_count[-1] += 1

    # Number of layers should be equals to the width of the multiplier
    assert len(wires) == width

    for idx, layer in enumerate(wires):
        bits = len([item for item in layer if item != None])
        assert bits == expected_wire_count[idx]

    assert len(entities) == width ** 2 + 2 * (width - 1)
