import math
from os import listdir
def dic(tex1):
	d={}
	for i in tex1:
		c=0
		for j in tex1:
			if i==j:
				c=c+1
		d[i]=c
	return d



class BoW():
	l=[]	
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
	d=[]
	def __init__(self,S,T):
		
		self.S=S
		self.T=T
		m=len(self.S)
		n=len(self.T)

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
		print (lcs_set)
		s=lcs_set
		a=len(s[0])
		match=(a*2)/(b+e)
		lcs.d.append(round(match*100,2))
		



def char(z):
	a = z
	b = "%&*()+,?/:;@#$~!"
	for char in b:
		a = a.replace(char,"")
	return a

path=input()
files=[p for p in listdir(path) if p.endswith('.txt')]
print (files)
# b=[]
# d=[]
for i in range(len(files)-1):
	list1=open(files[i])
	tex1=str(list1.read())
	tex1=char(tex1)
	b=len(tex1)
	tex3=list(tex1.split())
	print (tex1)
	for j in range(i,len(files)):

		list2= open(files[j])
		tex2= str(list2.read())
		tex2=char(tex2)
		e=len(tex2)
		tex4= list(tex2.split())
		print(tex2)

		BoW(tex3,tex4)
		lcs(tex1,tex2)
	print (BoW.l)
	print (lcs.d)	