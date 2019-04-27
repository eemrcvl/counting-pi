import os 
import numpy as np
import pandas as pd

def countDigits(pidigits):
    ls=list(map(int,pidigits))
    values=[0,0,0,0,0,0,0,0,0,0] #values of digits, initialized to zero 
    for i in ls:
        values[i-1] = values[i-1] + 1 #iterate through the digits and if the number is found increment the index of the number
                                        #e.g. if value is 0 then increment zero in the values list      
    return pd.Series(values,['0','1','2','3','4','5','6','7','8','9'])

file=open('pi.txt','r')
pi=file.read()
pidigits=pi.split(".")[1]  
print(countDigits(pidigits))

