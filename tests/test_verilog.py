from nose import with_setup

from .test_utils import reset_counts

@with_setup(reset_counts,)
def test_generate():
    pass
