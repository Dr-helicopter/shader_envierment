import os
import subprocess
import sys
import venv
from pathlib import Path


def create_and_run_venv(venv_dir, script, *script_args):
    """
    starts a virtual environment, and runs a compile script with an argument.

    Parameters:
    - fule: Path to the file to compile.
    - x,y: Argument to pass to the compile script.
    """

    # Ensure the virtual environment directory exists
    venv_path = Path(venv_dir)
    venv_path.mkdir(parents=True, exist_ok=True)

    # Create the virtual environment
    venv.create(venv_path, with_pip=True)
    print(f"Virtual environment created at {venv_path}")

    # Determine the path to the Python interpreter in the venv
    venv_python = venv_path / 'bin' / 'python' if os.name != 'nt' else\
        venv_path / 'Scripts' / 'python.exe'

    # Run the script with the argument
    subprocess.run([venv_python, script, *script_arg], check=True)
    print("cimpile Script executed successfully.")

    print("Virtual environment terminated")


if __name__ == "__main__":

    venv_dir = 'venv'
    script_path = 'compile_shader.py'
    script_arg = sys.argv[1:]
    print(script_arg)
    if len(sys.argv) == 2:
        create_and_run_venv(venv_dir, script_path, *script_arg)
    elif len(sys.argv) == 4:
        create_and_run_venv(venv_dir, script_path, *script_arg)
