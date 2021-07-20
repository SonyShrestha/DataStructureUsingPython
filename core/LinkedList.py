class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        llstr = ''

        while itr:
            llstr = llstr + str(itr.data)+' --> ' 
            itr = itr.next
        print(llstr)

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self,data):
        # If there is no element in linked list
        if self.head is None: 
            node=Node(data,None)
            return
        
        # If there are elements in linked list iterate through list from beginning till end
        itr=self.head
        while itr.next:
            itr=itr.next
        
        itr.next=Node(data,None)

    def insert_list(self,data_list):
        for ele in data_list:
            self.insert_at_end(ele)

    def insert_at(self,insert_idx,data):
        if insert_idx<0 or insert_idx>self.get_count():
            print("Invalid index position")
            return
        
        if insert_idx==0:
            self.insert_at_beginning(data)
            return
        
        else:
            counter=0
            itr=self.head
            while itr:
                if counter==insert_idx-1:
                    node=Node(data,itr.next)
                    itr.next=node
                    break
                itr=itr.next
                counter+=1
    
    def remove_at(self,delete_idx):
        if delete_idx<0 or delete_idx>=self.get_count():
            raise Exception("Invalid Index")

        if delete_idx==0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == delete_idx - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count+=1

    def remove_by_value(self,data):
        if self.head is None:
            return

        if self.head.data==data:
            self.head=self.head.next
            return 
        
        else:
            itr=self.head
            while itr.next:
                if itr.next.data==data:
                    itr.next=itr.next.next
                    return
                itr=itr.next


    def insert_after_value(self,after_value,data):
        if self.head is None:
            return

        if self.head.data==after_value:
            self.head.next=Node(data,self.head.next)
            return 

        itr=self.head
        while itr:
            if itr.data==after_value:
                itr.next=Node(data,itr.next)
                break
            itr=itr.next

    def get_count(self):
        itr=self.head
        counter=0
        while itr:
            counter+=1
            itr=itr.next
        return counter
        

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_beginning(1)
    ll.insert_at_end(3)
    ll.insert_list(["Sony","Shrestha"])
    ll.insert_at(2,"Hello")
    #ll.remove_at(1)
    ll.insert_after_value(1,"Smart")
    ll.remove_by_value("Sony")
    ll.print()
    length=ll.get_count()
    print(length)
