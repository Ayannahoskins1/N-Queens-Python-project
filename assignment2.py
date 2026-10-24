class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node

    def display(self):
        current = self.head

        while current is not None:
            print(current.data, end=" -> ")
            current = current.next

        print("None")

    def make_circular(self):
        if self.head is None:
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = self.head

    def is_circular(self):
        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False


my_list = LinkedList()

number_of_nodes = int(input("How many nodes do you want? "))

for i in range(number_of_nodes):
    value = int(input("Enter a value: "))
    my_list.append(value)

print("\nYour linked list:")
my_list.display()

choice = input("Do you want to make the linked list circular? (yes/no): ")

if choice.lower() == "yes":
    my_list.make_circular()

if my_list.is_circular():
    print("The linked list is circular.")
else:
    print("The linked list is not circular.")