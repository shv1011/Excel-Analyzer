from cx_Freeze import setup, Executable
import sys

# Dependencies
build_exe_options = {
    "packages": ["flask", "pandas", "jinja2", "os"],  # Add any other modules you are using
    "include_files": ["templates/", "static/", "requirements.txt"],  # Include important folders and files
    "excludes": ["tkinter"]  # Exclude any unnecessary libraries
}

# Base option for console vs GUI application
base = None
if sys.platform == "win32":
    base = "Console"

# Executable file configuration
executables = [
    Executable(
        script="app.py",  # Replace with your main script
        base=base,
        target_name="ExcelAnalyzer.exe"  # Name of the output executable
    )
]

# Setup configuration
setup(
    name="ExcelAnalyzer",
    version="1.0",
    description="A Flask-based Excel Analysis Tool",
    options={"build_exe": build_exe_options},
    executables=executables
)
