import os
from pathlib import Path

paths = sorted(Path(dirpath).iterdir(), key=os.path.getmtime)
