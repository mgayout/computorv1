import sys
from cmpt import computor

def main():
    try:
        if len(sys.argv) != 2:
            raise ValueError("bad args")
        if len(sys.argv[1]) == 0:
            raise ValueError("bad args")
        cmpt = computor()
        cmpt.run(sys.argv[1])

    except ValueError as err:
        print(ValueError.__name__ + ":", err)
    except Exception as err:
        print(Exception.__name__ + ":", err)

if __name__ == "__main__":
    main()