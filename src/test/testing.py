'''
Created on Feb 25, 2021

@author: kimj0
'''
import unittest
import sys; sys.argv = ['', 'Test.testArray']
from CovidProject.Controller.Reader1 import remove




class Test(unittest.TestCase):

    '''test created to test the remove method works correctly'''
    def testArray(self):
        self.assertEquals(remove)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testArray']
    unittest.main()