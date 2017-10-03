"""
Module for currency exchange

This module provides several string parsing functions to implement a 
simple currency exchange routine using an online currency service. 
The primary function in this module is exchange.

ALANNA FISCHER (AEF222)
9/27/17
"""
##some of the work is from me (aef222) when I took CS1110 last year as well as
##some help from consulting hours 


import cornell


#PART  A

def before_space(s):
    """Returns: Substring of s; up to, but not including, the first space
    Parameter s: the string to slice
    Precondition: s has at least one space in it"""
    space = s.index(" ")
    return s[0:space]


def after_space(s):
    """Returns: Substring of s after the first space
    Parameter s: the string to slice
    Precondition: s has at least one space in it"""
    space = s.index(" ")
    return s[space+1:]


#PART B

def first_inside_quotes(s):
    """Returns: The first substring of s between two (double) quote characters
    Parameter s: a string to search
    Precondition: s is a string with at least two (double) quote characters
    inside."""
    x=s.find('"')
    y=s.index('"',x+1)
    inner=s[x+1:y]
    return inner


def get_lhs(json):
    """Returns: The LHS value in the response to a currency query.
    Parameter json: a json string to parse
    Precondition: json is the response to a currency query"""
    first = json.index("lhs")
    last=json[first+4:]
    return first_inside_quotes(last)


def get_rhs(json):
    """The RHS value in the response to a currency query.
    Parameter json: a json string to parse
    Precondition: json is the response to a currency query"""
    second = json.index("rhs")
    tail=json[second+4:]
    return first_inside_quotes(tail)


def has_error(json):
    """Returns: True if the query has an error; False otherwise.
    Parameter json: a json string to parse
    Precondition: json is the response to a currency query"""
    error_index = json.index('error')
    err_msg_start = error_index + 6
    t1=first_inside_quotes(json[err_msg_start:])
    return t1 != ''


#PART C

def currency_response(currency_from, currency_to, amount_from):
    """
    Returns: a JSON string that is a response to a currency query.
    
    A currency query converts amount_from money in currency currency_from 
    to the currency currency_to. The response should be a string of the form
    
        '{"success":true, "lhs":"<old-amt>", "rhs":"<new-amt>", "error":""}'
    
    where the values old-amount and new-amount contain the value and name for the 
    original and new currencies. If the query is invalid, both old-amount and 
    new-amount will be empty, while "success" will be followed by the value false.
    
    Parameter currency_from: the currency on hand (the LHS)
    Precondition: currency_from is a string
    
    Parameter currency_to: the currency to convert to (the RHS)
    Precondition: currency_to is a string
    
    Parameter amount_from: amount of currency to convert
    Precondition: amount_from is a float
    """
   
    f = cornell.urlread('http://cs1110.cs.cornell.edu/2017fa/a1server.php?src='\
                        +currency_from+'&dst='+currency_to+'&amt='\
                        +str(amount_from))
    return f


#PART D

def iscurrency(currency):
    """
    Returns: True if currency is a valid (3 letter code for a) currency. 
    It returns False otherwise.

    Parameter currency: the currency code to verify
    Precondition: currency is a string.
    """
    return not has_error(currency_response(currency, currency, 1.0))


def exchange(currency_from, currency_to, amount_from):
    """Returns: amount of currency received in the given exchange.

    In this exchange, the user is changing amount_from money in currency 
    currency_from to the currency currency_to. The value returned represents the 
    amount in currency currency_to.

    The value returned has type float.

    Parameter currency_from: the currency on hand (the LHS)
    Precondition: currency_from is a string for a valid currency code
    
    Parameter currency_to: the currency to convert to (the RHS)
    Precondition: currency_to is a string for a valid currency code
    
    Parameter amount_from: amount of currency to convert
    Precondition: amount_from is a float"""
    
    f=cornell.urlread('http://cs1110.cs.cornell.edu/2017fa/a1server.php?src='\
                      +currency_from+'&dst='+currency_to+'&amt='\
                      +str(amount_from))
    x=get_rhs(f)
    z=before_space(x)
    a=float(z)
    return a