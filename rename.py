import os, glob, re, csv

machinefile = open("MAC_machine_list.csv", "r")

machinedata = csv.reader(machinefile, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)

for row in machinedata:
	if(re.match(row[1], "beacon1") or re.match(row[1], "beacon2")):
		match = "rslt-" + row[0] + "-" + "beacon" + "-*"
	else:
		match = "rslt-" + row[0] + "-" + row[1] + "-*"

	filelist = glob.glob("*")

	for list in filelist:
		if(re.match(match, list)):
			name = list.split("-")
			if(re.match(row[1], "beacon1") or re.match(row[1], "beacon2")):
				del name[:3]
				name.insert(0, row[1])
				name.insert(0, row[2])
			else:
				del name[:2]
				name.insert(0, row[2])

			path_name = "-".join(name)
			os.rename(list, path_name)
			print(path_name)


#list = glob.glob('*')

#match = "rslt-b827ebf98d0c*"

#TSL-800(2)
#for i in list:
#	if(re.match(match, i)):
#		name = i.split("-")
#		del name[:2]
#		name.insert(0, "TSL-800(2)")
#		path_name = "-".join(name)
#		os.rename(i, path_name)
