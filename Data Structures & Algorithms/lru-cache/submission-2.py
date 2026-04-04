class Node:
    def __init__(self, key, val, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.tail = Node(0,0)
        self.head = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.key2object = {}

    def get(self, key: int) -> int:
        if key not in self.key2object:
            return -1
        
        self.key2object[key].prev.next = self.key2object[key].next
        self.key2object[key].next.prev = self.key2object[key].prev


        prev_temp = self.head.next
        self.head.next = self.key2object[key]
        self.key2object[key].prev = self.head
        prev_temp.prev = self.key2object[key]
        self.key2object[key].next = prev_temp

        return self.key2object[key].val
        

    def put(self, key: int, value: int) -> None:
        if key not in self.key2object:
            self.key2object[key] = Node(key, value)
            self.capacity -= 1
        else:
            self.key2object[key].prev.next = self.key2object[key].next
            self.key2object[key].next.prev = self.key2object[key].prev
            self.key2object[key].val = value
        cur = self.key2object[key]
            
        temp = self.head.next
        self.head.next = cur
        cur.prev = self.head
        temp.prev = cur
        cur.next = temp
        
        if self.capacity < 0:
            remove_node = self.tail.prev
            self.tail.prev = remove_node.prev
            self.tail.prev.next = self.tail
            self.key2object.pop(remove_node.key)
            self.capacity += 1





        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)