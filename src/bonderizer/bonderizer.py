"""
   Copyright 2023 Christopher Zorn

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""
import os


from cookiecutter.main import cookiecutter

import fire


import util


SCRIPT_DIR=os.path.dirname(__file__)


class Bonderizer(object):
    """
    Given code that defines an interface with a consumer and producer
    generate a composable service workload runtime.
    """

    def new(self, name:str, output_dir:str = os.getcwd()):
        """
        Create a new project given a name.
        """
        # XXX - Use other scaffolders other than cookiecutter. composability is key!
        # XXX - You can use build tools for creating new projects too
        # Create project from the cookiecutter-pypackage/ template
        cookiecutter("gh:twonds/bonderizer-hello-py-cookiecutter",
                     no_input=True, output_dir=output_dir,
                     extra_context={'project_name': name})
        print(f"Created {name}")


    def cli(self, project_interface: str):
        """
        Generate CLI code for a project's runtime
        """
        print(project_interface)
        util.install_interface_dependencies(project_interface)
        # Read and import the interface
        interface = util.import_interface(project_interface)
        print(interface, dir(interface))
        # Find the producer class


    def grpc(self, project_dir: str = os.getcwd()):
        """
        Generate gRPC code for a project's runtime
        """
        # Find the producer class

    def protobuf(self, project_dir: str = os.getcwd()):
        """
        Generate a protobuf from a project's code
        """

    def openapi(self, project_dir: str = os.getcwd()):
        """
        Generate openapi code and framework for a project's runtime
        """


def cli():
    fire.Fire(Bonderizer)


if __name__ == '__main__':
    cli()
