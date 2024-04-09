class FourCal:
	def __init__(self, first, second):
		self.first = first
		self.second = second
	def setdata(self, first, second):
		self.first = first
		self.second = second
	def add(self):
		result = self.first + self.second
		return result

if __name__ == "__main__":
	print(FourCal(3,2))
