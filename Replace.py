"""
* author - ${USER}
* date - ${11/23/2020}
* time - ${3:30 pm}
* package - ${PACKAGE_NAME}
* Title - Replace of Username by using User Input
"""

import re
from os import name
class Valid_name :
    def __init__(self):
        self.name= name
    def method(self) :
        regex_name=re.compile(r"^[A-za-z]{1}[a-z]{2}$")
        k= regex_name.search(self.name)
        s = 'Hello <<UserName>>, How are you?'
        num1 = input('enter User Name')
        str_new = s.replace('UserName', num1)
        print(str_new)
        if k:
            print('valid')
        else:
            print('Invalid')
if __name__=='__main__' :
    try :
        object=Valid_name()
        object.method()
    except :
        print("Exception occured")



