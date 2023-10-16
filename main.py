import datetime


print ("выберете действие(если + то 1, если - то 2):")
plus_or_minus: int = input()

while plus_or_minus!= "1" and plus_or_minus!= "2":
    print("введите 1 или 2")
    plus_or_minus: int = input()

pluspp: int = input()

#ReadingFile
f = open('data/pp.txt')
currentpp: int = 0

for line in f:
    line = int(line)
    currentpp = int(currentpp)
    pluspp = int(pluspp)

    if plus_or_minus == "1":
        currentpp = line + pluspp
    elif plus_or_minus == "2":
        currentpp = line - pluspp

print(currentpp)
f.close()
#writeToFile
f = open('data/pp.txt', 'w')

f.write(str(currentpp))

f.close()

x = datetime.datetime.now()
print(x.strftime("%x"))

#LOGGING
f = open('data/log.txt', 'a')

if plus_or_minus == "1":
    f.writelines(str(x.strftime("%x")) + ' ')
    f.writelines(str(pluspp) + '\n')
elif plus_or_minus == "2":
    f.writelines(str(x.strftime("%x")) + ' ' "-")
    f.writelines(str(pluspp) + '\n')
f.close()