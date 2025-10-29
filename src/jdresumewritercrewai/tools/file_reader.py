from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import json
import os


class FileReadInput(BaseModel):
    """Input schema for FileReadTool."""
    file_path: str = Field(..., description="The path to the file to read")


class FileReadTool(BaseTool):
    name: str = "Read File Content"
    description: str = (
        "Reads and returns the content of a file from the local filesystem. "
        "Supports text files, JSON files, and other readable formats. "
        "Useful for loading candidate profiles, job descriptions, or configuration data."
    )
    args_schema: Type[BaseModel] = FileReadInput

    def _run(self, file_path: str) -> str:
        """Read content from a file."""
        try:
            # Check if file exists
            if not os.path.exists(file_path):
                return f"Error: File '{file_path}' does not exist."
            
            # Read the file
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # If it's a JSON file, pretty-print it
            if file_path.endswith('.json'):
                try:
                    data = json.loads(content)
                    content = json.dumps(data, indent=2)
                except json.JSONDecodeError:
                    pass  # Return as-is if not valid JSON
            
            return content
        
        except PermissionError:
            return f"Error: Permission denied accessing '{file_path}'."
        except Exception as e:
            return f"Error reading file: {str(e)}"

