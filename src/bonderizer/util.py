import importlib.util
import os
import sys
import subprocess

from pathlib import Path


def import_interface(file_path):
    # XXX - how do we get this right?
    module_name = 'interface'
    print(file_path)
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


def install_interface_dependencies(project_interface_path: str):
    # Install dependencies
    project_interface_path = Path(project_interface_path)
    print(project_interface_path.parts)
    call_args = [sys.executable, '-m', 'pip', 'install', '-U']
    requirements_path = os.path.join(project_interface_path.parts[0], 'requirements.txt')
    print(requirements_path)
    if os.path.exists(requirements_path):
        call_args += ['-r', requirements_path]
    else:
        call_args.append(project_interface_path.parts[0])
    subprocess.check_call(call_args)

