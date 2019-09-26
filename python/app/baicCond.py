class mybasic:
    def rateSlow(past,now): #test case1
        result=False
        if (  (past<0) and (now - past)>=0 ):
            result=True
        else:
            result=False
        return result

    def myCase2(past, now, Rate_p, Rate): #test case2
        result=False
        if ( rateSlow(Rate_p, Rate) ) and ( rateSlow(past,now) ):
            result=True
        else:
            result=False
        return result

    def TarMax(tick_max,tick_end_p, targetVar):
        result=False
        if (self.tick_max/self.tick_end_p>targetVar):
            result=True
        else:
            result=False
        return result
    def TarEnd(tick_end,tick_end_p, targetVar):
        result=False
        if (self.tick_end/self.tick_end_p>targetVar):
            result=True
        else:
            result=False
        return result