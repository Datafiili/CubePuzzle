## -------------------- Soma Cube -------------------- ##
#Written By: Aarni Junkkala

#Brute forcing all solutions.

class shape():
    directions = []
    def __init__(self,directions):
        self.directions = directions

def CreateShapes():
    Palikat = []
    ## -------------------- Create shapes -------------------- ##
    #Direction of how the shape is build,
    #starts from the position x and direction tells where next part is
    #Directions need to be strings, so some pieces where there is multiple steps can work.
    
    #Forawrd = 0
    #Back = 1
    #Up = 2
    #Down = 3
    #Right = 4
    #Left = 5

    #This one is not nesessary as we can create 3 boards and represent all possible solutions with that
    # [][][]
    Palikat.append(shape([["0","0"],["2","2"],["4","4"]]))

    # Iso monimutkainen
    Palikat.append(shape([['3', '0', '0', '4'], ['5', '0', '0', '3'], ['2', '0', '0', '5'], ['4', '0', '0', '2'], ['3', '4', '4', '1'], ['0', '4', '4', '3'], ['2', '4', '4', '0'], ['1', '4', '4', '2'], ['3', '1', '1', '5'], ['5', '1', '1', '2'], ['2', '1', '1', '4'], ['4', '1', '1', '3'], ['3', '5', '5', '0'], ['0', '5', '5', '2'], ['2', '5', '5', '1'], ['1', '5', '5', '3']]))


    #   []
    # [][][]
    Palikat.append(shape([['0', '0', '12'], ['0', '0', '13'], ['0', '0', '14'], ['0', '0', '15'], ['4', '4', '53'], ['4', '4', '52'], ['4', '4', '50'], ['4', '4', '51'], ['2', '2', '30'], ['2', '2', '31'], ['2', '2', '34'], ['2', '2', '35']]))

    # [][]
    #   [][]  
    Palikat.append(shape([['0', '2', '0'], ['0', '3', '0'], ['0', '4', '0'], ['0', '5', '0'], ['2', '0', '2'], ['2', '1', '2'], ['2', '4', '2'], ['2', '5', '2'], ['4', '0', '4'], ['4', '1', '4'], ['4', '2', '4'], ['4', '3', '4']]))
    
    # []
    # [][]
    Palikat.append(shape([['3', '0'], ['3', '4'], ['3', '1'], ['3', '5'], ['2', '0'], ['2', '4'], ['2', '1'], ['2', '5']]))
    # 

    #Corner piece
    Palikat.append(shape([['0', '4', '52'], ['0', '5', '42'], ['0', '4', '53'], ['0', '5', '43'], ['4', '0', '12'], ['5', '0', '12'], ['4', '0', '13'], ['5', '0', '13']]))
    #Pienempi monimutkainen
    Palikat.append(shape([['3', '0', '4'], ['5', '0', '3'], ['2', '0', '5'], ['5', '0', '2'], ['3', '4', '1'], ['5', '3', '1'], ['2', '5', '1'], ['4', '2', '1'], ['3', '1', '5'], ['5', '1', '2'], ['2', '1', '5'], ['4', '1', '3'], ['3', '5', '0'], ['5', '2', '0'], ['2', '4', '0'], ['4', '3', '0']]))
    
    return Palikat

def CheckPositions(L1,L2,Area): #Checks if L1 are empty and L2 are not.
    for i in range(len(L1)):
        if Area[L1[i]] != None:
            return False
    for i in range(len(L2)):
        if Area[L2[i]] == None:
            return False
    return True

