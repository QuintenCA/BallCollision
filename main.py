import pygame
import math
import random
from circle import Circle
from vector import Vector
from hitbox import Hitbox

def color():
	pool = 200
	
	r = random.randint(0, pool)
	g = random.randint(0, pool - r)
	b = pool - r - g
	
	return r, g, b


def distance(point1, point2):
	xdist = point2[0] - point1[0]
	ydist = point2[1] - point1[1]
	
	distance = math.sqrt(xdist ** 2 + ydist ** 2)
	return distance

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode([1080, 720])
t = 0

circles = []
objects = []
cue = Circle([200, 400], 9.9, "gray")

circles.append(Circle([800, 400], 10, color()))

circles.append(Circle([824, 388], 10, color()))
circles.append(Circle([824, 412], 10, color()))

circles.append(Circle([848, 376], 10, color()))
circles.append(Circle([848, 400], 10, color()))
circles.append(Circle([848, 424], 10, color()))

circles.append(Circle([872, 364], 10, color()))
circles.append(Circle([872, 388], 10, color()))
circles.append(Circle([872, 412], 10, color()))
circles.append(Circle([872, 436], 10, color()))

circles.append(Circle([896, 352], 10, color()))
circles.append(Circle([896, 376], 10, color()))
circles.append(Circle([896, 400], 10, color()))
circles.append(Circle([896, 424], 10, color()))
circles.append(Circle([896, 448], 10, color()))

objects.extend(circles)

# objects.append(pygame.Rect(60, 0, 460, 40))
# objects.append(pygame.Rect(560, 0, 460, 40))
# objects.append(pygame.Rect(60, 680, 460, 40))
# objects.append(pygame.Rect(560, 680, 460, 40))
# objects.append(pygame.Rect(0, 60, 40, 600))
# objects.append(pygame.Rect(1040, 60, 40, 600))

objects.append(Hitbox(460, 40, 290, 20, [100, 50, 30]))
objects.append(Hitbox(460, 40, 790, 20, [100, 50, 30]))
objects.append(Hitbox(460, 40, 290, 700, [100, 50, 30]))
objects.append(Hitbox(460, 40, 790, 700, [100, 50, 30]))
objects.append(Hitbox(40, 600, 20, 360, [100, 50, 30]))
objects.append(Hitbox(40, 600, 1060, 360, [100, 50, 30]))

pockets = []
pockets.append(Circle([40, 40], 18, "black"))
pockets.append(Circle([1040, 40], 18, "black"))
pockets.append(Circle([40, 680], 18, "black"))
pockets.append(Circle([1040, 680], 18, "black"))
pockets.append(Circle([540, 35], 18, "black"))
pockets.append(Circle([540, 685], 18, "black"))

held = True
aiming = False
while True:
	clock.tick(1000)
	t += 1
	screen.fill([0, 100, 0])
	
	pygame.draw.rect(screen, [80, 40, 25], [0, 0, 1080, 40])
	pygame.draw.rect(screen, [80, 40, 25], [0, 680, 1080, 40])
	pygame.draw.rect(screen, [80, 40, 25], [0, 0, 40, 720])
	pygame.draw.rect(screen, [80, 40, 25], [1040, 0, 40, 720])

	objects[15].draw()
	objects[16].draw()
	objects[17].draw()
	objects[18].draw()
	objects[19].draw()
	objects[20].draw()
	
	for pocket in pockets:
		pocket.draw()
		
	for circle in circles:
		circle.move(objects)
		
	if held:
		cue.pos = pygame.mouse.get_pos()
		if cue.pos[0] > 400:
			cue.pos = [400, cue.pos[1]]
		cue.draw()
	else:
		cue.move(objects)
		
	pygame.display.flip()
	
	if aiming and not pygame.mouse.get_pressed()[0]:
		cue.color = "gray"
		aiming = False
		xdist = cue.pos[0] - pygame.mouse.get_pos()[0]
		ydist = cue.pos[1] - pygame.mouse.get_pos()[1]
		
		cue.velocity = Vector(xdist / 50, ydist / 50)
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
		if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
			if held:
				held = False
			elif distance(pygame.mouse.get_pos(), cue.pos) < cue.radius and cue.velocity.magnitude() < 0.01:
				cue.color = "white"
				aiming = True
