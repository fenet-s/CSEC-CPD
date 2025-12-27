class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.count = 0
        self.que = deque()
        

    def consec(self, num: int) -> bool:
        self.que.append(num)
        if num == self.value:
            self.count += 1

        if len(self.que) > self.k:
            removed = self.que.popleft()
            if removed == self.value:
                self.count -= 1

        return self.count == self.k
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)