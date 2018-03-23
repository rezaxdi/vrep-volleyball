import vrep
import time

vrep.simxFinish(-1)
# This port number (19997) is not allowed to be used by teams 
clientID=vrep.simxStart('127.0.0.1',19997,True,True,5000,5)
vrep.simxStartSimulation(clientID, vrep.simx_opmode_oneshot)
vrep.simxClearStringSignal(clientID, 'startRoundSignal', vrep.simx_opmode_oneshot)

time.sleep(1)
while True :
	inp = raw_input("Press Space + Enter to start the round q + Enter to quit ...")
	if inp is ' ' :
		vrep.simxSetStringSignal(clientID, 'startRoundSignal', 'start', vrep.simx_opmode_oneshot)
		print 'round signal set'
		time.sleep(0.1)
		vrep.simxClearStringSignal(clientID, 'startRoundSignal', vrep.simx_opmode_oneshot)
		time.sleep(0.1)
	if inp is 'q' :
		print 'finish'
		break


