class Wire(object):
    """
    The value of a Wire can be:
    1. Left empty: which means that it will take the value of whatever that
        is driven into it by the output, or
    2. Another wire, or
    3. Bit value 1 or 0
    """

    _count = 0

    def __init__(self, value=None, label=None):
        assert isinstance(value, Wire) or value in (0, 1, None)

        self.id = Wire._count
        self._value = value
        self._label = label
        Wire._count += 1

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        assert isinstance(value, Wire) or value in (0, 1, None)

        self._value = value

    @classmethod
    @property
    def count(clf):
        return clf._count

    @classmethod
    def reset_count(clf):
        clf._count = 0

    def __repr__(self):
        return self._label if self._label else 'Wire'
