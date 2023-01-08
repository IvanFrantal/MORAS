# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 18:22:32 2022

@author: frant
"""



"""
a = "(moj string) A + B + C + D"

#ideja je da nađeš dio gdje provjeravas jel 1. odnosno nulti string (
# i ubacis uvijet da mora zadnji biti ) i ako je gotovo
 

label = a[1:].split(")")[0]
label1 = a.split(")")[1]

labelneki = a.split(")")
print(labelneki)

print(label)
print(label1)
"""

# ----------------------------------

#neka ideja
# sigurno ces trebati gledati pocinje li ti sa $
# pa ces gledati ostale stvari
# tipa rastavis si ovako $ --> MV --> (A,B)
"""


MVstring = "$MV(12,54)"
MVstrArg1 = MVstring.split(",")[0].split("(")[1]
MVstrArg2 = MVstring.split(",")[1].split(")")[0]

#print(MVstrArg1)
#print(MVstrArg2)

MVmainString = "$MV({},{})".format(MVstrArg1, MVstrArg2)

if MVmainString == MVstring:
    print("@{}".format(MVstrArg1))
    print("D=M")
    print("@{}".format(MVstrArg2))
    print("M=D")
    
    
# ---------------------------



SWPstring = "$SWP(45,100)"
SWPstrArg1 = SWPstring.split(",")[0].split("(")[1]
SWPstrArg2 = SWPstring.split(",")[1].split(")")[0]

#print(SWPstrArg1)
#print(SWPstrArg2)

SWPmainString = "$SWP({},{})".format(SWPstrArg1, SWPstrArg2)

if SWPmainString == SWPstring:
    print("@{}".format(SWPstrArg1))
    print("D=M")
    print("@R0")
    print("M=D")
    
    print("@{}".format(SWPstrArg2))
    print("D=M")
    print("@{}".format(SWPstrArg1))
    print("M=D")
    
    print("@R0")
    print("D=M")
    print("@{}".format(SWPstrArg2))
    print("M=D")
    

# ---------------------------
    

SUMstring = "$SUM(29,111)"
SUMstrArg1 = SUMstring.split(",")[0].split("(")[1]
SUMstrArg2 = SUMstring.split(",")[1].split(")")[0]

#print(SUMstrArg1)
#print(SUMstrArg2)

SUMmainString = "$SUM({},{})".format(SUMstrArg1, SUMstrArg2)

if SUMmainString == SUMstring:
    print("@R0")
    print("D=M")
    print("@{}".format(SUMstrArg1))
    print("M=D")
    print("@{}".format(SUMstrArg2))
    print("D=M")
    print("@{}".format(SUMstrArg1))
    print("M=D+M")
    
"""    
    

line = "$MV(50,10)"

linesplit = line.split("(")[0]
print(linesplit + "\n")

arg1 = line.split(",")[0].split("(")[1]
arg2 = line.split(",")[1].split(")")[0]

print(arg1)
print(arg2)



    
    