import unittest
from selenium import webdriver
import page # a file that I created

class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(r"C:\Users\paulk\Desktop\Selenium\Selenium101")
        self.driver.get("http://www.python.org")

    def test_example(self): #if any method starts with "test_"
        print("Test")
        assert True
    
    def not_a_test(self):
        print("this is true")

    def tearDown(self):
        self.driver.close()

    if __name__ == "__main__":
        unittest.main()