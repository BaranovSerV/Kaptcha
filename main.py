import numpy as np
from PIL import Image, ImageOps
import os
from tabulate import tabulate
import matplotlib.pyplot as plt
#конвертировали картинку в массив битов

cwd1=os.getcwd()
png_dir=os.path.join(cwd1,"Symbols")
png_files=os.listdir(png_dir)
png_list=[]
n=len(png_files)
for i in range(n):

    file_path = os.path.join(png_dir, png_files[i])
    img = Image.open(file_path).convert('L')
    img_inverted = ImageOps.invert(img)

    p = np.array(img_inverted)
    p[p > 0] = 1
    png_list.append(p)
print(n)

def Sc_Mult(a,b):
    N=len(a[0])
    S=0
    for i in range (N):
        for j in range(N):
            S+=a[i,j]*b[i,j]
    return S

V=np.zeros((n,n))
for i in range(n):
    for j in range(n):
        V[i,j]=Sc_Mult(png_list[i],png_list[j])
print(V)
print("Invert:", np.linalg.inv(V))
#считаем коэф А

# I=np.zeros((n,n))#функия кронекера
# for i in range(n):
#     for j in range(n):

#         if i==j: I[i,j]=1
#         else: I[i,j]=0
# ##метод холецкого

# L=np.zeros((n,n))
# L[0,0]=np.sqrt(V[0,0])
# L[1,0]=V[1,0]/L[0,0]
# L[1,1]=np.sqrt(V[1,1]-(L[1,0])**2)
# for i in range(2,n-1):
#     L[i,0]=V[i,0]/L[0,0]
#     L[i+1,1]=(V[i+1,1]-L[i+1,0]*L[1,0])/L[1,1]
# for i in range(2,n-1):

#     t=0
#     r=0
#     for k in range(0,i):
#         t+=(L[i,j])**2
#         L[i,i]=np.sqrt(V[i,i]-t)
#         r+=L[i+1,j]*L[i,j]
#         L[i+1,i]=(V[i+1,i]-r)/L[i,i]
# c=0
# for i in range(n-1):
#     c+=L[n-1,i]
#     L[n-1,n-1]=np.sqrt(V[n-1,n-1]-c)

#
# LT=np.transpose(L)
# Y=scipy.linalg.solve(L,I)
# A=scipy.linalg.solve(LT,Y)#нашли А


#считаем коэф А
A=np.linalg.inv(V)

#ищем сопряжённые вектора
sopr_list=[]
for i in range(n):
    v_sopr=np.zeros(np.shape(png_list[0]))
    for j in range(n):
        v_sopr += A[i,j]*png_list[j]
    sopr_list.append(v_sopr)



#НАЙДЁМ В И С

cwd2=os.getcwd()
q_dir=os.path.join(cwd1,"Distorted img")
q_files=os.listdir(q_dir)
q_list=[]
m=len(q_files)
for i in range(m):
    file_path = os.path.join(q_dir, q_files[i])
    Img = Image.open(file_path).convert('L')
    Img_inverted = ImageOps.invert(Img)
    q = np.array(Img_inverted)
    q[q > 0] = 1
    q_list.append(q)


def DI(Q,V_sopr, V):#функия, которая считает одно слагаемое для вектора В
    B=np.zeros(np.shape(Q))
    C=np.zeros(np.shape(Q))

    for i in range(len(V_sopr)):
        B+=Sc_Mult(V_sopr[i],Q)*(V[i]+Q*(-1.0))

        for j in range(len(V_sopr)):
           if j!=i:
               C+=Sc_Mult(V_sopr[i],Q)**2 * Sc_Mult(V_sopr[j],Q) * V[j]
    Q=Q+B-C
    return Q

#РЕАЛИЗУЕМ МЕТОД
print("Enter the number of iterations: ")
a=int(input())

print("Enter a number of Distorted image according to the list: ")
k=int(input())
qq=DI(q_list[k],sopr_list, png_list)
iter=1

A=a-1
while (iter!=(A)):
    for i in range(n):
        if Sc_Mult(qq,sopr_list[i])!=Sc_Mult(png_list[i],sopr_list[i]):
            c=0
        else:
            c=1
            break
    if c<1:
        qq = DI(qq, sopr_list, png_list)
        iter+=1
    else: break

print(iter+1)

print(tabulate(np.matrix.round(qq), numalign="right"))


t=len(qq)
plt.xlim(t,0)
plt.ylim(t,0)
plt.grid()

for i in range(t):

    for j in range(t):
        if qq[i,j]>=0.9:
            plt.plot(j,i, color="green", marker="o", markersize=7)
plt.show()
