from abc import ABC, abstractmethod

class Entity(ABC):
    """
    This abstract class represents a single entity in a hardware design.
    e.g. a full adder, half adder, AND gate etc.

    All entities will have inputs and outputs.
    """

    @property
    @abstractmethod
    def inputs(self):
        pass

    @property
    @abstractmethod
    def outputs(self):
        pass
