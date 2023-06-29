class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:
    def __init__(self):
        self.len = 1000
        self.table = defaultdict(ListNode)

    def put(self, key: int, value: int) -> None:
        hash = self.hash(key)
        if self.table[hash].value is None:
            self.table[hash] = ListNode(key, value)
            return

        node = self.table[hash]

        while node:
            if node.key == key:
                node.value = value
                return
    
            if node.next is None:
                break

            node = node.next
        
        node.next = ListNode(key, value)

    def get(self, key: int) -> int:
        hash = self.hash(key)
        node = self.table[hash]

        while node:
            if node.key == key:
                return node.value

            node = node.next

        return -1

    def remove(self, key: int) -> None:
        hash = self.hash(key)
        node = self.table[hash]
        
        while node:
            if node.key == key:
                node.value = -1
                return

            node = node.next

    def hash(self, key: int) -> int:
        return key % self.len


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)