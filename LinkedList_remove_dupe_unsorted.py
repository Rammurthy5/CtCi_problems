"""
Remove dupes from an unsorted doubly linked list

"""


from DataStructures.LinkedList_design import ch

d = dict()

ch.print_list()

def remove_dupes(head):
    curr_node = head

    while curr_node.next is not None:

        if curr_node.data in d:
            ch.remove(curr_node.data)
        else:
            d[curr_node.data] = None

        curr_node = curr_node.next

    if curr_node.data in d:
        ch.remove(curr_node.data)


remove_dupes(ch.head)
ch.print_list()



