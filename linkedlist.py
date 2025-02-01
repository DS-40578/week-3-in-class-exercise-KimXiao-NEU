from nodes import Node
from book import Book
class Linkedlist:
    def __init__(self):
        self.head = None
    
    def add_to_front(self, data):
        new_node = Node(data, self.head)
        self.head = new_node # like a stack, newly added node always becomes the head node
    
    def create_loop(self):
        if self.head is None:
            return
        current = self.head
        while current.next_node is not None:
            current = current.next_node
        current.next_node = self.head
    
    def start_new(self, target):
        if self.head is None or self.head.data == target:
            return  # No need to do anything if the list is empty or target is already at the front

        current = self.head
        previous = None

    # Traverse the list to find the target node and its previous node
        while current is not None and current.data != target:
            previous = current
            current = current.next_node
        # If the target node wasn't found, return
        if current is None:
            return
        # Remove the target node by updating the previous node's next to skip the target node
        if previous:
            previous.next_node = current.next_node
        else:
            self.head = current
        current.next_node = self.head
        self.head = current

    def is_loop(self):
        current = self.head
        temp_set= set()
        while current is not None:
            if current in temp_set:
                return True
            temp_set.add(current)
            current = current.next_node
        return False
    

    def __str__(self):
        return_str =""
        current = self.head # self.head is the current first node
        while current is not None: # check if there's next_node
            return_str += str(current) + " "
            current = current.next_node
        return return_str
    
    def find(self, target_value):
        current = self.head
        while current is not None: # check if there's next_node
            if current.data == target_value:
                return current
            current = current.next_node
        return None
    
    def count(self):
        return self.head.count()
    
    def iterative_count(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next_node
        return count
    
    def to_list(self):
        lst = []
        current = self.head
        while current is not None:
            lst.append(current.data)
            current = current.next_node
        return lst
    
    def find_first_index(self, target):
        current = self.head
        count = 0
        while current is not None: # current is the linkedlist!
            if current.data == target:
                return count
            current = current.next_node
            count += 1
        return -1
    
    def find_last_index(self, target):
        current = self.head
        count = 0
        last_index = -1
        while current is not None:
            print(f"go in to the loop, current = {current},current.data = {current.data},count= {count}")
            if current.data == target:
                print(f"go in to if check,current.data={current.data},count={count}")
                last_index = count
                print(f"last_index updated to{last_index}")
            current = current.next_node
            print(f"after if check, now current is{current}")
            count += 1
            print(f"updating count to {count}")
        return last_index
                  
    def calc_price(self) :
        return self.head.calculate_price()
    
    def iterative_filter(self, predicate):
        '''param: predicate lambda that takes in a Node
        object and returns True/False'''
        current = self.head
        #new_head = None
        new_ll = Linkedlist()
        while current is not None:
            if predicate(current) == True:
                #new_node = Node(current.data, new_head)
                #new_head = new_node
                new_ll.add_to_front(current.data)
            current = current.next_node
        return new_ll
    
  

ll = Linkedlist()
ll.add_to_front(Book("Lake of Souls", False))
ll.add_to_front(Book("Intro to Python",True))
ll.add_to_front(Book("DAta Science in python", False))
ll.add_to_front(Book("Linear Algebra for dummies", True))
ll.add_to_front(Book("Into the heart of the sea", False))
ll.add_to_front(Book("Destroy all humans", True))
ll.add_to_front(Book("A", True))
ll.add_to_front(Book("B", True))
ll.add_to_front(Book("C", True))
print(ll.calc_price())
print(ll.count())
item = ll.find("A")
print(item)
paperback = lambda node: True if node.data.is_paper else False
new_ll = ll.iterative_filter(paperback)
print(new_ll)

ll2 = Linkedlist()
ll2.add_to_front("D")
ll2.add_to_front("C")
ll2.add_to_front("B")
ll2.add_to_front("A")

result = ll2.find_first_index("D")
result_last = ll2.find_last_index("D")
print("find the first D")
print(result)
print("find the last D")
print(result_last)
print(ll2.is_loop())

print(ll2)
ll2.start_new("C")
print(ll2)
