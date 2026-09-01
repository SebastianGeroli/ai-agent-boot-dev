import os


def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        absolute_directory = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(absolute_directory, file_path))
        valid_target_dir = os.path.commonpath([absolute_directory, target_file]) == absolute_directory
        if not valid_target_dir:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        if os.path.isdir(target_file):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
    
        os.makedirs(os.path.dirname(target_file), exist_ok=True)
        with open(target_file, mode="w") as file:
            file.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {e}"

schema_write_file = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "Writes a file with the contents provided.",
        "parameters": [{
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": "Directory path to list files from, relative to the working directory (default is the working directory itself)",
                },
            },
            
        },
{
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": "Directory path to list files from, relative to the working directory (default is the working directory itself)",
                },
            },
            
        }
        ],
        
    },
}