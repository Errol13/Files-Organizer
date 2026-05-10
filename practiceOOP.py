from abc import ABC, abstractmethod

class Item(ABC):
       def __init__(self, title, location, id):
               self.title = title
               self._location = location
               self.__id = id

       @abstractmethod
       def borrow(self, member_name):
               pass
       def info(self):
             print(self.title, self._location)

class Book(Item):
        
        def __init__(self, title, location,id, author):
              super().__init__(title, location, id)
              self.author = author
        def borrow(self, member_name):
              print(f"Member {member_name} borrowed Book {self.title}")

class DVD(Item):
        def __init__(self, title, location, id, duration):
               super().__init__(title, location, id)
               self.duration = duration
        def borrow(self, member_name):
                print(f"Member {member_name} borrowed DVD {self.title}")

if __name__ == "__main__":
    book_A = Book("The Great Gatsby", "Shelf A3", "B001", "F. Scott Fitzgerald")
    dvd_A = DVD("Inception", "Shelf B1", "D001", "120 minutes")
    book_A.borrow("John Doe")
    book_A._location
       
    try:
       book_A.__id
    except AttributeError as e:
         print("Cannot access private attribute:", e)

    print(dvd_A.duration)