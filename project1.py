import logging, sys
logging.basicConfig(level=logging.ERROR)  
def collatz(number): 
    if number % 2 == 0:
       return number // 2
    elif number % 2 != 0:
         return 3 * number + 1
try:
    num = int(input('Enter the integer value: '))
    if num < 1:
        raise ValueError
        sys.exit()
    while num != 1:
          num = collatz(num)
          print(num)
except (TypeError, ValueError):
          logging.error('The value you inter is not an integer or Number must be positive')
     
    


 
 
