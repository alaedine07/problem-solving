#!/bin/python3
import math
import os
import random
import re
import sys
if __name__ == '__main__':
    n = int(input())
    n = bin(n).replace("0b","")
    str(n)
    binary_array = []
    for number in n:
        binary_array.append(number)
    count = 0
    result = 0
    for i in binary_array:
        if i == '0':
            count = 0
        else:
            count += 1
            result = max(count,result)
print(result)           

   
           


