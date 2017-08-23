def bow(tex1,tex2):
	d={}
	for i in tex1:
		c=0
		for j in tex1:
			if i==j:
				c=c+1
		d[i]=c
	print (d)
	e={}
	for i in tex2:
		c=0
		for j in tex2:
			if i==j:
				c=c+1
		e[i]=c 
	print (e)

	dps=0
	for k,v in d.items() :
		for  k1,v1 in e.items():
			if k==k1:
				dps = dps+(v*v1)

	v1=list(d.values())
	v2=list(e.values())
	print(v1,v2)
	sum=0
	for i in range(len(v1)):
		sum=sum+(v1[i]**2)
	f1=sum
	sum1=0
	for j in range(len(v2)):
		sum1=sum1+(v2[j]**2)
	f2=sum1
	print(sum,sum1)

	fun=dps/((f1**1/2)*(f2**1/2))
	print ('BoW match:',fun*100)

def lcs(S,T):
	m = len(S)
	n = len(T)
	counter = [[0]*(n+1) for x in range(m+1)]
	longest = 0
	lcs_set = []
	for i in range(m):
		for j in range(n):
			if S[i] == T[j]:
				c = counter[i][j] + 1
				counter[i+1][j+1] = c
				if c > longest:
					lcs_set = []
					longest = c
					lcs_set.append(S[(i-c+1):(i+1)])
				elif c == longest:
					lcs_set.append(S[(i-c+1):(i+1)])
					# print (lcs_set)
	return lcs_set
def char(z):
	a = z
	b = "%&*()+,?/:;@#$~!"
	for char in b:
		a = a.replace(char,"")
	return a


#main
list1=open(input())
tex1=str(list1.read())
tex1=char(tex1)
b=len(tex1)
tex3=list(tex1.split())
# print (tex1)
list2=open(input())
tex2= str(list2.read())
tex2=char(tex2)
e=len(tex2)
tex4= list(tex2.split())
# print(tex2)
bow(tex3,tex4)
s=lcs(tex1,tex2)
# print (s)
a=len(s[0].lstrip())
match=(a*2)/(b+e)
print ('string match :', match*100)

