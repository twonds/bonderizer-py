import zope

from hello.interface import IGreeterProducer


@zope.interface.implementer((IGreeterProducer)
class Greeter:

    def say_hello(name: str) -> str:
        """ """
        return f"Hello {name}"
