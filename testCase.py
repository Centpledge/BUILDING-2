import sentiment_mod as s

class testCase():
    def testMod(self,outResult,expectedResult1,expectedResult2 = None):
        if outResult == expectedResult1 or outResult ==expectedResult2:
            print "OK"
        else :
            print "ERROR"
            
testCase().testMod(s.sentiment("computer science"),"comSc","art")
