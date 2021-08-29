import math
from Matrix import Matrix


class Vector(Matrix):

    def __init__(self, m, init=True):
        Matrix.__init__(self, m, 1, init)

    def __add__(self, other):
        first = Matrix.fromVector(self)
        second = Matrix.fromVector(other)
        vec = Vector.fromMatrix(Matrix.__add__(first, second))
        return vec

    def __sub__(self, other):
        first = Matrix.fromVector(self)
        second = Matrix.fromVector(other)
        vec = Vector.fromMatrix(Matrix.__sub__(first, second))
        return vec

    def __mul__(self, other):
        first = Matrix.fromVector(self)
        second = Matrix.fromVector(other)
        vec = Matrix.__mul__(first, second)
        return vec

    def __getitem__(self, idx):
        return self.rows[idx][0]

    def __setitem__(self, idx, item):
        self.rows[idx][0] = item

    def getMagnitude(self):
        summ = 0
        for i in range(self.m):
            summ += i**2

        return math.sqrt(summ)

    def normalize(self):
        magnitude = self.getMagnitude()
        if magnitude != 0:
            for i in range(self.m):
                self[i] /= magnitude

    def getNormalized(self):
        vec = self
        vec.normalize()
        return vec

    @classmethod
    def cos(cls, self, other):
        return Vector.dotProduct(self, other) / (self.getMagnitude() * other.getMagnitude())

    @classmethod
    def sin(cls, self, other):
        return math.sqrt(1 - Vector.cos(self, other) ** 2)

    @classmethod
    def getAngle(cls, self, other):
        return math.acos(Vector.cos(self, other)) / math.pi * 180


    @classmethod
    def dotProduct(cls, self, other):
        if self.get_rank() == other.get_rank():
            sum = 0
            for i in range(other.m):
                sum += self[i] * other[i]
            return sum
        else:
            raise Exception("Vectors's dimensions must be equal")

    @classmethod
    def crossProduct(cls, self, other):
        if self.m == 3 and other.m == 3:
            vec = Vector.makeZero(3)
            vec[0] = self[1] * other[2] - self[2] * other[1]
            vec[1] = self[2] * other[0] - self[0] * other[2]
            vec[2] = self[0] * other[1] - self[1] * other[0]

            return vec
        else:
            raise Exception("Vectors's dimensions must be equal to 3")

    @classmethod
    def _makeVector(cls, rows):
        vec = Vector.fromMatrix(Matrix._makeMatrix(rows))
        return vec

    @classmethod
    def makeRandom(cls, m, low=0, high=10):
        vec = Vector.fromMatrix(Matrix.makeRandom(m, 1, low, high))
        return vec

    @classmethod
    def makeZero(cls, m):
        vec = Vector.fromMatrix(Matrix.makeZero(m, 1))
        return vec

    @classmethod
    def fromList(cls, list):
        vec = Vector.fromMatrix(Matrix.fromList([[i]for i in list]))
        return vec

    @classmethod
    def fromMatrix(cls, matrix):
        vec = Vector(matrix.m)
        vec.m = matrix.m
        vec.n = matrix.n
        vec.rows = matrix.rows
        return vec


