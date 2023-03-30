class Queue:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__rear=-1
        self.__front=0

    def is_full(self):
        if(self.__rear==self.__max_size-1):
            return True
        return False

    def is_empty(self):
        if(self.__front>self.__rear):
            return True
        return False

    def enqueue(self,data):
        if(self.is_full()):
            print("Queue is full!!")
        else:
            self.__rear+=1
            self.__elements[self.__rear]=data

    def dequeue(self):
        if(self.is_empty()):
            print("Queue is empty!!")
        else:
            data=self.__elements[self.__front]
            self.__front+=1
            return data

    def display(self):
        for index in range(self.__front, self.__rear+1):
            print(self.__elements[index])

    def get_max_size(self):
        return self.__max_size

queue1=Queue(4)
print("It is full",queue1.is_full())
print("It is empty",queue1.is_empty())
queue1.enqueue(100)
queue1.display()
queue1.enqueue(200)
queue1.enqueue(300)
queue1.enqueue(400)
queue1.display()
queue1.enqueue(500)
queue1.display()
print("element deleted",queue1.dequeue())
queue1.display()
                

#Q1
class Queue:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__rear=-1
        self.__front=0

    def is_full(self):
        if(self.__rear==self.__max_size-1):
            return True
        return False

    def is_empty(self):
        if(self.__front>self.__rear):
            return True
        return False

    def enqueue(self,data):
        if(self.is_full()):
            print("Queue is full!!")
        else:
            self.__rear+=1
            self.__elements[self.__rear]=data

    def dequeue(self):
        if(self.is_empty()):
            print("Queue is empty!!")
        else:
            data=self.__elements[self.__front]
            self.__front+=1
            return data

    def display(self):
        for index in range(self.__front, self.__rear+1):
            print(self.__elements[index])

    def get_max_size(self):
        return self.__max_size

    def __str__(self):
        msg=[]
        index=self.__front
        while(index<=self.__rear):
            msg.append((str)(self.__elements[index]))
            index+=1
        msg=" ".join(msg)
        msg="Queue data:"+msg
        return msg

def divi(queue1):
    size=queue1.get_max_size()
    queue2=Queue(size)
    while size>0:
        element=queue1.dequeue()
        if all(element%i==0 for i in range(1,11)):
            queue2.enqueue(element)
        size-=1
    return queue2
                    

queue1=Queue(5)
queue1.enqueue(13983)
queue1.enqueue(10080)
queue1.enqueue(7113)
queue1.enqueue(2520)
queue1.enqueue(2500)
queue1.display()
print(divi(queue1))


#Q2
class Queue:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__rear=-1
        self.__front=0
    def is_full(self):
        if(self.__rear==self.__max_size-1):
            return True
        return False
    def is_empty(self):
        if(self.__front>self.__rear):
            return True
        return False
    def enqueue(self,data):
        if(self.is_full()):
            print("full")
        else:
            self.__rear+=1
            self.__elements[self.__rear]=data
    def dequeue(self):
        if(self.is_empty()):
            print("empty")
        else:
            data=self.__elements[self.__front]
            self.__front+=1
            return data
    def display(self):
        for index in range(self.__front,self.__rear+1):
            print(self.__elements[index])
    def get_max_size(self):
        return self.__max_size
    def _str_(self):
        msg=[]
        index=self.__front
        while(index<=self.__rear):
            msg.append((str)(self.__elemnets[index]))
            index+=1
        msg=" ".join(msg)
        msg="Queue data:"+msg
        return msg
def merge(q1,q2):
    l1=[]
    l2=[]
    l3=[]

    while(not q1.is_empty()):
        l1.append(q1.dequeue())
    while(not q2.is_empty()):
        l2.append(q2.dequeue())

    check=0
    if len(l1)<len(l2):
        length=len(l1)
    else:
        length=len(l2)
        check=1

    if str(l1[0]).isdigit():
        integer=l1
        string=l2
    else:
        integer=l2
        string=l1

    flag=0
    j,k=0,0
    for  i in range(0,2*length):
        if flag==0:
            l3.append(integer[j])
            flag=1
            j+=1
        elif flag==1:
            l3.append(string[k])
            flag=0
            k+=1
    if check==0:
        for i in l2:
            if i not in l3:
                l3.append(i)
    elif check==1:
        for i in l1:
            if i not in l3:
                l3.append(i)
    merge=Queue(len(l3))
    for item in l3:
        merge.enqueue(item)
    return merge

q1=Queue(3)
q2=Queue(6)
q1.enqueue(3)
q1.enqueue(6)
q1.enqueue(8)
q2.enqueue("b")
q2.enqueue("y")
q2.enqueue("u")
q2.enqueue("t")
q2.enqueue("r")
q2.enqueue("0")

m=merge(q1,q2)
m.display()







    




            











