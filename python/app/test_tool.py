import unittest
import tool
import time
import datetime
import mock
#from unittest.mock import patch

class TestStockTool(unittest.TestCase):
    def setUp(self):
        self.stockTool=tool.stockTool()
        
        
        now = datetime.datetime.today()
        # stocknmber='3661'E
        # num=[]
        # num = self.stockTool.fetch_from(20,8,2019)
        # print(num)
        #self.url ='http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date='+str(num[0]) +'&stockNo='+ stocknmber + '&_=' +str(time.mktime(now.timetuple()))
        self.url = 'http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=20190809&stockNo=3661&_=1548124490.0'
        #print(url)#http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=20181109&stockNo=1101&_=1548124490.0
        print('In setUp()')

    def tearDown(self):
        print('In tearDown()')

    def test_gennumArr(self):
        self.assertEqual('20190820',tool.gennumArr(20,8,2019) )
        self.assertEqual('',tool.gennumArr(20,8,1911) )
        self.assertEqual('',tool.gennumArr(20,-1,2019) )
        self.assertEqual('20191028',tool.gennumArr(-1,10,2019) )

    def test_fetch_from(self):
        self.assertEqual(['20190826', '20190926'],self.stockTool.fetch_from(20,8,2019) )
        
    def test_comna(self):
        dict={}
        conect=-1
        
        conect, dict=self.stockTool.comna(self.url)
        self.assertEqual(0,conect)
        #self.assertNotEqual(0, self.stockTool.comna(self.url) )

    # def test_catchM1(self):
    #     dict={}
    #     conect=-1
    #     catch=-1
    #     
    #     conect, dict=self.stockTool.comna(self.url)
    #     catch=self.stockTool.test_catch(dict)
    #     self.assertEqual(0, catch)
    # def test_catchFail(self):
    #     dict={}
    #     conect=-1
    #     catch=-1
    #     self.url = 'http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=20181109&stockNo=1597&_=1548124490.0'
    #     conect, dict=self.stockTool.comna(self.url)
    #     catch=self.stockTool.test_catch(dict)
    #     self.assertEqual(-1, catch) 
#use suite:

#use mock:
    def test_catchM1(self):
        catch=-1

        #conect, dict=self.stockTool.comna(self.url)
        mock_thing = mock.MagicMock()
        mock_thing.return_value = {"data":[["108/08/01","1,625,161","165,460,861","100.00","104.00","99.60","101.50","+0.50","1,293"]]}
        catch=self.stockTool.test_catch(mock_thing()  )
        self.assertEqual(0, catch)
    def test_catchFail(self):
        catch=0

        mock_thing = mock.MagicMock()
        mock_thing.return_value = {"sta":[["108/08/01","1,625,161","165,460,861","100.00","104.00","99.60","101.50","+0.50","1,293"]]}
        catch=self.stockTool.test_catch(mock_thing()  )
        self.assertEqual(-1, catch)
        
if __name__ == '__main__':
    unittest.main(verbosity=2)