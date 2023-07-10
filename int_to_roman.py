class Solution(object):
    def __init__(self,integer):
        self.integer=integer
    def conver(self):
        roman_list={
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
        }
        result=''
        for value,symbol in roman_list.items():
             while self.integer>=value:
                 result+=symbol
                 self.integer-=value
        return result           

            

        
 

print("Integer to roman calcultaor upto 1000:",end="\n")
y=input("Enter the integer")
y=int(y)
x=Solution(y)
print("Answer:"+" "+ x.conver())