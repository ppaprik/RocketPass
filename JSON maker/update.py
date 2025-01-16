import os
import subprocess


#----------------------------------------------------------------------------------------------------
# VARIABLES

# Define the environment name and the path to your requirements.txt and app.py
ENV_NAME = ".env"
REQUIREMENTS_FILE = "requirements.txt"
APP_SCRIPT = "app.py"


#----------------------------------------------------------------------------------------------------
# FUNCTIONS

def get_env_python(env_name):
    """
        Returns the path to the virtual environment's Python interpreter.
        """
    if os.name == "nt":
        return os.path.join(env_name, "Scripts", "python.exe")
    return os.path.join(env_name, "bin", "python")


def update_dependencies(env_path, requirements_file):
    """
        Updates all packages except those with specified versions.
    """
    
    print("Upgrading pip...")
    subprocess.run([env_path, "-m", "pip", "install", "--upgrade", "pip"], check=True)
    
    print("Updating dependencies...")
    
    # Get the list of packages with fixed versions
    specified_versions = []
    with open(requirements_file, 'r') as file:
        for line in file:
            if "==" in line:
                specified_versions.append(line.strip())
    
    # Get the list of outdated packages
    result = subprocess.run([env_path, "-m", "pip", "list", "--outdated", "--format=freeze"], capture_output=True, text=True)
    outdated_packages = result.stdout.splitlines()

    # Update packages what are outdated and not fixed
    for package_info in outdated_packages:
        package_name = package_info.split("==")[0]  # Get the package name
        should_skip = False

        for spec in specified_versions:
            if package_name in spec:  # Check if the package has a fixed version
                should_skip = True
                break

        if should_skip:
            print(f"Skipping {package_name} (fixed version specified).")
            continue
        
        try:
            print(f"Updating {package_name}...")
            subprocess.run([env_path, "-m", "pip", "install", "--upgrade", package_name], check=True)
        except subprocess.CalledProcessError as error:
            print(f"Error updating {package_name}: {error}")
            continue
    
    print("Dependencies updated successfully.")
    

def main():
    env_path = get_env_python(ENV_NAME)
    update_dependencies(env_path, REQUIREMENTS_FILE)


#----------------------------------------------------------------------------------------------------
# MAIN

if __name__ == "__main__":
    main()