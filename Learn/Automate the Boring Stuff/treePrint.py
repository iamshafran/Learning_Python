"""

     *
    ***
   *****
  *******
 *********
***********

"""


def treePrint(symbol, height):
    for i in range(1,height+1):
        if i == 1:
            print(' ' * int(height) + (symbol * i))
        print(' ' * int(height - i) + (symbol * (i * 2)) + symbol)


treePrint('+', 20)
