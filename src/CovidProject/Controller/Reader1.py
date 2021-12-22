'''
Created on Jan 28, 2021

@author: Kim Johnson
'''
import csv



'''Using a file object from file IO to open the csv file.
   No need for expections because when using "with" the file closes automatically.
   Print("") makes whitespaces.
   Next is an array of titles then I print the array above each row.
   Lastly I print out my name to be output onto the screen.
   '''

with open('covid19-download (1).csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print("")
        titles = ["pruid", "prname", "prnameFR","date","update","numconf","numprob","numdeaths","numtotal","numtested","numrecovered","percentrecover","ratetested","numtoday","percenttoday","ratetotal","ratedeaths","numdeathstoday","percentdeaths","numtestestedtoday","numrecovredtoday","percentactive","numactive","rateactive"]
        print(titles)
        print(row)
        count=0
        count = count + 1
        if count == 100:
            break
        print("")
        print("Program By: Kim Johnson")
        print("")
'''Displays menu options to the screen and allows for user input selection.'''
def mainMenu():
    print("1. Reload data from dataset")
    print("2. Using data from memory write to a new file")
    print("3. Display one record from in-memory data")
    print("4. Create a new record and store it in the data structure in memory")
    print("5. Edit a record in the data structure")
    print("6. Delete a record from the data structure")
    print("7. Quit/Exit")
    print("Program By: Kim Johnson")
    print("")
    '''Gets users selection, then calls the method for the selection selected.'''
    selection=int(input("Enter choice:"))
    if selection==1:
        reload()
    elif selection==2:
        newfile()
    elif selection==3:
        one()
    elif selection==4:
        create()
    elif selection==5:
        edit()
    elif selection==6:
        remove()
    elif selection==7:
        exit()
    else:
        print("Invalid choice. Enter 1-7")
        mainMenu()
        '''Method created to reload csv file.'''
def reload():
    with open('covid19-download (1).csv','r') as file:
        reader=csv.reader(file)
        for row in reader:
            print(row)
            print("Program By: Kim Johnson")
    anykey=input("Enter any key to return to main menu")
    mainMenu()
'''Method to create a new written file'''         
def newfile():
    file = open("covid.csv", 'w')
    file.write("['1', 'Canada', 'Canada', '2021-01-09', '', '652473', '0', '16833', '652473', '14509978', '552388', '84.66', '386014', '8127', '1.26', '1735.80', '44.78', '126', '2.58', '89218', '6417', '12.76', '83252', '221.48', '105104', '279.61', '1831', '4.87', '56098', '149.24', '1009', '2.68', '8014', '21.32', '144', '0.38']")
    file.close()
    print("new written file was created")
    print("Program By: Kim Johnson")
    anykey=input("Enter any key to return to main menu")
    mainMenu()


'''Method prints one row of data from csv.'''
def one():
    with open('covid19-download (1).csv','r') as file:
        reader=csv.reader(file)
        row1 = next(reader)
        print(row1)
        print("")
        print("Program by: Kim Johnson")
        anykey=input("Enter any key to return to main menu")
    mainMenu()
    
def create():
    cv=["UK","South Africa"]
    print(cv)
    print("Creating a new object in memory")
    print("Program By: Kim Johnson")
    anykey=input("Enter any key to return to main menu")
    mainMenu()
def edit():
    cv=["UK","South Africa"]
    print(cv)
    cv.append("NewYork")
    print(cv)
    print("")
    print("Edited array in memory")
    print("")
    print("Program By: Kim Johnson")
    anykey=input("Enter any key to return to main menu")
    mainMenu()
    
def remove():
    cv=["UK","South Africa"]
    print(cv)
    cv.pop(1)
    print(cv)
    print("File delete/removed from in memory array")
    print("Program By: Kim Johnson")  
    anykey=input("Enter any key to return to main menu")
    mainMenu()
    
mainMenu()
    
            