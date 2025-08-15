import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Calculate and return the area of the circle."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Calculate and return the perimeter (circumference) of the circle."""
        return 2 * math.pi * self.radius


circle = Circle(5) 
print(f"Radius: {circle.radius}")
print(f"Area: {circle.area():.2f}")
print(f"Perimeter: {circle.perimeter():.2f}")



from datetime import datetime

class Person:
    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = date_of_birth  # format: "YYYY-MM-DD"

    def age(self):
        """Calculate and return the age of the person."""
        today = datetime.today()
        birth_date = datetime.strptime(self.date_of_birth, "%Y-%m-%d")
        return today.year - birth_date.year - (
            (today.month, today.day) < (birth_date.month, birth_date.day)
        )

    def greet(self):
        """Return a greeting message."""
        return f"Hello, my name is {self.name} and I am from {self.country}, I am {self.age()} years old."



p = Person("Alice", "USA", "2000-05-15")
print(p.greet())



class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero"
        return a / b



calc = Calculator()
print(calc.add(10, 5))
print(calc.subtract(10, 5))
print(calc.multiply(10, 5))
print(calc.divide(10, 5))




import math

class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))



circle = Circle(5)
print(circle.area(), circle.perimeter())

square = Square(4)
print(square.area(), square.perimeter())

triangle = Triangle(3, 4, 5)
print(triangle.area(), triangle.perimeter())




class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not self.root:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, root, key):
        if key < root.key:
            if root.left:
                self._insert(root.left, key)
            else:
                root.left = Node(key)
        else:
            if root.right:
                self._insert(root.right, key)
            else:
                root.right = Node(key)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, root, key):
        if not root:
            return False
        if root.key == key:
            return True
        elif key < root.key:
            return self._search(root.left, key)
        else:
            return self._search(root.right, key)



tree = BST()
tree.insert(10)
tree.insert(5)
tree.insert(15)
print(tree.search(10))
print(tree.search(7))




class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.stack:
            return "Stack is empty"
        return self.stack.pop()



stack = Stack()
stack.push(1)
stack.push(2)
print(stack.pop())
print(stack.pop())
print(stack.pop())



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def delete(self, key):
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            return
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        if temp:
            prev.next = temp.next


ll = LinkedList()
ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.display()
ll.delete(20)
ll.display()



class ShoppingCart:
    def __init__(self):
        self.items = {}  # {item_name: (price, quantity)}

    def add_item(self, name, price, quantity=1):
        if name in self.items:
            self.items[name] = (price, self.items[name][1] + quantity)
        else:
            self.items[name] = (price, quantity)

    def remove_item(self, name):
        if name in self.items:
            del self.items[name]

    def total_price(self):
        return sum(price * quantity for price, quantity in self.items.values())


cart = ShoppingCart()
cart.add_item("Apple", 2, 3)
cart.add_item("Banana", 1.5, 2)
print(cart.total_price())
cart.remove_item("Apple")
print(cart.total_price())



class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.stack:
            return "Stack is empty"
        return self.stack.pop()

    def display(self):
        print(self.stack)



stack = Stack()
stack.push(5)
stack.push(10)
stack.display()
stack.pop()
stack.display()



class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.queue:
            return "Queue is empty"
        return self.queue.pop(0)



queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())




class Bank:
    def __init__(self):
        self.accounts = {}  
    def create_account(self, account_number, initial_balance=0):
        if account_number in self.accounts:
            return "Account already exists"
        self.accounts[account_number] = initial_balance

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number] += amount
        else:
            return "Account not found"

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            if self.accounts[account_number] >= amount:
                self.accounts[account_number] -= amount
            else:
                return "Insufficient funds"
        else:
            return "Account not found"

    def get_balance(self, account_number):
        return self.accounts.get(account_number, "Account not found")


bank = Bank()
bank.create_account("123", 500)
bank.deposit("123", 200)
print(bank.get_balance("123"))
bank.withdraw("123", 100)
print(bank.get_balance("123"))
