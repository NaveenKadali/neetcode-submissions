class MyHashSet:

    def __init__(self):

        import math
        self.required_bit_groups = [0 for i in range(math.ceil(10000001/32))]
    
    def add(self, num: int) -> None:
        index = num//32
        shift_value = num%32

        print("add", index, shift_value, num%32, num/32)
        self.required_bit_groups[index] |= (1<<shift_value)

    def remove(self, num: int) -> None:
        
        index = num//32
        shift_value = num%32

        bit_to_make_zero = 1 << shift_value
        self.required_bit_groups[index] = self.required_bit_groups[index] & (~ bit_to_make_zero)

    def contains(self, num: int) -> bool:

        index = num//32
        shift_value = num%32
        bit_group = self.required_bit_groups[index]
        
        if (bit_group & (1 << shift_value)):
            return True
        else:
            return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)