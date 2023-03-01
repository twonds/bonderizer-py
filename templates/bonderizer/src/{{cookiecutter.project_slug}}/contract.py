# This will be the definition of a contract from consumer to producer
# It is the shared code to test a contract or ensure consumers and producers
# adhere their contract and do not break it
#
# Test can and should be outside this code but use this code to execute tests
#
#
# The designer or creator should ask three questions about the contract
# What does the contract expect?
# What does the contract guarantee?
# What does the contract maintain?
#
# It should contain the following pieces of information:
# Acceptable and unacceptable input values or types, and their meanings
# Return values or types, and their meanings
# Error and exception condition values or types that can occur, and their meanings
# Side effects
# Preconditions
# Postconditions
# Invariants
# Performance guarantees, e.g. for time or space used,
# Can the performance contract map to deployment resources for CPU and memory?
# Can the performance contract map to creating SLO/SLA monitors etc?
#
from zope.interface import verify

from {{ cookiecutter.project_slug }}.consumer.greeter import Greeter
from {{ cookiecutter.project_slug }}interface import IGreeter

# XXX - Should the default just have a liveliness and readiness check?
#       That should be done instead of hello etc
def say_hello(name: str) -> str:
    g = Greeter()
    verify.verifyObject(IGreeter, g)

    message = g.say_hello(name)

    assert type(message) is str

