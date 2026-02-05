#!/usr/bin/python3
"""Dragon with swim/fly capabilities via mixins"""


class SwimMixin:
    """Mixin adding swim method"""

    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """Mixin adding fly method"""

    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon combining swim, fly, and roar"""

    def roar(self):
        print("The dragon roars!")


draco = Dragon()