from pathlib import Path

ROOT = Path.cwd()

folders = [
    "core",
    "database",
    "research",
    "intelligence",
    "ui",
    "cache",
    "reports",
    "logs",
    "docs",
    "tests",
    "data/input",
    "data/output",
]

files = [
    "app.py",
    "config.py",
    "requirements.txt",
    ".gitignore",
    "README.md",
]

package_folders = [
    "core",
    "database",
    "research",
    "intelligence",
    "ui",
]

print("=" * 50)
print("BD Product Intelligence - Project Setup")
print("=" * 50)

# Create folders
for folder in folders:
    path = ROOT / folder
    path.mkdir(parents=True, exist_ok=True)
    print(f"[Folder] {folder}")

# Create package files
for folder in package_folders:
    init_file = ROOT / folder / "__init__.py"
    init_file.touch(exist_ok=True)
    print(f"[File] {folder}/__init__.py")

# Create root files
for file in files:
    f = ROOT / file
    f.touch(exist_ok=True)
    print(f"[File] {file}")

print("=" * 50)
print("Project structure created successfully!")
print("=" * 50)