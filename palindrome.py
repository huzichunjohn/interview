#/usr/bin/env python
# -*- coding: utf-8 -*-

def palindrome(n):
    total = 0
    for i in range(n+1):
        if str(i) == str(i)[::-1]:
            print i
            total += 1
    return total

def max_palindrome(n):
    for i in range(n, -1, -1):
        if str(i) == str(i)[::-1]:
            break
    return i

if __name__ == "__main__":
    print palindrome(99999)
    print max_palindrome(99999)
