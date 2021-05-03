s = input()
numbers = list(map(int, s.split()))
mul=1
for i in range(0,len(numbers)):
	mul*=numbers[i]
print(mul)
	

