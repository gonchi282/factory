#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os, glob, re, csv

#マシンの名前、MAC、仕事を読み込む
machinefile =  open("MAC_machine_list.csv", "r")  
machinedata = csv.reader(machinefile, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)

for row in machinedata:
	# データの端末がbeacon
	if(re.match(row[1], "beacon1") or re.match(row[1], "beacon2")):
		# 
		match = "rslt-" + row[0] + "-" + "beacon" + "-*"
	else:
		# それ以外
		match = "rslt-" + row[0] + "-" + row[1] + "-*"

	# カレントディレクトリのファイルをリストに入れる
	filelist = glob.glob("*")

	# renameする
	for list in filelist:
		# ファイルリストとmatchが同じ場合
		if(re.match(match, list)):
			# そのファイルの名前変える
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

#ファイルクローズ
machinefile.close()

