import argparse
import os

my_parser = argparse.ArgumentParser(
    description="Simple solution for ex6.\nThis is a simple find command written in python.",
    epilog="Enjoy the program! :)",
)

# optional args that take a value
my_parser.add_argument(
    "-type", help="type accepts two values: f for file and d for directory"
)


# flags
my_parser.add_argument(
    "-print", action="store_true", help="print results", default=True
)


# Execute parse_args()
args = my_parser.parse_args()

if args.print:
    for path, currentDirectory, files in os.walk("."):
        if args.type:

            if args.type == "f":
                for file in files:
                    print(os.path.join(path, file))

            elif args.type == "d":
                print(path)

            else:
                print(f"find: Unknown argument to -type: {args.type}")

        else:
            for file in files:
                print(os.path.join(path, file))
            print(path)
