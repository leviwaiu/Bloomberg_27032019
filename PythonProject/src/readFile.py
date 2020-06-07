import matplotlib.pyplot as plt
import datetime
import re
import os
import statistics

path = "../data/"
ls = os.listdir(path)

months = "January|February|March|April|May|June|July|August|September|October|November|December"
dateList = []

previously_announced = []
none = []

def openFile(fileName):
    file = open(fileName, "r")

    dates = []
    list = 1
    for line in file:
            regEx = "[\d]+\s+[A-z]+\s+[\d]+"
            regExList = re.findall(regEx, line)
            if "INTENTION TO RETURN CAPITAL" in line.upper():
                list = 2
            for a in regExList:
                dates.append(datetime.datetime.strptime(a, "%d %B %Y"))

    dates.sort()
    if list == 1:
        dateList.append(dates[0])
    else:
        previously_announced.append(dates[0])


for file in ls:
    print(file)
    openFile("../data/" + file)

dateList.sort()
previously_announced.sort()

datesBetweenList = []
prevAnnouncedList = []

for x in range(len(dateList) - 2):
    datesBetween = dateList[x+1] - dateList[x]
    #Convert to seconds
    datesBetween = datesBetween.total_seconds() / 86400
    datesBetweenList.append(datesBetween)

for x in range(len(previously_announced) - 2):
    datesBetween = previously_announced[x+1] - previously_announced[x]
    #Convert to seconds
    datesBetween = datesBetween.total_seconds() / 86400
    prevAnnouncedList.append(datesBetween)

plt.figure(1)
plt.title("Dates between Press Releases")
plt.plot(datesBetweenList,"bo")
plt.show()

plt.figure(2)
plt.title("Dates between Company Documents")
plt.plot(prevAnnouncedList,"ro")
plt.show()

eliminateAnomaly = []
for date in datesBetweenList:
    if date < 50 :
        eliminateAnomaly.append(date)


eliminatePrevAno = []
for date in prevAnnouncedList:
    if date < 50:
        eliminatePrevAno.append(date)

plt.figure(3)
plt.title("Dates between Press Releases without Anomaly")
plt.plot(eliminateAnomaly,"go")
plt.show()

plt.figure(4)
plt.title("Dates between Company Documents without Anomaly")
plt.plot(eliminatePrevAno,"ro")
plt.show()



print(statistics.mean(eliminateAnomaly))
print(statistics.median(eliminateAnomaly))
print(statistics.mode(eliminateAnomaly))
print(statistics.stdev(eliminateAnomaly))


print(statistics.mean(eliminatePrevAno))
print(statistics.median(eliminatePrevAno))
print(statistics.mode(eliminatePrevAno))
print(statistics.stdev(eliminatePrevAno))

