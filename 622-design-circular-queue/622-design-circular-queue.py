class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.circularQueue = [-1]*k
        self.frontIdx = -1
        self.rearIdx = -1

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
        self.rearIdx = (self.rearIdx+1) % self.size   
        self.circularQueue[self.rearIdx] = value
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        self.frontIdx = (self.frontIdx+1) % self.size
        self.circularQueue[self.frontIdx] = -1
        
        return True
    
    def Front(self) -> int:
        if self.isEmpty():
            return -1
        
        return self.circularQueue[(self.frontIdx+1)%self.size]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        
        return self.circularQueue[self.rearIdx]

    def isEmpty(self) -> bool:
        for val in self.circularQueue:
            if val != -1:
                return False
        return True

    def isFull(self) -> bool:
        for val in self.circularQueue:
            if val == -1:
                return False
        return True

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()