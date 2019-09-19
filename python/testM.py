# testlist = [test1,test3] #key
# #value = []
# #=>inputlist={test1:5,test3:3} 
# class unitTest:
#     def __init__(self):
#         print("init unitTest")
#     #private value = "     Awoo~", // 輸入值
#     def setValue(self, value):
#         self.value = value
#     #virtual expected // 預期得到的結果
#     def setExpected(self, expected):
#         self.expected = expected()
#     #obj TestCase: method
#     #obj virtual func(expected, trim(value)); // 經過 trim 後兩者必須相同
#     #obj result = areEqual(input,expected)
#
# class testfunc(unitTest.TestCase):
#     def __init__(self):
#         print("init testfunc")
#     self.value = self.setValue() #var value = "     Awoo~", // 輸入值
#     self.expected = self.setExpected();  # 預期得到的結果 
#     #result = unitTest.func(expected, trim(value)); // 經過 trim 後兩者必須相同 
#     #return result
from baicCond import mybasic as mybasic

def expected(func):
    var = func();
    return value

def areEqual(input,expected):
    if input == expected:
        return True
    else:
        return False

class TestMo:
    def __init__(self, index, start, targetVar):
        self.start = start
        # self.max = max
        self.index = index
        self.targetVar = targetVar
        self.Tcase110up=0
        self.Tcase110ups=0
        self.Tcase110upf=0
        self.Tcase110=0
    def mycondition(self):  
    #def mycondition(self, self.__index, self.__start, self.__targetVar):
        print("mycondition")
        print(self.index)
        print(self.start)
        print(self.targetVar)
    def myconditionSub1(self):  
    #def myconditionSub1(self, self.__index, self.__start, self.__targetVar):
        print("myconditionSub1")
        print(self.index)
        print(self.start)
        print(self.targetVar)
    def myconditionSub2(self):  
    #def myconditionSub2(self, self.__index, self.__start, self.__targetVar):   
        print("myconditionSub2")
        print(self.index)
        print(self.start)
        print(self.targetVar)

class cond5(TestMo):
    def __init__(self, index, start, tick_max_p, tick_end, tick_end_p, MTMn, MTMn_p, MTMRate, MTMRate_p, MTMMA, MTMMA_p, MTMMARate, MTMMARate_p, jval, jRate, jRate_p, dif, difRate, macd, macdRate, WRn, WRnRate, obv, obvRate, rsi3, rsi3Rate, rsi6, rsi6Rate, targetVar):
        TestMo.__init__(self, index, start, targetVar)  #super().__init__(index, start, targetVar)
        self.result1=False
        self.result2=False
        self.result3=False
        self.result4=False
        self.MTMn=MTMn
        self.MTMn_p=MTMn_p
        self.MTMRate=MTMRate
        self.MTMRate_p=MTMRate_p
        self.MTMMA=MTMMA
        self.MTMMA_p=MTMMA_p
        self.MTMMARate=MTMMARate
        self.MTMMARate_p=MTMMARate_p
        self.jval=jval
        self.jRate=jRate
        self.jRate_p=jRate_p
        self.dif=dif
        self.difRate=difRate
        self.macd=macd
        self.macdRate=macdRate
        self.WRn=WRn
        self.WRnRate=WRnRate
        self.obv=obv
        self.obvRate=obvRate
        self.rsi3=rsi3
        self.rsi3Rate=rsi3Rate
        self.rsi6=rsi6
        self.rsi6Rate=rsi6Rate
        self.tick_max_p=tick_max_p
        self.tick_end=tick_end
        self.tick_end_p=tick_end_p
    def mycondition(self):
        self.result1=mybasic.rateSlow(self.MTMRate_p, self.MTMRate)
    def myconditionSub1(self):
        #if (self.result1== True) and (self.dif>0) and (self.difRate>0):
        #if (self.result1== True) and (self.obvRate>0):
        #if( (self.result1== True) and (self.difRate>0) and (self.difRate-difRate_p)>=0) ):
        #if( (self.result1== True) and (self.jRate_p<0) and (self.jRate - self.jRate_p)>=0 ): #test case1
        self.result2 = mybasic.myCase2(self.jRate_p, self.jRate, self.MTMRate_p, self.MTMRate) #if( (self.result1== True) and  (mybasic.rateSlow(self.jRate_p, self.jRate)): #test case1
        #if (self.result1== True) and (self.rsi3Rate>0):  #test case2
        if (self.result2== True):
            #self.result2=True
            self.Tcase110up=1
        else:
            #self.result2=False
            self.Tcase110up=0
    def myconditionSub2(self):
        #if (self.result2== True) and (self.tick_end_p/self.tick_end>self.targetVar):
        if (self.result2== True) and (self.tick_max_p/self.tick_end>self.targetVar):
            self.Tcase110ups=1
            self.Tcase110upf=0
        else:
            self.Tcase110ups=0
            self.Tcase110upf=1
        # if (self.result2== True) and (self.tick_max_p/self.tick_end>self.targetVar):
        #     self.Tcase110up=1
        # else:
        #     self.Tcase110up=0
        #print("cond5 myconditionSub2============")

