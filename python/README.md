# Python unitest
mock（中文是模仿，但我幾乎沒看到有人用中文來稱呼他），這部分我的解讀是，因為程式內所有的動作不見得都是我們所撰寫的，有些可能是引用第三方套件或他人所撰寫的程式，其實我們沒有必要為他寫個測試等等，而是用Mock的機制去簡單模擬有跑過那個外掛的Function的方式，也就是去模仿那個Function有作動的意思。
[Python 文章收集] 用 Mock 來做 Python Unit Test: http://puremonkey2010.blogspot.com/2017/08/python-mock-python-unit-test.html 
example.py
def func1(x): 
return x**2 

def func2(x): 
return func1(x) + x*5

tests.py
import unittest 
from example import func1, func2 

class ExampleTest(unittest.TestCase): 
"""Test example 
""" 
def test_func2(self): 
self.assertEqual(func2(5), 50) 
self.assertEqual(func2(-5), 0)
在 example 這個模組中 func2 中 會呼叫 func1 並加上 x*5 然後回傳結果，如果要對 func2 做單元測試時，要先確定 func1 這支函式是正確如預期的運作，test_func2 中的 assertEqual 才能成立。在簡單的程式中這樣做自然不是問題，但如果 func1 變得很複雜且又有使用到其他函數時，要怎麼保證 func2 在測試時不會受到 func1 的影響呢？這時候就可以利用 mock 來將我們的目標獨立開來。
"""Test example for mocking 
""" 
@mock.patch('example.func1') 
def test_func2(self, mock_func1): 
mock_func1.return_value = 0 
self.assertEqual(func2(5), 25) 
mock_func1.return_value = 10 
self.assertEqual(func2(-5), -15) 
1. 利用 mock 將 example module 中 func1 替換成 mock_func1，之後在 fun2 中碰到 func1 的時候就會變成使用 mock_func1
2. 而在這裡我們定義 mock_func1.return_value = 0，也就是之後不管 func1 的輸入是什麼都只會回傳 0 這個值
3. 藉由這樣的方式就可以把 func1 獨立開來，只要確認 func2 的邏輯是否有符合我們的目標
[Python] 測試雙刀，unittest 和 mock: https://medium.com/bryanyang0528/python-api%E6%B8%AC%E8%A9%A6%E5%9F%BA%E6%9C%AC%E5%8A%9F-unittest-%E5%92%8C-mock-401701399043 

*unitest+CI/CD+ Day 3 Pyramid 專案說明: https://ithelp.ithome.com.tw/articles/10199740 
Python 單元測試（Unit Testing）: https://imsardine.wordpress.com/tech/unit-testing-in-python/ 
首先用 self-test code 做簡單的測試：
class Calculator:
def mod(self, dividend, divisor):
remainder = dividend % divisor
quotient = (dividend - remainder) / divisor
return quotient, remainder

if __name__ == '__main__':
cal = Calculator()
assert cal.mod(5, 3) == (1, 2) # 5 / 3 = 1 ... 2
assert cal.mod(8, 4) == (1, 0) # 8 / 4 = 2 ... 0
改成 unittest 的寫法：
import unittest

class Calculator:

def mod(self, dividend, divisor):
remainder = dividend % divisor
quotient = (dividend - remainder) / divisor
return quotient, remainder

class CalculatorTest(unittest.TestCase): 1

def test_mod_with_remainder(self): 2
cal = Calculator()
self.assertEqual(cal.mod(5, 3), (1, 2)) 3

def test_mod_without_remainder(self):
cal = Calculator()
self.assertEqual(cal.mod(8, 4), (1, 0)) 4

def test_mod_divide_by_zero(self):
cal = Calculator()
assertRaises(ZeroDivisionError, cal.mod, 7, 1) 5

