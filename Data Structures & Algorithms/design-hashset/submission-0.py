class MyHashSet:

    def __init__(self):
        self.set_variable = set()

    def add(self, key: int) -> None:
        if key in self.set_variable:
            pass
        else:
            self.set_variable.add(key)

    def remove(self, key: int) -> None:
        if key in self.set_variable:
            self.set_variable.remove(key)

    def contains(self, key: int) -> bool:
        if key in self.set_variable:
            return True
        else:
            return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)