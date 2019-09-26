import requests
#import numpy as np
from bs4 import BeautifulSoup
import datetime
import time
import json
import urllib.parse
#from os import listdir


stocknmber='3661'
num=[]
#num = fetch_from(20,9,2019)
#url ='http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date='+str(num[ind]) +'&stockNo='+ stocknmber + '&_=' +str(time.mktime(now.timetuple()))
#print(url)#http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=20181109&stockNo=1101&_=1548124490.0

#genneral numArr
def gennumArr(startday,startmonth,startyear):
    #handle_data:
    # if (type(startyear)=="int"):
    #     print("type int")
    #     tmp_year=str(startyear)

    #  if (type(startday)=="int"):
    #     print("type int")
    #     if startday==0:
    #         tmp_day='28'
    #     else:
    #         tmp_day=str(startday)

    #  if (type(startmonth)=="int"):
    #     print("type int")
    #     if (startmonth)/10<1:
    #         tmp_month="0"+str(startmonth)
    #     else:
    #         tmp_month=str(startmonth)

    if startmonth<=0:
        print("the input value of month is error")
        return ""
    if startyear<=1911:
        print("the input value of year is error")
        return ""

    if startday<=0:
        tmp_day='28'
    elif (startday > 0) and (startday<10):
        tmp_day="0"+str(startday)
    else:
        tmp_day=str(startday)
    # else:
    #     if startday > 28:
    #         tmp_day='28'
    #     else:
    #         #tmp_day=str(startday)
    #         if (startday)/10<1:
    #             tmp_day="0"+str(startday)
    #         else:
    #             tmp_day=str(startday)

    if (startmonth > 0) and (startmonth<10):    #if (startmonth)/10<1:
        tmp_month="0"+str(startmonth)
    else:
        tmp_month=str(startmonth)

    tmp_year=str(startyear)
    #casDate:numArr2.append(casDate(year,month,day))
    num_tmp=[]
    num_tmp=[tmp_year,tmp_month,tmp_day]
    #print(num_tmp)
    #tmpstr=''.join(num_tmp)

    #numArr2.append(''.join(num_tmp))

    #print("gennumArr:")
    #print(''.join(num_tmp))
    #print(type(''.join(num_tmp)))
    #print(numArr2)
    return (''.join(num_tmp))

class baicA:
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

class stockTool(object):
    def __init__(self):
        print("stockTool init:")
        pass

    def test_catch(self, data_dict):
        catch=-1
        try:
            len1=len(data_dict['data'])
            #print("len of data_dict['data']={}".format(len1))
            if len1 > 0:
                #print("catch success")
                catch=0
            else:
                print("catch fail!")
            return catch
        except:
            print("catch fail!")
            return catch
            
    
    def comna(self, url):
        try:
            data_dict={}
            conect=-1
    
            list_req= requests.get(url)
            #print(list_req) #<Response [200]>
            if list_req=="200":
            #if list_req=="<Response [200]>":
                print("conect success")
            soup = BeautifulSoup(list_req.content, "html.parser")
            #print(soup)
            #print(soup.text)
            #getjson=json.loads(soup.text)
            #print(getjson)
            #print(type(getjson))
            #data_dict=getjson
            data_dict=json.loads(soup.text)
            #print(data_dict)
            #print(type(data_dictB))
            #print(data_dictB['data'])
            # for xtd in range(0,len(data_dict['data'][0])):
            #     for xts in range(0,len(data_dict['data'][0][0])):
            #         data_list.append(data_dict['data'][xtd][xts])
            #save_month_txt(data_dict,stocknmber,tmpfilename)
            conect = 0 #conect = test_catch(data_dict)
        except:
            print("conect fail!")
        return conect, data_dict
        
    # def fetch_from(self, year: int, month: int):
    #     for year, month in self._month_year_iter(month, year, today.month, today.year):
    #         self.raw_data.append(self.fetcher.fetch(year, month, self.sid))
    #         self.data.extend(self.raw_data[-1]['data'])
    #     return self.data
    def fetch_from(self, start_day: int, start_month: int, start_year: int):
    #def fetch_from(self, start_day, start_month, start_year):
        """Genneral Arr from year, month, day to current"""
        numArr=[]
        iyear=start_year
        imonth=start_month
        # print("fetch_from_init:")
        # print(start_year)
        # print(start_month)
        # print(start_day)
        try:
            while(iyear<=datetime.datetime.today().year):
                # print("start")
                if (iyear==datetime.datetime.today().year) and (imonth==datetime.datetime.today().month):
                    # print("stage1")
                    if (start_day==datetime.datetime.today().day):
                        break
                    numArr.append(gennumArr(datetime.datetime.today().day,imonth,iyear))
                    break
                else:
                    # print("stage2")
                    # print(iyear)
                    # print(imonth)
                    # print(datetime.datetime.today().day)
                    # tmp=gennumArr(datetime.datetime.today().day,imonth,iyear)
                    # print(tmp)
                    numArr.append(gennumArr(datetime.datetime.today().day,imonth,iyear))
                    # print(numArr)
                    imonth=imonth+1
                    if imonth>12:
                        iyear=iyear+1
                        imonth=1
        
            #numArr.append(gennumArr(start_day,start_month,start_year))
            #print("fetch_from:")
            #print(numArr)
            #print(type(numArr))
            return numArr
        except:
            print("Genneral Arr for date error")
            return [0]
    
    def getstock(self, stocknmber,num):
        catchwaitTime=5
        conect_fail_number=[]
        fullCatch=-1
    #start
        print(range(0,len(num)))
        for ind in range(0,len(num)):
            print("\n")
            #data_title=[]
            data_dict={}
            conect=-1
            catch=-1
    
            print("cirle=%d" % int(ind))
            params = {"date":num[ind],"stockNo":stocknmber}
            #params = {"date":"20181209","stockNo":"1101"}
            print(params)
            # print('\n')
            #print("numberZZ=%s" % (NoA[ind]))
    
            # num_tmp=[]
            # num_tmp=[str(datetime.datetime.today().year),tmp_month,str(datetime.datetime.today().day)]
            # #print(num_tmp)
            # num[2]=''.join(num_tmp)
            # print(num)
        
            time.sleep(catchwaitTime)
    
            url ='http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date='+str(num[ind]) +'&stockNo='+ stocknmber + '&_=' +str(time.mktime(now.timetuple()))       
            conect = comna(url)    #conect=comna(url)
            failtest=0
            if conect<0:
                failtest=failtest+1
                if failtest>=3:
                    conect_fail_number.append(stocknmber)
                    break
            catch=test_catch(data_dict)    # catch=test_catch()
            if catch<0:
                catch_fail_number.append(stocknmber)
                break
            else:
                #save_tmpmonth_txt(data_dict,stocknmber,tmpfilename)
                pass
        fullCatch=0
        return fullCatch