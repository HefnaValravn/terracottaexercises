from abc import ABC, abstractmethod


class StorageDevice:
    def __init__(self, block_count, block_size):
        self.__available_blocks = [i for i in range(0, block_count)]
        self.__used_blocks = []
        self.__block_size = block_size
        
    @property
    def available_block_count(self):
        return len(self.__available_blocks)
    
    @property
    def used_block_count(self):
        return len(self.__used_blocks)
    
    @property
    def total_block_count(self):
        return self.available_block_count() + self.used_block_count()
    
    @property
    def block_size(self):
        return self.__block_size
    
    
    def allocate(self, block_count):
        if block_count > self.available_block_count:
            raise RuntimeError("Not enough space")
        for i in range(0, block_count):
            self.__used_blocks.append(self.__available_blocks.pop())
            
            
    def free(self, blocks):
        for block in blocks:
            if block not in self.__used_blocks:
                raise RuntimeError("Block not in use")
            self.__used_blocks.remove(block)
            self.__available_blocks.append(block)
            
            
            
            
class Entity(ABC):
    
    @staticmethod
    def is_valid_name(name):
        ...
        
    def __init__(self, storage, name):
        self.__storage = storage
        if not self.is_valid_name(name):
            raise RuntimeError("Invalid name")
        self.__name = name
        
        
    @property
    def name(self):
        return self.__name
        
    @name.setter
    def name(self, value):
        if not self.is_valid_name(value):
            raise RuntimeError("Invalid name")
        self.__name = value
    
    
    @property
    def storage(self):
        return self.__storage
    
    @property
    @abstractmethod
    def size_in_blocks(self):
        ...
        
    @property
    def size_in_bytes(self):
        return self.size_in_blocks() * self.storage.block_size
    
    @abstractmethod
    def clear(self):
        ...
            
            
            
class File(Entity):
    def __init__(self, storage, name):
        super().__init__(storage, name)
        self._blocks = []
        
        
    def grow(self, block_count):
        allocated_blocks = self.storage.allocate(block_count)
        self._blocks.extend(allocated_blocks)
        
        
    @property
    def size_in_blocks(self):
        return len(self._blocks)
    
    
    def clear(self):
        self.storage.free(self._blocks)
        self._blocks = []
        
        
        
class Directory(Entity):
    def __init__(self, storage, name):
        super().__init__(storage, name)
        self._children = []
        
    def add(self, entity):
        self._children.append(entity)
        
    @property
    def size_in_blocks(self):
        return sum(child.size_in_blocks for child in self._children)
        
    def clear(self):
        for child in self._children:
            if child.size_in_blocks != 0:
                child.clear()
        
        self._children = []
    