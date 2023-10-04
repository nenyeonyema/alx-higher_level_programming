#!/usr/bin/python3

for rev_letter in range(ord('z'), ord('a') - 1, -1):
    print("{:c}".format(rev_letter if rev_letter % 2 == 0 else rev_letter - 32), end='')
