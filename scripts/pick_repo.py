import json, random

with open("targets.json") as f:
    repos = json.load(f)

repo = random.choice(repos)

with open("selected_repo.txt", "w") as f:
    f.write(repo)

print("Selected:", repo)
