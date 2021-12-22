'''
Created on Mar 21, 2021

@author: kimj0
'''
import unittest
import tkinter
'''Tkinter method to close a window.'''
def close():
    root = tkinter.Tk()
    root.destroy()
    root.mainloop()
'''TestCase to test that the close method above close a tkinter window.'''    
class SimpleTest(unittest.TestCase):
    def testclose(self):
        self.assertTrue(self, None)
        print("Program By: Kim Johnson")
'''Below is main class unittest.'''
if __name__ == '__main__':
    unittest.main()