
####Formatting

x = 10

print(f'The answer is {x} for today')


#### Counter object


from collections import Counter
d = {}
#d['dragons']
d = Counter()
d['dragons'] += 1
#print(d)
c= Counter('red green red blue red blue green'.split()) #splits into list by different words
#print(c)
print(c.most_common(2)) #most 2 common values


print(list(c.elements())) #creates a list of all elements
print(list(c)) # creates a list of distinct elements
print(list(c.values())) #creates a lost of how many different elements there are
print(list(c.items())) #combines colour and how many times appear


#### Statistics


from statistics import mean, median, mode, stdev, pstdev

print(mean([50,52,53]))
print(median([50,52,53]))
print(mode([50,52,53]))
print(stdev([50,52,53]))
print(pstdev([50,52,53]))


s = [10,20,30]
t = [40,50,60]
u = s + t
print(u)

print(u[:2]) #first two elements
print(u[-2:]) #last two elements

print(u[:2] + u[-2:])

#print(dir(list))
s = 'abracadabra'
i = s.index('c') #when i appears in the word
print(i)
print(s[i]) #what is i in the word abracadabra
print(s.count('c')) #how many c letters in the word


#Chaned comparisons

s = [10,5,70,2]
s.sort()

s = [10,5,70,2]
t = sorted(s)
print(s)
print(t)

print(sorted('cat')) #sorts alphabetically or from smallest


#lambda


lambda x: x**2 #function

print((lambda x: x**2)(5))

print(100+ (lambda x: x**2)(5) + 50)

f = lambda x,y: 3*x + y

print(f(3,8))

x= 10
y = 20
f = lambda : x ** y #if you dont define arguments it passess by default

print(f())


#Chaned comparisons


x = 15
print(x>6)

x > 6 and x < 20

6 < x < 20
