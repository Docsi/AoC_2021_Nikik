from time import perf_counter

start_time = perf_counter()

pos1 = [0,0] #dis, depth
pos2 = [0,0,0] #dis, depth, aim

try:
    file = open("../notes/y2021d2.txt", "r")
except IOError:
    print ('Error: Can not find file!')
    exit()
while True:
	line = file.readline().strip()
	if not line:
		break
	dir = line.split(" ")
	move = int(dir[1])
	if dir[0]=="forward":
		pos1[1] += move
		pos2[0] += move
		pos2[1] += move*pos2[2]
	elif dir[0]=="up":
		pos1[0] -= move
		pos2[2] -= move
	elif dir[0]=="down":
		pos1[0] += move
		pos2[2] += move
file.close()

print(f'A:\nPosition: {pos1[0]}, Depth: {pos1[1]}\nMultiplied: {pos1[0]*pos1[1]}')
print(f'B:\nPosition: {pos2[0]}, Depth: {pos2[1]}, Aim: {pos2[2]}\nMultiplied: {pos2[0]*pos2[1]}')

end_time = perf_counter()
print("--- Runtime: {} secs ---".format(end_time - start_time))