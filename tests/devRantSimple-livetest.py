import sys
sys.path.append('../devRantSimple')
import devRantSimple as dRS

# print(dRS.getUserRant("ewpratten", 1))

prevdata = ""
i = 0
while prevdata != dRS.InvalidResponse:
	prevdata = dRS.getUserRant("ewpratten", i)["text"]
	print(prevdata)
	i+=1