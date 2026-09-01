import os
import subprocess


def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    try:
        absolute_directory = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(absolute_directory, file_path))
        valid_target_dir = os.path.commonpath([absolute_directory, target_file]) == absolute_directory
        if not valid_target_dir:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_file):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", target_file]
        if args:
            command.extend(args)
        result = subprocess.run(
            command,
            cwd=absolute_directory,
            capture_output=True,
            text=True,timeout=30
        )
        output:list[str]=[]
        if result.returncode != 0:
            output.append(f"Process exited with code {result.returncode}")
        if result.stdout == None and result.stderr == None:
            output.append("No output produced")
        if result.stdout:
            output.append(f"\nSTDOUT: {result.stdout}")
        if result.stderr:
            output.append(f"\nSTDERR: {result.stderr}")
        return "\n".join(output)
    except Exception as e:
        return f"Error: executing Python file: {e}"
    
