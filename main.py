import unittest
from selenium import webdriver
import page # a file that I created

class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(r"C:\Users\paulk\Desktop\Selenium")
        self.driver.get("http://www.python.org")
        driver = self.driver

    def test_example(self): #if any method starts with "test_"
        print("Test")
        assert True
    
    def not_a_test(self):
        print("this will not print")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
        unittest.main()