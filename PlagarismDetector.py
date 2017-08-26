import math
from os import listdir

def dic(tex1):
	#forming a dictionary
	d={}
	for i in tex1:
		c=0
		for j in tex1:
			if i==j:
				c=c+1
		d[i]=c
	return d

class BoW():
	# this method is used to compare 2 texts and get percent of matching words.
	# we take sentences as list of words 		
	def __init__(self,l1,l2):
		self.l1=l1
		self.l2=l2
		d=dic(self.l1)
		e=dic(self.l2)
		dps=0
		for k,v in d.items() :
			for  k1,v1 in e.items():
				if k==k1:
					dps = dps+(v*v1)
		v1=list(d.values())
		v2=list(e.values())
		# print(v1,v2)
		sum=0
		for i in range(len(v1)):
			sum=sum+(v1[i]**2)
		f1=sum
		sum1=0
		for j in range(len(v2)):
			sum1=sum1+(v2[j]**2)
		f2=sum1
		# print(sum,sum1)
		fun=dps/((f1**(1/2))*(f2**(1/2)))
		BoW.l.append(round(fun*100,2))

class lcs():
	#in this method we can find longest common string in both text. 
	#we compare 2 strings by each characher and calculate percent of mactching
	def __init__(self,S,T):
		
		self.S=S
		self.T=T
		m=len(self.S)
		n=len(self.T)
		try:
			assert (len (m)>0,len(n)>0)
		
		mat = [[0]*(n+1) for x in range(m+1)]
		longest = 0
		lcs_set = []
		for i in range(m):
			for j in range(n):
				if S[i] == T[j]:
					c = mat[i][j] + 1
					mat[i+1][j+1] = c
					if c > longest:
						lcs_set = []
						longest = c
						lcs_set.append(S[(i-c+1):(i+1)])
					elif c == longest:
						lcs_set.append(S[(i-c+1):(i+1)])
		except Exception as e:
			raise Exception ('null')
		print (lcs_set)
		s=lcs_set
		a=len(s[0])
		match=(a*2)/(m+n)
		lcs.d.append(round(match*100,2))
		
def print_mat(files,b):
	# printing the results in a 2d matrix for better understanding 
	print('               ',end='')
	for i in range (len(b)):
		print(files[i],'  ',end='')
	print('')	
	
	for i in range (len(b)):
		print(files[i],':',end='')
		for j in b[i]:
			print ('{:12.2f}'.format(j),end='')
		print('')

def length(b):
	try:
		a=len(b)
		if a>0:
			return a
		else:
			raise Exception('HELLO')
	except Exception as e:
		print(e)

def char(z):
	#this fuctions is to remove any special characters from the sentences.
	a = z
	b = "%&*()+,?/:;@#$~!"
	for char in b:
		a = a.replace(char,"")
	return a

path=input()
files=[p for p in listdir(path) if p.endswith('.txt')]# opening files into a list 
# print (files)
B=[]
E=[]
for i in range(len(files)):
	list1=open(files[i])
	tex1=str(list1.read())
	tex1=char(tex1)
	b=length(tex1)
	tex3=list(tex1.split())
	print (tex1)
	BoW.l=[]
	lcs.d=[]
	for j in range(len(files)):

		list2= open(files[j])
		tex2= str(list2.read())
		tex2=char(tex2)
		e=length(tex2)
		tex4= list(tex2.split())
		print(tex2)

		BoW(tex3,tex4)
		lcs(tex1,tex2)
	B.append(BoW.l)

	E.append(lcs.d)	
# print (B)
# print (E)
print ('Bag of words')
print_mat(files,B)
print ('  ----------------------------- -------------------------------------  ')
print('String Matching')
print_mat(files,E)