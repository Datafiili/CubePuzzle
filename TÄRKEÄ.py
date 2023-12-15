from time import process_time
from progress.bar import Bar
import copy

class shape():
    directions = []
    
    def __init__(self,directions):
        self.directions = directions

def CreateShapes():
    Palikat = []
    ## -------------------- Create shapes -------------------- ##
    #TODO MUUTA SUUNNA STRINGEIKSI
    #Direction of how the shape is build, starts from the position x and direction tells where next part is

    #Forawrd = 0
    #Back = 1
    #Up = 2
    #Down = 3
    #Right = 4
    #Left = 5

    #This one is not nesessary as we can create 3 boards and represent all possible solutions with that
    # [][][]
    Palikat.append(shape([[0,0],[2,2],[4,4]]))

    #   []
    # [][][]
    Palikat.append(shape([[0,0,12],[0,0,13],[0,0,14],[0,0,15],[4,4,53],[4,4,52],[4,4,50],[4,4,51],[2,2,30],[2,2,31],[2,2,34],[2,2,35]]))

    # [][]
    #   [][]  
    Palikat.append(shape([[0,2,0],[0,3,0],[0,4,0],[0,5,0],[2,0,2],[2,1,2],[2,4,2],[2,5,2],[4,0,4],[4,1,4],[4,2,4],[4,3,4]]))
    
    # []
    # [][]
    Palikat.append(shape([[3,0],[3,4],[3,1],[3,5],[2,0],[2,4],[2,1],[2,5]]))
    # 
    # Iso monimutkainen
    Palikat.append(shape([[3,0,0,4],[5,0,0,3],[2,0,0,5],[4,0,0,2],[3,4,4,1],[0,4,4,3],[2,4,4,0],[1,4,4,2],[3,1,1,5],[5,1,1,2],[2,1,1,4],[4,1,1,3],[3,5,5,0],[0,5,5,2],[2,5,5,1],[1,5,5,3]]))

    #Corner piece
    Palikat.append(shape([[0,4,52],[0,5,42],[0,4,53],[0,5,43],[4,0,12],[5,0,12],[4,0,13],[5,0,13]]))
    #Pienempi monimutkainen
    Palikat.append(shape([[3,0,4],[5,0,3],[2,0,5],[5,0,2],[3,4,1],[5,3,1],[2,5,1],[4,2,1],[3,1,5],[5,1,2],[2,1,5],[4,1,3],[3,5,0],[5,2,0],[2,4,0],[4,3,0]]))
    
    return Palikat

def ImpossibleSetting(Area):
    #Corners
    if Area[0] == None and Area[1] != None and Area[3] != None and Area[9] != None:
        return False
    if Area[2] == None and Area[1] != None and Area[5] != None and Area[11] != None:
        return False
    if Area[6] == None and Area[7] != None and Area[3] != None and Area[15] != None:
        return False
    if Area[8] == None and Area[7] != None and Area[5] != None and Area[17] != None:
        return False
    if Area[18] == None and Area[19] != None and Area[21] != None and Area[9] != None:
        return False
    if Area[20] == None and Area[19] != None and Area[23] != None and Area[11] != None:
        return False
    if Area[24] == None and Area[25] != None and Area[15] != None and Area[21] != None:
        return False
    if Area[26] == None and Area[25] != None and Area[23] != None and Area[17] != None:
        return False
    
    #Sides
    if Area[1] == None and Area[0] != None and Area[2] != None and Area[4] != None and Area[10] != None:
        return False
    if Area[3] == None and Area[0] != None and Area[6] != None and Area[4] != None and Area[12] != None:
        return False
    if Area[5] == None and Area[2] != None and Area[4] != None and Area[8] != None and Area[14] != None:
        return False
    if Area[7] == None and Area[6] != None and Area[8] != None and Area[4] != None and Area[16] != None:
        return False
    if Area[11] == None and Area[2] != None and Area[10] != None and Area[20] != None and Area[14] != None:
        return False
    if Area[17] == None and Area[8] != None and Area[16] != None and Area[14] != None and Area[26] != None:
        return False
    if Area[9] == None and Area[10] != None and Area[12] != None and Area[0] != None and Area[18] != None:
        return False
    if Area[15] == None and Area[6] != None and Area[24] != None and Area[16] != None and Area[12] != None:
        return False
    if Area[19] == None and Area[18] != None and Area[20] != None and Area[22] != None and Area[10] != None:
        return False
    if Area[21] == None and Area[22] != None and Area[18] != None and Area[24] != None and Area[12] != None:
        return False
    if Area[23] == None and Area[26] != None and Area[20] != None and Area[14] != None and Area[22] != None:
        return False
    if Area[25] == None and Area[24] != None and Area[26] != None and Area[22] != None and Area[16] != None:
        return False
    
    #Faces
    if Area[4] == None and Area[1] != None and Area[3] != None and Area[5] != None and Area[7] != None and Area[13] != None:
        return False
    if Area[10] == None and Area[1] != None and Area[9] != None and Area[11] != None and Area[19] != None and Area[13] != None:
        return False
    if Area[12] == None and Area[3] != None and Area[9] != None and Area[21] != None and Area[15] != None and Area[13] != None:
        return False
    if Area[14] == None and Area[5] != None and Area[11] != None and Area[17] != None and Area[23] != None and Area[13] != None:
        return False
    if Area[16] == None and Area[7] != None and Area[15] != None and Area[17] != None and Area[25] != None and Area[13] != None:
        return False
    if Area[22] == None and Area[19] != None and Area[21] != None and Area[23] != None and Area[25] != None and Area[13] != None:
        return False
    
    #Center
    if Area[13] == None and Area[4] != None and Area[10] != None and Area[14] != None and Area[12] != None and Area[16] != None and Area[22] != None:
        return False
    
    #print("Area holder didn't fail")
    
    #If all checks fail, then piece is in a good place
    return True

