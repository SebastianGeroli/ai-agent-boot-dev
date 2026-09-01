import os

def get_file_content(working_directory: str, file_path: str) -> str:
    absolute_directory = os.path.abspath(working_directory)
    target_file = os.path.normpath(os.path.join(absolute_directory, file_path))
    valid_target_dir = os.path.commonpath([absolute_directory, target_file]) == absolute_directory
    if not valid_target_dir:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(target_file):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    try:
        file = open(target_file)
        MAX_CHARS = 10000
        content = file.read(MAX_CHARS)
        # After reading the first MAX_CHARS...
        if file.read(1):
            content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
        return content
    except Exception as e:
        return f"Error: {e}"
