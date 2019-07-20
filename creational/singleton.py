class Singleton:
	__instance = None
	@staticmethod
	def getIncstance():
		if Singleton.__instance == None:
			Singleton()
		return Singleton.__instance
	
	def __init__(self):
		if Singleton.__instance != None:
			raise Exception("This class is Singleton.")
		else:
			Singleton.__instance = self

#first instance
mySingleton = Singleton()
print(mySingleton)

#verify instance
print(mySingleton.getIncstance())

#tried to create another instance
#should raise exception
mySingleton2 = Singleton()
print(mySingleton2)

#unreachable
print(mySingleton2.getIncstance())