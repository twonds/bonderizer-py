import fire


class Bonderizer(object):
    """
    Bonds run time code or framework with a simple
    interface and consumer and producer. This needs work.
    """

    def new(self):
        """
        Create a new project
        """

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
