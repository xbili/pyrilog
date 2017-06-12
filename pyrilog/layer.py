class Layer(object):
    """Layer of wires in a PPRT."""

    _count = 0

    def __init__(self, columns=None):
        self.id = Layer._count
        self._columns = columns if columns != None else 0

        # Dictionary to contain all the wires
        #   Key: Column position
        #   Value: Wires in that column
        self._wires = {}

        for i in range(0, self._columns):
            self._wires[i] = []

        Layer._count += 1

    def get_wires(self, col=None):
        """Returns the list of wires in a column"""

        if col != None:
            return self._wires.get(col)

        res = []
        for wires in self._wires.values():
            for wire in wires:
                res.append(wire)

        return res

    def add_wire(self, wire):
        """Adds a wire into the layer"""

        column = wire.column

        if self._wires.get(column, None) == None:
            self._wires[column] = []
            self._columns += 1

        self._wires[column].append(wire)

    def get_rows(self):
        """Returns the number of rows this layer has"""

        return max([len(wires) for wires in self._wires.values()])

    def get_columns(self):
        """Returns the number of columns this layer has"""

        return self._columns

    def reset_count():
        Layer._count = 0
