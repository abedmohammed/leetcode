class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache(object):
    def __init__(self, capacity):
        self.dic = {}
        self.capacity = capacity
        self.head = ListNode(0, 0)
        self.tail = ListNode(-1, -1)
        self.head.prev = self.tail
        self.tail.next = self.head

    def get(self, key):
        if(key in self.dic):
            node = self.dic[key]
            self.removeFromList(node)
            self.addToHead(node)
            return node.value
        else:
            return -1
        

    def put(self, key, value):
        if(key in self.dic):
            node = self.dic[key]
            self.removeFromList(node)
            self.addToHead(node)
            node.value = value
        else:
            if(len(self.dic) >= self.capacity):
              self.removeFromTail()
            node = ListNode(key, value)
            self.addToHead(node)
            self.dic[key] = node


    def removeFromList(self, node):
        previousNode = node.prev
        nextNode = node.next

        previousNode.next = nextNode
        nextNode.prev = previousNode

    def addToHead(self, node):
        oldHead = self.head.prev
        oldHead.next = node
        node.prev = oldHead
        node.next = self.head
        self.head.prev = node

    def removeFromTail(self):
        if len(self.dic) == 0: return
        tailNode = self.tail.next
        self.removeFromList(tailNode)
        self.dic.pop(tailNode.key)

    def printList(self):
        node = self.tail
        string = ""
        while(node):
            string += str(node.key) + " -> "
            node = node.next
        print(string)
            

        
        


        


lRUCache = LRUCache(2)
lRUCache.put(1, 2)
lRUCache.put(2, 2)
lRUCache.printList()
lRUCache.get(1)
lRUCache.get(1)
lRUCache.printList()
lRUCache.put(2, 2)
lRUCache.printList()
lRUCache.get(1)
lRUCache.printList()
lRUCache.put(3, 3)
lRUCache.printList()
lRUCache.get(2)
lRUCache.put(4, 4)
lRUCache.get(1)
lRUCache.get(3)
lRUCache.get(4)
lRUCache.printList()