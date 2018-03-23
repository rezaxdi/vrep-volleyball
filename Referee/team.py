import vrep
import time

vrep.simxFinish(-1) 
# Team A port# 20001 & Team B port# 20002
clientID = vrep.simxStart('127.0.0.1',20001,True,True,5000,5)
ourRound = 0
counter = 0

while True :
	time.sleep(0.05)
	res, startSignal = vrep.simxGetStringSignal(clientID, 'teamStartSignal', vrep.simx_opmode_oneshot)
	res, endSignal = vrep.simxGetStringSignal(clientID, 'endSignal', vrep.simx_opmode_oneshot)

	# Getting object handles
	if startSignal == 'team a round started.' :
		ourRound = 1
		# Ball
		res, ball=vrep.simxGetObjectHandle(clientID,'Ball', vrep.simx_opmode_oneshot)
		# Team A
		res, target1=vrep.simxGetObjectHandle(clientID, 'Quadricopter_target#1', vrep.simx_opmode_oneshot)
		res, target2=vrep.simxGetObjectHandle(clientID, 'Quadricopter_target#2', vrep.simx_opmode_oneshot)
		# Team B
		# res, target1=vrep.simxGetObjectHandle(clientID, 'Quadricopter_target', vrep.simx_opmode_oneshot_wait)
		# res, target2=vrep.simxGetObjectHandle(clientID, 'Quadricopter_target#0', vrep.simx_opmode_oneshot_wait)

	if 'ball' in locals() and 'target1' in locals() and 'target2' in locals() :
		res, p = vrep.simxGetObjectPosition(clientID, ball, -1, vrep.simx_opmode_oneshot)
		if counter < 3 and p[2] != 0:
			p[2] = p[2]-1.5
			res = vrep.simxSetObjectPosition(clientID, target1, -1, p, vrep.simx_opmode_oneshot)
			counter += 1
	
	if endSignal == 'round ended.' and ourRound == 1 :
		break

