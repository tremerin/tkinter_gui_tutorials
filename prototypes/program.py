import sys

def prototype():
    print(f"Number of arguments {len(sys.argv)}")
    for argument in sys.argv:
        print(argument)


if __name__ == "__main__":
    prototype()