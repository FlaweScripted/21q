class donto:
    def __init__(self,adatsor):
        reszletek = adatsor.split(';')
        
        self.ssz = reszletek[0]
        self.datum = reszletek [1]
        self.gyoztes = reszletek [2]
        self.eredmeny = reszletek [3]
        self.vesztes = reszletek [4]
        self.helyszin = reszletek [5]
        self.varosAllam = reszletek [6]
        self.nezoszam = int(reszletek[7])
        
    def __str__(self):
        return f"{self.datum},{self.helyszin}: {self.gyoztes} - {self.vesztes} {(self.helyszin)}" 
    
    #0
    print("Super Bowl döntői.")
    
    #1
    finp = open("SuperBowl.txt", mode="rt", encoding="utf-8") 
    adatSorok = finp.read().split('\n')
    finp.close
    
    dontok =[]
    for  i in range(1, len(adatSorok)): 
        if(adatSorok[i] != ""):
            donto = donto(adatSorok[i])
            dontok.append(donto)
            

#3
for item in dontok:
    print(item)            
            