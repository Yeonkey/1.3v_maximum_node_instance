from random import *
import itertools
import matplotlib.pyplot as plt
import numpy as np


#초기랜덤좌표 생성
fw=open("inputfile.txt","w")

Coordinates = [[] for i in range(1000)] #원소 개수 500개

num = int(randint(0, 1000)) # 1000X1000좌표에서 랜덤 넘버 뽑기
def randomxy (z):   #2차원 배열에서 x좌표는 중복 허용한 랜덤 y도 일단 중복 허용한 랜덤
    global num
    for i in range(z):
        HelpCoordinates = [[]]
        num = int(randint(0, 1000))
        HelpCoordinates[0].append(num)
        num = int(randint(0, 1000))
        HelpCoordinates[0].append(num)
        while HelpCoordinates in Coordinates:
            HelpCoordinates = [[]]
            num = int(randint(0, 1000))
            HelpCoordinates[0].append(num)
            num = int(randint(0, 1000))
            HelpCoordinates[0].append(num)
        Coordinates[i] = HelpCoordinates
randomxy(1000)


Coordinates = list(itertools.chain(*Coordinates)) #3차원리스트를 2차원리스트로
Coordinates2 = list(itertools.chain(*Coordinates))

j=1
while j<=len(Coordinates2):
    fw.write(str(Coordinates2[j-1])+' ')
    fw.write(str(Coordinates2[j]))
    fw.write('\n')
    j+=2
fw.close()
print("---------------- \ninputfile에 저장")
Coordinates = np.array(Coordinates)
plt.scatter(Coordinates[:, 0], Coordinates[:, 1])
plt.show()
