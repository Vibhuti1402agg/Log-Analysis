import re
import operator

error = {}
user = {}
with open('syslog.log','r') as f:
	for line in f.readlines():
		usr = re.findall(r"\(([\w.]*)\)",line)[0]
		if "INFO" in line:
			if usr not in user:
				user[usr] = {"e":0,"i":0}
			user[usr]["i"] += 1
		if "ERROR" in line:
			err = re.findall(r"ERROR ([\w ']*)",line)[0]
			if usr not in user:
				user[usr] = {"e":0,"i":0}
			user[usr]["e"] += 1
			if err not in error:
				error[err] = 0
			error[err] += 1

user = sorted(user.items())
error = sorted(error.items(), key = operator.itemgetter(1),reverse = True)

with open('error_message.csv','w') as f2:
	f2.write("Error,Count" + "\n")
	for errors in error:
		f2.write(errors[0] + "," + str(errors[1]) + "\n")

with open('user_stats.csv','w') as f3:
	f3.write("Username,INFO,ERROR \n")
	for users in user:
		f3.write(users[0] + "," + str(users[1]["i"]) + "," + str(users[1]["e"]) + "\n")


