# create class
class IOString():
    # constructor to set default value
    def __init__(self):
        self.str1 = " "

    # function to get input from users
    def get_string(self):
        self.str1 = input('enter string : ')

    # function to print the string in upper case
    def print_upper(self):
        print('result iz : ' , self.str1.upper())   
    def print_string_cap(self):
        print('result iz : ' , self.str1.capitalize())


#object creation
str1 = IOString()


# call functions
str1.get_string()
str1.print_upper()
str1.print_string_cap()
