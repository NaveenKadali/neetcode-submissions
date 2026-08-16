class MyHashSet:

    def __init__(self):
        self.hash_buckets = [[] for i in range(1000)]
        

    def add(self, key: int) -> None:
        hash_bucket_index = key % 1000;

        if key in self.hash_buckets[hash_bucket_index]:
            pass
        else:
            self.hash_buckets[hash_bucket_index].append(key)

    def remove(self, key: int) -> None:
        
        hash_bucket_index = key % 1000;
        
        if key in self.hash_buckets[hash_bucket_index]:
            self.hash_buckets[hash_bucket_index].remove(key)

        

    def contains(self, key: int) -> bool:

        hash_bucket_index = key % 1000;

        if key in self.hash_buckets[hash_bucket_index]:
            return True
        else:
            return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)