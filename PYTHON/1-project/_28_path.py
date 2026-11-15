from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
print(f"BASE_DIR:{BASE_DIR}")
print("########")
print(f"BASE_DIR subfolder:{BASE_DIR.parent}")