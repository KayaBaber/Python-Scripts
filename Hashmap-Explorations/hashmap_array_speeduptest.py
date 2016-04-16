import math
from datetime import datetime
#Compare the speeds of a dictonary (hashmap) and a 2D list (nested array)
#Don't care about the order, only doing global statistics

sqrValues = 1000*4

#Assign values to a 2D array
nestArray=[]
startTime = datetime.now()
for i in range(sqrValues):
    nestArray.append([])
    for j in range(sqrValues):
        nestArray[i].append(math.sin(i)+math.cos(j))
arrayAssignTime = datetime.now() - startTime
print arrayAssignTime

#Assign values to hashmap
hashmap={}
startTime = datetime.now()
for i in range(sqrValues):
    for j in range(sqrValues):
        hashmap[(i,j)] = math.sin(i)+math.cos(j)
hashAssignTime = datetime.now() - startTime
print hashAssignTime

print arrayAssignTime - hashAssignTime
print '\n'


#sum up all values
runTotal = 0.0
startTime = datetime.now()
for i in range(sqrValues):
    for j in range(sqrValues):
        runTotal += nestArray[i][j]
arraySumTime = datetime.now() - startTime
print arraySumTime

runTotal = 0.0
startTime = datetime.now()
for i in range(sqrValues):
    for j in range(sqrValues):
        runTotal += hashmap[(i,j)]
hashSumTime = datetime.now() - startTime
print hashSumTime

print arraySumTime - hashSumTime
