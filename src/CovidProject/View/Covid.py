'''
Created on Feb 19, 2021

@author: kimj0
'''
import csv
import tkinter
from tkinter import Button
from tkinter import Label
from tkinter import messagebox
from tkinter import Text
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    pass
'''Creates a new window for graphs'''
def NewWin():
    root = tkinter.Tk()
    root.geometry("600x600")
    root.wm_title("GRAPHS")
    labelwin = tkinter.Label(root,text="SELECT A GRAPH BY CLICKING ON A BUTTON BELOW" ,fg='blue')
    labelwin.pack(side='top',padx=5,pady=5)
    btnga = Button(root,text="Graph English Province Names and Province Id",command=GA)
    btnga.pack(side='top',padx =5 , pady =5)
    btnga1 = Button(root,text="Graph English Province Names and NumDeaths", command=GA1)
    btnga1.pack(side='top',padx=5, pady=5)
    btnga2 = Button(root,text="Graph English Province Names and Dates",command=GA2)
    btnga2.pack(side='top',padx=5,pady=5)
    btnga3 = Button(root,text="Graph English Province Names and NumToday",command=GA3)
    btnga3.pack(side='top',padx=5,pady=5)
    btnga4 = Button(root,text="Graph English Province Names and RateTotal",command=GA4)
    btnga4.pack(side='top',padx=5,pady=5)
    btnga5 = Button(root,text="Graph French Province Names and Province Id",command=GA5)
    btnga5.pack(side='top',padx=5,pady=5)
    btnga6 = Button(root,text="Graph French Province Names and NumDeaths",command=GA6)
    btnga6.pack(side='top',padx=5,pady=5)
    btnga7 = Button(root,text="Graph French Province Names and RateTotal", command=GA7)
    btnga7.pack(side='top',padx=5,pady=5)
'''Creates a graph with english names from csv'''
def GA():
    csv_file='covid19-download (1).csv'
    data = pd.read_csv(csv_file)
    Id = data["pruid"]
    Names = data["prname"]
    x=[]
    y=[]
    x=list(Id)
    y=list(Names)
    plt.bar(x,y)
    plt.xlabel('Id->')
    plt.ylabel('Names->')
    plt.title('English Province Names and Province Id "Program By: Kim Johnson"')
    plt.show()
'''Creates another graph with english names from csv'''
def GA1():
    csv_file='covid19-download (1).csv'
    data = pd.read_csv(csv_file)
    Deaths = data["numdeaths"]
    Names = data["prname"]
    x=[]
    y=[]
    x=list(Deaths)
    y=list(Names)
    plt.bar(x,y)
    plt.xlabel('Deaths->')
    plt.ylabel('Names->')
    plt.title('English Province Names and NumDeaths "Program By: Kim Johnson')
    plt.show()
'''Creates another graph with english names from csv'''
def GA2():
    csv_file='covid19-download (1).csv'
    data = pd.read_csv(csv_file)
    Dates = data["date"]
    Names = data["prname"]
    x=[]
    y=[]
    x=list(Dates)
    y=list(Names)
    plt.bar(x,y)
    plt.xlabel('Dates->')
    plt.ylabel('Names->')
    plt.title('English Province Names and Date "Program By: Kim Johnson')
    plt.show()
'''Creates another graph with english names from csv'''
def GA3():
    csv_file='covid19-download (1).csv'
    data = pd.read_csv(csv_file)
    Today = data["numtoday"]
    Names = data["prname"]
    x=[]
    y=[]
    x=list(Today)
    y=list(Names)
    plt.bar(x,y)
    plt.xlabel('numtoday->')
    plt.ylabel('Names->')
    plt.title('English Province Names and NumToday "Program By: Kim Johnson')
    plt.show()
'''Creates another graph with english names from csv'''
def GA4():
    csv_file='covid19-download (1).csv'
    data = pd.read_csv(csv_file)
    RateTotal = data["ratetotal"]
    Names = data["prname"]
    x=[]
    y=[]
    x=list(RateTotal)
    y=list(Names)
    plt.bar(x,y)
    plt.xlabel('ratetotal->')
    plt.ylabel('Names->')
    plt.title('English Province Names and RateTotal "Program By: Kim Johnson"')
    plt.show()
'''Creates another graph with french names from csv'''
def GA5():
    csv_file='covid19-download (1).csv'
    data = pd.read_csv(csv_file)
    Id = data["pruid"]
    NamesFR = data["prnameFR"]
    x=[]
    y=[]
    x=list(Id)
    y=list(NamesFR)
    plt.bar(x,y)
    plt.xlabel('Id->')
    plt.ylabel('NamesFR->')
    plt.title('French Province Names and Province Id "Program By: Kim Johnson"')
    plt.show()
'''Creates another graph with french names from csv'''
def GA6():
    csv_file='covid19-download (1).csv'
    data = pd.read_csv(csv_file)
    Deaths = data["numdeaths"]
    NamesFR = data["prnameFR"]
    x=[]
    y=[]
    x=list(Deaths)
    y=list(NamesFR)
    plt.bar(x,y)
    plt.xlabel('Deaths->')
    plt.ylabel('NamesFR->')
    plt.title('French Province Names and NumDeaths "Program By: Kim Johnson"')
    plt.show()
