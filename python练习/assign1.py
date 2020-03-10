print('Hello from a file')


hrs = input("Enter Hours:")
rte = input("Enter Rate:")
h = float(hrs)
r = float(rte)
if h >= 40 :
    pay=40*r+(h-40)*r*1.5
    print (pay)


score = input("Enter Score: ")
s = float(score)
if s<0.0 or s>1.0:
    print("Error")
elif 0.0<s<0.6:
    print("F")
elif 0.6<=s<0.7:
    print("D")
elif 0.7<=s<0.8:
    print("C")
elif 0.8<=s<0.9:
    print("B")
elif 0.9<=s<1.0:
    print("A")


hrs = input("Enter Hours:")
rte = input("Enter Rate:")
h = float(hrs)
r = float(rte)
def computepay():
    p=40*r+(h-40)*1.5*r
    return p
def computepay2():
    pa=h*r
    return pa
if h >= 40:
    print(computepay())
else:
    print(computepay2())


numlist =list()
while True:
    num = input("Enter a number: ")
    if num == "done" :
        break
    try:
        num = int(num)
        numlist.append(num)
    except:
        print("Invalid input")
largest = None
#比较最大
for larva in numlist:
    if largest is None:
        largest = larva
    elif larva > largest:
        largest = larva
print ("Maximum is",largest)
smallest = None
#比较最小
for smallva in numlist:
    if smallest is None:
        smallest = smallva
    elif smallva < smallest:
        smallest = smallva
print("Minimum is", smallest)
