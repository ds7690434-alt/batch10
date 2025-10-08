def fetch_number_from_string(s):
    """ this method we will split the string and return only  the float file
     the string in 'str: $ 32.39 ' format"""
    l = s.split("$")
    return float(l[1])