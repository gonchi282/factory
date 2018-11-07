import os, glob, re

list = glob.glob('*')

match = "rslt-b827ebf98d0c*"

#TSL-800(2)
for i in list:
	if(re.match(match, i)):
		name = i.split("-")
		del name[:2]
		name.insert(0, "TSL-800(2)")
		path_name = "-".join(name)
		os.rename(i, path_name)
