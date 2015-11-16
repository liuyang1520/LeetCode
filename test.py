class abc(object):

	def __init__(self, x):
		self.a = x
		# self.b = "Another"


	def change(self):
		self.a = "New a"
		self.b = "sdsdf"




s = abc("Origin")
s.change()
print s.a, s.b