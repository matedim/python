#-------------------------------------------------------------------------------
# Name:        модуль1
# Purpose:
#
# Author:      GerasimenkoDA
#
# Created:     01.10.2014
# Copyright:   (c) GerasimenkoDA 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

def main():
    pass

if __name__ == '__main__':
    main()
import random
die1=random.randint(1,6)
#die2=random.randint(1,6)
die2=random.randrange(6)+1
total=die1+die2
print("При вашем броске выпало", die1,"и", die2, "очков, в сумме",total)
input("\n\nНажмите Enter, чтобы выйти")
