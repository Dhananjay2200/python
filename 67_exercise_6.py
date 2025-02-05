class library:
    def __init__(self):
        self.nobook=0
        self.books=[]

    def addbook(self,book):
        self.books.append(book)
        self.nobook=len(self.books)
    def showinfo(self):
        print(f"The libray has {self.nobook} books.     books are")
        
        for book in self.books:
            print(book)


li=library()
li.addbook("harry potter-1")
li.addbook("harry potter-1")
li.addbook("harry potter-1")
li.addbook("harry potter-1")
li.addbook("harry potter-1")
li.addbook("harry potter-1")
li.addbook("harry potter-1")
li.addbook("harry potter-1")
li.addbook("harry potter-1")
li.addbook("harry potter-1")
li.addbook("harry potter-1")
li.addbook("harry potter-1")
li.showinfo()