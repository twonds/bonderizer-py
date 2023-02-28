import zope.interface

from hello.interface import IGreeter
from hello.api import Greeter


@zope.interface.implementer(IGreeter)
class Greeter:

    def __init__(self):
        self.api = Greeter()

    def say_hello(name: str) -> str:
        """ """
        self.api.say_hello(name)
