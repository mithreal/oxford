# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 11:18:42 2017

@author: ulfgard
"""
import copy

def wordList(string):
    wordList = []
    testString = copy.deepcopy(string)
    spaces = testString.count(" ")
    words = spaces + 1
    i = 0
    while i < words:
        if i == spaces:
            endI = len(testString)+1
        else:
            endI = testString.find(" ")+1
        word = testString[0:(endI-1)]
        testString = testString[endI:]
        wordList.append(word)        
        i += 1
    return(wordList)
        
def compWordLists(sign, WL1, WL2): # string1 is 1st string, string2 is the comparison string
    matchData = []
    WL1_0 = copy.deepcopy(WL1)
    WL2_0 = copy.deepcopy(WL2)

    if sign == "Right":
        WL1_0 = copy.deepcopy(WL1)
        WL2_0 = copy.deepcopy(WL2)
        WL1 = WL2_0
        WL2 = WL1_0
    elif sign == "Left":
        WL1 = WL1_0
        WL2 = WL2_0
    else:
        return("Error - sign not specified")

    def getMatches(list1, list2):
        if len(list1) != len(list2):
            return({})
        L = len(list1)
        matchData = {}
        matchStrings = {}
        match = False
        matchTF = []
        matches = []
        matchList = []
        matchWord = ""
        matchNumber = 0
        matchPercentage = 0
        i = 0
        while i < (L):
#            print(i)
            word1 = list1[i]
            word2 = list2[i]
            if word1 == word2:
                matchNumber += 1
                match = True
                matchWord = word1
            else:
                match = False
                matchWord = None
 #           print("match:", match)
            matches.append(match)
            matchList.append(matchWord)
            i += 1
        matchPercentage = 100*(matchNumber/L)
        if matchPercentage != 0:
            matchData = {"matchList" : matchList, 
                         "matchPercentage" : matchPercentage, 
                         "matchNumber" : matchNumber}
#        print(matchData)
        return(matchData)


    def caseA(L, m, n, WL1, WL2):
        matchData = []
        localShift = 0
#        print("here")
        o1 = []
        o2 = []
        matchStrings = {}
        i = 0  
        while i < L:
            o1 = WL1[i:]
            o2 = WL2[:(L-i)]
#            print(o1, "\n", o2)
            matchInfo = getMatches(o1, o2)
#            print(matchInfo)
            if matchInfo != {}:
#                print(matchInfo["matchNumber"])
                if matchInfo["matchNumber"] != 0:
#                    print(True)
#                    matchInfo["shift"] = localShift
                    matchInfo["WL1"] = o1
                    matchInfo["WL2"] = o2
                    matchData.append(matchInfo)
#            print(i)
#            print(o1, "\n", o2)
#            print(matchInfo)
            i += 1
#        print(matchData)
        return(matchData)
        
    def caseB(L, m, n, WL1, WL2):
        matchData = []
        localShift = 0
        o1 = []
        o2 = []
        matchStrings = {}
        i = 0
        while i < L:
            sIndex1 = m - n + i
  #          print("sIndex1:",sIndex1)
            o1 = WL1[sIndex1:]
            o2 = WL2[:n-i]
#            l1 = len(o1)
#            l2 = len(o2)
#            print(l1, o1, "\n", l2, o2)
            matchInfo = getMatches(o1, o2)
            if matchInfo !={}:
#                print(True)
#                matchInfo["shift"] = localShift
                matchInfo["WL1"] = o1
                matchInfo["WL2"] = o2
#                print(matchInfo)
                matchData.append(matchInfo)
            i += 1
        return(matchData)

    def shiftMatch(WL1, WL2):
        testData = []
        dataContainer = []
        matchData = []
       # shift = 0  
#        print("start")
        if len(WL2) > 3:            
            shift = int(2*len(WL2)/3)
        else:
            shift = 0 
#        print("shift:", shift)
        i = 0
        while i < shift:
#            print("here")
            print("\n-----\ni",i)
            o2 = WL2[i:]
#            print(o2)
            m = len(WL1)
            n = len(o2)    
            localShift = i
            if m <= n:
                L = m
                case = "A"
            else:
                L = n
                case = "B"
            if case == "A":
                print("Case A")
                tempData = caseA(L, m, n, WL1, WL2)
            if case == "B":
                print("Case B")
                tempData = caseB(L, m, n, WL1, WL2)
#            print(type(tempData))
 #           print("tempData\n",tempData[0])
            if tempData[0] != []:
                if tempData[0] in testData:
                    print("degenerate data")
                else:
                    print("unique data")
                    testData.append(copy.deepcopy(tempData[0]))
                    dataX = tempData[0]
                    dataX["shift"] = localShift
                    print("dataX\n", dataX, "tempData[0]", tempData[0])
                    matchData.append(tempData[0])
                    
                
            print(tempData)



            i += 1  
        print("\ntestData:\n",testData)

        return(matchData)
        
    matchData = shiftMatch(WL1, WL2)
#    print("matchData", matchData)
    print("-----\n\n")   
    return(matchData)
    
def evaluateOverlap(matchData):
    if matchData == []:
        return(None)
    matchValues = {}
    variables = ["matchNumber", "shift", "matchPercentage"]
    def testVariable(testVar, matchData):
        i = 0
        L = len(matchData)
        print(L)
        matchSets = []
        matchHigh = 0
        matchIndex = 0    
        while i < L:
            evalData = matchData[i]
            print("testVar:", testVar)
            tempMatchNo = evalData[testVar]
            if tempMatchNo > matchHigh:
                matchHigh = tempMatchNo
                matchIndex = i
                tmp = (matchIndex, matchHigh)
                matchSets = [tmp]
                print(i, matchHigh)
            elif tempMatchNo == matchHigh:
                tmpOld = (matchIndex, matchHigh)
                tmpNew = (i, matchHigh)
                matchSets.append(copy.deepcopy(tmpOld))
                matchSets.append(copy.deepcopy(tmpNew))
                matchIndex = i
            i += 1
        return(matchSets, matchIndex, matchHigh)
    i = 0
    while i < 3:
        testVar = variables[i]
        print(testVar)
        result = testVariable(testVar, matchData)
        matchSets = result[0] 
        matchIndex = result[1]
        matchHigh = result[2]
        matchTMP = matchData[matchIndex]
        print(matchTMP)
        matchPer = matchTMP["matchPercentage"]
        if i == 0:
            if matchHigh == 0:
                return(None)
        if len(matchSets) == 1:
            if matchPer < 50:
                return(None)
            matchValues = matchData[matchIndex]
            return(matchValues)
        elif i == 2:
            if matchPer < 50:
                return(none)
            bestMatch = matchSet[0]
            bestMatch = bestMatch[0]
            print(bestMatch)
            matchValues = matchData[bestMatch]
        i += 1
    return(matchValues)