def TestDirection(Area,Directions,AreaIndex,PieceIndex):
    AreaHolder = Area[:]
    #If already taken, then doesn't work.
    if AreaHolder[AreaIndex] != None:
        print("Spot taken",AreaIndex)
        return False
        
    
    CurIndex = AreaIndex #Where we are currently
    AreaHolder[CurIndex] = PieceIndex
    for i in range(len(Directions)):
        
        #What index we move into
        if Directions[i] == 0:
            CurIndex += 9
        if Directions[i] == 1:
            CurIndex += -9
        if Directions[i] == 2:
            CurIndex += 3
        if Directions[i] == 3:
            CurIndex += -3
        if Directions[i] == 4:
            CurIndex += 1
        if Directions[i] == 5:
            CurIndex += -1
        
        #Out of bounds
        if CurIndex < 0 or CurIndex > 26:
            print("Out of bounds")
            return False

        #Already taken
        if AreaHolder[CurIndex] != None:
            print(AreaHolder)
            print("Adding to taken place",CurIndex, " taken by",AreaHolder[CurIndex])
            return False
            
            
        AreaHolder[CurIndex] = PieceIndex        
    
    if ImpossibleSetting(AreaHolder):
        print("Yeah")
        return AreaHolder
    else:
        print("Area impossible")
        return False
        
def TestPiece(Area,Pieces,PieceIndex):
        
    #Checks if board is already full, then returns
    BoardFull = True
    for i in range(len(Area)):
        if Area[i] != None:
            BoardFull = False
    if BoardFull:
        return Area
    
    if PieceIndex > 6: #Can't test too far
        #print("PieceIndex too high!")
        return False
    
    AreaHolder = Area[:] #Making new area so old one doesn't change.
    WorkingAreas = []
    print("PieceIndex:",PieceIndex,"Amount of directions:",len(Pieces[PieceIndex].directions))
    with Bar('Prosessoi palikkaa ' + str(PieceIndex), max= len(Pieces[PieceIndex].directions) *len(AreaHolder)) as bar:

        #Loops all directions of current piece
        for i in range(len(Pieces[PieceIndex].directions)): #Foreach direction of the piece
            for k in range(len(AreaHolder)): #Foreach spot on the board
                Result = TestDirection(AreaHolder,Pieces[PieceIndex].directions[i],k,PieceIndex)
                if Result != False:
                    WorkingAreas.append(Result)
                bar.next()
    print("Working areas:",WorkingAreas)
    Final = []
    
    for i in range(len(WorkingAreas)):
#         print("Area:",i+1)
#         print(WorkingAreas[i][0:8])
#         print(WorkingAreas[i][9:17])
#         print(WorkingAreas[i][18:26])
        
        Result = TestPiece(WorkingAreas[i],Pieces,PieceIndex+1)
        if Result != False:
            Final.append(Result)
    #print("Result:",Result)
    return Result




if __name__ == '__main__':
    Pieces = CreateShapes()
    #for i in range(len(Pieces)):
    #    print("Piece" + str(i+1),Pieces[i].directions)
    board1 = []
    for i in range(27):
        board1.append(None)
    board1[0] = 0
    board1[1] = 0
    board1[2] = 0
    a = TestPiece(board1,Pieces,1)
    for i in range(len(a)):
        print(a[i])
    
