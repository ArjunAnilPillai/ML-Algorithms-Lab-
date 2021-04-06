import matplotlib.pyplot as plt

entries = 7

dic = [[62,55,80,72,91,87,53], [82,60,72,79,93,78,50]]
'''
#If required for input purposes
flag = True
while flag:
    print("Enter list")
    line = input()
    line = line.split(',')
    curList = []
    for i in line:
        curList.append(int(i))
    dic.append(curList)
    print("Continue? (1/0)")
    choice = int(input())
    if choice == 0:
        flag = False'''


y = dic[-1]
x = dic[0:-1]

xmean = []
ymean = sum(y)/len(y)
for i in x:
    xmean.append(sum(i)/len(i))


xixbar = []
xixsq = []
yiybar = []
xixyiy = []
for i in y:
    yiybar.append(i - ymean)

for i in range(0, len(x)):
    curList = []
    curListsq = []
    curListxiy = []
    counter = 0
    for j in x[i]:
        curList.append(j - xmean[i])
        curListsq.append((j - xmean[i]) ** 2)
        curListxiy.append((j - xmean[i]) * yiybar[counter])
        counter += 1
    xixbar.append(curList)
    xixsq.append(curListsq)
    xixyiy.append(curListxiy)

coeff = []
for i in range(len(x)):
    cur = sum(xixyiy[i])/sum(xixsq[i])
    coeff.append(cur)

ans = ymean
for i in range(len(x)):
    ans -= coeff[i]*xmean[i]

coeffPrint = [round(i, 4) for i in coeff]

ansPrint = round(ans, 4)
print('Equation is y = ({})x + ({})'.format(coeffPrint[0],  ansPrint))

pred_y = []

for i in range(entries):
    pred_y.append(coeff[0]*x[0][i] + ans)

print('\nActual values')
for i in y:
    print(i, end = ', ')

print("\n\nPredicted values")
for i in pred_y:
    print(round(i, 4), end = ', ')
print('\n')

#Required summations for calculating different errors
sumnormal, sumsq, sumrelnormal, sumrelsq = 0, 0, 0, 0
for i in range(entries):
    sumnormal += abs(pred_y[i] - y[i])
    sumsq += (pred_y[i] - y[i]) ** 2
    sumrelnormal += abs(y[i] - ymean)
    sumrelsq += (y[i] - ymean) ** 2
    '''l = [abs(pred_y[i] - y[i]), (pred_y[i] - y[i]) ** 2, abs(y[i] - ymean), (y[i] - ymean) ** 2]
    for i in l:
        print(round(i, 4), end = '\t')
    print()'''

'''for i in (sumnormal, sumsq, sumrelnormal, sumrelsq):
    print(round(i, 4))'''

#Different types of error
mae = round((sumnormal/entries), 4)
mse = round((sumsq/entries), 4)
rae = round((sumnormal/sumrelnormal), 4)
rse = round((sumsq/sumrelsq), 4)
rmse = round(((sumsq/entries)**0.5), 4)
rrse = round(((sumsq/sumrelsq)**0.5), 4)

print('Mean Absoulte Error =', mae)
print('Mean Squared Error =', mse)
print('Relative Absoulte Error =', rae)
print('Relative Squared Error =', rse)
print("Root Mean Squared Error = ", rmse)
print("Root Relative Squared Error = ", rrse)

# Plotting graph
fig = plt.figure()
ax = plt.axes()
pltPoints = [(x[0][i], y[i]) for i in range(entries)]
pltPoints.sort()
pltX = [i[0] for i in pltPoints]
pltY = [i[1] for i in pltPoints]
lineX = [pltX[0], pltX[-1]]
A, B = coeff[0] * pltX[0] + ans, coeff[0] * pltX[-1] + ans
lineY = [A, B]
plt.scatter(pltX, pltY, label = 'Actual')
plt.plot(lineX, lineY, color = 'red', label = 'Predicted')
plt.xlabel('X (Predictor variable)')
plt.ylabel('Y (Predicted variable)')
plt.title('Actual values vs Predicted values')
plt.legend()
plt.savefig('181CO109 graph.pdf')
plt.show()
