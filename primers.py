
# How to use: copy and paste these two bits of text into a program called IDLE (search for it on the uni system)
# Each needs to be in front of arrows (>>>) which tell you where IDLE starts
# then type (no quote marks) "primer('sequence goes here')". Press enter.
# currently it doesn't put DR and UR on the same line as their prefixes and suffixes. Not sure why
 


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
    rc(s, 0, 35)
    if s[-37:-35] == 'tag' or 'cta':  #takes last 37 bases, checks first 3 for stops  
        print 'bad codon found'
        if s[-36:-34] == 'tag':
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
        rc(s, -37, -3)
