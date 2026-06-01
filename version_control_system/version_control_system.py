import sys

commands = {
    "config": "Get and set a username.",
    "add": "Add a file to the index.",
    "log": "Show commit logs.",
    "commit": "Save changes.",
    "checkout": "Switch between commits and restore a previous file state."
}

help_text = """These are VCS commands:
config Get and set a username.
add Add a file to the index.
log Show commit logs.
commit Save changes.
checkout Switch between commits and restore a previous file state.
"""

# Якщо немає аргументів або аргумент --help
if len(sys.argv) == 1 or sys.argv[1] == "--help":
    print(help_text)

else:
    command = sys.argv[1]

    if command in commands:
        print(commands[command])
    else:
        print(f"'{command}' is not a VCS command.")

import sys
import os

# Створення папки vcs
os.makedirs("vcs", exist_ok=True)

config_file = os.path.join("vcs", "config.txt")
index_file = os.path.join("vcs", "index.txt")

# Створення файлів, якщо їх немає
open(config_file, "a").close()
open(index_file, "a").close()

commands = {
    "config": "Get and set a username.",
    "add": "Add a file to the index.",
    "log": "Show commit logs.",
    "commit": "Save changes.",
    "checkout": "Switch between commits and restore a previous file state."
}

help_text = """These are VCS commands:
config Get and set a username.
add Add a file to the index.
log Show commit logs.
commit Save changes.
checkout Switch between commits and restore a previous file state.
"""

args = sys.argv

# Немає аргументів або --help
if len(args) == 1 or args[1] == "--help":
    print(help_text)

# CONFIG
elif args[1] == "config":

    if len(args) == 2:
        with open(config_file, "r") as f:
            username = f.read().strip()

        if username:
            print(f"The username is {username}.")
        else:
            print("Please, tell me who you are.")

    else:
        username = args[2]

        with open(config_file, "w") as f:
            f.write(username)

        print(f"The username is {username}.")

# ADD
elif args[1] == "add":

    if len(args) == 2:
        with open(index_file, "r") as f:
            files = [line.strip() for line in f if line.strip()]

        if not files:
            print("Add a file to the index.")
        else:
            print("Tracked files:")
            print("\n".join(files))

    else:
        filename = args[2]

        if not os.path.exists(filename):
            print(f"Can't find '{filename}'.")
        else:
            with open(index_file, "r") as f:
                tracked = [line.strip() for line in f]

            if filename not in tracked:
                with open(index_file, "a") as f:
                    f.write(filename + "\n")

            print(f"The file '{filename}' is tracked.")

# Інші команди з етапу 1
elif args[1] in commands:
    print(commands[args[1]])

else:
    print(f"'{args[1]}' is not a VCS command.")