class MyHashSet:

    def __init__(self):
        self.set_variable = [None]*10000001

    def add(self, key: int) -> None:

        if self.set_variable[key] is not None:
            pass
        else:
            self.set_variable[key] = key

    def remove(self, key: int) -> None:

        if self.set_variable[key] is not None:
            self.set_variable[key] = None

    def contains(self, key: int) -> bool:

        if self.set_variable[key] is not None:
            return True
        else:
            return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)