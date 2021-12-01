from time import perf_counter

DAY = 1
start_time = perf_counter()

data = []
inc = 0
incB = 0

try:
	file = open("../notes/y2021d" + str(DAY) + ".txt", "r")
except IOError:
	print ('Error: Can not find file!')
	exit()

data = [int(x) for x in file.read().split('\n') if x!='']
file.close()

for i in range(0, len(data)-1):
	if data[i+1] > data[i]:
		inc += 1
	if i<len(data)-3 and data[i] < data[i+3]:
		incB += 1

print('A: ', inc, '\nB: ', incB)

end_time = perf_counter()
print("--- Runtime: {} secs ---".format(end_time - start_time))