if __name__ == '__main__':
unittest.main() 6
1 只要繼承自 unittest.TestCase 即可，類別名稱沒有特別要求，但通常會在後面串上 Test。
2 以 test 開頭的方法都會被視為 test method，分別代表不同的 test case。
3 用 TestCase.assert*() 來做檢查。下面會說明它跟直接用 assert 來做驗證有什麼差別。
4 這裡故意寫成 (1, 0)，是為了產生 test failure。
5 用 TestCase.assertRaises() 來驗證呼叫某個 function 必須丟出 exception。這裡故意少寫了 self.，是為了產生 test error。
6 透過 unittest.main() 可以執行同一 module 裡所有的 test case
Python Tutorial 第六堂（1）使用 unittest 單元測試:　http://www.codedata.com.tw/python/python-tutorial-the-6th-class-1-unittest/ 
unittest 模組主要包括四個部份：
測試案例（Test case）測試的最小單元。
測試設備（Test fixture）執行一或多個測試前必要的預備資源，以及相關的清除資源動作。
測試套件（Test suite）一組測試案例、測試套件或者是兩者的組合。
測試執行器（Test runner）負責執行測試並提供測試結果的元件。
測試套件
根據測試的需求不同，你可能會想要將不同的測試組合在一起，例如，CalculatorTestCase 中可能有數個 test_xxx 方法，而你只想將 test_plus 與 test_minus 組裝為一個測試套件的話，可以如下：
suite = unittest.TestSuite()
suite.addTest(CalculatorTestCase('test_plus'))
suite.addTest(CalculatorTestCase('test_minus'))
如果想要自動載入某個 TestCase 子類別中所有 test_xxx 方法，可以如下：
unittest.TestLoader().loadTestsFromTestCase(CalculatorTestCase)
也可以將許多測試套件再全部組合為另一個測試套件：
suite1 = module1.TheTestSuite()
suite2 = module2.TheTestSuite()
alltests = unittest.TestSuite([suite1, suite2])
測試執行器
你可以在程式碼中直接使用 TextTestRunner，例如：
suite = (unittest.TestLoader()
.loadTestsFromTestCase(CalculatorTestCase))
unittest.TextTestRunner(verbosity=2).run(suite)
或者是透過 unittest.main 函式來執行： 
unittest.main(verbosity=2)
(django unnitest Django 1.6 最佳实践: 如何正确进行 Unit Tests: http://www.weiguda.com/blog/31/ , https://code.ziqiangxuetang.com/django/django-test.html )
*mock.patch: https://medium.com/@Sean_Hsu/testing-in-python-feat-django-%E4%B8%80-%E5%96%AE%E5%85%83%E6%B8%AC%E8%A9%A6%E5%8F%8A%E5%8A%9F%E8%83%BD%E6%B8%AC%E8%A9%A6%E7%AF%87-94d68ef465e3 




輕鬆學習 Python：透過操控瀏覽器擷取網站資料: https://medium.com/datainpoint/python-essentials-web-scraping-with-selenium-638175f839ee 
Python Selenium 自動測試網頁: https://www.itread01.com/content/1549614440.html, https://docs.seleniumhq.org/docs/03_webdriver.jsp#introducing-the-selenium-webdriver-api-by-example
Global — 把webdriver放在Python的安裝目錄=>假設我把Python安裝在 C:\Users\NorthBei\Documents\python3.6，那麼就把下載的webdriver解壓縮得到的.exe檔放在這個資料夾內 https://medium.com/@NorthBei/在windows上安裝python-selenium-簡易教學-eade1cd2d12d
自動測試指令碼，多用於regression testing
caps = DesiredCapabilities.INTERNETEXPLORER
caps['requireWindowFocus'] = True
driver_ie="C:\\Users\\yaqi.zhang\\Downloads\\\IEDriverServer_Win32_2.42.0\\IEDriverServer.exe";
driver=webdriver.Ie(driver_ie,capabilities=caps)
一般用來尋找tag的語句如下
我所用到的所有庫
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from selenium.common.exceptions import NoSuchElementException 

by_name
driver.find_element_by_name('btnOK').click()

by_id
driver.find_element_by_id('btnOK').click()

by_xpath
driver.find_element_by_xpath("//input[@value='Save']").click()

在table中選擇
tr=driver.find_element_by_xpath("//tbody[@id='ListBody']/tr[1]")
td=tr.find_elements(By.TAG_NAME, "td")[2]

if td.text =='':
return 

通過css選元素
tr = driver.find_element_by_css_selector('tr.Selectable')
tr.click()
time.sleep (sleep_sec)

處理Alter
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def AcceptAlert(driver):
try:
WebDriverWait(driver, 3).until(EC.alert_is_present(),
'Timed out waiting for PA creation ' +
'confirmation popup to appear.')

alert = driver.switch_to_alert()
alert.accept()
print ("alert accepted")
except TimeoutException:
print ("no alert")

處理彈出的其他視窗
main_window_handle = None
while not main_window_handle:
main_window_handle = driver.current_window_handle
driver.find_element_by_name('CMD_TEMPLATES').click()
time.sleep(sleep_sec)
signin_window_handle = None
while not signin_window_handle:
for handle in driver.window_handles:
if handle != main_window_handle:
signin_window_handle = handle
break
driver.switch_to.window(signin_window_handle)
driver.find_element_by_name('bcnClose').click()
driver.switch_to.window(main_window_handle)

所尋找的網頁元素不存在
try:
tr = driver.find_element_by_css_selector('tr.Selectable')
tr.click()
time.sleep (sleep_sec)

tr=driver.find_element_by_xpath("//tbody[@id='ListBody']/tr[1]")
td=tr.find_elements(By.TAG_NAME, "td")[2]

if td.text =='':
print('There is no policy')
return 

else:

tr.click()
time.sleep (sleep_sec_short)

driver.find_element_by_name('btnOK').click() 
print('Choose existing policy')

except NoSuchElementException:
print('there is no item')
return
Selenium, pyvirtualdisplay: 利用 Python 做網頁自動化測試 https://medium.com/@jemmy1234/%E5%88%A9%E7%94%A8-python-%E5%81%9A%E7%B6%B2%E9%A0%81%E8%87%AA%E5%8B%95%E5%8C%96%E6%B8%AC%E8%A9%A6-902d6361b4e3 
訂定測試頁面和項目
2. 測試項目 — 就是想要測試的東西，例如:登入按鈕，XX統記表，頁面選單等。
3. 測試功能 — 想要測試的功能，例如:登入功能，字樣顯示，按鈕功能等。
4. 前置作業 — 就是在測試這個功能前需要先做完的工作。例如有一些功能
要等登入後才能測試，這時候就可以把測試登入功能的測試編號直接填寫在這，代表一定要等登入功能測試通過才需要繼續進行本項測試，否則就可以直接略過了。
5. 測試手法 — 要怎麼測試這項功能。如果是按鈕的話可以直接寫按下按鈕，如果是下拉選單的話，可以寫說先按下此下拉選單後再點選第N項。
6. 預期結果 — 如果依照前面的測試手法，沒意外的話應該會出現一符合的結果，可以用描述性文字寫在這裡。
7. 測試結果 — 如果有符合前一項預期結果的話，這裡就會填上通過，否則填上失敗。
將程式移至Jenkins
其實這一步不是必須的，會這樣做的原因是因為我希望這個測試程式可以每天定時跑一次，畢竟每天都有新的 commit 產生，誰也無法保證今天測試沒問題的結果明天會不會就失敗了，因此最好的方法就是直接把測試程式送上 Jenkins 並設定每天定時執行。而我在 Jenkins 上的設定很簡單，就是直接開一個專案後，時間到時直接執行 shell script ，讀取我的 python 程式後即開始進行網頁自動測試，最後產生出來的測試報告再放置到一公開資料夾中，讓所有人皆可以透過網路方式 (FTP / HTTP …) 方式進行下載。
而在這裡我有遇到一個大問題，就是我在 Jenkins 上，若手動執行Python程式，所有的測試皆會順利跑完，但是如果讓 Jenkins自動執行時，Python程式在打開瀏覽器時就會掛掉了。後來原因查了很久，才知道說對於 Ubuntu 或其他 Linux-base 系統，背景執行的程式理論上應無法直接操作介面，所以當然瀏覽器也無法被開啟。而就是因為這個原因，我才會再加上 pyVirtualDisplay這個套件，利用它來開啟一個虛擬的 headless 瀏覽器，於是就不會牽扯到 Ubuntu 的介面操作問題。
跨浏览器测试介绍: https://developer.mozilla.org/zh-CN/docs/Learn/Tools_and_testing/Cross_browser_testing/Introduction
使用selenium做自動化測試常見問題 ：https://kknews.cc/code/yexq52g.html
1、selenium中如何判斷元素是否存在？
答：isElementPresent

2、selenium中hidden或者是display ＝ none的元素是否可以定位到？
答：不可以定位到

3、自動化測試的時候是不是需要連接資料庫做數據校驗？
答：UI自動化不需要，接口測試會需要

4、webdriver可以用來做接口測試嗎？
答：有一定難度，不推薦做接口測試

5、如何去定位頁面上動態加載的元素？
答：觸發動態加載元素的事件，直至動態元素出現，進行定位

6、如何去定位屬性動態變化的元素？
答：xpath或者css通過同級、父級、子級進行定位

7、點擊連結以後，selenium是否會自動等待該頁面加載完畢？
答：會的等待該頁面加載完的

8、自動化測試用例從哪裡來？
答：手工用例中抽取出來，可以參考自動化用例的執行策略

9、你覺得自動化測試最大的缺陷是什麼？
答：不穩定、可靠性、不易維護、成本與收益不成正比

10、什麼是分層測試？
答：UI測試、集成/接口測試、單元測試這些都可以算做分層測試
