from random import random, shuffle
from datetime import datetime
import uuid

class SmallObject:
	def __init__(self):
		self.num = uuid.uuid4()

class BigObject:
	def __init__(self):
		self.num = random()
		self.list = [random(), random(), random(), random()]
		self.biggerlist = [self.list, self.list, self.list]

print "begin ..."

a = []
for i in xrange(1, 1000):
	a.append(uuid.uuid4())
shuffle(a)
b = []
for i in xrange(1, 1000):
	b.append(BigObject())
shuffle(b)
c = []
for i in xrange(1, 1000):
	c.append(SmallObject())
shuffle(c)

print "..."

start1 = datetime.now()
for element in a:
	if element in a:
		pass
end1 = datetime.now()

start2 = datetime.now()
for element in b:
	if element in b:
		pass
end2 = datetime.now()

start3 = datetime.now()
for element in c:
	if element in c:
		pass
end3 = datetime.now()


print "speed of first operation:", end1-start1
print "speed of second operation:", end2-start2
print "speed of third operation:", end3-start3

# traversing lists of objects is minimally dependent on the size of the object
# but traversing lists of uuid4s is about ~4x faster