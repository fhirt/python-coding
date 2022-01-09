from pathlib import Path

new_dir = Path.home() / "new_directory"
new_dir.mkdir(exist_ok=True)
print("exists", new_dir.exists())
print("is dir", new_dir.is_dir())

nested_dir = new_dir / "folder_a" / "folder_b"
nested_dir.mkdir(parents=True, exist_ok=True)

file_path = new_dir / "file1.txt"
print("exists", file_path.exists())
file_path.touch()
print("exists", file_path.exists())
print("is file", file_path.is_file())


file_path = new_dir / "folder_c" / "file2.txt"
file_path.parent.mkdir(parents=True, exist_ok=True)
file_path.touch()