#this is a toolbox for the project that will allow us to use functions equivalent to native functions in python
def uppercase(string:str)->str:
    STRING=""
    for i in string:
        if ord(i) in range(97,123):
            i=chr(ord(i)-32)
        STRING+=i
    return STRING
def remove_value(lst, val)->list:
    return [item for item in lst if item != val]