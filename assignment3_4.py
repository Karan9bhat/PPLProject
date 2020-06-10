import turtle
wn = turtle.Screen()
wn.bgcolor("light green")
wn.title("Turtle")
skk = turtle.Turtle()

##########-----------------------------------------      ANIMALS      -------------------------------------######################



class Lion :
	legs = 0
	wings = True
	bones = True
	def set_parts(self, legs, wings, bones) :
		self.legs = legs
		self.__Wings = wings
		self.__Bones = bones
	def get_parts(self) :
		return self.legs, self.__Wings, self.__Bones

l = Lion()
l.set_parts(4, False, True)

print(l.get_parts())

class Tiger(Lion) :
	pass

l = Tiger()
l.set_parts(4, False, True)
print(l.get_parts())

class Crow(Lion) :
	pass
	legs = 2
	wings = True
	def set_parts(self, legs, wings) :
		self.legs = legs
		self.__Wings = wings
	def get_parts(self) :
		return self.legs, self.__Wings, self.bones

l = Crow()
l.set_parts(2, True)
print(l.get_parts())

class Snakes() :
	def __init__(self, legs = 0, wings = False, bones = True) :
		self.__legs = legs
		self.__wings = wings
		self.__bones = bones
	def set_legs(self, legs) :
		self.__legs = legs
	def set_wings(self, wings) :
		self.__wings = wings
	def set_bones(self, bones) :
		self.__bones = bones
	def get_legs(self, legs) :
		print(self.__legs)
	def get_bones(self, bones) :
		print(self.__bones)
	def get_wings(self, wings) :
		print(self.__wings)

s = Snakes()
s.set_legs(0)
s.set_bones(True)
s.set_wings(False)
s.get_legs(0)
s.get_wings(False)
s.get_bones(True)

class Dog(Lion) :
	pass
	def bark(self) :
		return "WOOF!"

d = Dog()
d.set_parts(4, False, True)
print(d.get_parts(), d.bark())

class Dog :
	def bark(self) :
		print("The Dogs BARK")

class Cat(Dog) :
	def bark(self) :
		super().bark()
		print("The Cats MEOW")

c = Cat()
c.bark()

class ant(Lion) :
	pass
	legs = 6
	def set_legs(self, legs) :
		self.legs = legs
	def get_legs(self) :
		return self.legs

a = ant()
a.set_parts(6, False, False)
print(a.get_parts())

class dolphin(Lion) :
	pass
	def swim(self) :
		return "Dolphins can swim"

d = dolphin()
d.set_parts(0, False, True)
print(d.get_parts(), d.swim())

class shark(dolphin) :
	pass
	def predator(self) :
		print("Sharks are the most dangerous predators in sea")
	def fins(self) :
		print("Sharks have fins")

shark().predator()
shark().fins()
class snails(Dog) :
	pass
	def crawl(self) :
		print("Snails crawl")
	def bark(self) :
		super().bark()
		print("Snails are slow")
		
snails().crawl()
snails().bark()




##################---------------------------           Shapes            -------------------------###############################


class circle :
	def __init__(self) :
		self.sides = 0
		self.__angle = 360
	def set_properties(self, side, angle) :
		self.sides = side
		self.__angles = angle
	def get_properties(self) :
		print("Sides, Angle : ", self.sides, ",", self.__angle)
	def area_of_circle(self) :
		print("Area of a circle is 3.14*r^2")
	def draw(self) :
		skk.circle(100)
	def hexagon_draw(self, side) :
		for i in range(0, self.sides) :
			skk.forward(250)
			skk.right(60)

c = circle()
c.set_properties(0, 360)
c.get_properties()
c.area_of_circle()
c.draw()

class triangle(circle) :
	pass
	def difference_in_triangle_and_circle(self) :
		super().area_of_circle()
		print("Area of triangle is 0.5*b*h")
	def draw(self, side) :
		for i in range(self.sides) :
			skk.forward(170)
			skk.right(120)
	
t = triangle()
t.set_properties(3, 360)
t.get_properties()
t.difference_in_triangle_and_circle()
t.draw(3)

class square() :
	def __init__(self) :
		self.sides = 4
	def edges(self) :
		print("The square has four equal sides")
	def draw(self, side) :
		for i in range(self.sides) :
			skk.forward(200)
			skk.right(360/self.sides)
	def draw_rectangle(self) :
		for i in range(2) :
			skk.forward(150)
			skk.right(90)
			skk.forward(90)
			skk.right(90)

class rectangle(square) :
	pass
	def edges(self) :
		print("The rectangle has four opposite equal sides")
		super().draw_rectangle()

square().edges()
square().draw(4)
rectangle().edges()

class pentagon(triangle) :
	pass
	def each_angle(self) :
		print("Each angle is of 72 degrees for regular pentagon")
	def draw(self, side) :
		for i in range(self.sides) :
			skk.forward(150)
			skk.right(360/self.sides)

p = pentagon()
p.set_properties(5, 360)
p.get_properties()
p.each_angle()
p.draw(5)

class hexagon(circle) :
	pass
	def Sides(self) :
		return "Number of sides of hexagon is six"

h = hexagon()
h.set_properties(6, 360)
print(h.get_properties(), h.Sides())
h.hexagon_draw(6)

class tetrahedron :
	def __init__(self) :
		self.sides = 8
		self.__angles = 360
		self._vertices = 5
	def set_properties(self, side, angle, vertex) :
		self.sides = side
		self.__angles = angle
		self._vertices = vertex
	def get_properties(self) :
		return self.sides, self.__angles, self._vertices
	def special_property(self) :
		print("It is a 3D figure")

t = tetrahedron()
t.set_properties(8, 360, 5)
print(t.get_properties())

class cube(tetrahedron) :
	pass
	def special_property(self) :
		super().special_property()
		print("Cube is also 3D")

c = cube()
c.set_properties(12, 360, 8)
print(c.get_properties())
c.special_property()





















