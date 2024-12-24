class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.cursor_l = 0
        self.cursor_i = 0
        return self

    def __next__(self):
        if self.cursor_l < len(self.list_of_list):
            for i in self.list_of_list[self.cursor_l:]:
                if self.cursor_i == len(i):
                    self.cursor_l += 1
                    self.cursor_i = 0
                else:    
                    for item in i[self.cursor_i]:
                        self.cursor_i += 1
                        return item
        raise StopIteration
                
list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

for i in FlatIterator(list_of_lists_1):
    print(i)