import json,subprocess,datetime,sys,os, platform, time
from shutil import copyfile

def launchTest(sleep, nbCPUID, nbLaunch, virtual):
	# COPIER FICHEIR ASM avant modification
	copyfile("../_Detector.asm","../dump.asm")
	f = open("../_Detector.asm", "r")
	contents = f.readlines()
	f.close

	# Insertion des lignes CPUID dans fichier ASM
	f = open("../_Detector.asm", "w")
	contents.insert(19, "		CPUID\n" * nbCPUID)
	contents = "".join(contents)
	f.write(contents)
	f.close()

	# Lancement du binaire et recuperation du code retour
	result=[]
	for i in range(0,nbLaunch):
		result.append(os.system('../Detector'))
		time.sleep(sleep)
	ratio = 0
	for r in result:
		# Calculer le pourcentage de detection
		ratio += r
	ratio = (ratio/nbLaunch) * 100

	# Remise en etat initial du fichier asm
	copyfile("../dump.asm","../_Detector.asm")
	return formatCSVOutput(sleep, nbCPUID, nbLaunch, virtual, ratio)



def formatCSVOutput(sleep, nbCPUID, nbLaunch, virtual, ratio):
	if virtual:
		hostType = "virtual"
	else :
		hostType = "physical"
	OS = os.name
	platformType= platform.system() + platform.release()
	processor = platform.processor()
	output = processor + "," + OS + "," + platformType + "," + hostType + "," + str(nbCPUID) + "," + str(nbLaunch) + "," + str(sleep) + "," + str(ratio)
	return output