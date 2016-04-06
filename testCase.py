import sentiment_mod as s

class testCase():
    def testMod(self,outResult,expectedResult1,expectedResult2 = None):
        if outResult == expectedResult1 :
            print "OK"
            print outResult
            print " "
            
        else :
            print "ERROR"
            print outResult
            print " "
s.showWord()
testCase().testMod(s.sentiment("first object "),"art") #OK
testCase().testMod(s.sentiment("art"),"art")# OK
testCase().testMod(s.sentiment("mechanical "),"comSc") # OK
testCase().testMod(s.sentiment("aesthetic social public   "),"art")#OK
testCase().testMod(s.sentiment("integrated  less useful   "),"comSc") #OK
testCase().testMod(s.sentiment("logical single short  "),"comSc") #OK
testCase().testMod(s.sentiment("traditional able "),"art")#OK
testCase().testMod(s.sentiment("traditional able "),"comSc")#ERROR
testCase().testMod(s.sentiment("great  further "),"art")#OK
testCase().testMod(s.sentiment("great  further "),"comSc")#ERROR
testCase().testMod(s.sentiment(" notable material same required  "),"comSc") # 3.6 3.6 3.8 3.8
testCase().testMod(s.sentiment("object able "),"comSc")# 3.3 3.6 ERROR
testCase().testMod(s.sentiment("object same "),"comSc") # 3.3 3.8 ERROR
testCase().testMod(s.sentiment("object logical "),"comSc") #3.3 4.8  OK
testCase().testMod(s.sentiment("object step "),"comSc") #3.3 4.5 OK
testCase().testMod(s.sentiment("traditional step "),"comSc") # 3.6 4.5 OK
testCase().testMod(s.sentiment("special popular object "),"comSc") # 3.2 3.2 3.3 OK
testCase().testMod(s.sentiment("mechanical latter twentieth "),"comSc") # 15.8 6.0 6.0 ERROR
testCase().testMod(s.sentiment("complete traditional controversial "),"comSc")# 11.9 3.6 3.6 ERROR
testCase().testMod(s.sentiment("special material less"),"comSc")#  OK
testCase().testMod(s.sentiment("integrated less great "),"comSc") #OK
testCase().testMod(s.sentiment("art logical single short    "),"comSc") # ERROR 1art 3comSc
testCase().testMod(s.sentiment("art logical single short same    "),"comSc") # OK 1art 4comSc