def ImpossibleSetting(Area):
    #Corners
    if CheckPositions([0],[1,3,9],Area):
        return False
    if CheckPositions([6],[1,5,11],Area):
        return False
    if CheckPositions([8],[3,7,15],Area):
        return False
    if CheckPositions([8],[5,7,17],Area):
        return False
    if CheckPositions([18],[9,19,21],Area):
        return False
    if CheckPositions([20],[11,19,23],Area):
        return False
    if CheckPositions([24],[15,21,25],Area):
        return False
    if CheckPositions([26],[17,23,25],Area):
        return False
    
    #Sides
    if CheckPositions([1],[0,2,4,10],Area):
        return False
    if CheckPositions([3],[0,4,6,12],Area):
        return False
    if CheckPositions([5],[2,4,8,14],Area):
        return False
    if CheckPositions([7],[4,6,8,16],Area):
        return False
    if CheckPositions([9],[0,10,12,18],Area):
        return False
    if CheckPositions([11],[2,10,14,20],Area):
        return False
    if CheckPositions([15],[6,12,16,24],Area):
        return False
    if CheckPositions([17],[8,14,16,26],Area):
        return False
    if CheckPositions([19],[10,18,20,22],Area):
        return False
    if CheckPositions([21],[12,18,22,24],Area):
        return False
    if CheckPositions([23],[14,20,22,26],Area):
        return False
    if CheckPositions([25],[16,22,24,26],Area):
        return False
    
    #Faces
    if CheckPositions([4],[1,3,5,7,13],Area):
        return False
    if CheckPositions([10],[1,9,11,19],Area):
        return False
    if CheckPositions([12],[3,9,13,15,21],Area):
        return False
    if CheckPositions([14],[5,11,17,23,13],Area):
        return False
    if CheckPositions([16],[7,13,15,17,25],Area):
        return False
    if CheckPositions([22],[13,19,21,23,25],Area):
        return False
    
    #Center
    if CheckPositions([13],[4,10,12,14,16,22],Area):
        return False

    #2-piece horizontal
    if CheckPositions([0,1],[2,3,4,9,10],Area):
        return False
    if CheckPositions([1,2],[0,4,5,10,11],Area):
        return False
    if CheckPositions([3,4],[0,1,5,6,7,12,13],Area):
        return False
    if CheckPositions([4,5],[1,2,3,7,8,13,14],Area):
        return False
    if CheckPositions([6,7],[3,4,8,15,16],Area):
        return False
    if CheckPositions([7,8],[4,5,6,16,17],Area):
        return False
    if CheckPositions([9,10],[0,1,11,12,13,18,19],Area):
        return False
    if CheckPositions([10,11],[1,2,9,13,14,19,20],Area):
        return False
    if CheckPositions([12,13],[3,4,9,10,14,15,16,21,22],Area):
        return False
    if CheckPositions([13,14],[4,5,10,11,12,16,17,22,23],Area):
        return False
    if CheckPositions([15,16],[6,7,12,13,17,24,25],Area):
        return False
    if CheckPositions([16,17],[7,8,13,14,15,25,26],Area):
        return False
    if CheckPositions([18,19],[9,10,20,21,22],Area):
        return False
    if CheckPositions([19,20],[10,11,18,22,23],Area):
        return False
    if CheckPositions([21,22],[12,13,18,19,23,24,25],Area):
        return False
    if CheckPositions([22,23],[13,14,19,20,21,25,26],Area):
        return False
    if CheckPositions([24,25],[15,16,21,22,26],Area):
        return False
    if CheckPositions([25,26],[16,17,22,23,24],Area):
        return False
    
    #2-piece vertical (up)
    if CheckPositions([0,3],[1,4,6,9,12],Area):
        return False
    if CheckPositions([1,4],[0,2,3,5,7,10,13],Area):
        return False
    if CheckPositions([2,5],[1,4,8,11,14],Area):
        return False
    if CheckPositions([3,6],[0,4,7,12,15],Area):
        return False
    if CheckPositions([4,7],[1,3,5,6,8,13,16],Area):
        return False
    if CheckPositions([5,8],[2,4,7,14,17],Area):
        return False
    if CheckPositions([9,12],[0,3,10,13,15,18,21],Area):
        return False
    if CheckPositions([10,13],[1,4,9,11,12,14,16,19,22],Area):
        return False
    if CheckPositions([11,14],[2,5,10,13,17,20,23],Area):
        return False
    if CheckPositions([12,15],[3,6,9,13,16,21,24],Area):
        return False
    if CheckPositions([13,16],[4,7,10,12,14,15,17,22,25],Area):
        return False
    if CheckPositions([14,17],[5,8,11,13,16,23,26],Area):
        return False
    if CheckPositions([18,21],[9,12,19,22,24],Area):
        return False
    if CheckPositions([19,22],[10,13,18,20,21,23,25],Area):
        return False
    if CheckPositions([20,23],[11,14,19,22,26],Area):
        return False
    if CheckPositions([21,24],[12,15,18,22,25],Area):
        return False
    if CheckPositions([22,25],[13,16,19,21,23,24,26],Area):
        return False
    if CheckPositions([23,26],[14,17,20,22,25],Area):
        return False
    
    #2-piece forward
    if CheckPositions([0,9],[1,3,10,12,18],Area):
        return False
    if CheckPositions([1,10],[0,2,4,9,11,13,19],Area):
        return False
    if CheckPositions([2,11],[1,5,10,14,20],Area):
        return False
    if CheckPositions([3,12],[0,4,6,9,13,15,21],Area):
        return False
    if CheckPositions([4,13],[1,3,5,7,10,12,14,16,22],Area):
        return False
    if CheckPositions([5,14],[2,4,8,11,13,17,23],Area):
        return False
    if CheckPositions([6,15],[3,7,12,16,24],Area):
        return False
    if CheckPositions([7,16],[4,6,8,13,15,17,25],Area):
        return False
    if CheckPositions([8,17],[5,7,14,16,26],Area):
        return False
    if CheckPositions([9,18],[0,10,12,19,21],Area):
        return False
    if CheckPositions([10,19],[1,9,11,13,18,20,22],Area):
        return False
    if CheckPositions([11,20],[2,10,14,19,23],Area):
        return False
    if CheckPositions([12,21],[3,9,13,15,18,22,24],Area):
        return False
    if CheckPositions([13,22],[4,10,12,14,16,19,21,23,25],Area):
        return False
    if CheckPositions([14,23],[5,11,13,17,20,22,26],Area):
        return False
    if CheckPositions([15,24],[6,12,16,21,25],Area):
        return False
    if CheckPositions([16,25],[7,13,15,17,22,24,26],Area):
        return False
    if CheckPositions([17,26],[8,14,16,23,25],Area):
        return False
    
    #print("Area holder didn't fail")
    
    #If all checks fail, then piece is in a good place
    return True

