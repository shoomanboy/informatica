#!/bin/python3

import sys

n = int(input().strip())
p = int(input().strip())
# your code goes here
answer = min(p // 2, (n - p) // 2)

print(answer)