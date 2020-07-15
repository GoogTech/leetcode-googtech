'''
@Author: Goog Tech
@Date: 2020-07-13 17:51:29
@Description: ordered list
@FilePath: /leetcode-googtech/data-structures-and-algorithms/Python/list/unordered list/OrderedList.py
'''

'''
@description: 声明链表
'''
class Node:
    
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data
    
    def getNext(self):
        return self.next
    
    def setData(self,newdata):
        self.data = newdata
    
    def setNext(self,newnext):
        self.next = newnext
        

'''
@description: 操作有序链表
'''
class OrderedList:
    
    ''' 初始化链表 '''
    def __init__(self):
        self.head = None

    ''' 判断链表是否为空 '''
    def isEmpty(self):
        return self.head == None
    
    ''' 向链表中插入新节点 '''
    def add(self,item):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous =  current
                current = current.getNext()
        temp = Node(item)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

    ''' 获取链表的长度 '''
    def getLength(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count

    ''' 搜索链表中指定数值节点 '''
    def search(self,item):
        current = self.head
        found = False
        stop  = False
        while current != None and not found and not stop:
            try:
                if current.getData() == item:
                    found = True
                else:
                    if current.getData > item:
                        stop = True
                    else:
                        current = current.getNext()
            except AttributeError:
                print('error: the node of head is null')
                exit(1)
        return found

    ''' 移除链表中指定数值节点 ''' 
    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext)
        return found


'''
@description: 测试
'''
ud = OrderedList()
ud.add(1)
ud.add(2)
ud.add(3)
print('链表的长度: %s'%ud.getLength())
print('链表是否为空: %s'%ud.isEmpty())
print('是否成功查找到指定元素: %s'%ud.search(1))
print('是否成功移除指定元素: %s'%ud.remove(2))
print('链表的长度: %s'%ud.getLength())
