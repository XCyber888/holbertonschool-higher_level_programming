#!/usr/bin/python3
"""Module for Dragon and its Mixins."""


class SwimMixin:
    """Mixin to add swimming behavior."""
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """Mixin to add flying behavior."""
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon class combining swimming and flying abilities."""
    def roar(self):
        print("The dragon roars!")
