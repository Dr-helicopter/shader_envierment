import os
import subprocess
import venv
from pathlib import Path


DEPENDENCIES = [
    "numpy",
    "glfw",
    "PyOpenGl",
]


def setup_venv(venv_dir):
    """
    Sets up a virtual environment and installs predefined dependencies.

    Parameters:
    - venv_dir: Directory for the virtual environment.
    """
    venv_path = Path(venv_dir)
    venv_python = venv_path / 'bin' / 'python' if os.name != 'nt' else\
        venv_path / 'Scripts' / 'python.exe'

    if not venv_path.exists():
        # Create the virtual environment if it doesn't exist
        venv.create(venv_path, with_pip=True)
        print(f"Virtual environment created at {venv_path}")
    else:
        print(f"Virtual environment already exists at {venv_path}")

    # Upgrade pip
    subprocess.run([venv_python, '-m', 'pip', 'install', '--upgrade', 'pip'],
                   check=True)
    print("Pip upgraded.")

    # Install predefined dependencies
    print(f"Installing dependencies: {', '.join(DEPENDENCIES)}...")
    subprocess.run([venv_python, '-m', 'pip', 'install', *DEPENDENCIES],
                   check=True)

    print("Dependencies installed.")

    print("Setup complete. Activate the virtual \
            environment to start using it.")


if __name__ == "__main__":
    venv_dir = "venv"
    setup_venv(venv_dir)
