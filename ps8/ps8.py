# 6.00 Problem Set 8
#
# Intelligent Course Advisor
#
# Name:
# Collaborators:
# Time:
#

import time

SUBJECT_FILENAME = "subjects.txt"
VALUE, WORK = 0, 1

#
# Problem 1: Building A Subject Dictionary
#
def loadSubjects(filename):
    """
    Returns a dictionary mapping subject name to (value, work), where the name
    is a string and the value and work are integers. The subject information is
    read from the file named by the string filename. Each line of the file
    contains a string of the form "name,value,work".

    returns: dictionary mapping subject name to (value, work)
    """

    # The following sample code reads lines from the specified file and prints
    # each one.

    classes = {}
    inputFile = open(filename)
    #reads the name, value and work for each line and saves them in a dictionary
    #as a float and a tuple of an integer and a float
    for line in inputFile:
            s = line.split(',')
            s[2].strip('\n')
            classes[s[0]] = (int(s[1]),int(s[2]))           
    return classes
                    
        


def printSubjects(subjects):
    """
    Prints a string containing name, value, and work of each subject in
    the dictionary of subjects and total value and work of all subjects
    """
    totalVal, totalWork = 0,0
    if len(subjects) == 0:
        return 'Empty SubjectList'
    res = 'Course\tValue\tWork\n======\t====\t=====\n'
    subNames = subjects.keys()
    subNames.sort()
    for s in subNames:
        val = subjects[s][VALUE]
        work = subjects[s][WORK]
        res = res + s + '\t' + str(val) + '\t' + str(work) + '\n'
        totalVal += val
        totalWork += work
    res = res + '\nTotal Value:\t' + str(totalVal) +'\n'
    res = res + 'Total Work:\t' + str(totalWork) + '\n'
    print res

def cmpValue(subInfo1, subInfo2):
    """
    Returns True if value in (value, work) tuple subInfo1 is GREATER than
    value in (value, work) tuple in subInfo2
    """
    val1 = subInfo1[VALUE]
    val2 = subInfo2[VALUE]
    return  val1 > val2

def cmpWork(subInfo1, subInfo2):
    """
    Returns True if work in (value, work) tuple subInfo1 is LESS than than work
    in (value, work) tuple in subInfo2
    """
    work1 = subInfo1[WORK]
    work2 = subInfo2[WORK]
    return  work1 < work2

def cmpRatio(subInfo1, subInfo2):
    """
    Returns True if value/work in (value, work) tuple subInfo1 is 
    GREATER than value/work in (value, work) tuple in subInfo2
    """
    val1 = subInfo1[VALUE]
    val2 = subInfo2[VALUE]
    work1 = subInfo1[WORK]
    work2 = subInfo2[WORK]
    return float(val1) / work1 > float(val2) / work2

#
# Problem 2: Subject Selection By Greedy Optimization
#
def greedyAdvisor(subjects, maxWork, comparator):
    """
    Returns a dictionary mapping subject name to (value, work) which includes
    subjects selected by the algorithm, such that the total work of subjects in
    the dictionary is not greater than maxWork.  The subjects are chosen using
    a greedy algorithm.  The subjects dictionary should not be mutated.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    comparator: function taking two tuples and returning a bool
    returns: dictionary mapping subject name to (value, work)
    """

    subsort = []
    inserted = False
    results = {}
    #generate a sorted list with the comparator
    for k,v in subjects.items():
        if len(subsort) == 0:
            subsort.append((k,v))
            inserted = True
        if not inserted:
            for i in range(len(subsort)):
                if comparator(v,subsort[i][1]):
                    subsort.insert(i,(k,v))
                    inserted = True
                    break
            if not inserted:           
                subsort.append((k,v))
        inserted = False
        
    #take as many from the list as maxWork allows
    currentwork = maxWork
    subcounter = 1
    for i in range(len(subsort)):              
        if currentwork - subsort[i][1][1] > 0:
            results[subsort[i][0]] = subsort[i][1]
            currentwork -= subsort[i][1][1]
    return results
        
                
                
def testga():
    s = loadSubjects("subjects.txt")
    
    #tests cmpValue
    b = greedyAdvisor(s,40,cmpValue)
    print 'cmpValue'
    printSubjects(b)
    
    #tests cmpWork
    b = greedyAdvisor(s,40,cmpWork)
    print 'cmpWork'
    printSubjects(b)

    #tests cmpRatio
    b = greedyAdvisor(s,40,cmpRatio)
    print 'cmpRatio'
    printSubjects(b)
    
            
        

##    if comparator == cmpWork:
##
##    if comparator == cmpRatio:

