import argparse

my_parser = argparse.ArgumentParser(
    description="Simple solution for ex5.\nThis is a simple cat command written by python.",
    epilog="Enjoy the program! :)",
)

# positional args that are required and the order matters!
my_parser.add_argument("file_dir", help="Your file directory")


# flags
my_parser.add_argument(
    "-n", "--number", action="store_true", help="number all output lines"
)

my_parser.add_argument(
    "-E", "--show_ends", action="store_true", help="display $ at end of each line"
)


# Execute parse_args()
args = my_parser.parse_args()

with open(args.file_dir, "r") as file:
    if args.number:
        line_number = 0
        for line in file.readlines():
            line_number += 1
            print(f"    {line_number}  {line}", end="")

    elif args.show_ends:
        line_number = 0
        for line in file.readlines():
            line_number += 1
            new_line = line.replace("\n", "$")
            print(f"    {line_number}  {new_line}")

    else:
        print(file.read())
