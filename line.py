import math


def round2(number):
	return round(number * 1000000) / 1000000


class Line:
	def __init__(self, p1, p2, length=0):
		self.ray = False
		self.p1 = p1
		if length is not None and (type(p2) == int or type(p2) == float):
			if length == 0:
				length = 1
				self.ray = True
			self.p2 = (p1[0] + length * math.cos(p2), p1[1] + length * math.sin(p2))
		else:
			self.p2 = p2
		
	def intersect(self, other):
		denominator = self.A() * other.B() - other.A() * self.B()
		if denominator == 0:
			return None
		
		x = round2((other.B() * self.C() - self.B() * other.C()) / denominator)
		y = round2((self.A() * other.C() - other.A() * self.C()) / denominator)
		
		point = (x, y)
		
		if self.ray and Line(self.p1, point).angle() == self.angle():
				self.p2 = point
		
		if other.ray and Line(other.p1, point).angle() == other.angle():
				other.p2 = point
		
		if not ((self.p1[0] <= x <= self.p2[0] or self.p2[0] <= x <= self.p1[0]) and
		        (self.p1[1] <= y <= self.p2[1] or self.p2[1] <= y <= self.p1[1])):
			return None
		
		if not ((other.p1[0] <= x <= other.p2[0] or other.p2[0] <= x <= other.p1[0]) and
		        (other.p1[1] <= y <= other.p2[1] or other.p2[1] <= y <= other.p1[1])):
			return None
		
		return point
	
	def length(self):
		dist = math.sqrt((self.xdist() ** 2) + self.ydist() ** 2)
		return round2(dist)
	
	def xdist(self):
		return self.p2[0] - self.p1[0]

	def ydist(self):
		return self.p2[1] - self.p1[1]
	
	def A(self):
		return self.p2[1] - self.p1[1]
	
	def B(self):
		return self.p1[0] - self.p2[0]
	
	def C(self):
		return self.A() * self.p1[0] + self.B() * self.p1[1]
	
	def center(self):
		point = ((self.p1[0] + self.p2[0]) / 2, (self.p1[1] + self.p2[1]) / 2)
		return point
	
	def angle(self):
		return round2(math.atan2(self.ydist(), self.xdist()))
		
		