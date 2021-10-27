import sys
input = sys.stdin.readline

class Soluction :
    def __init__(self):
        self.n = int(input())
        self.a , self.b = map(int, input().rstrip().split(" "))
        self.aArr = []
        self.preFixA = []
        self.bArr =[]
        self.preFixB = []

        self.maxA = 0
        self.maxB = 0
        
        self.dictA = dict()
        self.dictB = dict()
    
    def makeArr(self) :
        for i in range(self.a) :
            temp = int(input().rstrip()) 
            self.aArr.append(temp)
            if temp in self.dictA :
                self.dictA[temp] +=1
            elif temp <= self.n :
                self.dictA[temp] = 1

            if i == 0 :
                self.preFixA.append(temp)
            else :
                self.preFixA.append(temp + self.preFixA[i-1])
            
            self.getADictInfo(i,0)

        st = 1
        ed = self.a
        for i in range(self.a // 2 + 1) :
            temp = self.preFixA[-1] + self.aArr[i]
            self.preFixA.append(temp)
            self.getADictInfo(st + i,ed + i)



        for i in range(self.b) :
            temp = int(input().rstrip())
            self.bArr.append(temp)
            if temp in self.dictB :
                self.dictB[temp] += 1
            elif temp <= self.n :
                self.dictB[temp] = 1

            if i == 0 :
                self.preFixB.append(temp)
            else :
                self.preFixB.append(temp + self.preFixB[i-1])
            self.getBDictInfo(i,0)

        st = 1
        ed = self.b

        for i in range(self.b // 2 + 1) :
            temp = self.preFixB[-1] + self.bArr[i]
            self.preFixB.append(temp)
            self.getBDictInfo(st + i,ed + i)
    
    def getADictInfo(self,st, ed) :
        if ed < 1 :
            return
        target = self.preFixA[ed]
        if st == 0 :
            self.checkDictA(target)

        for j in range(st, ed - 1) :
            temp = target - self.preFixA[j]
            self.checkDictA(temp)

    def checkDictA(self, num) :
        if num <= self.n :
            if num in self.dictA :
                self.dictA[num] += 1
            else :
                self.dictA[num] = 1

    def getBDictInfo(self,st, ed) :
        if ed < 1 :
            return
        target = self.preFixB[ed]
        if st == 0 :
            self.checkDictB(target)

        for j in range(st, ed-1) :
            temp = target - self.preFixB[j]
            self.checkDictB(temp)

    def checkDictB(self, num) :
        if num <= self.n :
            if num in self.dictB :
                self.dictB[num] += 1
            else :
                self.dictB[num] = 1

    def getAnswer(self) :
        self.makeArr()
        answer = 0
        for k in self.dictA.keys() :
            tk = self.n - k 
            if tk == 0 :
                answer += self.dictA[k]
                continue
            if tk in self.dictB :
                answer += (self.dictA[k] * self.dictB[tk])
        if len(self.dictA) == 0 :
            if self.n in self.dictB :
                answer += self.dictB[self.n]
        return answer



s = Soluction()
print(s.getAnswer())



        

