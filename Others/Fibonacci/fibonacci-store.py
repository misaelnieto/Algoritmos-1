#!/usr/bin/env python
"""
This is the fibonacci algorithm as narrated in the book Algorithms,
Copyright c 2006 S. Dasgupta, C. H. Papadimitriou, and U. V. Vazirani, 
Chapter 0, Page 13

This algorithm computes N fibonacci numbers, but instead of using recursive
function, it just stores past results in an array, so we avoid expensive
calculations for past values.

In a core i5 with 4 GB of RAM this takes:

time ./fibonacci-store.py 100
Generating 300 fibonacci numbers:
real    0m0.048s
user    0m0.038s
sys 0m0.009s



"""
import sys
results = [0,1]

def fib(n):
    results[n] = results[n-1] + results[n-2]

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
    #Reserve memory for all results
    results = range(N)
    for i in range(2, N):
        fib(i)
    # print results