def TestDirection(Area,Directions,AreaIndex,PieceIndex):
    Debug = False
    AreaHolder = Area[:]
    #If already taken, then doesn't work.
    if AreaHolder[AreaIndex] != None:
        if Debug:
            print("Spot taken",AreaIndex)
        return False
        
    
    CurIndex = AreaIndex #Where we are currently or going out of bounds
    AreaHolder[CurIndex] = PieceIndex
    for i in range(len(Directions)):
        for k in range(len(Directions[i])):
            #What index we move into
            if Directions[i][k] == "0": #F
                if k == len(Directions[i]) - 1 and CurIndex in [18,19,20,21,22,23,24,25,26]:
                    return False
                CurIndex += 9
            if Directions[i][k] == "1": #B
                if k == len(Directions[i]) - 1 and CurIndex in [0,1,2,3,4,5,6,7,8]:
                    return False
                CurIndex += -9
            if Directions[i][k] == "2": #U
                if k == len(Directions[i]) - 1 and CurIndex in [6,7,8,15,16,17,24,25,26]:
                    return False
                CurIndex += 3
            if Directions[i][k] == "3": #D
                if k == len(Directions[i]) - 1 and CurIndex in [0,1,2,9,10,11,18,19,20]:
                    return False
                CurIndex += -3
            if Directions[i][k] == "4": #R
                if k == len(Directions[i]) - 1 and CurIndex in [2,5,8,11,14,17,20,23,26]:
                    return False
                CurIndex += 1
            if Directions[i][k] == "5": #L
                if k == len(Directions[i]) - 1 and CurIndex in [0,3,6,9,12,15,18,21,24]:
                    return False
                CurIndex += -1
        
        #Out of bounds
        if CurIndex < 0 or CurIndex > 26:
            if Debug:
                print("Out of bounds")
            return False

        #Already taken
        if AreaHolder[CurIndex] != None:
            if Debug:
                print(AreaHolder)
                print("Adding to taken place",CurIndex, " taken by",AreaHolder[CurIndex], "Current pieceindex", PieceIndex)
            return False

        AreaHolder[CurIndex] = PieceIndex        
    
    if ImpossibleSetting(AreaHolder):
        if Debug:
            print("Yeah")
        return AreaHolder
    else:
        if Debug:
            print("Area impossible")
        return False

