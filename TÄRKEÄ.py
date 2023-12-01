from time import process_time
from progress.bar import Bar
import copy

class shape():
    directions = []
            

def Testaa():
    Palikat = []
    ## -------------------- Create shapes -------------------- ##

    #Direction of how the shape is build, starts from the position x and direction tells where next part is

    #Forawrd = 0
    #Back = 1
    #Up = 2
    #Down = 3
    #Right = 4
    #Left = 5

    # [][][]
    palikka = shape()
    palikka.directions.append(["0","0"])
    palikka.directions.append(["4","4"])
    palikka.directions.append(["2","2"])
    Palikat.append(palikka)

    #   []
    # [][][]
    palikka = shape()
    palikka.directions.append(["0","0","12"])#Forawrd
    palikka.directions.append(["0","0","13"])
    palikka.directions.append(["0","0","14"])
    palikka.directions.append(["0","0","15"])
    palikka.directions.append(["4","4","53"])#Right
    palikka.directions.append(["4","4","52"])
    palikka.directions.append(["4","4","53"])
    palikka.directions.append(["4","4","50"])
    palikka.directions.append(["4","4","51"])
    palikka.directions.append(["2","2","30"])#Up
    palikka.directions.append(["2","2","31"])
    palikka.directions.append(["2","2","34"])
    palikka.directions.append(["2","2","35"])
    
    Palikat.append(palikka)
   
    # [][]
    #   [][]  
    palikka = shape()
    palikka.directions = ["0","3","0"]
    Palikat.append(palikka)

    # []
    # [][]
    palikka = shape()
    palikka.append(["0","2"])
    Palikat.append(palikka)
    
    # 
    #
    palikka = shape()
    palikka.directions = ["3","0","4","4"]
    Palikat.append(palikka)

    #Corner piece
    palikka = shape()
    palikka.directions.append(["0","4","52"]) #Eteen, oik, vas ylös
    palikka.directions.append(["0","5","42"]) #Eteen, vas, oik yl
    palikka.directions.append(["0","4","53"]) #Et, oik, vas al
    palikka.directions.append(["0","5","43"]) #Et, oik, vas al
    palikka.directions.append(["4","0","12"]) #oik, et, taaks, yl
    palikka.directions.append(["5","0","12"]) #vas, et, taaks, yl
    palikka.directions.append(["4","0","13"]) #oik, et, taaks, al
    palikka.directions.append(["5","0","13"]) #vas, et, taaks, al
    Palikat.append(palikka)

    palikka = shape()
    palikka.directions = ["2","0","0","4"]
    Palikat.append(palikka)

    # ----- Builds the area that shapes need to fill in ----- #
    area = []
    for i in range(3):
        area.append([])
        for k in range(3):
            area[i].append([])
            for l in range(3):
                area[i][k].append(["e"])
    print("Base area:")
    for i in range(3):
        print(area[i])
    areaBackup = copy.deepcopy(area)
    ## -------------------- Testing possibilities ------------------------- ##
    
    
    workingAreas = []
    
    #Brute force
    #Place the piece to position on the map and test if it fits into the final shape, without exiting or touching other pieces
    totalPossibilities = 0
    onnistuneet = 0
    epäonnistuneet = 0
    
    with Bar('Prosessoi sanojen keksintää', max=162) as bar:

        for i in range(1):
            #print("Palikka " + str(i))
            for k in range(len(area)):
                for l in range(len(area[k])):
                    for j in range(len(area[k][l])):
                        #print("Area[" + str(k) + "][" + str(l) + "][" + str(j) + "]")
                        for a in range(6): #6 possible directions for all pieces
                            try:
                                area = copy.deepcopy(areaBackup)
                                area[k][l][j] = i
                                k1 = k
                                l1 = l
                                j1 = j
                                for d in range(len(Palikat[i].directions)):
                                    for p in range(len(Palikat[i].directions[d])):
                                        di = Palikat[i].directions[d]
                                        if di == "0":
                                            k1 += 1
                                        if di == "1":
                                            k1 -= 1
                                        if di == "2":
                                            j1 += 1
                                        if di == "3":
                                            j1 -= 1
                                        if di == "4":
                                            l1 += 1
                                        if di == "5":
                                            l1 -= 1
                                        
                                        if p == len(Palikat[i].directions[d]) - 1:
                                            area[k1][l1][j1] = i
                                        print(1.2)
                                        #creates new data to be saved
                                        
                                        
                                        print(1.3)   
                                workingAreas.append(copy.deepcopy(area))
                                onnistuneet += 1
                                print("Total possibilites atm: " + str(totalPossibilities))
                            except:
                                epäonnistuneet += 1
                            totalPossibilities += 1
                            #bar.next()

    #Forawrd = 0
    #Back = 1
    #Up = 2
    #Down = 3
    #Right = 4
    #Left = 5
    
    
    print("Total possibilities " + str(totalPossibilities))
    print("Total of great possibilities " + str(onnistuneet))    
    print("Total of failed possibilities " + str(epäonnistuneet))
    
    for i in range(len(workingAreas)):
        print("Working area " + str(i + 1))
        for k in range(len(workingAreas[i])):
            print(workingAreas[i][k])
    
    print("Area backup:")
    for i in range(len(areaBackup)):
        print(areaBackup[i])

if __name__ == '__main__':
    Testaa()