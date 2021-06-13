from faker import Faker ### python -m pip install Faker ###
import random
### These libraries are needed for this to work ###


ex = Faker()  # allows use of faker library for random ip addresses
randomlist = []  # empty list that will be filled
portlist = [['20', 'FTP'], ['22', 'SSH'], ['23', 'Telnet'], ['25', 'SMTP'], [
    '80', 'HTTP'], ['110', 'POP3'], ['119', 'NNTP'], ['123', 'NTP']]

### TASK 1 ########

# creating the 1000 entries for the list
for i in range(0, 1000):
    randomlist.append([])
# fills each entry with a list of source ip, port number, destination ip, destination port
    for n in range(0, 1):
        h = random.randint(0, 7)
        n = ex.ipv4()  # source IP
        p = portlist[h][0]  # source port
        a = ex.ipv4()  # destination IP
        d = str(random.randint(1024, 49151))  # destination IP
        e = portlist[h][1]
        # using extend instead of append function in order to add the entire list at once
        randomlist[i].extend((n, p, a, d, e))
for i in range(0,1000):
	print(randomlist[i])


### TASK 2 ######

for i in range(len(portlist)):
	portname = portlist[i][1]
	portcounter = 0
	for i in randomlist:
		if i[4] == portname:
	   		portcounter += 1
	print(portname + " was found " + str(portcounter) + " times")

### TASK 3 #####

# Splits first ip address 
badip = randomlist[0][0]
bp = badip.split('.')
del bp[-1]
nbp = '.'.join(bp)


# Looks for the matching string in the whole list
for i in range(len(randomlist)):
	badipcounter = 0
	for i in randomlist: 
		tmpip = i[0]
		tmpipa = tmpip.split('.') #spliting the ip address of every string in the list
		del tmpipa[-1]
		newtmpip = '.'.join(tmpipa) 
		if newtmpip == nbp:
			badipcounter += 1
print("bad ip found " + str(badipcounter) + " times")
