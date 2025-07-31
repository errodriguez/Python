#! /usr/bin/env python

def minion_game0(string):
    # your code goes here

    def counter(minion):
        c = 0
        for l in minion:
            i = string.index(l) 
            for j in range(i, len(string)):
                c += string.count(string[i:j+1])
        return c
 

    string = string.lower()
    vowels = set([ 'a', 'e', 'i', 'o', 'u'])
    stuart = set(string).difference(vowels)
    kevin = set(string).intersection(vowels)
    s = counter(stuart)
    k = counter(kevin)
            
    print( "Stuart " + str(s) if s>k else "Kevin " + str(k) )
  

def minion_game1(string):
    string = string.upper()
    vowels = 'AEIOU'
    k = 0
    s = 0

    for i in range(len(string)):
        if string[i] in vowels:
            k += len(string) - i
        else:
            s += len(string) - i

    print( "Stuart " + str(s) if s>k else "Kevin " + str(k) )


if __name__ == '__main__':
    s = input()
    minion_game1(s)
