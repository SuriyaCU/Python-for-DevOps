from pathlib import Path
from typing import Union
import datetime

def archive_log_files(log_directory: Union[str, Path], archive_date: str) -> list[Path]:
    """
    Finds and renames all .log files in a directory with a date stamp.
    """
    
    # --- Input Validation ---
    
    # 1. Validate log_directory type
    if not isinstance(log_directory, (str, Path)):
        raise TypeError("log_directory must be a string or a pathlib.Path object.")
    
    # Convert to Path object for uniform processing
    path_obj = Path(log_directory)
    
    # 2. Validate directory existence and type
    if not path_obj.exists() or not path_obj.is_dir():
        raise ValueError(f"The path '{log_directory}' does not exist or is not a directory.")
    
    # 3. Validate archive_date type
    if not isinstance(archive_date, str):
        raise TypeError("archive_date must be a string.")
    
    # 4. Validate YYYY-MM-DD format
    try:
        datetime.datetime.strptime(archive_date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("archive_date must be in YYYY-MM-DD format.")

    # --- Archiving Logic ---
    
    renamed_files = []
    
    # Iterate through all items in the directory
    for item in path_obj.iterdir():
        # Check if it's a file and has the .log extension
        if item.is_file() and item.suffix == ".log":
            # Construct the new filename: {original_stem}-{archive_date}.log
            new_name = f"{item.stem}-{archive_date}{item.suffix}"
            new_path = item.with_name(new_name)
            
            # Perform the rename
            item.rename(new_path)
            
            # Track the successfully renamed file
            renamed_files.append(new_path)
            
    return renamed_files