from random import*
import numpy as np
def saisir():
    global N
    test=False
    while test==False:
        N=int(input("N="))
        test=3<=N<=20
def remplir(T,N):
    for i in range (0,N):
        T[i]=randint(0,1)
def distinct (L,i):
    for i in range(0,N):
        if (L[i+1]!=L[i]):
            return True
        else:
            return False

def remplirL(L,N):
    for i in range (0,N):
        test=False
        while test==False :
            L[i]=input("[L",i,"]="
            test=distinct() and L[i]=[a,z]
def gen(T,L,N):
    global code
    test=False
    code=""
    for i in range (0,N):
        if T[i]==1 :
            code=str(T[i])+L[i]
        else:
            code=str(T[i])+ord(L[i])
def netoyer(ch,code):
    ch=code
    ch1=""
    for i in range (0,len(ch)):
      while ch[i]!="0":
          ch1=ch[i]
          i+=1















#p.p
saisir()
T=np.array([int]*N)
remplir(T,N)
L=np.array([str]*N)
remplirL(L,N)
gen(T,L,N)
netoyer(ch,code)
print("code=",code)
print("code valide =",ch1)
