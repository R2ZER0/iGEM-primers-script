
# How to use: copy and paste these two bits of text into a program called IDLE (search for it on the uni system)
# Each needs to be in front of arrows (>>>) which tell you where IDLE starts
# then type "primer('sequence goes here')". Press enter.
# currently it doesn't put DR and UR on the same line as their prefixes and suffixes. Not sure why
# To confirm the primers fit where they should, use ApE’s alignment tool

 


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
    





def primers(s):
    print 'UF is CTAgag' + s[0:37] #print first 37 bases with the prefix
        print 'UR is (add ctc at end)' #reverses the first 34 bases of the primer
    rc(s, 0, 34)
    ## if s[-37:-35] == 'tag' or 'cta': 
    ## ^ easy thing to be caught out on, this actually means:
    ##   if (s[-37:-35] == ‘tag’) or (‘cta’): 
    ## ‘or’ works solely with boolean logic, and in python all non-empty strings
    ##  are True (noidea why), so this if statement can never fail!
    
    if (s[-37:-34] == 'tag') or (s[-37:-34] == 'cta'):  #takes last 37 bases, checks first 3 for stops  
        print 'bad codon found'
        if s[-36:-33] == 'tag':
            print 'bad codon found again'
            print 'DF is ta' + s[-35:]
            print 'DR is TAGta'
            rc(s, -35, -3)

        else:
            print 'DF is ta' + s[-36:]
            print 'DR is TAGta'
                rc(s, -36, -3)
        # if tag or cta, take one base from the start, give df with prefix
    else:
        print 'codons fine, DF is ta' + s[-37:]
        print 'DR is TAGta'
        rc(s, -37, -3) # this will take DF, take 3 from the end, and produce its complement. 
#ALso cool would be to get it run batches of sequences, and, most helpfully, remove the whitespace from sequences copied and pasted from the registry, because that’s a hassle

