import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        # TODO - your code here
        if self.h == 1:
            return self.g[0][0]

        elif self.h == 2:
            return (self.g[0][0]*self.g[1][1]-self.g[0][1]*self.g[1][0])

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        # TODO - your code here
        sum_trace = 0

        for i in range(self.h):
            for j in range(self.w):
                if i == j:
                    sum_trace += self.g[i][j]

        return sum_trace

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")

        # TODO - your code here
        if self.h == 2:
            if self.g[0][0] * self.g[1][1] == self.g[0][1] * self.g[1][0]:
                return "ad = bc. Therefore the Matrix is not invertible"
            else:
                detA = 1/(self.determinant()) 
                inverse = [[detA*self.g[1][1],detA*-self.g[0][1]],[detA*-self.g[1][0],detA*self.g[0][0]]]
        elif self.h == 1:
            inverse = [[1/self.g[0][0]]]
        return Matrix(inverse)    

    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here
        matrix_transpose = []
        for i in range(self.w):
            row_matrix = []
            for j in range(self.h):
                row_matrix.append(self.g[j][i])
            matrix_transpose.append(row_matrix)
        return Matrix(matrix_transpose)

    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        #   
        # TODO - your code here
        #
        matrix_addition = []
        for i in range(self.h):
            new_row = []
            for j in range(self.w):
                addition = self.g[i][j] + other.g[i][j]
                new_row.append(addition)

            matrix_addition.append(new_row)
        return Matrix(matrix_addition)

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        #   
        # TODO - your code here
        #
        negative =[]
        for i in range(self.h):
            new_row = []
            for j in range(self.w):
                new_row.append(-1*self.g[i][j])
            negative.append(new_row)    
        return Matrix(negative)        

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        #   
        # TODO - your code here
        #
        matrix_subtraction = []
        for i in range(self.h):
            new_row = []
            for j in range(self.w):
                subtraction = self.g[i][j] - other.g[i][j]
                new_row.append(subtraction)
            matrix_subtraction.append(new_row)
        return Matrix(matrix_subtraction)


    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        #   
        # TODO - your code here
        #
        #get_row func
        def get_row(matrix, row):
            return matrix[row]

        #get_column func
        def get_column(matrix, column_number):
            column = []
            for i in range(len(matrix)): 
                column.append(matrix[i][column_number])

            return column
        
        #dot_product func
        def dot_product(vector_one, vector_two):
            dot_product = 0
            for i in range(len(vector_one)):
                dot_product += vector_one[i] * vector_two[i]

            return dot_product
        
        result = []
        for i in range(self.h):
            row = get_row(self.g, i)
            row_result = []
            for j in range(other.w):
                column = get_column(other.g, j)
                mul = dot_product(row,column)
                row_result.append(mul)
            
            result.append(row_result)     

        return Matrix(result)




    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            pass
            #   
            # TODO - your code here
            #
            for i in range(self.h):
                for j in range(self.w):
                    self.g[i][j] = other * self.g[i][j]
            return Matrix(self.g)            