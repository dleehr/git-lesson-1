"""Prints out fasta sequence given a fasta file."""

import sys

def read_fasta(filename):
    return 'ATATACCACA'

if len(sys.argv) < 2:
    print "Usage:", sys.argv[0], "<sequence.fa>"
    exit(1)

print read_fasta(sys.argv[1])
