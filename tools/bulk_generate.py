import subprocess
import argparse
import json
import sys
import os

import gi


def generate(modules):
    index = 1
    for module, version in modules.items():
        out = subprocess.check_output(["python3", "generate.py", module, version])
        with open(f"../src/gi-stubs/repository/{module}.pyi", "wb") as file:
            file.write(out)
        print(f"Generating... ({index}/{len(modules)})", end="\r")
        index += 1
    print()


def table(_dict: dict, row_names=None, _spaces=4, suffix=""):
    length_list = [len(x) for x in _dict]

    largest_length = max(length_list)
    new_dict = {}

    print(
        row_names[0] + " " * ((largest_length + _spaces) - len(row_names[0]) + 1),
        row_names[1],
    )
    for key, value in _dict.items():
        spaces = " " * ((largest_length + _spaces) - len(key))
        new_dict[key + suffix + spaces] = value

    return new_dict.items()


def list_with_grep(dir, grep_statement):
    ls_out = subprocess.run(
        ["bash", "-c", f"ls {dir} | grep {grep_statement}"],
        stdout=subprocess.PIPE,
    )

    if ls_out.returncode != 0:
        print(f"No gir files found in {dir}")
        return {}

    return {
        x.split("-")[0]: os.path.splitext(x.split("-")[1])[0]
        for x in ls_out.stdout.decode().splitlines()
    }


def search_grep(gp_s):
    if (path := os.environ.get("GI_TYPELIB_PATH")) is not None:
        paths = path.split(":")
        files = {}

        for p in paths:
            files.update(list_with_grep(p, gp_s))

        return files
    else:
        return list_with_grep("/usr/share/gir-1.0/", gp_s)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="bulk_generate")

    parser.add_argument("-g", "--grep", help="Find gir types with grep statements")
    parser.add_argument(
        "-j", "--json", help="A json dictionary of module name and version"
    )

    args = parser.parse_args()

    try:
        gi.require_version("GIRepository", "2.0")
    except ValueError:
        print("Install pygobject <= 3.5")
        sys.exit(2)

    if args.grep is not None:
        modules = search_grep(args.grep)
    elif args.json is not None:
        modules = json.loads(args.json)
    else:
        print("No operation")
        sys.exit(1)

    print("Current modules:")

    for m, v in table(
        modules, row_names=["\tModule", "Version"], _spaces=2, suffix=":"
    ):
        print(f"\t{m}{v}")

    prompt = input("Is this correct (Y/N)?: ")
    if prompt in ["N", "n"]:
        sys.exit(1)

    generate(modules)
