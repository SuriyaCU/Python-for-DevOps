import shutil
from pathlib import Path
from typing import Union

def create_backup(source_dir: Union[str, Path], dest_dir: Union[str, Path]) -> None:
    """
    Creates a clean backup of a source directory to a destination directory.

    If the destination directory exists, it is removed before copying.

    Args:
        source_dir (Union[str, Path]): The directory to back up.
        dest_dir (Union[str, Path]): The directory to create the backup in.
    
    Raises:
        TypeError: If arguments are not str or pathlib.Path.
        ValueError: If source_dir does not exist or is not a directory.
    """
    
    # 1. Input Validation: Check types
    if not isinstance(source_dir, (str, Path)) or not isinstance(dest_dir, (str, Path)):
        raise TypeError("Both source_dir and dest_dir must be a string or pathlib.Path object.")

    # Convert to Path objects for consistent manipulation
    src = Path(source_dir)
    dst = Path(dest_dir)

    # 2. Input Validation: Check if source exists and is a directory
    if not src.exists() or not src.is_dir():
        raise ValueError(f"Source directory '{src}' does not exist or is not a directory.")

    # 3. Clean the destination: If it exists, remove it entirely
    if dst.exists():
        if dst.is_dir():
            shutil.rmtree(dst)
        else:
            # Handle edge case where dest_dir name exists but is a file
            dst.unlink()

    # 4. Perform the recursive copy
    # shutil.copytree creates the destination directory itself
    shutil.copytree(src, dst)

# --- Example Usage ---
if __name__ == "__main__":
    # Setup for demonstration
    temp_source = Path("./app_config")
    temp_source.mkdir(exist_ok=True)
    (temp_source / "config.yaml").write_text("setting: true")

    try:
        # Test with strings
        create_backup("./app_config", "./backup_dir")
        print("Backup created successfully using strings.")

        # Test with Path objects
        create_backup(Path("./app_config"), Path("./backup_dir"))
        print("Backup replaced successfully using Path objects.")

    except (TypeError, ValueError) as e:
        print(f"Error: {e}")