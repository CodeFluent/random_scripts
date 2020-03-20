class Node:

    def __init__(self, data, next=None):
        self.next = next
        self.data = data
    
    def __str__(self):
        return self.data

class LinkedList:

    def __init__(self, head=None):
        self.head = head
    
    


# declare nodes
node1 = Node(3)
node2 = Node(2)
node3 = Node(3)

# connect the nodes
node1.next = node2
node2.next = node3
    # 1 -> 2 -> 3

# loop through nodes
currentNode = node1
while currentNode.next is not None:
    print(currentNode.data, "->")
    currentNode = currentNode.next

    