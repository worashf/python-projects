
class  Node:

    def __init__(self, value):
        self.value  = value
        self.next = None

class LinkedList:

    def __init__(self):
        self.head= None
        self.tail = None
        self.length = 0
   
    # check if the list is empty
    def is_empty(self):
        return self.head == None and self.length  == 0 # check both the head  is None and length is 0
    
    # get the size of the list
    def get_size(self):
        return self.length
    
    # print list => print_list
    def print_list(self):
        if self.head is None:
            print("the list is empty, please add some")
        temp = self.head
        print("the length of the list is:", self.length)
        while temp is not None:
            print("Node value is: ", temp.value)
            temp = temp.next

    # get head =>  get_head
    def get_head(self):
        return self.head

    # get tail => get_tail
    def get_tail(self):
        return self.tail

    # insert data at the end of the list  -> push
    def  insert_last(self, value):
        new_node  =  Node(value)
        if not self.head:
            self.head  = new_node
            self.tail  = new_node
        else:
            self.tail.next  = new_node
            self.tail  = new_node
        self.length +=  1
        return  new_node
    

    # delete node from the end of the linked list -> pop
    def remove_last(self):
        if self.head is None: # if the list is empty
            return  "The list is empty, can't remove."
        
        current  = self.head
        new_tail  = None
        while current.next is not None: # traverse the list to get the new tail
                new_tail  = current
                current  = current.next
        if new_tail is None:  # if the list has only one node
            self.head = None
            self.tail   =None
        else:
          
            new_tail.next  = None
            self.tail  = new_tail
        self.length -= 1
        return current
           
    # insert  node at the beging of the list => prepend
    def prepend(self, value):
        new_node  = Node(value)

        if not self.head  and self.length == 0: # if the list is empty
            self.head   = new_node
            self.tail  = new_node
        else:
            new_node.next  = self.head
            self.head = new_node
        self.length +=  1
        return  new_node


    # remove the first node  from  the list
    def  remove_first(self):
        if self.head  is None and self.length  == 0: # if the list is empty
             return  "The list is empty, can't remove."
        
        removed_node = self.head
        self.head  = removed_node.next
        removed_node.next =  None
        self.length -= 1

        return  removed_node.value # return the value of removed node
    
    # get the node at specific index from list => get_at_index.
    def  get_at_index(self, index):
         try:
             if index < 0  or index  >= self.length:
                 raise IndexError("No node at: " + str(index))
             count  = 0 
             current  = self.head
             while count  !=  index:
                
                 current = current.next
                 count += 1
         
             return  current 


         except IndexError as err:
            print(f"{err}")
          
            return None


    # insert node at specific index
    def add_at_index(self, index, value):
        try:    
               inserted_node  = None
               if index < 0  or index  > self.length:
                 raise IndexError("can't add at index: " + str(index))
               elif index == 0:
                   inserted_node  = self.prepend(value)
               elif  index == self.length:
                   inserted_node = self.insert_last(value)
               else:
                   inserted_node =  Node(value)
                   prev_node = self.get_at_index(index-1)
                   inserted_node.next = prev_node.next
                   prev_node.next = inserted_node
                   self.length += 1
               return  inserted_node
                   
        except  IndexError as err:
            return err
        
     #  update the value of the node at specific index list. => update_at_index
    def update_at_index(self,index, value):
        try: 
            node = self.get_at_index(index)
            if node is not None:
               node.value = value
               return  node
            else:
                raise IndexError("Node is not found at: " + str(index))
        
       
        except  Exception  as error:
             return  error



    # remove node from specific index
    def remove_at_index(self, index):
        if index < 0 or index >= self.length or self.length == 0:
            return False
        elif index == 0:
            self.remove_first()
            return True
        elif index == self.length - 1:
            self.remove_last()
            return True
        else:
            prev_node = self.get_at_index(index - 1)
            temp = prev_node.next
            prev_node.next = temp.next
            temp = None
            self.length -= 1
            return True
        
    # reverse list =>  reverse
    def reverse(self):
        if self.length == 0 or self.length == 1:
            print("The list cannot be reversed")
            return False
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = None
        prev = None
        for i in range(self.length):
            after = temp.next
            temp.next = prev
            prev = temp
            temp = after
        return True



    
if __name__  == '__main__':
    linked_list  = LinkedList()
    linked_list.prepend(10)
    pend =  linked_list.prepend(15)
    linked_list.insert_last(50)
    linked_list.insert_last(60)


    print(linked_list.get_head().value)

    print(linked_list.reverse())
    linked_list.print_list()
    
    print(linked_list.get_head().value)

        
      
       

        
          