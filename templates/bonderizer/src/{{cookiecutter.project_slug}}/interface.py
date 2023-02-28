# There needs to be a way to bridge or provide a client or agent from
# consumer and producer. This has to be interchangable.
# There needs to be a way to bridge or provide a client or agent from
# consumer and producer. This has to be interchangable.
# Is an agent interface class the way to go?
# https://opensource.com/article/19/9/zopeinterface-python-package
from zope.interface import Interface

# Is this overkill? We want an interface and possibly a registry.
# https://zopeinterface.readthedocs.io/en/latest/adapter.html
#
# Can that be used to create a connection between consumer and producer?

# What goes in the python module? How do we generalize that?
#
class IGreeter(zope.interface.Interface):
    """
    A hello world greeter service
    """

    def say_hello(name: str) -> str:
        """
        """
