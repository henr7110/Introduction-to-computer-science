from string import*

def Match(target,key):
    """returns number of instances string: key is found in string: target by looping"""

#Checks the parameter for type str
    try:
        str(target)
    except ValueError:
        return none
    try:
        str(key)
    except ValueError:
        return none

#if the key is longer than target, it can't be in target. 
    targetlen = len(target)
    keylen = len(key)

    if keylen > targetlen:
        return 0

#loop that goes through the lenght of target and finds all instances of key
    counter = 0
    search_start = 0
    while search_start <= targetlen - keylen:

#if key is not found, then don't itterate counter
        if find(target,key,search_start) == -1:
            return counter
#else it will be found, and the start is moved up to where it was found
#while counter is incremented.
        search_start = find(target,key,search_start) + keylen
        counter += 1
#when finished, counter is returned for total number of key instances
    return counter

def MatchR(target, key):
    """returns number of instances string: key is found in string: target by recursion"""
#Checks the parameter for type str
    try:
        str(target)
    except ValueError:
        return none
    try:
        str(key)
    except ValueError:
        return none

    targetlen = len(target)
    keylen = len(key)

    
    if targetlen < keylen:  #base case
        return 0

#itterative state that passes on smaller problem to itself and evaluates
#first part for key.
    else:
        if key == target[:keylen]:
            return 1 + countSubStringMatchRecursive (target[keylen:], key) 
        else:
            return 0 + countSubStringMatchRecursive (target[keylen:], key)
    
def subStringMatchExact (target, key):
    """finds the locations where key appear in target expressed as tuple"""
#Checks the parameter for type str
    try:
        str(target)
    except ValueError:
        print ' target not int'
        return none
    try:
        str(key)
    except ValueError:
        print 'key not int'
        return none

    results = ()
#too short or no targets won't yield an answer
    targetlen = len(target)
    keylen = len(key)
    if keylen > targetlen:
        return results
    if key  == '' or target == '':
        return results

#goes through the lenght of target and saves all locations of key
    search_start = 0
    while search_start <= targetlen - keylen:

#if key is not found, location isn't saved
        if find(target,key,search_start) == -1:
            return results

#else it is saved, and seach_start is moved up
        results += (find(target,key,search_start),)
        search_start = find(target,key,search_start) + keylen
 
#when finished, tuple of locations are returned
    return results        

def constrainedMatchPair(firstMatch,secondMatch,length):
    results = ()
    for i in secondMatch:
        for n in firstMatch:
            if n + length + 1 == i:
                results += (n,)
    return results
         

def subStringMatchExactlyOneSub(key,target):
    """search for all locations of key in target, with one substitution"""
    allAnswers = ()
    for miss in range(0,len(key)):
        # miss picks location for missing element
        # key1 and key2 are substrings to match
        key1 = key[:miss]
        key2 = key[miss+1:]
        print 'breaking key',key,'into',key1,key2
        # match1 and match2 are tuples of locations of start of matches
        # for each substring in target
        match1 = subStringMatchExact(target,key1)
        match2 = subStringMatchExact(target,key2)
        print match1 , match2
        # when we get here, we have two tuples of start points
        # need to filter pairs to decide which are correct
        filtered = constrainedMatchPair(match1,match2,len(key1))
        allAnswers = allAnswers + filtered
        print 'match1',match1
        print 'match2',match2
        print 'possible matches for',key1,key2,'start at',filtered
    return allAnswers
