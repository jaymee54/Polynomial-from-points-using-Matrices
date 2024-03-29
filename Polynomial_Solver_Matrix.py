def GetPoints():
    X_output = float(input("Input your x coordinate:\n"))
    Y_output = float(input("Input your y coordinate:\n"))
    return([X_output,Y_output])


def MatrixInit(Point_array):
    Matrix = []
    for i in Point_array:
        row = [1]
        for j in range(1,len(Point_array)):
            row.append(i[0]**j)
        row.append(i[1])
        Matrix.append(row)
    return(Matrix)

def PrintMatrix(Matrix):
    print("-------------------")
    for Row in Matrix:
        print(Row)
    print("-------------------")


def SubtractRows(RowOne, RowTwo):
    if len(RowOne) != len(RowTwo):
        print('Subtraction Error')
        return
    else:
        RowAnswer = []
        for i in range(0,len(RowOne)):
            RowAnswer.append(RowOne[i]-RowTwo[i])
    return(RowAnswer)

def MultiplyRow(Scalar, Row):
    RowAnswer = []
    for i in Row:
        RowAnswer.append(Scalar*i)
    return(RowAnswer)

def FirstNonZeroEntry(Row):
    for i in range(0,len(Row)):
        if Row[i] != 0:
            return(i)
    print('0 Row Error')
    return

def RowReductionDownward(Matrix, RowIndex):
    #here row 0 is the top row
    Row = Matrix[RowIndex-1]
    FirstIndex = FirstNonZeroEntry(Row)
    MatrixAnswer = []
    for i in range(0,RowIndex):
        MatrixAnswer.append(Matrix[i])
    for i in range(RowIndex,len(Matrix)):
        RowAnswer = SubtractRows(Matrix[i],MultiplyRow(Matrix[i][FirstIndex]/Row[FirstIndex],Row))
        MatrixAnswer.append(RowAnswer)
    return(MatrixAnswer)


def Unitary(Matrix):
    MatrixAnswer = []
    for i in Matrix:
        FirstIndex = FirstNonZeroEntry(i)
        MatrixAnswer.append(MultiplyRow(1/i[FirstIndex],i))
    return(MatrixAnswer)

'''
#this is an abandoned first attempt
def UpperTriangular(Matrix):
    #This doesnt always work
    RowIndex = FirstNonZeroEntry(Matrix[-1])+1
    #RowReductionDownward(Matrix,RowIndex)
    if RowIndex < len(Matrix):
        return(UpperTriangular(RowReductionDownward(Matrix,RowIndex)))
    else:
        return(Matrix)
'''

def UpperTriangularLoop(Matrix,RowIndex):
    if RowIndex < len(Matrix):
        return(UpperTriangularLoop(RowReductionDownward(Matrix,RowIndex),RowIndex+1))
    else:
        return(Matrix)

def UpperTriangular(Matrix):
    return(UpperTriangularLoop(Matrix,1))


def DoubleTransposeMatrix(Matrix):
    MatrixAnswer = []
    for RowIndex in range(len(Matrix)-1,-1,-1):
        RowAnswer = []
        Row = Matrix[RowIndex]
        for EntryIndex in range(len(Row)-2,-1,-1):
            RowAnswer.append(Row[EntryIndex])
        RowAnswer.append(Row[len(Row)-1])
        MatrixAnswer.append(RowAnswer)
    return(MatrixAnswer)

def LowerTriangular(Matrix):
    return(DoubleTransposeMatrix(UpperTriangular(DoubleTransposeMatrix(Matrix))))

def RowReducedFormSolution(Matrix):
    return(Unitary(LowerTriangular(UpperTriangular(Matrix))))

def GetCoords():
    CoordList = []
    Bool = True
    while Bool:
        coord = GetPoints()
        CoordList.append(coord)
        print("Sucessfully added the point " + str(coord))
        NewBool = False
        Yes = ["Yes","yes","Y","y","Yeah","yeah"]
        YesOrNo = input("Do you want to add another coordinate? y/n:\n")
        for i in Yes:
            if YesOrNo == i:
                NewBool = True
        Bool = NewBool
    return(CoordList)

def GetRowReducedFormSolutionFromCoords():
    return(RowReducedFormSolution(MatrixInit(GetCoords())))

def PrintPolynomialSolution(RRMatrix):
    RowAnswers = []
    for Row in RRMatrix:
        RowAnswers.append(Row[-1])
    PolynomialSolution = ""
    for EntryIndex in range(0,len(RowAnswers)):
        #print(str(RowAnswers[EntryIndex])+"x^"+str(EntryIndex)+" + ")
        PolynomialSolution += (str(RowAnswers[EntryIndex])+"x^"+str(EntryIndex)+" + ")
    print(PolynomialSolution[0:-3])

#print('Test')
#PrintMatrix(MatrixInit([[1,2],[2,3],[3,4],[4,5],[5,6]]))
#print(SubtractRows([4,5,6],[1,2,3]))
#print(FirstNonZeroEntry([0,0,1,0,0]))
#print(MultiplyRow(2,[1,2,3]))
#PrintMatrix(RowReductionDownward(MatrixInit([[1,2],[2,3],[3,4],[4,5],[5,6]]),1))
#PrintMatrix(UpperTriangular(MatrixInit([[1,2],[2,4],[3,4],[4,8],[5,10]])))
#PrintMatrix(Unitary(UpperTriangular(MatrixInit([[1,2],[2,4],[3,4],[4,8],[5,10]]))))
#PrintMatrix(DoubleTransposeMatrix(MatrixInit([[1,2],[2,3],[3,4],[4,5],[5,6]])))
#PrintMatrix(LowerTriangular(UpperTriangular(MatrixInit([[1,2],[2,4],[3,4],[4,8],[5,10]]))))
#PrintMatrix(Unitary(LowerTriangular(UpperTriangular(MatrixInit([[1,2],[2,4],[3,4],[4,8],[5,10]])))))
#PrintMatrix(RowReducedFormSolution(MatrixInit([[1,2],[2,4],[3,4],[4,8],[5,10]])))
#PrintMatrix(RowReducedFormSolution(MatrixInit([[0,0],[1,0.003],[2,0.009],[3,0.029],[4,0.088],[5,0.237],[6,0.5],[7,0.763],[8,0.912],[9,0.971],[10,0.991],[11,0.997],[12,1]])))
#PrintMatrix(RowReducedFormSolution(MatrixInit([[0,1],[1,1.107],[2,1.225],[3,1.355],[4,1.5]])))
#print(GetPoints()[0])
#print(GetCoords())
PrintPolynomialSolution(GetRowReducedFormSolutionFromCoords())
