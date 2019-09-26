from baicCond import mybasic as mybasic

class CalMo2:
    def __init__(self, index, start, jRate, jRate_p, targetVar):  #super().__init__(index, start, targetVar):
        print("CalMo2 __init__")
        self.start = start
        # self.max = max
        self.index = index
        self.targetVar = targetVar
        self.Tcase110up=0
        self.Tcase110ups=0
        self.Tcase110upf=0
        self.Tcase110=0
        self.jRate=jRate
        self.jRate_p=jRate_p
    #def mycondition(self,self.__start,index,Sarray):
    def case1(self, Mnow, Mpast):
        self.result1=mybasic.rateSlow(self.Mpast, self.Mnow)
    def case2(self, Mnow, Mpast):
        self.result2 = mybasic.myCase2(self.jRate_p, self.jRate, self.Mpast, self.Mnow)
        if (self.result2== True):
            #self.result2=True
            self.Tcase110up=1
        else:
            #self.result2=False
            self.Tcase110up=0
    def case3(self):
        #if (self.result2== True) and (self.tick_end_p/self.tick_end>self.targetVar):
        if (self.result2== True) and (self.tick_max_p/self.tick_end>self.targetVar):
            self.Tcase110ups=1
            self.Tcase110upf=0
        else:
            self.Tcase110ups=0
            self.Tcase110upf=1

class CalMo:
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
        print(self.index+self.start+self.targetVar)
    def myconditionSub1(self):  
    #def myconditionSub1(self, self.__index, self.__start, self.__targetVar):
        print("myconditionSub1")
        print(self.start-self.index-self.targetVar)
    def myconditionSub2(self):  
    #def myconditionSub2(self, self.__index, self.__start, self.__targetVar):   
        print("myconditionSub2")
        print(self.start*self.index*self.targetVar)
        
class cond4(CalMo):
    def __init__(self, index, start, tick_max_p, tick_end, targetVar):
        CalMo.__init__(self, index, start, targetVar)  #super().__init__(index, start, targetVar)
        self.result1=False
        self.result2=False
        self.tick_max_p=tick_max_p
        self.tick_end=tick_end
    def mycondition(self):
        if (self.start/self.targetVar>=0): #test case1
            self.result1=True
        else:
            self.result1=False
    def myconditionSub1(self):
        if ( (self.result1== True) and  (self.tick_max_p/self.targetVar)>=0 ): #test case1
            self.result2=True
            self.Tcase110up=1
        else:
            self.result2=False
            self.Tcase110up=0
    def myconditionSub2(self):
        if (self.result2== True) and (self.tick_end/self.targetVar>self.targetVar):
            self.Tcase110ups=1
            self.Tcase110upf=0
        else:
            self.Tcase110ups=0
            self.Tcase110upf=1

class cond5(CalMo):
    def __init__(self, index, start, tick_max_p, tick_end, tick_end_p, MTMn, MTMn_p, MTMRate, MTMRate_p, MTMMA, MTMMA_p, MTMMARate, MTMMARate_p, jval, jRate, jRate_p, dif, difRate, macd, macdRate, WRn, WRnRate, obv, obvRate, rsi3, rsi3Rate, rsi6, rsi6Rate, targetVar):
        CalMo.__init__(self, index, start, targetVar)  #super().__init__(index, start, targetVar)
        self.result1=False
        self.result2=False
        self.result3=False
        self.result4=False
        self.MTMn=MTMn
        self.MTMn_p=MTMn_p
        self.Mnow=MTMRate
        self.Mpast=MTMRate_p
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
        self.result1=False
        self.Mnow=Mnow
        self.Mpast=Mpast
        print(self.index)
        self.index=3
        print(self.index)
        #print("cond4 mycondition============")
        if (  (self.Mpast<0) and (self.Mnow - self.Mpast)>=0 ): #test case1
        #if (  (self.Mnow >0) ): #test case2
            self.result1=True
        else:
            self.result1=False
        return self.result1
    def myconditionSub1(self):
        self.result1=False
        self.Mnow=Mnow
        self.Mpast=Mpast
        print(self.index)
        self.index=5
        print(self.index)
        #print("cond4 myconditionSub1============")
        if (  (self.Mpast<0) and (self.Mnow - self.Mpast)>=0 ): #test case1
        #if (  (self.Mnow >0) ): #test case2
            self.result1=True
        else:
            self.result1=False
        return self.result1
    def myconditionSub2(self):
        #if (self.result2== True) and (self.tick_end_p/self.tick_end>self.targetVar):
        if (self.result2== True) and (self.tick_max_p/self.tick_end>self.targetVar):
            self.Tcase110ups=1
            self.Tcase110upf=0
        else:
            self.Tcase110ups=0
            self.Tcase110upf=1
        #print("cond4 myconditionSub2============")