import subprocess
import os

def create_requirements_file():
    """
    Generates a requirements.txt file listing all installed packages
    in the current Python environment, excluding Windows-specific packages.
    The requirements.txt file is placed within a 'src_files' directory.
    """
    # Define the directory and file path
    directory = 'src_files'
    requirements_file = os.path.join(directory, 'requirements.txt')
    
    # Ensure the directory exists
    os.makedirs(directory, exist_ok=True)
    
    try:
        # Run pip freeze to capture the output
        installed_packages = subprocess.run(['pip', 'freeze'], check=True, text=True, capture_output=True).stdout
        
        # Filter out Windows-specific packages
        filtered_packages = []
        for package in installed_packages.split('\n'):
            # Combine conditions to exclude Windows-specific packages
            if 'pywin32' not in package and 'pypiwin32' not in package:
                filtered_packages.append(package)
        
        # Write the filtered output to requirements.txt in the 'src_files' directory
        # This overwrites the file if it already exists
        with open(requirements_file, 'w') as file:
            file.write('\n'.join(filtered_packages))
        
        print(f"'{requirements_file}' file has been created successfully in the '{directory}' directory, excluding Windows-specific packages.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to generate '{requirements_file}': {e}")

if __name__ == '__main__':
    create_requirements_file()