class cond4(TestMo):
    def __init__(self, index, start, tick_max_p, tick_end, tick_end_p, MTMn, MTMn_p, MTMRate, MTMRate_p, MTMMA, MTMMA_p, MTMMARate, MTMMARate_p, jval, jRate, jRate_p, dif, difRate, macd, macdRate, WRn, WRnRate, obv, obvRate, rsi3, rsi3Rate, rsi6, rsi6Rate, targetVar):
        TestMo.__init__(self, index, start, targetVar)  #super().__init__(index, start, targetVar)
        self.result1=False
        self.result2=False
        self.result3=False
        self.result4=False
        self.MTMn=MTMn
        self.MTMn_p=MTMn_p
        self.MTMRate=MTMRate
        self.MTMRate_p=MTMRate_p
        self.MTMMA=MTMMA
        self.MTMMA_p=MTMMA_p
        self.MTMMARate=MTMMARate
        self.MTMMARate_p=MTMMARate_p
        self.jval=jval
        self.jRate=jRate
        self.jRate_p=jRate_p
        self.dif=dif
        self.difRate=difRate
        self.macd=macd
        self.macdRate=macdRate
        self.WRn=WRn
        self.WRnRate=WRnRate
        self.obv=obv
        self.obvRate=obvRate
        self.rsi3=rsi3
        self.rsi3Rate=rsi3Rate
        self.rsi6=rsi6
        self.rsi6Rate=rsi6Rate
        self.tick_max_p=tick_max_p
        self.tick_end=tick_end
        self.tick_end_p=tick_end_p
    #def mycondition(self,self.__start,index,Sarray):
    def mycondition(self):
        #print("cond4 mycondition============")
        #if (  (self.MTMRate >0) and (self.MTMn- self.MTMMA) > 0 ): #(self.MTMn >0) and 
        #if (  (self.MTMn >0) and (self.MTMRate >0) ):
        #if (  (self.MTMn_p < self.MTMMA_p) and (self.MTMn > self.MTMMA) ):
        if (  (self.MTMRate_p<0) and (self.MTMRate - self.MTMRate_p)>=0 ): #test case1
        #if (  (self.MTMRate >0) ): #test case2
            self.result1=True
        else:
            self.result1=False
    def myconditionSub1(self):
        #if (self.result1== True) and (self.dif>0) and (self.difRate>0):
        #if (self.result1== True) and (self.obvRate>0):
        #if( (self.result1== True) and (self.difRate>0) and (self.difRate-difRate_p)>=0) ):
        if( (self.result1== True) and (self.jRate_p<0) and (self.jRate - self.jRate_p)>=0 ): #test case1
        #if (self.result1== True) and (self.rsi3Rate>0):  #test case2
        
            self.result2=True
            self.Tcase110up=1
        else:
            self.result2=False
            self.Tcase110up=0
    def myconditionSub2(self):
        #if (self.result2== True) and (self.tick_end_p/self.tick_end>self.targetVar):
        if (self.result2== True) and (self.tick_max_p/self.tick_end>self.targetVar):
            self.Tcase110ups=1
            self.Tcase110upf=0
        else:
            self.Tcase110ups=0
            self.Tcase110upf=1
        # if (self.result2== True) and (self.tick_max_p/self.tick_end>self.targetVar):
        #     self.Tcase110up=1
        # else:
        #     self.Tcase110up=0
        #print("cond4 myconditionSub2============")

