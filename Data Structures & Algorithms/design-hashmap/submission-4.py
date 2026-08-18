class LinkedList:
    def __init__(self, key=None, value=None) -> None:
        self.key = key
        self.value = value
        self.next = None
    
    def add(self, key, value):

        if self.key is None:
            self.key = key
            self.value = value
            return
        
        while self.key is not None and self.value is not None:

            if self.key == key:
                self.value = value
                return
            elif self.next:
                self = self.next
            else:
                self.next = LinkedList()
                self.next.add(key=key, value=value)
    
    def get(self, key):

        if self.key == key:
            return self.value
        
        while self.next:
            self = self.next
            return self.get(key=key)
        
        return -1
    
    def remove(self, key):

        if self.key == key:
            if self.next:
                self.key = self.next.key
                self.value = self.next.value
                self.next = self.next.next
            else:
                self.key = None
                self.value = None
                self.next = None
        else:
            if self.next:
                self.next.remove(key=key)
            else:
                return 
                

class MyHashMap:

    def __init__(self, key=None, value=None):
        self.hash_buckets = [[LinkedList(key=key, value=value)] for i in range(1000000//1000)]

    def get_hash_map_linked_list(self, key):

        bucket_index = key % 1000
        hash_bucket = self.hash_buckets[bucket_index]
        linked_list = hash_bucket[0]

        return linked_list

    def put(self, key: int, value: int) -> None:

        linked_list = self.get_hash_map_linked_list(key)
        linked_list.add(key, value)


    def get(self, key: int) -> int:
        
        linked_list = self.get_hash_map_linked_list(key)
        return_value = linked_list.get(key)
        
        return return_value


    def remove(self, key: int) -> None:
        
        linked_list = self.get_hash_map_linked_list(key)
        return_value = linked_list.remove(key)
        
        return return_value
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)