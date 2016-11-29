# lab07.py
# YOUR NAME(S) AND NETID(S) HERE
# Initial skeleton by W. White (WMW2)
# October 7, 2015
"""Functions for Lab 7"""


def lesser_than(thelist,value):
    """Returns:  number of elements in thelist strictly less than value
    
    Example:  lesser_than([5, 9, 1, 7], 6) evaluates to 2
    
    Parameter thelist: the list to check (WHICH SHOULD NOT BE MODIFIED)
    Precondition: thelist is a list of ints
    
    Parameter value:  the value to compare to the list
    Precondition:  value is an int"""
    assert type(value)==int and type(thelist)==list
    n=0
    for x in thelist:
        if value<x:
            n=n+1
    return n


def uniques(thelist):
    """Returns: The number of unique elements in the list. 
    
    Example: unique([5, 9, 5, 7]) evaluates to 3
    Example: unique([5, 5, 1, 'a', 5, 'a']) evaluates to 3
    
    Parameter thelist: the list to check (WHICH SHOULD NOT BE MODIFIED)
    Precondition: thelist is a list."""
    assert type(thelist)==list
    list2=[]
    for x in thelist:
        if x is not in list2:
            list2.append(x)
    return len(list2)
    
    for x in thelist:
        if list2.count(x)==1:
           print x
        else
          print list2.append(x)
    return len(list2)


def clamp(thelist,min,max):
    """Modifies the list so that every element is between min and max.
    
    Any number in the list less than min is replaced with min.  Any number
    in the list greater than max is replaced with max. Any number between
    min and max is left unchanged.
    
    This is a PROCEDURE. It modified thelist, but does not return a new list.
    
    Example: if thelist is [-1, 1, 3, 5], then clamp(thelist,0,4) changes
    thelist to have [0,1,3,4] as its contents.
    
    Parameter thelist: the list to modify
    Precondition: thelist is a list of numbers (float or int)
    
    Parameter min: the minimum value for the list
    Precondition: min <= max is a number
    
    Parameter max: the maximum value for the list
    Precondition: max >= min is a number"""
    assert type(thelist)==list
    assert max>=min
    for x in thelist:
        pos=thelist.index(x)
        if x> max:
            thelist.remove(x)
            x= max
            thelist.insert(pos,x)
        elif x<min:
            thelist.remove(x)
            x=min
            thelist.insert(pos,x)
    return thelist