from random import seed, randint
from time import time
import argparse
class arg:
	parser = argparse.Argpars
	def__init__(self):

class encryipt():
	
	def main(self, x, alphabet):
		num3 = (self.num1 * self.num2 + alphabet.index(x)**11)**11
		
		seed(self.num2)
		pro = (num3+randint(1,1000000))
		#print(str(pro))
		
		binary2 = int("{0:b}".format(pro))
		return binary2
		#return pro

	def isPrime(self, p):
		if(p==2):return True
		if(not(p&1)):return False
		return pow(2,p-1,p)==1
		
	def set_prime(self, tom, prv=1):
		x= False
		seed(time())
		y=None
		while x == False:
			
			
			if y != prv:
				# seed(tom)
				
				# self.seed = randint(1,10000)
				
				# seed(self.seed)
				y = randint(10**600, 10**700)
				x = self.isPrime(y)
				# tom += 1
		print(tom)
		return y	
	def __init__(self,message):
		
		alphabet = 'abcdefghijklmnopqrstuvwxyz 1234567890.!@#$%^&*()~{}:"|\\<>?/.,\';[]'
		self.message = message

		self.num1 = self.set_prime(tom=300)
		print(self.num1)
		self.num2 = self.set_prime(prv=self.num1, tom=200)
		print(self.num2)
		print("[", end = '')
		for i in self.message:
			print('{},'.format(self.main(i, alphabet)), end='')
		print("]", end='')
a = encryipt("reute9ptute9ru9 uyg")
