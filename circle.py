from vector import Vector
from line import Line
from hitbox import Hitbox
import pygame
import math


def dist(point1, point2):
	xdist = point2[0] - point1[0]
	ydist = point2[1] - point1[1]

	distance = math.sqrt(xdist ** 2 + ydist ** 2)
	return distance


class Circle:
	def __init__(self, pos, radius, color="white"):
		self.pos = pos
		self.radius = radius
		self.velocity = Vector(0, 0)
		self.color = color
		self.mass = radius ** 2 / 100

	def momentum(self):
		return Vector().make(self.velocity.magnitude() * self.mass, self.velocity.direction())

	def move(self, circles):
		v = self.velocity

		self.pos = [self.pos[0] + v.x, self.pos[1] + v.y]
		self.velocity.mult(0.999)

		if self.pos[0] < 0 + self.radius and v.x < 0:
			v.x *= -1
		if self.pos[0] > 1080 - self.radius and v.x > 0:
			v.x *= -1
		if self.pos[1] < 0 + self.radius and v.y < 0:
			v.y *= -1
		if self.pos[1] > 720 - self.radius and v.y > 0:
			v.y *= -1

		for circle in circles:
			if circle != self:
				self.collide(circle)

		pygame.draw.circle(pygame.display.get_surface(), self.color, self.pos, self.radius)

	def draw(self):
		pygame.draw.circle(pygame.display.get_surface(), self.color, self.pos, self.radius)

	def collide(self, other):
		if type(other) == Circle:
			xdist = other.pos[0] - self.pos[0]
			ydist = other.pos[1] - self.pos[1]
			distance = math.sqrt(xdist ** 2 + ydist ** 2)

			if distance < self.radius + other.radius:  # then we have collision!
				print()
				print("ball1 pre-collision momentum:", self.momentum().magnitude())
				print("ball2 pre-collision momentum:", other.momentum().magnitude())
				print("total pre-collision momentum:", self.momentum().add(other.momentum()).magnitude())
				print()

				# Find the vectors after circles bounce off of each other
				angle = math.atan2(ydist, xdist)
				totalmass = self.mass + other.mass
				relativeV = self.velocity.sub(other.velocity)
				tangent = angle + math.pi / 2
				angleDiff = relativeV.direction() - tangent
				energyloss = relativeV.magnitude() * 0.05

				impactV = Vector().make(relativeV.magnitude() * math.sin(angleDiff), angle)
				impactV = impactV.mult(2 * other.mass / totalmass)

				impactV2 = Vector().make((energyloss - impactV.magnitude() * self.mass) / other.mass, angle)

				self.velocity = self.velocity.sub(impactV)
				other.velocity = other.velocity.add(impactV2)

				self.pos = [self.pos[0] + self.velocity.x, self.pos[1] + self.velocity.y]
				other.pos = [other.pos[0] + other.velocity.x, other.pos[1] + other.velocity.y]

				print()
				print("ball1 post-collision momentum:", self.momentum().magnitude())
				print("ball2 post-collision momentum:", other.momentum().magnitude())
				print("total post-collision momentum:", self.momentum().add(other.momentum()).magnitude())
				print()
				print()

		if type(other) == pygame.Rect:
			p1 = other.topleft
			p2 = other.topright
			p3 = other.bottomleft
			p4 = other.bottomright

			perp = Line(self.pos, other.center)


	def hit(self, rectangle):
		if not (self.pos[0] + self.radius > rectangle.x or
				self.pos[0] - self.radius < rectangle.x + rectangle.width or
				self.pos[1] - self.radius < rectangle.y + rectangle.height or
				self.pos[1] + self.radius > rectangle.y):

			return False

		else:
			p1 = rectangle.topleft
			p2 = rectangle.topright
			p3 = rectangle.bottomleft
			p4 = rectangle.bottomright

			if not (dist(p1, self.pos) < self.radius or dist(p2, self.pos) < self.radius
					or dist(p3, self.pos) < self.radius or dist(p4, self.pos) < self.radius):
				return False

		angle = math.atan2(rectangle.center[1] - self.pos[1], rectangle.center[0] - self.pos[0])

		if 0 <= angle < math.pi / 4 or (7 / 4) * math.pi <= angle < 2 * math.pi or (3 / 4) * math.pi <= angle < (
				5 / 4) * math.pi:
			self.velocity.x = -self.velocity.x
		elif math.pi / 4 <= angle < (3 / 4) * math.pi or (5 / 4) * math.pi <= angle < (7 / 4) * math.pi:
			self.velocity.y = -self.velocity.y
