#!/usr/bin/python3
charc = ""
for i in range(ord('a'), ord('z') + 1):
    if chr(i) != 'q' and chr(i) != 'e':
        charc += chr(i)
print("{}".format(charc), end="")
