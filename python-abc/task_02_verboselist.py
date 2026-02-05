#!/usr/bin/python3
"""VerboseList module."""


class VerboseList(list):
    """List subclass with operation notifications."""

    def append(self, item):
        """Append item and print notification."""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """Extend list and print notification."""
        super().extend(iterable)
        print(f"Extended the list with [{len(iterable)}] items.")

    def remove(self, item):
        """Remove item and print notification."""
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Pop item and print notification."""
        item = super().pop(index)
        print(f"Popped [{item}] from the list.")
        return item
