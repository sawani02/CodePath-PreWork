
# Question: Print concentric rectangular pattern in a 2d matrix. 
#Question link: https://www.interviewbit.com/problems/prettyprint/


class Solution:
    # @param A : integer
    # @return a list of list of integers
    def prettyPrint(self, A):
        #inputNumber = 3
        inputRow = (2*A) - 1
        inputColumn = (2*A) - 1

        Matrix = [[0 for rowNumber in range(inputRow)] for columnNumber in range(inputColumn)]


        testRowNumber = 0
        testColumnNumber = 0
        rowCouterForExecution = 0
        columnCounterForExecution = 0
        rowCountertoKeepTrack = 0
        while (A > 0):

   
            for row in range(testRowNumber,inputRow):
        
            
                for column in range(testColumnNumber,inputColumn):
                    if (rowCouterForExecution == 0) or (row == (inputRow - 1)):
                    #print ('First or Last Row')
                    #print ('[{0}][{1}] == {2}'.format(row,column,inputNumber))
                        Matrix[row][column] = A
                    elif (columnCounterForExecution == 0 or column == (inputColumn -1)):
                    #print ('Start and End of a Column')
                    #print ('[{0}][{1}] == {2}'.format(row,column,inputNumber))
                        Matrix[row][column] = A
                        columnCounterForExecution = columnCounterForExecution + 1
                    else:
                        #print ('Other Rows')
                        #print ('[{0}][{1}] == 0'.format(row,column))
                        Matrix[row][column] = 0
                    columnCounterForExecution = 0
                    rowCouterForExecution = rowCouterForExecution + 1

            rowCouterForExecution = 0
            columnCounterForExecution = 0
            testRowNumber = testRowNumber + 1
            testColumnNumber = testColumnNumber + 1
            inputColumn = inputColumn - 1
            inputRow = inputRow - 1
            A = A - 1
        return Matrix        

        