Branch = [0,None,None,None,None,None,None] #Shows what branch we are on
Branches = [0,None,None,None,None,None,None] #Shows how many branches are there

def SetBranch(index,num,branches,b):
    for i in range(index,len(Branch)):
        Branch[i] = None
        Branches[i] = None
    Branch[index] = num
    Branches[index] = b
    
    print(Branch)
    print(Branches)

def TestPiece(Area,Pieces,PieceIndex):
    
    global Branch, Branches
    #Checks if board is already full, then returns
    BoardFull = True
    for i in range(len(Area)):
        if Area[i] != None:
            BoardFull = False
            break
    if BoardFull:
        return Area
    
    if PieceIndex > 6: #Can't test too far
        #print("PieceIndex too high!")
#         Number += 1
#         print(Number,"Area (PieceI) is:",Area)
#         if Number > 1:
#             while True:
#                 True
        return Area
    
    AreaHolder = Area[:] #Making new area so old one doesn't change.
    EmptySpaces = AreaHolder.count(None)
    WorkingAreas = []
    #print("PieceIndex:",PieceIndex,"Amount of directions:",len(Pieces[PieceIndex].directions))
    #with Bar('Prosessoi palikkaa ' + str(PieceIndex), max= len(Pieces[PieceIndex].directions) * EmptySpaces) as bar:

    #Loops all directions of current piece
    for i in range(len(Pieces[PieceIndex].directions)): #Foreach direction of the piece
        for k in range(len(AreaHolder)): #Foreach spot on the board
            if AreaHolder[k] == None:
                Result = TestDirection(AreaHolder,Pieces[PieceIndex].directions[i],k,PieceIndex)
                if Result != False:
                    WorkingAreas.append(Result)
                    #bar.next()
    #print("Working areas:",WorkingAreas)
    Final = []
    
    for i in range(len(WorkingAreas)):
        #SetBranch(PieceIndex,i,Branches,len(WorkingAreas))

        Result = TestPiece(WorkingAreas[i],Pieces,PieceIndex+1)
        
        
        if Result != False and Result != []:
            Final.append(Result)
    
    if Final != [] and PieceIndex > 1:
        return Final[0]
    
    return Final

if __name__ == '__main__':
    #     start = time.time()
    Pieces = CreateShapes()
    #for i in range(len(Pieces)):
    #    print("Piece" + str(i+1),Pieces[i].directions)
    
    board1 = []
    for i in range(27):
        board1.append(None)
    board1[4] = 0
    board1[13] = 0
    board1[22] = 0
    Result = TestPiece(board1,Pieces,1)
    
    board1 = []
    for i in range(27):
        board1.append(None)
    board1[0] = "0"
    board1[9] = "0"
    board1[18] = "0"
    Result += TestPiece(board1,Pieces,1)
    
    board1 = []
    for i in range(27):
        board1.append(None)
    board1[1] = "0"
    board1[10] = "0"
    board1[19] = "0"
    Result += TestPiece(board1,Pieces,1)
    
    print(Result)
    print(len(Result))