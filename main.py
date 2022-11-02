
# ******************************
# Make your Code
# ******************************
import random

numbers1 = []
numbers2 = []
result = []
for i in range(10):
	numbers1.append(random.randint(0,100))
	numbers2.append(random.randint(0,100))
print (numbers1)
print (numbers2)

for i in range(10):
	result.append(numbers1[i] + numbers2[i])

print(result)