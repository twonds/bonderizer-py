import os

import fire


class Bonderizer(object):
    """
    Given code that defines an interface with a consumer and producer
    generate a composable service workload runtime.
    """

    def new(self, name:str):
        """
        Create a new project given a name
        """
        # XXX - how do we document name
        print(f"Created {name}")
        

    def cli(self):
        """
        Generate CLI code for a project's runtime
        """


    def grpc(self):
        """
        Generate gRPC code for a project's runtime
        """

    def protobuf(self):
        """
        Generate a protobuf from a project's code
        """

    def openapi(self):
        """
        Generate openapi code and framework for a project's runtime
        """


def cli():
    fire.Fire(Bonderizer)


if __name__ == '__main__':
    cli()
