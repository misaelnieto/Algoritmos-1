#!/usr/bin/env python
"""
This is the fibonacci algorithm as narrated in the book Algorithms,
Copyright c 2006 S. Dasgupta, C. H. Papadimitriou, and U. V. Vazirani, 
Chapter 0, Page 12

This algorithm computes N fibonacci numbers with a recursive function.

For N>30 the fib sequence will be start to take longer and longer.

In a core i5 with 4 GB of RAM this takes:

time ./fibonacci.py 100
Generating 30 fibonacci numbers:
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765 10946 17711 28657 46368 75025 121393 196418 317811 514229

real    0m1.054s
user    0m1.036s
sys 0m0.011s


"""
import sys

def fib(n):
    """
    Oh! recursivity!
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib (n-2)


if __name__ == '__main__':
    #This is just for taking arguments in the command line.
    if len(sys.argv) != 2:
        print "Usage: %s N" % sys.argv[0]
        print "Where N is the number of fibonacci numbers to generate"
        sys.exit(1)

    #Data sanitization
    try:
        N = int(sys.argv[1])
        if N <0:
            print "No negative numbers please!"
            sys.exit(1)
    except ValueError:
        print "Please, use integers for N!"
        sys.exit(1)
        
    #Finally
    print "Generating %i fibonacci numbers:" % N
    for i in range(N):
        print fib(i),
