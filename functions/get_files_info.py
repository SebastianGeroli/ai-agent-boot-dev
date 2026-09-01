import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
    absolute_directory = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(absolute_directory, directory))
    valid_target_dir = os.path.commonpath([absolute_directory, target_dir]) == absolute_directory
    if not valid_target_dir:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(target_dir):
        return f'Error: "{directory}" is not a directory'
    try:
        dir_contents = os.listdir(target_dir)
        lines = []
        for content in dir_contents:
            path = os.path.join(target_dir, content)
            lines.append(f"- {content}: file_size={os.path.getsize(path)}, is_dir={os.path.isdir(path)}")
        return "\n".join(lines)
    except Exception as e:
        return f"Error: {e}"
