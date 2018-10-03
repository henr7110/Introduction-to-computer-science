##answers = { 1.1:false, 1.2:false, 1.3:false, 1.3:false, 1.4:false, 1.5: false, 1.6:
##true, 1.7:true, 2.1:no, 2.2:yes, 3.1:6, 3.2:'''the function recursively sums up the numbers of an integer'''
##}

#4)

def first_N(n):
    counter = 0
    test = 1
    while counter < n:
        square = test**2.0
        if square % 1  == 0 and square % 2 != 0:
            print int(square)
            counter += 1
        test += 1

#6

def findSide():
    from math import sqrt

    area = input('enter the area')
    length = input('enter the length')
    adjacent_side = float(area/length)
    print adjacent_side

    
    
    
        
        
    


