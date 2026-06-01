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