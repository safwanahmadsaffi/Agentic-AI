#!/usr/bin/env python3
"""
Auto-formatting script for Python code.
Run this script to automatically format your Python files.
"""

import subprocess
import sys
import os

def run_command(command, description):
    """Run a command and handle errors."""
    print(f"Running {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        if result.stdout:
            print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed:")
        print(f"Error: {e.stderr}")
        return False

def main():
    """Main formatting function."""
    print("🚀 Starting code formatting...")
    
    # Get the current directory
    current_dir = os.getcwd()
    print(f"Working directory: {current_dir}")
    
    # Format with black
    black_success = run_command(
        f'python -m black "{current_dir}"',
        "Black code formatter"
    )
    
    # Sort imports with isort
    isort_success = run_command(
        f'python -m isort "{current_dir}"',
        "Import sorting with isort"
    )
    
    # Auto-format with autopep8
    autopep8_success = run_command(
        f'python -m autopep8 --in-place --recursive --aggressive --aggressive "{current_dir}"',
        "Auto-formatting with autopep8"
    )
    
    print("\n" + "="*50)
    if all([black_success, isort_success, autopep8_success]):
        print("🎉 All formatting tools completed successfully!")
    else:
        print("⚠️  Some formatting tools encountered errors. Check the output above.")
    
    print("="*50)

if __name__ == "__main__":
    main()
