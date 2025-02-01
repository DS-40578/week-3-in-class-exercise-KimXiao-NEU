class Node:
    def __init__(self, data, next_node = None):
        self.data = data 
        self.next_node = next_node

    '''
    def __str__(self):
        if self.next_node is None:
            return str(self.data)
        else:
            return str(self.data) + '-->' + str(self.next_node)
    '''
    def __str__(self):
        return str(self.data)

    def count(self): # count number of nodes in the linked list
        print("in the node that stores", self.data)
        if self.next_node is None:
            print("hit our base case ")
            return 1
        else:
            print("recursive call, calling count with the node storing,", self.next_node)
            return 1 + self.next_node.count()
        
    def calculate_price(self):
        if self.next_node is None:
            return self.data.price
        return self.data.price  + self.next_node.calculate_price()

test = Node("A1",Node("B",Node("A2")))
print(test)
result = test.count()
print(result)