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
    multiplier = [Wire()] * 4
    multiplicand = [Wire()] * 4

    wires, entities = create(multiplier, multiplicand, 4)

    # TODO: Figure out the test case for this.


def assert_NxN_pprt(width):
    multiplier = [Wire()] * width
    multiplicand = [Wire()] * width

    wires, entities, compensation = _create_partial_products(multiplier, multiplicand)
    pprt_wires, pprt_entities = _reduce_partial_products(wires)

    # TODO: Figure out the test case for this.


def assert_NxN_partial_products(width):
    multiplier = [Wire()] * width
    multiplicand = [Wire()] * width

    wires, entities, compensation = _create_partial_products(multiplier, multiplicand)

    _assert_multiplier(width, wires, entities)


def _assert_multiplier(width, wires, entities):
    assert len(entities) == width ** 2 + 2 * (width - 1)
