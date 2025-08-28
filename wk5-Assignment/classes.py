# Assignment 1: OOP - Design Your Own Class

class Book:
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
    
    def read(self, pages_read):
        if pages_read > self.pages:
            print(f"You can’t read more pages than the book has! 📚")
        else:
            print(f"You read {pages_read} pages of '{self.title}' by {self.author}.")
    
    def get_summary(self):
        return f"'{self.title}' by {self.author}, {self.pages} pages, priced at ${self.price}."
    
    def __str__(self):
        return f"{self.title} by {self.author}"


# Inheritance Example
class EBook(Book):
    def __init__(self, title, author, pages, price, file_size, format_type):
        super().__init__(title, author, pages, price)
        self.file_size = file_size  # in MB
        self.format_type = format_type  # e.g. PDF, EPUB
    
    def download(self):
        print(f"Downloading '{self.title}' ({self.file_size}MB, {self.format_type}) 💾")
    
    def read(self, pages_read):
        # Override the parent method to show reading digitally
        print(f"You read {pages_read} pages of the eBook '{self.title}' on your device 📱.")


# Testing 
book1 = Book("1984", "George Orwell", 328, 15.99)
print(book1.get_summary())
book1.read(50)

ebook1 = EBook("Digital Minimalism", "Cal Newport", 304, 9.99, 2, "EPUB")
print(ebook1.get_summary())
ebook1.download()
ebook1.read(40)


# Activity 2: Polymorphism Challenge

class Animal:
    def move(self):
        pass  # Abstract-like method (to be overridden)


class Dog(Animal):
    def move(self):
        print("The dog runs 🐕")


class Bird(Animal):
    def move(self):
        print("The bird flies 🐦")


class Fish(Animal):
    def move(self):
        print("The fish swims 🐟")


# Vehicle Example
class Vehicle:
    def move(self):
        pass


class Car(Vehicle):
    def move(self):
        print("The car drives 🚗")


class Plane(Vehicle):
    def move(self):
        print("The plane flies ✈️")


# --- Testing Polymorphism ---
animals = [Dog(), Bird(), Fish()]
for a in animals:
    a.move()

vehicles = [Car(), Plane()]
for v in vehicles:
    v.move()
