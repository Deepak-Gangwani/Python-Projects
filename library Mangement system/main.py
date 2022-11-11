from ast import main
from tkinter import E


class Library:
    def __init__(self,list,name):
        self.bookslist=list
        self.name=name
        self.lendDict={}  # created an empty dictionary

    def diplayBooks(self):
        try:
            print(f"We have following books in library: {self.name}")
            for book in self.bookslist:
                print(book)
        except Exception as e:
            print(e)        

    def lendBook(self,user,book):
        try:
            if book not in self.lendDict.keys():
                self.lendDict.update({book:user})
                print("lender-Book databases has been updated. You can take the book now")
            else:
                print(f"Sorry,The book is already been issued to {self.lendDict[book]}")
        except Exception as e:
            print(e)        

    def addBook(self,book):
        try:
            self.bookslist.append(book)
            print(f"The {book} is been added to book list,thank you for submitting")
        except Exception as e:
            print(e)

    def returnBook(self,book):
        try:
            self.bookslist.remove(book)
        except Exception as e:
            print(e)

if __name__ == "__main__":
    deepak= Library(["python","javascript","c++","c","HTML","CSS","java"],"MiniLibrary")
    while(True):
        print(f"--------Welcome to the {deepak.name}-----------\nEnter your choices to continue--> ")
        print("1) Display Books")
        print("2) Lend A Book")
        print("3) Add A Book")
        print("4) Return A Book")
        try:
            user_input=input("Enter your choice option-->")
            if user_input=='1':
                deepak.diplayBooks()
            if user_input=='2':
                book=input("Enter your book name-->")
                user=input("Enter your name-->")
                deepak.lendBook(user,book)
            if user_input=='3':
                book=input("Enter the book name you want to add-->")
                deepak.addBook(book)
            if user_input=='4':
                book=input("Enter the book name-->")
                deepak.returnBook(book)
        except: 
            print("You have entered invalid choice")               
    
                 
         
        print("press 'q' to quit & 'c' to continue the program")
        user_input2 = input()
        if user_input2=='q':
            exit()
        elif user_input2=='c':
            continue
        else:
            print("Entered invalid character")
            continue    
