
# then type "primer('sequence goes here')". Press enter. (You must include the apostrophes or it won't work. The sequence text should turn green)
# currently it doesn't put DR and UR on the same line as their prefixes and suffixes. Not sure why
# To confirm the primers fit where they should, use ApE's or IDT's alignment tool
# Additional point: coding genes need slight alterations to the prefixes and suffixes (promoters remain the same). For genes, add CTAg not CTAgag. UR adds c not ctc
 


def rc(sequence, n, b):
    reverse = ''
    ss = sequence[n:b]
    for base in ss:

        if base == 'a':
            reverse = 't' + reverse

        if base == 't':
            reverse =  'a' + reverse

        if base == 'c':
            reverse =  'g' + reverse


        if base == 'g':
            reverse = 'c' + reverse
        if len(reverse) == len(ss):
            print reverse

def sprimers(s):
    c = len(s)
    h = c/ 2   # sets mid point
    a = h - 2  # moves the division point 2 places back
    r = s[0:a] # sets left slice
    l = s[a:]  # sets right slice
    otte = h + 3  # sets slice point for reverse (on right)
    

    print 'UF is CTAgag' + r
    print 'DF is (add ta at end) ' + l
    print 'UR is (add ctc to end)'
    rc(s, 0, otte)
    print 'DR is TAGta'
    rc(s, otte, None)
    
def primers(s):
    if len(s) < 101:
        sprimers(s)
        return
    else:
        print 'UF is CTAgag' + s[0:37] #print first 37 bases with the prefix
        print 'UR is (add ctc at end)' #reverses the first 34 bases of the primer
        rc(s, 0, 34)
    ## if s[-37:-35] == 'tag' or 'cta':
    ## ^ easy thing to be caught out on, this actually means:
    ##   if (s[-37:-35] == 'tag') or ('cta'):
    ## 'or' works solely with boolean logic, and in python all non-empty strings
    ##  are True (noidea why), so this if statement can never fail!

        if (s[-37:-34] == 'tag') or (s[-37:-34] == 'cta'):  #takes last 37 bases, checks first 3 for stops
            print 'bad codon found'
            if s[-36:-33] == 'tag':
                print 'bad codon found again'
                print 'DF is (add ta at end)' + s[-35:]
                print 'DR is TAGta'
                rc(s, -32, None)

            else:
                print 'DF is (add ta at end)' + s[-36:]
                print 'DR is TAGta'
                rc(s, -33, None)
        # if tag or cta, take one base from the start, give df with prefix
        else:
            print 'codons fine, DF is (add ta at end)' + s[-37:]
            print 'DR is TAGta'
            rc(s, -34, None)
# this will take DF, take 3 from the end, and produce its complement.




#ALso cool would be to get it run batches of sequences, and, most helpfully, remove the whitespace from sequences copied and pasted from the registry, because that's a hassle
# -> for the latter, ApE can do it, but yeah that would be cool

from Bio.Seq import Seq
from Bio.Alphabet import generic_dna

def primers2raw(raw_seq):
    """primers2, accepting a raw sequence string"""
    return primers2( Seq(raw_seq, generic_dna) )

def primers2(seq):
    """Takes a Seq object, returns the Clips primers"""
    UF = "ctagag" + seq[0:37]   # Upstream Forward
    UR = seq[0:34].reverse_complement() + "ctc"  # Upstream Reverse
    
    
    
    
# an experiment into functional programming
def UF(seq):
    return seq[0:37] + "ctagag"

def UR(seq):
    return rc(UF(seq)[0:34], 0, None) + "ctc"

def DF(seq):
    t = UR(seq)[-37:]
    while(t[0:3] not in ["tag", "cta"]):
        
    
