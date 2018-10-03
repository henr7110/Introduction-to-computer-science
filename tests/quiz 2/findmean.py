
def findMedian(L):

    if len(L) == 0:
        raise ValueError('list is empty')
    elif len(L) == 1:
        return L[0]
    elif len(L) == 2:
        return (L[0]+L[1])/2
    else:
        return findMedian(L[1:-1])
def test():
    l1 = [1.0]
    print 'testing' , l1
    print findMedian(l1)
    l2 = [1.0,2.0]
    print 'testing' , l2
    print findMedian(l2)
    l3 = [1.0,2.0,3.0,4.0,5.0]
    print 'testing' , l3
    print findMedian(l3)
    l4 = [1.0,2.0,3.0,4.0,5.0,6.0,7.0]
    print 'testing' , l4
    print findMedian(l4)
