#!/usr/bin/python3
import hidden_4


def hiddenfile():
    names = dir(hidden_4)
    for name in names:
        if name[:2] == "__":
            continue
        print("{}".format(name))


if __name__ == "__main__":
    hiddenfile()
