# Requirements File Generator

This script automates the creation of a `requirements.txt` file, which lists all packages installed in the current Python environment. It's designed to exclude Windows-specific packages, making the `requirements.txt` file more portable across different operating systems. The generated file is placed within a `src_files` directory.

## Features

- **Automatic Extraction**: Automatically extracts the list of installed Python packages using `pip freeze`.
- **Windows-Specific Exclusion**: Filters out packages that are specific to Windows environments, such as `pywin32` and `pypiwin32`.
- **Directory Management**: Ensures that the `src_files` directory exists and places the `requirements.txt` file within this directory.

## Usage

To use this script, simply run it from the command line in your Python environment:

```bash
python create_requirements_file.py
