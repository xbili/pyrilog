class Wire(object):
    """Wire encapsulates a connection in the Wallace tree."""

    _count = 0

    def __init__(self, column):
        self.id = Wire._count
        self.column = column

        Wire._count += 1

    @classmethod
    def get_count(clf):
        return clf._count

    @classmethod
    def reset_count(clf):
        clf._count = 0
