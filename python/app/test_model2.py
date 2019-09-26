import unittest
import model2

class TestM2(unittest.TestCase):
    def setUp(self):
        self.CalMo=model2.CalMo(1,2,2)
        self.cond4=model2.cond4(1,2,2,12,0)
        self.CalMo2=model2.CalMo2(1,2,2)
        print('In setUp()')


    def tearDown(self):
        print('In tearDown()')
    #basic test:
    # def test_CalMo_m1(self):
    #     self.assertNotEqual(3, self.CalMo.mycondition())
    # def test_CalMo_m2(self):
    #     self.assertNotEqual(3, self.CalMo.myconditionSub1())
    # def test_CalMo_m3(self):
    #     self.assertNotEqual(3, self.CalMo.myconditionSub2())

    #test for baicCond.py
    def test_CalMo2_m1(self):
        self.assertNotEqual(3, self.CalMo2.rateSlow(4,5))
    def test_CalMo2_m2(self):
        self.assertNotEqual(3, self.CalMo2.case2(3,5))

    #test for use super()      
    # def test_cond4_m1(self):
    #     self.assertNotEqual(3, self.cond4.mycondition())
    #result=>can't correct find the parameter which does not exist 
    def test_cond4_m2(self):
        self.assertNotEqual(3, self.cond4.myconditionSub1())
    
if __name__ == '__main__':
    unittest.main(verbosity=2)