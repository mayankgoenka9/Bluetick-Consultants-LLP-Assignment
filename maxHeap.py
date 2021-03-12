import sys

class MaxHeap: 

	def __init__(self, maxsize): 
		
		self.maxsize = maxsize 
		self.size = 0
		self.Heap = [User(0)] * (self.maxsize + 1) 
		self.Heap[0] = User(sys.maxsize) 
		self.FRONT = 1

	def parent(self, pos): 
		
		return pos // 2

	def leftChild(self, pos): 
		
		return 2 * pos 

	def rightChild(self, pos): 
		
		return (2 * pos) + 1

	def isLeaf(self, pos): 
		
		if pos >= (self.size//2) and pos <= self.size: 
			return True
		return False

	def swap(self, fpos, spos): 
		
		self.Heap[fpos], self.Heap[spos] = (self.Heap[spos], 
											self.Heap[fpos]) 

	def maxHeapify(self, pos): 

		if not self.isLeaf(pos): 
			if (self.Heap[pos]._id < self.Heap[self.leftChild(pos)]._id or
				self.Heap[pos]._id < self.Heap[self.rightChild(pos)]._id): 

				if (self.Heap[self.leftChild(pos)]._id > 
					self.Heap[self.rightChild(pos)]._id): 
					self.swap(pos, self.leftChild(pos)) 
					self.maxHeapify(self.leftChild(pos)) 

				else: 
					self.swap(pos, self.rightChild(pos)) 
					self.maxHeapify(self.rightChild(pos)) 

	def insert(self, element): 
		
		if self.size >= self.maxsize: 
			return
		self.size += 1
		self.Heap[self.size] = element 

		current = self.size 

		while (self.Heap[current]._id > 
			self.Heap[self.parent(current)]._id): 
			self.swap(current, self.parent(current)) 
			current = self.parent(current) 

	def Print(self): 
		
		for i in range(1, self.size+1): 
			print(str(self.Heap[i]._id))  

	def extractMax(self): 

		popped = self.Heap[self.FRONT] 
		self.Heap[self.FRONT] = self.Heap[self.size] 
		self.size -= 1
		self.maxHeapify(self.FRONT) 
		
		return popped 

class User: 

	def __init__(self, _id): 
		
		self._id = _id 

user = User(2)

print('The maxHeap is ')
      
maxHeap = MaxHeap(20)
maxHeap.insert(User(1))
maxHeap.insert(User(7))
maxHeap.insert(User(1))
maxHeap.insert(User(8))
maxHeap.insert(User(6))
maxHeap.Print()