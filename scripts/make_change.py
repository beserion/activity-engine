from datetime import datetime
import random

files = ["README.md", "CHANGELOG.md"]

file = random.choice(files)

with open(file, "a", encoding="utf-8") as f:
    f.write(f"\n- minor update @ {datetime.now()}")

print("Updated:", file)
