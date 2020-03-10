text = "X-DSPAM-Confidence:    0.8475"
print(float(text[text.find("0"):]))


# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
for infor in fh:
    infor = infor.rstrip()
    infor = infor.upper()
    print (infor)


# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
f = open(fname)
count = 0
numlist = list()
for line in f:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    numlist.append(line)
    count = count +1
su = 0
for num in numlist:
    num = num[num.find("0"):]
    su = float(su) + float(num)
print("Average spam confidence:"+" "+str(su/count))


fname = input("Enter file name: ")
fh = open(fname)
wordlist = list()
for line in fh:
    line = line.strip()
    l = line.split()
    for i in l:
        wordlist.append(i)
    wordlist.sort()
wordlist = list(set(wordlist))
print(wordlist)



fname = input("Enter file name: ")
fh = open(fname)
wordlist = list()
for line in fh:
    if not line.startswith("From "):
        continue
    w = line.split()
    w = w[1]
    print(w)
    wordlist.append(w)
print("There were",len(wordlist), "lines in the file with From as the first word")


name = input("Enter file:")
fn = open(name)
maillist = list()
for line in fn:
    if not line.startswith("From "):
        continue
    line = line.split()
    mail = line[1]
    maillist.append(mail)
mailbox = dict()
for mailadd in maillist:
    mailbox[mailadd] = mailbox.get(mailadd,0)+1
maxcount = None
maxmail = None
for word,count in mailbox.items():
   if maxcount is None or count > maxcount:
        maxmail = word
        maxcount = count
print(maxmail,maxcount)


fname = input("Please enter the file: ")
fl = open(fname)
timelist = list()
yy = list()
for info in fl:
    if not info.startswith("From "):
        continue
    info = info.strip()
    x = info.find(":")
    time = info[x-2:x+6]
    z = time.split(":")
    yy.append(z)
    for y in yy:
        hour = y[0]
    timelist.append(hour)
sumn = dict()
for count in timelist:
        sumn[count] = sumn.get(count,0)+1
final = list()
for k,v in sumn.items():
    xx = (k,v)
    final.append(xx)
    final = sorted(final)
for a,b in final:
    print(a,b)
