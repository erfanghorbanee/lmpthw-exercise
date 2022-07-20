import argparse

my_parser = argparse.ArgumentParser(description='Simple solution for ex4.',
                                    epilog='Enjoy the program! :)')

# positional args that are required and the order matters!
my_parser.add_argument('fname', help='Your first name')

my_parser.add_argument('lname', help='Your last name')

my_parser.add_argument('country', help='Your country')


# optional args that take a value
my_parser.add_argument('-a', help='option a')

my_parser.add_argument('-b', help='option b')

my_parser.add_argument('-c', help='option c')


# flags
my_parser.add_argument('-v',
                       '--verbose',
                       action='store_true',
                       help='flag v')

my_parser.add_argument('-d',
                       action='store_true',
                       help='flag d')

my_parser.add_argument('-e',
                       action='store_true',
                       help='flag e')



# Execute parse_args()
args = my_parser.parse_args()
print(f"Hello, dear {args.fname} {args.lname} from {args.country}!\n")
