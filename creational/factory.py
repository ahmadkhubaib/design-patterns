from abc import ABCMeta, abstractmethod

#interface
class Shape(metaclass=ABCMeta):
	@abstractmethod
	def draw(self):
		pass

#concrete classes
class Circle(Shape):
	def draw(self):
		print('Circle is drawn')

class Rectangle(Shape):
	def draw(self):
		print('Rectangle is drawn')

class Square(Shape):
	def draw(self):
		print('Square is drawn')

#Factory method to call concrete classes
class ShapeFactory(object):
	@staticmethod
	def get_shape(shape_type):
		if shape_type == 1:
			return Circle()
		elif shape_type == 2:
			return Rectangle()
		elif shape_type == 3:
			return Square()
		return None

if __name__ == "__main__":
	rectangle = ShapeFactory.get_shape(1)
	rectangle.draw()

	circle = ShapeFactory.get_shape(2)
	circle.draw()