import json,subprocess,datetime,sys,os, platform, time

def launchTest(sleep, nbCPUID, nbLaunch, virtual):
	#TODO Add of CPUID Line in file
	result=[]
	for i in range(0,nbLaunch):
		#result.append(1)
		result= result.append(os.system('./Detector'))
		print(result)
		time.sleep(sleep)
	return formatCSVOutput(sleep, nbCPUID, nbLaunch, virtual, result)



def formatCSVOutput(sleep, nbCPUID, nbLaunch, virtual, result):
	if virtual:
		hostType = "virtual"
	else :
		hostType = "physical"
	OS= os.name
	platformType= platform.system() + platform.release()
	output=[]
	output.append("OS, platformType, hostType , nbCPUID, nbLaunch, TimeSleep(ms), Detection rate (%)")
	for r in result:
		output.append(OS + "," + platformType + "," + hostType + "," + str(nbCPUID) + "," + str(nbLaunch) + "," + str(sleep) + "," + str(r))
	return output