import random
def write(string):
    File = open("attempts.txt", 'a')
    File.write(string+'\n')

array_length = 10#raw_input("Input the power of two (2**N) for the number range ")
array_length = 2**int(array_length) 
array = []
for i in range(1,(array_length)+1):
    array.append(i)
print array
answer = random.randint(1, len(array))

def binary(a, answer,attempts):
    if not a:
        return False
    else:
        guess = int(len(a))/2
        attempts += 1
        print "Computer guess was " + str(a[guess])
        if a[guess] > answer:
		print "Guess was higher than answer"
		return binary(a[0:guess], answer,attempts)
	elif a[guess] < answer:
		print "Guess was smaller than answer"
		return binary(a[guess+1:], answer, attempts)
	else:
		print "The answer was " + str(answer) + " and the attempts made " + str(attempts)
		write(str(attempts))       

for i in range(0,100):
	answer = random.randint(1, len(array))
	binary(array, answer, 0)
