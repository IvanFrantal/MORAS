# -*- coding: utf-8 -*-
"""
Created on Sun Jan  1 16:12:58 2023

@author: frant
"""

def _parse_macros(self, line):
    
    if not line[0] == "$":
        return
    
    else:
    
        arg1 = line.split(",")[0].split("(")[1]
        arg2 = line.split(",")[1].split(")")[0]
        

        if line.split("(")[0] == "$MV":
    
            MVstring = "$MV({},{})".format(arg1,arg2)
            
            MVstrArg1 = MVstring.split(",")[0].split("(")[1]
            MVstrArg2 = MVstring.split(",")[1].split(")")[0]
            
            MVmainString = "$MV({},{})".format(MVstrArg1, MVstrArg2)
            
            MVprint = "@{}".format(MVstrArg1) + "\n"
            + "D=M" + "\n"
            + "@{}".format(MVstrArg2) + "\n"
            + "M=D"
        
            if MVmainString == MVstring:
                return MVprint
        

# -------------------------------------------------------
    
        elif line.split("(")[0] == "$SWP":
            
            SWPstring = "$SWP({},{})".format(arg1,arg2)
            
            SWPstrArg1 = SWPstring.split(",")[0].split("(")[1]
            SWPstrArg2 = SWPstring.split(",")[1].split(")")[0]
            
            SWPmainString = "$SWP({},{})".format(SWPstrArg1, SWPstrArg2)
            
            SWPprint = "@{}".format(SWPstrArg1) + "\n"
            + "D=M" + "\n" 
            + "@R0" + "\n" 
            + "M=D" + "\n" 
            + "@{}".format(SWPstrArg2) + "\n" 
            + "D=M" + "\n" 
            + "@{}".format(SWPstrArg1) + "\n"
            + "M=D" + "\n"
            + "@R0" + "\n"
            + "D=M" + "\n"
            + "@{}".format(SWPstrArg2) + "\n"
            + "M=D"
            
            if SWPmainString == SWPstring:
                return SWPprint
    
        
# --------------------------------------------------------
        elif line.split("(")[0] == "$SUM":
            
            SUMstring = "$SUM({},{})".format(arg1,arg2)
            
            SUMstrArg1 = SUMstring.split(",")[0].split("(")[1]
            SUMstrArg2 = SUMstring.split(",")[1].split(")")[0]
            
            SUMmainString = "$SUM({},{})".format(SUMstrArg1, SUMstrArg2)
            
            SUMprint = "@R0" + "\n"
            + "D=M" + "\n"
            + "@{}".format(SUMstrArg1) + "\n"
            + "M=D" + "\n"
            + "@{}".format(SUMstrArg2) + "\n"
            + "D=M" + "\n"
            + "@{}".format(SUMstrArg1) + "\n"
            + "M=D+M"
            
            if SUMmainString == SUMstring:
                return SUMprint
            
            
        else: return "This macro does not exist"