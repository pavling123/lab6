import random
import time
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
def printmatrix(matrix):
    print("\n")
    for i in matrix:  # делаем перебор всех строк матрицы
        for j in i:  # перебираем все элементы в строке
            print("%5d" % j, end=' ')
        print()
countneg=0
countpos=0
summ=0
K = int(input("Введите число K "))  #пользовательский ввод
while True:
    N=int(input("Введите число N в интервале от 3 до 1000 включительно "))
    if N>=3 and N <= 1000:
        break
A=[[0]*N for i in range(N)] # создание матрицы A
for i in range(N):
    for j in range(N):
        A[i][j] = random.randint(-10,10)
F = A.copy() # Создание матрицы F равной A
B = [[0]*int(N//2) for i in range(N//2)] # создание матрицы B
for i in range(int(len(A)//2)):
    for j in range(int((len(A))//2)):
        B[i][j]=A[i][j]
C = [[0]*int(N//2) for i in range(N//2)] # создание матрицы C
for i in range(int(len(A)//2)):
    for j in range(int((len(A)+1)//2),len(A)):
        C[i][j-int((N+1)/2)]=A[i][j]
E = [[0] * int(N // 2) for i in range(N // 2)]  # создание матрицы E
for i in range((int(len(A)+1) // 2),len(A)):
    for j in range(int((len(A) + 1) // 2), len(A)):
        E[i - int((N+1)/2)][j - int((N + 1) / 2)] = A[i][j]
det= np.linalg.det(np.array(A))  # определитель матрицы A
for i in range(N//2): # Счетчик положительных элементов в четных столбцах матрицы C
    for j in range(N//2):
        if j%2==0 and C[i][j]>0:
            countpos+=1
for i in range(N//2): # Счетчик отрицательных элементов в нечетных столбцах матрицы C
    for j in range(N//2):
        if j%2==1 and C[i][j] < 0:
            countneg+=1
if countpos > countneg: # При выполнении этого условия мы меняем С и B  местами симметрично
    for i in range(N//2):
        for j in range(N//2):
            temp=B[i][N//2-j-1]
            B[i][N//2-j-1]=C[i][j]
            C[i][j]=temp
    for i in range(N//2):
        for j in range(N//2):
            F[i][j]=B[i][j]
            F[i][(N+1)//2+j]=C[i][j]
else:                               # Иначе меняем C и E местами несимметрично
    for i in range(N//2):
        for j in range((N+1)//2,N):
            F[i][j]=E[i][j-N//2-N%2]
    for i in range((N+1)//2,N):
        for j in range((N+1)//2,N):
            F[i][j]=C[i-N//2-N%2][j-N//2-N%2]
for i in range(N):
    for j in range(N):
        if i == j:
            summ+=F[i][j]
        if i == N-j-1:
            summ+=F[i][j]
if N%2==1:
    summ-=F[N//2][N//2]
if det > summ:
    print(np.dot(np.array(A),(np.transpose(A)))-K*np.dot(F,np.linalg.inv(A)))
else:
    print((K*np.linalg.inv(A)+np.tril(A)-np.transpose(F))*K)

fig, ax = plt.subplots()                            #matplotlib
ax.set(xlabel='column number', ylabel='value')
for i in range(N):
    for j in range(N):
        plt.bar(i, A[i][j])
plt.show()

fig, ax = plt.subplots()
ax.set(xlabel='column number', ylabel='value')
ax.grid()
for j in range(N):
    ax.plot([i for i in range(N)], A[j][::])
plt.show()

ax = plt.figure().add_subplot(projection='3d')
ax.set(xlabel='x', ylabel='y', zlabel='z')
for i in range(N):
    plt.plot([j for j in range(N)], A[i][::], i)
plt.show()


sns.heatmap(data = F, annot = True)                 #seaborn
plt.xlabel('column number')
plt.ylabel('row number')
plt.show()

sns.boxplot(data = F)
plt.xlabel('column number')
plt.ylabel('value')
plt.show()

sns.set_style("whitegrid")
sns.lineplot(data = F)
plt.xlabel('column number')
plt.ylabel('value')
plt.show()
