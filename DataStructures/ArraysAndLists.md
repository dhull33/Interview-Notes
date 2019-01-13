**A. **Dynamic Arrays****

1. Can grow in size as new elements are added
2. Preserves the order of insertion
3. In Python this is of type ```List```
4. In C++ this is ```std::vector```
5. Behind the scenes:
    - Implemented with a static array of some set length
    - Elements are inserted into the next free position
      1. The worst case complexity for the insertion is O(1) since it does not depend on the size of the array
    - When the static array becomes full, a new array is created by copying over all the elements from the full array into a larger array with empty positions
      1. The worst case complexity for the copy is O(N) since we have to copy each element into the new array
    - Removing an element
      1. Element is removed
      2. All elements to the right are then moved over one element
      3. The worst case complexity for this is O(N) since it is dependent on the size of the array
    - Can be very slow depending on the size of the array and the operations being performed

**B. Linked List**

1. In Python the closest type is ```collections.deque```
2. In C++ the type is ```std::list```
3. Each element is stored independently as isolated units
4. Around each element there is a small container with a pointer that points to the next element
    1. If there is a pointer that also points to the previous element it is called a *Doubly Linked List*
    2. There is often an entry point container that points to the head and tail element
        1. Finding the first or last element has a complexity of O(1) since there is only one set of instructions needed to get the first or last element
    3. To find a specific element we have to traverse the linked list until we find the element
        1. This has a complexity of O(N) since the worst case scenario is we traverse the entire linked list
    4. Inserting a new element, provided we have already found where to insert it, has a complexity of O(1) since all we have to do is change the pointers between the elements where we are inserting
        1. Change at most 4 pointers (1 for the left element, 2 for the inserted element, and 1 for the right element) if it is a doubly linked list
    5. When removing an element all we have to do is change the pointers to the right element and the left element
        1. Has complexity of O(1)
5. **Pros:**
    1. Can append two lists in O(1) time
    2. Adding and removing elements is fast (O(1))
    3. Simplifies some operations
        1. Ideal for queues
    4. No preallocated storage
        1. can add elements until storage is full
6. **Cons:**
    1. Increased element access time
    2. Pointer overhead may be large
    