def bruteForceAdvisor(subjects, maxWork):
    """
    Returns a dictionary mapping subject name to (value, work), which
    represents the globally optimal selection of subjects using a brute force
    algorithm.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    returns: dictionary mapping subject name to (value, work)
    """
    nameList = subjects.keys()
    tupleList = subjects.values()
    bestSubset, bestSubsetValue = \
            bruteForceAdvisorHelper(tupleList, maxWork, 0, None, None, [], 0, 0)
    outputSubjects = {}
    for i in bestSubset:
        outputSubjects[nameList[i]] = tupleList[i]
    return outputSubjects

def bruteForceAdvisorHelper(subjects, maxWork, i, bestSubset, bestSubsetValue,
                            subset, subsetValue, subsetWork):

    # Hit the end of the list.
    if i >= len(subjects):
        if bestSubset == None or subsetValue > bestSubsetValue:
            # Found a new best.
            return subset[:], subsetValue
        else:
            # Keep the current best.
            return bestSubset, bestSubsetValue
    else:
        s = subjects[i]
        # Try including subjects[i] in the current working subset.
        if subsetWork + s[WORK] <= maxWork:
            subset.append(i)
            bestSubset, bestSubsetValue = bruteForceAdvisorHelper(subjects,
                    maxWork, i+1, bestSubset, bestSubsetValue, subset,
                    subsetValue + s[VALUE], subsetWork + s[WORK])
            subset.pop()
        bestSubset, bestSubsetValue = bruteForceAdvisorHelper(subjects,
                maxWork, i+1, bestSubset, bestSubsetValue, subset,
                subsetValue, subsetWork)
        return bestSubset, bestSubsetValue

#
# Problem 3: Subject Selection By Brute Force
#
def bruteForceTime():
    """
    Runs tests on bruteForceAdvisor and measures the time required to compute
    an answer.
    """
    import time
    s = loadSubjects('subjects.txt')

    for i in range (1,20):
        print 'Maxwork %d' % (i)

        starttime = time.time()
        bruteForceAdvisor(s, i)
        endtime = time.time()
        timedif = endtime - starttime
        print 'that took' , timedif, 'seconds'


# Problem 3 Observations
# ======================
#
# The algorith has an exponential complexity, and it takes 268 seconds if the Maxwork
# is 12. The suggestion is therefore to stop at 12 hours Maxwork, since that is an unreasonable amount of time

#
# Problem 4: Subject Selection By Dynamic Programming
#
def dpAdvisor(subjects, maxWork):
    """
    Returns a dictionary mapping subject name to (value, work) that contains a
    set of subjects that provides the maximum value without exceeding maxWork.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    returns: dictionary mapping subject name to (value, work)
    """
    memo = {}
    nameList = subjects.keys()
    tupleList = subjects.values()
    bestSubset, bestSubsetValue = \
            dpAdvisorHelper(tupleList, maxWork, 0, None, None, [], 0, 0,memo)
    outputSubjects = {}
    for i in bestSubset:
        outputSubjects[nameList[i]] = tupleList[i]
    return outputSubjects




def dpAdvisorHelper(subjects, maxWork, i, bestSubset, bestSubsetValue,
                           subset, subsetValue, subsetWork, memo):
    # Hit the end of the list.
    if i >= len(subjects):
        if bestSubset == None or subsetValue > bestSubsetValue:
            # Found a new best.
            return subset[:], subsetValue
        else:
            # Keep the current best.
            return bestSubset, bestSubsetValue
    in_memo = False
    #Is it in the memo?
            
    if i not in memo:
        s = subjects[i]
        # Try including subjects[i] in the current working subset.
        if subsetWork + s[WORK] <= maxWork:
            subset.append(i)
            bestSubset, bestSubsetValue = dpAdvisorHelper(subjects,
                    maxWork, i+1, bestSubset, bestSubsetValue, subset,
                    subsetValue + s[VALUE], subsetWork + s[WORK], memo)
            memo[bestSubsetValue] = bestSubset
            subset.pop()
        bestSubset, bestSubsetValue = dpAdvisorHelper(subjects,
                maxWork, i+1, bestSubset, bestSubsetValue, subset,
                subsetValue, subsetWork,memo)
        return bestSubsetValue, memo[bestSubsetValue]
    else:
        return memo[bestSubset], bestSubsetValue
#
# Problem 5: Performance Comparison
#
def dpTime():
    import time
    s = loadSubjects('tester.txt')

    for i in range (1,20):
        print 'Maxwork %d' % (i)

        starttime = time.time()
        dpAdvisor(s, i)
        endtime = time.time()
        timedif = endtime - starttime
        print 'that took' , timedif, 'seconds'
    # TODO...

# Problem 5 Observations
# ======================
#
# TODO: write here your observations regarding dpAdvisor's performance and
# how its performance compares to that of bruteForceAdvisor.
