"""
Unit test for module a1

When run as a script, this module invokes several procedures that 
test the various functions in the module a1.

ALANNA FISCHER (AEF222)
9/27/17
"""

import cornell
import a1

def testA(): 
    #These test cases are for before_space and attempt to capture all
    #possibilities when the program is exceuted 
    #Test Case 1.1
    result = a1.before_space('0.8963 Euros')
    cornell.assert_equals('0.8963', result)
    #Test Case 1.2
    result = a1.before_space('1167.1167 Iraqi Dinars       ')
    cornell.assert_equals('1167.1167', result)
     #Test Case 1.3
    result = a1.before_space('1 Bermudan       Dollar')
    cornell.assert_equals('1', result)
     #Test Case 1.4
    result = a1.before_space('2 Barbadian Dollars')
    cornell.assert_equals('2', result)
    #Test Case 1.5
    result = a1.before_space('                2 Barbadian Dollars')
    cornell.assert_equals('', result)
    #Test Case 1.6
    result = a1.before_space(' ')
    cornell.assert_equals('', result)
    
    #These test cases are for after_space and attempt to capture all
    #possibilities when the program is exceuted 
    #Test Case 1.7
    result = a1.after_space('.078 United States Dollars')
    cornell.assert_equals('United States Dollars',result)
    #Test Case 1.8
    result = a1.after_space('.078 ')
    cornell.assert_equals('',result)
    #Test Case 1.9
    result = a1.after_space(' .078 United States Dollars')
    cornell.assert_equals('.078 United States Dollars',result)
    #Test Case 1.10
    result = a1.after_space('8.988 Iranian Rial')
    cornell.assert_equals('Iranian Rial',result)
    #Test Case 1.11
    result = a1.after_space('Bermudan       Dollar')
    cornell.assert_equals('      Dollar', result)
    #Test Case 1.12
    result = a1.after_space(' ')
    cornell.assert_equals('', result)
    
    
def testB():
    #These test cases are for first_inside_quotes and attempt to capture all
    #possibilities when the program is exceuted 
    #Test Case 2.1
    result = a1.first_inside_quotes('A "B C" D')
    cornell.assert_equals('B C', result)
    #Test Case 2.2
    result = a1.first_inside_quotes('A    "B C"    D "E F"    G')
    cornell.assert_equals('B C', result)
     #Test Case 2.3
    result = a1.first_inside_quotes('A      J "HELLO" D K')
    cornell.assert_equals('HELLO', result)
     #Test Case 2.4
    result = a1.first_inside_quotes('A B "HELLO" K "B C" L     ')
    cornell.assert_equals('HELLO', result)
     #Test Case 2.5
    result = a1.first_inside_quotes('A B "" K "B C" L     ')
    cornell.assert_equals('', result)
    #Test Case 2.6
    result = a1.first_inside_quotes('A B "" C D')
    cornell.assert_equals('', result)
    #Test Case 2.6
    result = a1.first_inside_quotes('"A B C D"')
    cornell.assert_equals('A B C D', result)

    

    
    #These test cases are for get_lhs and attempt to capture all
    #possibilities when the program is exceuted
    #Test Case 2.7
    result = a1.get_lhs('{"success":true, "lhs":"2 United States Dollars",\
                        "rhs":"1.825936 Euros", "error":""}')
    cornell.assert_equals('2 United States Dollars', result)
     #Test Case 2.8
    result = a1.get_lhs('{ "success" : true, "lhs" : "1 United States Dollar",\
                        "rhs" : "3.672878 United Arab Emirates Dirhams",\
                        "error" : "" }')
    cornell.assert_equals('1 United States Dollar', result)
     #Test Case 2.9
    result = a1.get_lhs('{ "success" : true, "lhs" : "1 United States Dollar",\
                        "rhs" : "478.16 Armenian Drams", "error" : "" }')
    cornell.assert_equals('1 United States Dollar', result)
     #Test Case 2.10
    result = a1.get_lhs('{ "success" : false, "lhs" : "", "rhs" : "", "error" : "Source currency code is invalid." }')
    cornell.assert_equals('', result)
  
    #These test cases are for get_rhs and attempt to capture all
    #possibilities when the program is exceuted
    #Test Case 2.11
    result = a1.get_rhs('{ "success" : true, "lhs" : "1 United States Dollar",\
                        "rhs" : "3.672878 United Arab Emirates Dirhams",\
                        "error" : "" }')
    cornell.assert_equals('3.672878 United Arab Emirates Dirhams', result)
    #Test Case 2.12
    result = a1.get_rhs('{ "success" : true, "lhs" : "1 United States Dollar",\
                        "rhs" : "478.16 Armenian Drams", "error" : "" }')
    cornell.assert_equals('478.16 Armenian Drams', result)
    #Test Case 2.13
    result=a1.get_rhs('{ "success" : true, "lhs" : "1 United States Dollar",\
                      "rhs" : "1.25541 Australian Dollars", "error" : "" }')
    cornell.assert_equals('1.25541 Australian Dollars', result)
    #Test Case 2.14
    result=a1.get_rhs('{ "success" : false, "lhs" : "", "rhs" : "", "error" : "Exchange currency code is invalid." }')
    cornell.assert_equals('', result)
  
    
    #These test cases are for has_error and attempt to capture all
    #possibilities when the program is exceuted
    #Test Case 2.12
    result = a1.has_error('{"success":false, "lhs":"1.5 United States Dollars",\
                          "rhs":"6083.576325 Mongolian Tugrik",\
                          "error":"Source currency code is invalid."}')
    cornell.assert_equals(True, result)
    #Test Case 2.16
    result = a1.has_error('{ "success" : false, "lhs" : "", "rhs" : "", "error"\
                          : "Exchange currency code is invalid." }')
    cornell.assert_equals(True, result)
    #Test Case 2.17
    result = a1.has_error('{ "success" : true, "lhs" : "2.5 United States Dollars", "rhs" : "2.0952375 Euros", "error" : "" }')
    cornell.assert_equals(False, result)
    
    
    
