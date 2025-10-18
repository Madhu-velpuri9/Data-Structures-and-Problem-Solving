class Node:
    def __init__(self, data=None,next=None):
        self.next = next
        self.data = data
class LinkedList:
    def __init__(self,head=None):
        self.head = head
    def insertAtBeginning(self,data):
        node=Node(data,self.head)
        self.head=node
    def printList(self):
        if self.head==0:
            print("Linked List is Empty")
        itr=self.head
        llstr=''
        while itr:
            llstr+=str(itr.data)+ '-->'
            itr=itr.next
        print(llstr)
    def  insertAtend(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data,None)
    def insertVal(self,data_list):
        self.head=None
        for data in data_list:
            self.insertAtend(data)

    def getlength(self):
        count=0
        itr=self.head
        while itr:
            count+=1
            itr=itr.next

        return count
    def removeAt(self,index):
        if index<0 or index >self.getlength()-1:
            print('index invalid')
        if index==0:
            self.head=self.head.next
            return
        count=0
        itr=self.head
        while itr:
            if count == index-1:
                itr.next=itr.next.next
                break
            itr=itr.next
            count +=1
    def insertAt(self,index,data):
        if index<0 or index>self.getlength()-1:
            print('index invalid')
        if index==0:
            self.head=self.insertAtBeginning(data)
            return
        count=0
        itr=self.head
        while itr:
            if count==index-1:
                node=Node(data,itr.next)
                itr.next=node
                break
            itr=itr.next
            count+=1






ll=LinkedList()

ll.insertAtBeginning(1)
ll.insertAtBeginning(2)
ll.insertAtBeginning(3)
ll.insertAtend(4)
ll.insertAt(2,5)
ll.removeAt(3)
ll.printList()
print(ll.getlength())
ll.insertVal(['madhu','chinnu','love'])
ll.printList()


