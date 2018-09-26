import random

def simExperiment():
	N = 1000
	mas = [0 for i in range(N)]
	posCar = int(random.random()*N)
	mas[posCar] = 1

	choice = int(random.random()*N)
	exception = 0
	if choice == posCar:
		exception = int(random.random()*N)
		while exception == choice:
			exception = int(random.random()*N)
	else:
		exception = int(posCar)

	if (mas[exception] == 1):
		return 1
	else:
		return 0

wins = 0
numberTests = 100000
for i in range(numberTests):
	wins += simExperiment()

print(wins / numberTests)