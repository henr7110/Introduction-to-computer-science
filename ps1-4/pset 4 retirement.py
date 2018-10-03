# Problem Set 4
# Name: 
# Collaborators: 
# Time: 

#
# Problem 1
#

def nestEggFixed(salary, save, growthRate, years):
    """
    - salary: the amount of money you make each year.
    - save: the percent of your salary to save in the investment account each
      year (an integer between 0 and 100).
    - growthRate: the annual percent increase in your investment account (an
      integer between 0 and 100).
    - years: the number of years to work.
    - return: a list whose values are the size of your retirement account at
      the end of each year.
    """
    results = [salary*save*0.01]
    for i in range(1,years):
        results += [results[i-1]*(1+0.01*growthRate)+salary*save*0.01]
    return results

def testNestEggFixed():
    print 'salary = 10000   save = 10   growthRate = 15   years = 5'
    salary     = 10000
    save       = 10
    growthRate = 15
    years      = 5
    savingsRecord = nestEggFixed(salary, save, growthRate, years)
    print savingsRecord
    # Output should have values close to:
    # [1000.0, 2150.0, 3472.5, 4993.375, 6742.3812499999995]
    
    print 'salary = 1000 save = 4 growthRate = 5 years = 3'

    salary     = 1000
    save       = 4
    growthRate = 5
    years      = 3
    savingsRecord = nestEggFixed(salary, save, growthRate, years)
    print savingsRecord
    # Output should have values close to:
    # [40.0, 82.0, 126,10]

#
# Problem 2
#

def nestEggVariable(salary, save, growthRates):
    """
    - salary: the amount of money you make each year.
    - save: the percent of your salary to save in the investment account each
      year (an integer between 0 and 100).
    - growthRate: a list of the annual percent increases in your investment
      account (integers between 0 and 100).
    - return: a list of your retirement account value at the end of each year.
    """
    results = [salary*save*0.01]
    for i in range(1,len(growthRates)):
        results += [results[i-1]*(1+0.01*growthRates[i])+salary*save*0.01]
    return results
    

def testNestEggVariable():
    salary      = 10000
    save        = 10
    growthRates = [3, 4, 5, 0, 3]
    savingsRecord = nestEggVariable(salary, save, growthRates)
    print savingsRecord
    # Output should have values close to:
    # [1000.0, 2040.0, 3142.0, 4142.0, 5266.2600000000002]


#
# Problem 3
#

def postRetirement(savings, growthRates, expenses):
    """
    - savings: the initial amount of money in your savings account.
    - growthRate: a list of the annual percent increases in your investment
      account (an integer between 0 and 100).
    - expenses: the amount of money you plan to spend each year during
      retirement.
    - return: a list of your retirement account value at the end of each year.
    """
    results = [savings * (1 + 0.01 *growthRates[0])-expenses]

    for i in range(1,len(growthRates)):
        results += [results[i-1] * (1 + 0.01 * growthRates[i]) - expenses]
    return results


def testPostRetirement():
    savings     = 100000
    growthRates = [10, 5, 0, 5, 1]
    expenses    = 30000
    savingsRecord = postRetirement(savings, growthRates, expenses)
    print savingsRecord
    # Output should have values close to:
    # [80000.000000000015, 54000.000000000015, 24000.000000000015,
    # -4799.9999999999854, -34847.999999999985]

#
# Problem 4
#

def findMaxExpenses(salary, save, preRetireGrowthRates, postRetireGrowthRates,
                    epsilon):
    """
    - salary: the amount of money you make each year.
    - save: the percent of your salary to save in the investment account each
      year (an integer between 0 and 100).
    - preRetireGrowthRates: a list of annual growth percentages on investments
      while you are still working.
    - postRetireGrowthRates: a list of annual growth percentages on investments
      while you are retired.
    - epsilon: an upper bound on the absolute value of the amount remaining in
      the investment fund at the end of retirement.
    """
    befRet = nestEggVariable(salary, save, preRetireGrowthRates) #outputs list before ret.
    low = 0
    high = befRet[-1]
    expenses = ((low + high)/2.0)
    guess = postRetirement(befRet[-1], postRetireGrowthRates, expenses)
    ctr = 1
    while (abs(guess[-1])) > epsilon and ctr <= 100:
        if guess[-1] > 0.0:
            low = expenses
        else:
            high = expenses
        expenses = ((low + high)/2.0)
        guess = postRetirement(befRet[-1], postRetireGrowthRates, expenses)
        ctr += 1
    assert ctr <= 100, 'max itterations reached'
    return expenses

def testFindMaxExpenses():
    salary                = 10000
    save                  = 10
    preRetireGrowthRates  = [3, 4, 5, 0, 3]
    postRetireGrowthRates = [10, 5, 0, 5, 1]
    epsilon               = .01
    expenses = findMaxExpenses(salary, save, preRetireGrowthRates,
                               postRetireGrowthRates, epsilon)
    print expenses
