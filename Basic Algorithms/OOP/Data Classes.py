# Creating immutable data classes

from dataclasses import dataclass


@dataclass(frozen=True)  # TODO: "The "frozen" parameter makes the class immutable
class ImmutableClass:
    value1: str = "Value 1"
    value2: int = 0

    def some_func(self, new_val):
        self.value2 = new_val


obj = ImmutableClass()
print(obj.value1)

# TODO: attempting to change the value of an immutable class throws an exception
# obj.value1 = "Another Value"

# TODO: even functions within the class can't change anything
obj.some_func("Blah")