class cond1(TestMo):
    # def __init__(self,index,start,max,min,end,cal_rocday,targetVar):
    def __init__(self, index, start, targetVar):
        TestMo.__init__(self, index, start, targetVar)  #super().__init__(index, start, targetVar)
        # self.Tcase110up=Tcase110up00[0]
        # self.Tcase110ups=Tcase110up00[1]
        # self.Tcase110upf=Tcase110up00[2]
        # self.Tcase110=Tcase110up00[3]
    def mycondition(self):
    #def mycondition(self, self.index, self.start, self.targetVar):  
        print("cond1 mycondition")
        print(self.Tcase110up)
        print(self.Tcase110ups)
        print(self.Tcase110upf)
        print(self.Tcase110)
        print(self.start)
        # if num >= 2:
        #     result[index]=True
        #     suc=suc+1
        #     print("suc=", suc)
        # else:
        #     result[index]=False
        if self.start >= 3:
            self.Tcase110up=True
            # suc=suc+1
            # print("suc=", suc)
        else:
            self.Tcase110up=False
    def myconditionSub1(self):
    #def myconditionSub1(self, self.index, self.start, self.targetVar):
        print("cond1 myconditionSub1")
        print(self.Tcase110up)
        print(self.Tcase110ups)
        print(self.Tcase110upf)
        print(self.Tcase110)
        print(self.start)
        if self.Tcase110up:
            self.Tcase110up=True
            self.Tcase110=True
            self.Tcase110upf=False
        else:
            self.Tcase110upf=True
    def myconditionSub2(self):
    #def myconditionSub2(self, self.index, self.start, self.targetVar):
        print("cond1 myconditionSub2")
        print(self.Tcase110up)
        print(self.Tcase110ups)
        print(self.Tcase110upf)
        print(self.Tcase110)
        print(self.start)
        if self.Tcase110up:
            self.Tcase110=True

class cond3(TestMo):
    def __init__(self, index, start, jRate, macd, macdRate, WRn, WRnRate, MTMn, MTMRate, MTMMA, MTMMARate, rsi3, rsi3Rate, rsi6, rsi6Rate, tick_end, tick_end_p, targetVar):
        TestMo.__init__(self, index, start, targetVar)  #super().__init__(index, start, targetVar)
        self.result1=False
        self.result2=False
        self.result3=False
        self.result4=False
        self.jRate=jRate
        self.macd=macd
        self.macdRate=macdRate
        self.WRn=WRn
        self.WRnRate=WRnRate
        self.MTMn=MTMn
        self.MTMRate=MTMRate
        self.MTMMA=MTMMA
        self.MTMMARate=MTMMARate
        self.rsi3=rsi3
        self.rsi3Rate=rsi3Rate
        self.rsi6=rsi6
        self.rsi6Rate=rsi6Rate
        self.tick_end=tick_end
        self.tick_end_p=tick_end_p
    #def mycondition(self,self.__start,index,Sarray):
    def mycondition(self):
        print("cond3 mycondition")
        if (self.start > 0 ) and (self.jRate>0):
            self.result1=True
        else:
            self.result1=False
    def myconditionSub1(self):
        if (self.result1== True) and (self.macd>0) and (self.macdRate>0):
            self.result2=True
            self.Tcase110up=1
        else:
            self.result2=False
    def myconditionSub2(self):
        if (self.result2== True) and (self.tick_end_p/self.tick_end>self.targetVar):
            self.Tcase110ups=1
            self.Tcase110upf=0
        else:
            self.Tcase110ups=0
            self.Tcase110upf=1
        print("cond3 myconditionSub2")

class cond2(TestMo):
    def __init__(self, index, start, biasRate_p, tick_max, tick_end, tick_end_p, targetVar):
        TestMo.__init__(self, index, start, targetVar)  #super().__init__(index, start, targetVar)
        self.result1=False
        self.result2=False
        self.result3=False
        self.result4=False
        self.start_p=biasRate_p
        self.tick_max=tick_max
        self.tick_end=tick_end
        self.tick_end_p=tick_end_p
    #def mycondition(self,self.__start,index,Sarray):
    def mycondition(self):
        print("cond2 mycondition")
        if (self.start-self.start_p) > 0:
            self.result1=True
            self.Tcase110up=1
        else:
            self.result1=False
            self.Tcase110up=0
    def myconditionSub1(self):
    #def myconditionSub1(self,self.__start,index,Sarray):
        if (self.result1== True) and (self.tick_max-self.tick_end_p>self.targetVar):
            self.result2=True
            self.Tcase110ups=1
            self.Tcase110upf=0
        else:
            self.result2=False
            self.Tcase110ups=0
            self.Tcase110upf=1
    def myconditionSub2(self):
    #def myconditionSub2(self,self.__start,index,Sarray):
        if (self.result1== True) and (self.tick_end-self.tick_end_p>self.targetVar):
            self.Tcase110=1
        else:
            self.Tcase110=0
        print("cond2 myconditionSub2")

