from pathlib import Path

# folder where THIS script file lives
SCRIPT_DIR = Path(__file__).resolve().parent
print(f"Script directory: {SCRIPT_DIR}")
print("")
# project root is one level up from Extraction/
DATA_DIR = SCRIPT_DIR.parent / "data"
print(f"Data directory: {DATA_DIR}")