'''Creates another graph with french names from csv'''
def GA7():
    csv_file='covid19-download (1).csv'
    data = pd.read_csv(csv_file)
    RateTotal = data["ratetotal"]
    NamesFR = data["prnameFR"]
    x=[]
    y=[]
    x=list(RateTotal)
    y=list(NamesFR)
    plt.bar(x,y)
    plt.xlabel('RateTotal->')
    plt.ylabel('NamesFR->')
    plt.title('French Province Names and RateTotal "Program By: Kim Johnson"')
    plt.show()

with open('covid19-download (1).csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print("")
        titles = ["pruid", "prname", "prnameFR","date","update","numconf","numprob","numdeaths","numtotal","numtested","numrecovered","percentrecover","ratetested","numtoday","percenttoday","ratetotal","ratedeaths","numdeathstoday","percentdeaths","numtestestedtoday","numrecovredtoday","percentactive","numactive","rateactive"]
        print(titles)
        print(row)
        print("")
        print("Program By: Kim Johnson")
        print("")
'''Create a tkinter(GUI) window.'''
'''Size of window set to 400 by 400.'''
''' Title of window set to GUI.'''
root = tkinter.Tk()
root.geometry("400x400")
root.wm_title("CovidProject By: Kim Johnson")
'''A close function created to be called on later.'''
def Close():
    messagebox.showinfo("EXIT","Program is now closing...")
    root.destroy()
'''A Read function to read and display the dataset in a GUI setting'''
def Read1():
    root = tkinter.Tk()
    root.geometry("1000x1000")
    root.wm_title("READ CSV  Program By: Kim Johnson")
    label5= tkinter.Label(root,text='Program By: Kim Johnson')
    label5.pack(side = 'top')
    text_widget = tkinter.Text(root, height = 40, width = 100)
    text_widget.pack(side=tkinter.LEFT)
    
   
    with open('covid19-download (1).csv', 'r') as f:
        data = f.read()
        text_widget.insert("1.0", data)
'''A Display function to display records in an array using the GUI'''  
def Display1():
    messagebox.showinfo("Display Records In Array","Display records in a data structure                                                Look at console for output of array                                            Program By: Kim Johnson")
    file_CSV = open('covid19-download (1).csv')
    data_CSV = csv.reader(file_CSV)
    list_CSV = list(data_CSV)
    print(list_CSV)
'''A Create function to display that a new record has been created using a GUI'''    
def Create1():
    
        
    root = tkinter.Tk()
    root.geometry("500x500")
    root.wm_title("New Record Created Program By: Kim Johnson")
    text_widget1 = tkinter.Text(root, height = 30, width = 80)
    text_widget1.pack(side=tkinter.LEFT)
    words1 = """A new record has been created and stored in an array.         Array output:  UK,Africa                                      Program By: Kim Johnson"""
    text_widget1.insert("1.0", words1)
    cv=["UK","South Africa"]
    messagebox.showinfo("Created","A New Record Has Been Created                                             Program By: Kim Johnson")
'''A Edit function to display an array has been edited using a GUI'''  
def Edit1():
   
    messagebox.showinfo("Edit","Array in memory has been edited.                                             More info displayed in console                                                 Program By: Kim Johnson ")
    cv=["UK","South Africa"]
    print(cv)
    cv.append("NewYork")
    print(cv)
    print("")
    print("Edited array in memory")
    print("")
    print("Program By: Kim Johnson")


'''A Remove function to display an array has been deleted using a GUI'''     
def Remove1():
    messagebox.showinfo("Delete","Item has been deleted from in memory array                       More info displayed in console                                                Program By: Kim Johnson")
    cv=["UK","South Africa"]
    print(cv)
    cv.pop(1)
    print(cv)
    print("File delete/removed from in memory array")
    print("Program By: Kim Johnson")
    '''graph'''



'''labels to print out text to the screen using tkinker'''
'''Buttons to provide functionality'''    
label1 = tkinter.Label(root, text='"MENU OPTIONS"',fg='blue')
label1.pack(side= 'top',padx=5,pady=5)
label2 = tkinter.Label(root, text='Please select a menu option by clicking one of the buttons below' , fg='blue')
label2.pack(side = 'top',padx=5,pady=5)
btn1 = Button(root, text="Reload DataSet From File",command=Read1)
btn1.pack(side = 'top',padx=5,pady=5)
btn2 = Button(root, text="Display records in data structure", command=Display1)
btn2.pack(side= 'top',padx=5,pady=5)
btn3 = Button(root, text="Create a new record and store in data structure" ,command=Create1)
btn3.pack(side='top',padx=5,pady=5)
btn4 = Button(root, text="Edit record in data structure", command=Edit1)
btn4.pack(side='top',padx=5,pady=5)
btn5 = Button(root, text="Delete record in data structure", command=Remove1)
btn5.pack(side='top',padx=5,pady=5)
btn6 = Button(root, text="Go To Graph Selections", command=NewWin)
btn6.pack(side= 'top',padx=5,pady=5)



'''Creating an exit button with red text that calls the Close method as a command.'''
btn = Button(root, text="Exit", fg='red',command=Close)
'''Set the position of button to the top of the window.'''
btn.pack(side = 'top',padx=5,pady=5)

root.mainloop()


     