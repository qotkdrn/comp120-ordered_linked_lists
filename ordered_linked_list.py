# File: ordered_list.py
# Date: April 19, 2021
# Author: John Glick
# Description: Ordered linked list.

class Node:
    def __init__(self, item, next = None, prev = None):
        """ 
        Constructor.  Creates a node.
        Instance variables must be next, prev, and item.
        """
        self.item = item
        self.next = next 
        self.prev = prev

class OrderedLinkedList:
    def __init__(self):
        """ 
        Constructor.  Creates an empty ordered list.
        Instance variables must be front, back, and len.
        """
        self.front = None
        self.back = None
        self.len = 0

    def insert(self, x):
        """ 
        Insert x into the list so that it remains ordered
        (smallest to largest) after the insert.  Duplicates
        are ok.
        """
        x = Node(x)
        current = self.front

        if self.front is None:
            self.front = x
            self.back = x
        elif current.item >= x.item:
            self.front = x
            x.next = current
            current.prev = x
        else:
            while current.next != None: 
                if x.item < current.item:
                    break
                current = current.next
            if x.item < current.item:
                x.next = current
                x.prev = current.prev
                current.prev.next = x
                current.prev = x
            else:
                self.back = x
                current.next = x
                x.prev = current
        self.len += 1

    def __len__(self):
        """ Returns length of list """
        return self.len

    def __str__(self):
        """ Returns string representation of list """
        if self.front == None:
            return "[]"
        else:
            s = "["
            cur = self.front
            while cur.next != None:
                s += str(cur.item) + ", "
                cur = cur.next
            s += str(cur.item) + "]"
        return s

    def remove(self, x):
        """
        Removes the one instance of x in the list.
        Raises ValueError if x is not in the list.
        Do not perform any unnecessary comparisons -
        so if you are iterating down the list, and you reach
        an item greater than x, do not continue searching
        the list.
        """
        x = Node(x)
        current = self.front

        if self.front == None:
            raise ValueError
        if self.len == 1:
            self.front = self.back = None
            self.len -= 1
            return 

        while current.next != None:
            if x.item == current.item:
                break
            if x.item < current.item:
                raise ValueError
            if x.item > current.item and current.next.item == None:
                raise ValueError
            if x.item > self.back.item:
                raise ValueError
            current = current.next

        if self.front.item == x.item:
            self.front = self.front.next
            self.front.prev = None
            self.len -= 1
            return 
        if x.item > self.front.item and current.item is not self.back.item:
            current = current.prev
            current.next = current.next.next
            current.next.prev = current
            self.len -= 1   
            return         
        if self.back.item == x.item:
            self.back = self.back.prev
            self.back.next = None
            self.len -= 1
            return 
       
    def remove_all(self, x):
        """
        Removes all instances of x in the list.
        Raises ValueError if x is not in the list.
        The method must run in O(n) time, where n
        is the number of items in the list.  This means
        you must remove all items in one pass through the list.
        Remember that because the list is ordered, all copies
        of x will be next to one another in the list.
        Do not perform any unnecessary comparisons -
        so if you are iterating down the list, and you reach
        an item greater than x, do not continue searching
        the list.
        """
        x = Node(x)
        current = self.front
        count = 0
        while current.next != None:
            if x.item == current.item:
                count += 1
            current = current.next
        if self.back.item == x.item:
            count += 1
        for i in range(count):
            self.remove(x.item)

    def remove_duplicates(self):
        """
        Removes all duplicate items from the list, leaving just
        one copy of each different item.
        This method must be performed in one pass through list.
        """
        current = self.front
        lst = []
        while current.next != None:
            if current.item == current.next.item:
                lst.append(current.item)
            current = current.next
        for item in lst:
            self.remove(item)
        
    def merge(self, other_ordered_list):
        """
        Merges the items in the self list (the list calling the method), and 
        the items in other_ordered_list into a new orderedLinkedList object,
        that is then returned by the method.
        DO NOT simply create an empty orderedLinkedList object, and then
        insert each item in self and other_ordered_list into that new orderedLinkedList
        obect.  You must merge the items from self and 
        other_ordered_list into a newly created linked list, that operates in O(n) 
        running time, where n is the total number of items in both lists.
        (Think of the merge operation in merge sort as a guide for how to do this.)
        Duplicates are allowed.
        Leave self and other_ordered_list unchanged, so do not remove 
        the items from either list.  Just copy their items into your newly
        created list.  And don't try to reuse the nodes from either self
        or other_ordered_list.  You want to just copy the items from their nodes.
        """
        lst3 = OrderedLinkedList()
        if self.front is None:
            return other_ordered_list
        if other_ordered_list.front is None:
            return self
        l1 = 0
        l2 = self.len + other_ordered_list.len
        front1 = self.front
        front2 = other_ordered_list.front
        while l1 != l2:
            if front1.next is None:
                lst3.insert(front2.item)
                l1 += 1
            if front2.next is None:
                lst3.insert(front1.item)
                l1 += 1         
            if front1.item < front2.item and front1.next is not None:
                lst3.insert(front1.item)
                l1 += 1
                front1 = front1.next
            if front2.item < front1.item and front2.next is not None:
                lst3.insert(front2.item)
                l1 += 1
                front2 = front2.next
        return lst3

    def intersection(self, other_ordered_list):
        """
        Creates a new list that is the intersection of the items in the self list 
        (the list calling the method), 
        and the items in other_ordered_list, and this new list is returned.
        All items that appear in both lists should
        be in the intersection list.  You should keep just one copy of each item that
        appears in both lists, so for example,
        if there are two copies of an item in the self list, and 3 copies in the
        other_ordered_list list, then just one copy should be in the intersection.
        (Also, as another example, if there are 2 copies in the self list and 0 copies
        in the other list, then no copies should be in the intersection list.)
        You must find the intersection of self and other_ordered_list in one
        pass through both lists, and so its running time should be O(n), where n is 
        the total number of items in both lists.
        (This should have a similar feel to the merge operation.)
        Leave self and other_ordered_list unchanged, so do not remove 
        the items from either list.  Just copy their items into your newly
        created list.  And don't try to reuse the nodes from either self
        or other_ordered_list.  You want to just copy the items from their nodes.
        """
        lst3 = OrderedLinkedList()
        if self.len == 0 or other_ordered_list.len == 0:
            return lst3
        current = self.front
        other = other_ordered_list.front
        while current != None:
            if current.item == other.item:
                lst3.insert(current.item)
                if other_ordered_list.len > 0:  #in case other list is empty
                    other = other.next
                current = current.next
            elif current.item > other.item:
                other = other.next
            else:
                current = current.next
        if lst3.len > 0:
            lst3.remove_duplicates()
        return lst3
