#TRICKY BUT REAL EASY PYTHON CODE
# PRINT 0 IF NUM IS DIVISIBLE BY 5 ELSE PRINT 1
# THE CONDITION IS YOU ONLY HAVE THE KNOWLEDGE OF OPERATORS (+,-,*,%,**,//); PRINT STATEMENTS AND INPUT STATEMENTS

# TAKING IN A RANDOM NUMBER NUM
from math import floor


num = 19


rem = num %5
rem = rem + 4
floor_division_result  = rem // 5
print(floor_division_result)
