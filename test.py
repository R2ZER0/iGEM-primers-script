#!/usr/bin/python
# -*- coding: utf-8 -*-
# A simple primers generating test using sample data

# Our primers generating function
from primers import primers, primers2

# Biopython's sequence import library
from Bio import SeqIO

testfile_handle = open("test_seq1.fasta", "rU")

for record in SeqIO.parse(testfile_handle, "fasta"):
    print("Record: " + str(record.id))
    print("###### PRIMERS ######")
    primers(str(record.seq))
    
    print("###### PRIMERS2 #####")
    print(primers2(record.seq))
