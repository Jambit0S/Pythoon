# 2 Вариант
# Задание 3 5 и 6
# Cдвиг элементов массива на указанное число элементов

import math
import numpy as np

def ThreeQue(query,move):
    maxInd=len(query)-1
    for i in range(move):
        bufka=query[maxInd]
        index=maxInd-1
        while(index>=0):  
            query[index+1]=query[index]
            index=index-1
        query[0]=bufka
        
    return query   
    
def Five(first,second):
    
    for i in range(len(first)):
        first[i]=(first[i]-second[i])
        first[i]=first[i]**2
        
    summa=sum(first)
    return math.sqrt(summa)
   
def Six(matrix):
    ans=0
    for i in range(len(matrix)):
        ans=ans+matrix[i,i]
    
    return ans

movelist=np.array([1,2,3,4,5,6])
print(len(movelist))
print(ThreeQue(movelist,3))

a=np.array([1,2])
b=np.array([4,4])

print(Five(a,b))

matr=np.matrix([[1,2],[3,4]])
print(matr)
print(Six(matr))



