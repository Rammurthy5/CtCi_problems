"""
Write code to partition a linked list around a value x, such that all nodes less than x come before all nodes greater
 than or equal to x. Ifxis contained within the list, the values of x only need to be after the elements less than x
  (see below). The partition element x can appear anywhere in the "right partition"; it does not need to appear between
   the left and right partitions.
EXAMPLE
Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1[partition=5] Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8

"""

from DataStructures.LinkedList_design import ch, LinkedList

# ch is constructed linked list from a different module
# ch == a -> d -> d -> b -> c -> e -> e
def partition(head):
    if len(ch)<1:
        return "Linked List is empty"

    mid_element = round(len(ch) / 2)
    curr_node = head
    i = 0

    while i<mid_element+1:
        curr_node = curr_node.next
        i+=1

    mid_element = curr_node.data

    curr_node = head
    new_linkedlist = LinkedList()

    for i in range(len(ch)):
        if mid_element>curr_node.data:
            new_linkedlist.insert_left(curr_node.data)
        else:
            new_linkedlist.insert_last(curr_node.data)


    ch.print_list()

partition(ch.head)







