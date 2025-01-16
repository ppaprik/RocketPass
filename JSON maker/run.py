import os
import sys
import subprocess


#----------------------------------------------------------------------------------------------------
# VARIABLES

ENV_NAME = ".env"
REQUIREMENTS_FILE = "requirements.txt"
APP_SCRIPT = "app.py"


#----------------------------------------------------------------------------------------------------
# FUNCTIONS

def getEnvPython(env_name: str) -> str: 
    """
        Returns the path to the virtual environment's Python interpreter.
    """ 
    if os.name == "nt": 
        return os.path.join(env_name, "Scripts", "python.exe")
    else:
        return os.path.join(env_name, "bin", "python")


def createEnv(env_name: str) -> None:
    """
        Create a virtual environment if it doesn't exist.
    """
    if not os.path.exists(env_name):
        print("Creating virtual environment...")
        subprocess.run([sys.executable, "-m", "venv", env_name], check=True)
    else:
        print("Virtual environment already exists.")


def installRequirements(env_name: str, requirements_file: str, env_path: str) -> None:
    """
        Install requirements from a requirements file.
    """
    print("Installing requirements...")
    subprocess.run([env_path, "-m", "pip", "install", "-r", requirements_file], check=True)
    print("Requirements installed.")


def run(app_script: str, env_path: str) -> None:
    """
        Run the app script and terminate this script once app.py has been launched.
    """
    try:
        print("Running app...")
        subprocess.run([env_path, app_script], check=True)
    except subprocess.CalledProcessError as error:
        print(f"Error running app: {error}")

    print("Exiting...")
    sys.exit()


def main():
    createEnv(ENV_NAME)
    env_path = getEnvPython(ENV_NAME)
    installRequirements(ENV_NAME, REQUIREMENTS_FILE, env_path)
    run(APP_SCRIPT, env_path)


#----------------------------------------------------------------------------------------------------
# MAIN

if __name__ == '__main__':
    # main()

    # for testing
    run(APP_SCRIPT, getEnvPython(ENV_NAME))