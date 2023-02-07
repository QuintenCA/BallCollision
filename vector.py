import math


class Vector:
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y
	
	def magnitude(self, newMag=None):
		if newMag is None:
			return math.sqrt((self.x ** 2) + (self.y ** 2))
		
		dir = self.direction()
		self.x = newMag * math.cos(dir)
		self.y = newMag * math.sin(dir)
		return self
	
	def direction(self, newDir=None):
		if newDir is None:
			return math.atan2(self.y, self.x)
		
		mag = self.magnitude()
		self.x = mag * math.cos(newDir)
		self.y = mag * math.sin(newDir)
		return self
	
	def add(self, other):
		return Vector(self.x + other.x, self.y + other.y)
	
	def sub(self, other):
		return Vector(self.x - other.x, self.y - other.y)
	
	def dot(self, other):
		return (self.x * other.x) + (self.y * other.y)
	
	def mult(self, num):
		return self.magnitude(self.magnitude() * num)
	
	def inverse(self):
		return Vector(-self.x, -self.y)
	
	def make(self, newMag, newDir):
		self.magnitude(newMag)
		self.direction(newDir)
		return self
