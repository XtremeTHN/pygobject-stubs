import subprocess
import argparse
import json
import sys
import os

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

    print(row_names[0] + " " * ((largest_length + _spaces) - len(row_names[0]) + 1), row_names[1])
    for key, value in _dict.items():
        spaces = " " * ((largest_length + _spaces) - len(key))
        new_dict[key + suffix + spaces] = value
    
    return new_dict.items()

def search_grep(grep_statement):
    ls_out = subprocess.check_output(["bash", "-c", f"ls /usr/share/gir-1.0/ | grep {grep_statement}"])
    return {x.split(b"-")[0].decode(): os.path.splitext(x.split(b"-")[1])[0].decode() for x in ls_out.splitlines()}

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="bulk_generate")
    
    parser.add_argument("-g", "--grep", help="Find gir types with grep statements")
    parser.add_argument("-j", "--json", help="A json dictionary of module name and version")
    
    args = parser.parse_args()
    
    if args.grep is not None:
        modules = search_grep(args.grep)
    elif args.json is not None:
        modules = json.loads(args.json)
    else:
        print("No operation")
        sys.exit(1)
        
    print("Current modules:")

    for m, v in table(modules, row_names=["\tModule", "Version"], _spaces=2, suffix=":"):
        print(f"\t{m}{v}")
    
    prompt = input("Is this correct (Y/N)?: ")
    if prompt in ["N", "n"]:
        sys.exit(1)
    
    generate(modules)

