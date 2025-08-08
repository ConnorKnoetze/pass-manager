class Entries():
    def __init__(self):
        self.__entries = []
        self.__size = 0

    @property
    def entries(self):
        return self.__entries

    @entries.getter
    def entries(self):
        return self.__entries

    def add_entry(self, value):
        self.__entries.append(value)
        self.__size += 1

    @property
    def size(self):
        return self.__size
    
    @size.getter
    def size(self):
        return self.__size


    def __len__(self):
        return self.__size