def testC():
    #These test cases are for currency_response and attempt to capture all
    #possibilities when the program is exceuted
    #Test Case 3.1
    result = a1.currency_response('USD', 'EUR', 2.5)
    cornell.assert_equals('{ "success" : true, "lhs" : "2.5 United States Dollars", "rhs" : "2.0952375 Euros", "error" : "" }',result)
    #Test Case 3.2
    result = a1.currency_response('USA', 'EUR', 2.5)
    cornell.assert_equals('{ "success" : false, "lhs" : "", "rhs" : "", "error" : "Source currency code is invalid." }',result) 
    #Test Case 3.3
    Result = a1.currency_response('', 'EUR', 2.5)
    cornell.assert_equals('{ "success" : false, "lhs" : "", "rhs" : "", "error" : "Source currency code is invalid." }',result)
    #Test Case 3.4
    Result = a1.currency_response('USD', '', 2.5)
    cornell.assert_equals('{ "success" : false, "lhs" : "", "rhs" : "", "error" : "Source currency code is invalid." }',result)
def testD():
    #These test cases are for iscurrency and attempt to capture all
    #possibilities when the program is exceuted
    #Test Case 4.1
    result=a1.iscurrency('USD')
    cornell.assert_equals(True,result)
    #Test Case 4.2
    result=a1.iscurrency('AEP')
    cornell.assert_equals(False,result)
    #Test Case 4.3
    result=a1.iscurrency(' ')
    cornell.assert_equals(False,result)
    #Test Case 4.4
    result=a1.iscurrency('USD USA')
    cornell.assert_equals(False,result)
    
    #These test cases are for exchange and attempt to capture all
    #possibilities when the program is exceuted
    #Test Case 4.5
    result=a1.exchange('USD', 'EUR', 2.5)
    cornell.assert_floats_equal(2.0952375, result)
    #Test Case 4.6
    result=a1.exchange('USD', 'SDG', 2.5)
    cornell.assert_floats_equal(16.6931475, result)
    #Test Case 4.7
    result=a1.exchange('ETB', 'DOP', 1.0)
    cornell.assert_floats_equal(2.0149176591594, result)



testA()
testB()
testC()
testD()
print ("Module a1 passed all tests")