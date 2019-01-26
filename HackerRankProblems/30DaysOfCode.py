


def slice_my_string():
    """
    Given a string S, of length N that is indexed from 0 to N-1, print its even
    indexed and odd-indexed characters as 2 space separated strings on a single
    line. 0 is considered an even index in this exercise.
    """
    test_cases = int(input('How many strings do you want to slice? '))
    for i in range(test_cases):
        my_string = input('Enter your string: ')
        n = len(my_string)
        # using string indexing where the first number is the inclusive
        # starting point; n+1 is the exclusive ending point; 2 is the steps
        # to take
        print(my_string[0:n+1:2], my_string[1:n+1:2])



def print_number_as_string():
    """
    Read an integer N. Without any string methods, print the following: 1234...N.
    Note that "..." represents the values in between.
    """
    n = int(input("Enter an integer: "))
    i_exponent = len(str(n))
    i = 10**i_exponent
    j = 1
    sum_total = n
    while j < n:
        sum_total = (sum_total + (n-j)*i)
        j += 1
        i_exponent = len(str(sum_total))
        i = 10**i_exponent
    print(sum_total)


def reverse_array_of_numbers():
    """
    Given an array, A, of N integers, print A's elements in reverse order
    as a single line of space separated numbers
    """
    given_array = list(map(int, input("Enter a space separated sequence of "
                                      "numbers: ").rstrip().split()))
    reverse_array = given_array[::-1]
    for num in reverse_array:
        print(num, end=" ")


def friend_phone_book():
    """
    Given n names and phone numbers, assemble a phone book that maps
    friends' names to their respective phone numbers. You will then be given
    an unknown number of names to query your phone book for. For each name
    queried, print the associated entry from your phone book on a new line in
    the form name=phoneNumber; if an entry for name is not found, print Not
    found instead.
    """
    num_entries = int(input("How many entries? "))
    phone_book = {}
    for i in range(0, num_entries):
        entries = input("Input your friends name and phone number: ")
        my_friend = entries.split()
        phone_book[my_friend[0]] = my_friend[1]

    lookup_value = input("Lookup value: ")
    while True:
        phone_number = phone_book.get(lookup_value)
        if phone_number is None:
            print("Not found")
        else:
            print(lookup_value + "=" + phone_number)

        lookup_value = input("Lookup value: ")
        if lookup_value == "":
            return False

def factorial(n):
    """
    Write a factorial function that takes a positive integer N as a
    parameter and prints the result of N!
    """
    if n <= 1:
        return 1
    return n * factorial(n-1)

def binary_nums():
    """Given a base-10 integer, n, convert it to binary (base-2). Then find
    and print the base-10 integer denoting the maximum number of consecutive
    1's  in n's binary representation"""
    num_to_convert = int(input("What integer to convert? "))
    binary_int = bin(num_to_convert)
    stripped_bin = binary_int[2:]
    max_ones = 0
    current_ones = 0

    for i in range(0, len(stripped_bin)):
        if stripped_bin[i] == "1":
            current_ones += 1
            if max_ones < current_ones:
                max_ones = current_ones
        else:
            current_ones = 0

    print(max_ones)


def hourglass():
    """
    Given a 6x6 array, A, we define an hourglass in A to be a subset of
    values with indices falling in this patter in A's graphical representation:
    a b c
      d
    e f g
    Find the max sum of all possible hourglasses in A.
    Constraints: -9 <= A[i][j] <= 9, 0 <= i, j <= 5
    :return: max_sum
    """
    big = []

    for _ in range(6):
        big.append(list(map(int, input("Enter your numbers: ").rstrip().split())))
    max_sum = -50
    current_sum = 0

    for i in range(0, 4):
        for j in range(0, 4):
            current_sum = (big[i][j] + big[i][j+1] + big[i][j+2] + big[i+1][j+1] +
                           big[i+2][j] + big[i+2][j+1] + big[i+2][j+2])

            if current_sum > max_sum:
                max_sum = current_sum
    print(max_sum)

# Implementing a Linked List
class Element:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        """
        Adds a new element to the end of the list
        """
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, position):
        """Get an element from a particular position. Assume the first
        position is "1". Return None if position is not in the list"""
        counter = 1
        current = self.head
        if position < 1:
            return None
        while current and counter <= position:
            if position == counter:
                return current
            counter += 1
            current = current.next
        return None

    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        counter = 1
        current = self.head
        if position > 1:
            while current and counter < position:
                if counter == position - 1:
                    new_element.next = current.next
                    current.next = new_element
                current = current.next
                counter += 1
        elif position == 1:
            new_element.next = self.head
            self.head = new_element


    def delete(self, value):
        """Delete the first node with a given value."""
        current = self.head
        previous = None
        while current.value != value and current.next:
            previous = current
            current = current.next
        if current.value == value:
            if previous:
                previous.next = current.next
            else:
                self.head = current.next

    def insert_first(self, new_element):
        """Insert new element as the head of the linked list"""
        new_element.next = self.head
        self.head = new_element

    def delete_first(self):
        """Delete the first(head) element in the linked list and return it"""
        deleted_element = self.head
        if self.head:
            self.head = self.head.next
            deleted_element.next = None
        return deleted_element


# Implementing a Stack using a linked list
class Stack:
    """Implements the data structure Stack using a linked list"""
    def __init__(self, top=None):
        self.linked_list = LinkedList(top)

    def push(self, new_element):
        """
        Adds a new element to the top of the stack. The head of the linked
        list needs to be changed when adding a new element
        """
        return  self.linked_list.insert_first(new_element)

    def pop(self):
        """Removes the first element off the top of the stack and returns it"""
        return self.linked_list.delete_first()
