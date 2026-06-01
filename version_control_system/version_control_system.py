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

import sys
import os
import hashlib
import shutil

# Створення папок і файлів
os.makedirs("vcs", exist_ok=True)

config_file = os.path.join("vcs", "config.txt")
index_file = os.path.join("vcs", "index.txt")
log_file = os.path.join("vcs", "log.txt")
commits_dir = os.path.join("vcs", "commits")

os.makedirs(commits_dir, exist_ok=True)

open(config_file, "a").close()
open(index_file, "a").close()
open(log_file, "a").close()

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


def get_hash():
    with open(index_file, "r") as f:
        files = [line.strip() for line in f if line.strip()]

    content = ""

    for file in files:
        if os.path.exists(file):
            with open(file, "rb") as current_file:
                content += current_file.read().decode("utf-8", errors="ignore")

    return hashlib.sha256(content.encode()).hexdigest()


args = sys.argv

# HELP
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

# LOG
elif args[1] == "log":

    if os.path.getsize(log_file) == 0:
        print("No commits yet.")
    else:
        with open(log_file, "r") as f:
            print(f.read().strip())

# COMMIT
elif args[1] == "commit":

    if len(args) < 3:
        print("Message was not passed.")

    else:
        message = args[2]

        current_hash = get_hash()

        last_hash = ""

        if os.path.getsize(log_file) > 0:
            with open(log_file, "r") as f:
                first_line = f.readline().strip()

            if first_line.startswith("commit "):
                last_hash = first_line.split()[1]

        if current_hash == last_hash:
            print("Nothing to commit.")

        else:
            commit_dir = os.path.join(commits_dir, current_hash)
            os.makedirs(commit_dir, exist_ok=True)

            with open(index_file, "r") as f:
                files = [line.strip() for line in f if line.strip()]

            for file in files:
                if os.path.exists(file):
                    shutil.copy(file, commit_dir)

            with open(config_file, "r") as f:
                author = f.read().strip()

            log_entry = (
                f"commit {current_hash}\n"
                f"Author: {author}\n"
                f"{message}\n\n"
            )

            old_log = ""

            with open(log_file, "r") as f:
                old_log = f.read()

            with open(log_file, "w") as f:
                f.write(log_entry + old_log)

            print("Changes are committed.")

# Існуючі команди
elif args[1] in commands:
    print(commands[args[1]])

# Неправильна команда
else:
    print(f"'{args[1]}' is not a VCS command.")

import os
import sys
import hashlib
import shutil

os.makedirs("vcs", exist_ok=True)

config_file = os.path.join("vcs", "config.txt")
index_file = os.path.join("vcs", "index.txt")
log_file = os.path.join("vcs", "log.txt")
commits_dir = os.path.join("vcs", "commits")

os.makedirs(commits_dir, exist_ok=True)

for file in [config_file, index_file, log_file]:
    open(file, "a").close()

commands = {
    "config": "Get and set a username.",
    "add": "Add a file to the index.",
    "log": "Show commit logs.",
    "commit": "Save changes.",
    "checkout": "Restore a file."
}

help_text = """These are VCS commands:
config Get and set a username.
add Add a file to the index.
log Show commit logs.
commit Save changes.
checkout Restore a file."""


def get_hash():
    data = ""

    with open(index_file, "r") as f:
        files = [line.strip() for line in f if line.strip()]

    for file_name in files:
        if os.path.exists(file_name):
            data += file_name

            with open(file_name, "rb") as file:
                data += file.read().decode("utf-8", errors="ignore")

    return hashlib.sha256(data.encode()).hexdigest()


args = sys.argv

if len(args) == 1 or args[1] == "--help":
    print(help_text)

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

elif args[1] == "log":

    if os.path.getsize(log_file) == 0:
        print("No commits yet.")
    else:
        with open(log_file, "r") as f:
            print(f.read().strip())

elif args[1] == "commit":

    if len(args) < 3:
        print("Message was not passed.")

    else:

        with open(index_file, "r") as f:
            tracked_files = [line.strip() for line in f if line.strip()]

        if not tracked_files:
            print("Nothing to commit.")

        else:
            message = " ".join(args[2:])
            commit_hash = get_hash()

            latest_hash = ""

            if os.path.getsize(log_file) > 0:
                with open(log_file, "r") as f:
                    first_line = f.readline().strip()

                if first_line.startswith("commit "):
                    latest_hash = first_line.split()[1]

            if commit_hash == latest_hash:
                print("Nothing to commit.")

            else:
                commit_path = os.path.join(commits_dir, commit_hash)
                os.makedirs(commit_path, exist_ok=True)

                for file_name in tracked_files:
                    shutil.copy(file_name, commit_path)

                with open(config_file, "r") as f:
                    author = f.read().strip()

                new_log = (
                    f"commit {commit_hash}\n"
                    f"Author: {author}\n"
                    f"{message}\n\n"
                )

                with open(log_file, "r") as f:
                    old_log = f.read()

                with open(log_file, "w") as f:
                    f.write(new_log + old_log)

                print("Changes are committed.")

elif args[1] == "checkout":

    if len(args) < 3:
        print("Commit id was not passed.")

    else:
        commit_id = args[2]
        commit_path = os.path.join(commits_dir, commit_id)

        if not os.path.exists(commit_path):
            print("Commit does not exist.")

        else:
            for file_name in os.listdir(commit_path):
                shutil.copy(
                    os.path.join(commit_path, file_name),
                    file_name
                )

            print(f"Switched to commit {commit_id}.")

else:
    print(f"'{args[1]}' is not a VCS command.")