# coding: utf-8

# パッケージインポート
import csv
import re
import glob

# ファイルオープン
machinefile = open("MAC_machine_list.csv", "r")
# CSVを読み込む
machinecsv = csv.reader(machinefile)
# マシン名をリストに入れる
machinelist = [i[2] for i in machinecsv]
# マシンのジョブをリストに入れる
machinejob = [i[1] for i in machinecsv]
# ファイルクローズ
machinefile.close()


# ファイルリストを作成
filelist = glob.glob("*")
# マッチさせる文字列を作成
match = machinelist[0] #+ machinejob[0] + "*"
print(match)

for f in filelist:
	if re.match(match, f):
		print(f + "\n")


