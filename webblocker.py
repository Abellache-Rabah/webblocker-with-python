from datetime import datetime as dt
import time
hostfile = "/etc/hosts"
redirect ="127.0.0.1"
websites = [
	"www.fuq.com",
	"fuq.com",
	
	]
now = dt.now()
morning = now.replace(hour=8, minute=0, second=0, microsecond=0)
evning = now.replace(hour=18, minute=0, second=0, microsecond=0)
while True:
	if morning < now < evning:
		with open(hostfile, 'r+')as file:
			content = file.read()
			for site in websites :
				if site in content:
					pass
				else:
					print("writing " + site)
					file.write("\n" +redirect +" " +site )
	else:
		with open(hostfile,'r+') as file:
			content=file.readlines()
			file.seek(0)
			for line in content:
				if not any(site in line for site in websites):
					file.write(line)
			file.truncate()
	time.sleep(10)
