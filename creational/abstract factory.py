from abc import ABCMeta, abstractmethod

#shape interface
class Shape(metaclass=ABCMeta):
	@abstractmethod
	def draw(self):
		pass

#color interface
class Color(metaclass=ABCMeta):
	@abstractmethod
	def fill(self):
		pass

# factory interface to accomodate all type of interfaces
class AbstractFactory(metaclass=ABCMeta):
	@abstractmethod
	def get_color(self):
		pass
	
	@abstractmethod
	def get_shape(self):
		pass

class Rectangle(Shape):
	def draw(self):
		print('A rectangle is drawn.')

class Square(Shape):
	def draw(self):
		print('A square is drawn.')

class Green(Color):
	def fill(self):
		print('Green color is filled.')

class Blue(Color):
	def fill(self):
		print('Blue color is filled.')

#create shape factory by using abstract methods defined in abstract factory
class ShapeFactory(AbstractFactory):
	def get_shape(self,shape_type):
		if shape_type == None:
			return None
		elif shape_type == 1:
			return Rectangle()
		elif shape_type == 2:
			return Square()
		return None

	def get_color(self):
		return None

#create color factory by using abstract methods defined in abstract factory
class ColorFactory(AbstractFactory):
	def get_color(self,color_type):
		if color_type == None:
			return None
		elif color_type == 1:
			return Green()
		elif color_type == 2:
			return Blue()
		return None
	
	def get_shape(self):
		return None

class FactoryProducer(object):
	@staticmethod
	def get_factory(choice):
		if choice == 'shape':
			return ShapeFactory()
		elif choice == 'color':
			return ColorFactory()
		return None

if __name__ == "__main__":
	shape_factory = FactoryProducer.get_factory('shape')
	rectangle = shape_factory.get_shape(1)
	rectangle.draw()

	color_factory = FactoryProducer.get_factory('color')
	green = color_factory.get_color(1)
	green.fill()