class cond8(TestMo):
    #def __init__(self, index, start, targetVar):
    def __init__(self, index, start, start_p, weekWRn2, weekWRn2_p, resultWR_week, Weektick_max, Weektick_end_n, Weektick_end, result, targetVar):
        TestMo.__init__(self, index, start, targetVar)  #super().__init__(index, start, targetVar)
        self.result1=False
        self.result2=False
        self.result3=False
        self.result4=False
        self.start_p=start_p
        self.weekWRn2=weekWRn2
        self.weekWRn2_p=weekWRn2_p
        self.resultWR_week=resultWR_week
        self.Weektick_max=Weektick_max
        self.Weektick_end_n=Weektick_end_n
        self.Weektick_end=Weektick_end
        self.result=result
    def mycondition(self):
        print("cond8 mycondition")
        #if self.start<-60:
        if self.resultWR_week<=5:
            self.result1=True
        else:
            self.result1=False
    def myconditionSub1(self):
        if (self.result1== True) and (self.weekWRn2-self.weekWRn2_p<0):
            self.result2=True
        else:
            self.result2=False
    def myconditionSub2(self):
        if (self.result2== True) and self.start-self.start_p<0:
            self.result3=True
        else:
            self.result3=False
    def myconditionSub3(self):
        if (self.result3== True) and self.weekWRn2<-60:
            self.result4=True
        else:
            self.result4=False
    def myconditionSub4(self):
        #if (self.result1== True):
        if (self.result4== True) and self.start<-60:
            self.Tcase110up=1
        else:
            self.Tcase110up=0
    def myconditionSub5(self):
        #if (self.Tcase110up== True):
        if (self.Tcase110up== 1) and ( (self.Weektick_max/self.Weektick_end)>self.targetVar ):
            self.Tcase110ups=1
            self.Tcase110upf=0
        else:
            self.Tcase110ups=0
            self.Tcase110upf=1
    def myconditionSub6(self):
        #if (self.Tcase110up== 1):
        if (self.Tcase110up== 1) and ( (self.Weektick_end_n/self.Weektick_end)>self.targetVar ):
            self.Tcase110=1
        else:
            self.Tcase110=0

class cond9(TestMo):
    #def __init__(self, index, start, targetVar):
    def __init__(self, index, start, start_p, weekWRn2, weekWRn2_p, resultWR_week, Weektick_max, Weektick_end_n, Weektick_end, targetVar):
        TestMo.__init__(self, index, start, targetVar)  #super().__init__(index, start, targetVar)
        self.result1=False
        self.result2=False
        self.result3=False
        self.result4=False
        self.start_p=start_p
        self.weekWRn2=weekWRn2
        self.weekWRn2_p=weekWRn2_p
        self.resultWR_week=resultWR_week
        self.Weektick_max=Weektick_max
        self.Weektick_end_n=Weektick_end_n
        self.Weektick_end=Weektick_end
    def mycondition(self):
        print("cond3 mycondition")
        #if self.start<-60:
        if self.resultWR_week<=5:
            self.result1=True
        else:
            self.result1=False
    def myconditionSub1(self):
        if (self.result1== True) and (self.weekWRn2-self.weekWRn2_p<0):
            self.result2=True
        else:
            self.result2=False
    def myconditionSub2(self):
        if (self.result2== True) and self.start-self.start_p<0:
            self.result3=True
        else:
            self.result3=False
    def myconditionSub3(self):
        if (self.result3== True) and self.weekWRn2<-60:
            self.result4=True
        else:
            self.result4=False
    def myconditionSub4(self):
        #if (self.result1== True):
        if (self.result4== True) and self.start<-60:
            self.Tcase110up=1
        else:
            self.Tcase110up=0
    def myconditionSub5(self):
        #if (self.Tcase110up== True):
        if (self.Tcase110up== 1) and ( (self.Weektick_max/self.Weektick_end)>self.targetVar ):
            self.Tcase110ups=1
            self.Tcase110upf=0
        else:
            self.Tcase110ups=0
            self.Tcase110upf=1
    def myconditionSub6(self):
        #if (self.Tcase110up== 1):
        if (self.Tcase110up== 1) and ( (self.Weektick_end_n/self.Weektick_end)>self.targetVar ):
            self.Tcase110=1
        else:
            self.Tcase110=0
            
class Testd:

    def __init__(self, foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print('__bar')

if __name__ == '__main__':
    # test = Testd('hello')
    # test._Testd__bar()
    # print(test._Testd__foo)
    aa=cond1(2,50,100)
    aa.mycondition()
    aa.myconditionSub1()
    print(aa.Tcase110up)
    print("--------------------------------end Test1")
    bb=cond2(2,1,100)
    bb.mycondition()
    bb.myconditionSub1()
    print(aa.Tcase110up)