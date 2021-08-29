import random


class Matrix(object):

    def __init__(self, m, n, init=True):
        if init:
            self.rows = [[0] * n for x in range(m)]
        else:
            self.rows = []
        self.m = m
        self.n = n

    def __getitem__(self, idx):
        return self.rows[idx]

    def __setitem__(self, idx, item):
        self.rows[idx] = item

    def __str__(self):
        s = '\n'.join([' '.join([str(item) for item in row]) for row in self.rows])
        return s + '\n'

    def __repr__(self):
        s = str(self.rows)
        rank = str(self.get_rank())
        rep = "Matrix: \"%s\", rank: \"%s\"" % (s, rank)
        return rep

    def get_column_num(self):
        return self.n

    def get_row_num(self):
        return self.m

    def min(self):
        min_list = min(self.rows, key=min)
        return min(min_list)

    def max(self):
        min_list = max(self.rows, key=max)
        return max(min_list)

    def transpose(self):
        self.m, self.n = self.n, self.m
        self.rows = [list(item) for item in zip(*self.rows)]

    def get_transpose(self):
        m, n = self.n, self.m
        mat = Matrix(m, n)
        mat.rows = [list(item) for item in zip(*self.rows)]

        return mat

    def get_rank(self):
        return self.m, self.n

    def __eq__(self, mat):
        return mat.rows == self.rows

    def __add__(self, mat):
        if self.get_rank() != mat.get_rank():
            raise Exception("Trying to add matrixes of varying rank!")

        ret = Matrix(self.m, self.n)

        for x in range(self.m):
            row = [sum(item) for item in zip(self.rows[x], mat[x])]
            ret[x] = row

        return ret

    def __sub__(self, mat):
        if self.get_rank() != mat.get_rank():
            raise Exception("Trying to add matrixes of varying rank!")

        ret = Matrix(self.m, self.n)

        for x in range(self.m):
            row = [item[0] - item[1] for item in zip(self.rows[x], mat[x])]
            ret[x] = row

        return ret

    def __mul__(self, mat):
        if isinstance(mat, Matrix):
            matm, matn = mat.get_rank()

            if self.n != matm:
              raise Exception("Matrices cannot be multipled!")

            mat_t = mat.get_transpose()
            mulmat = Matrix(self.m, matn)

            for x in range(self.m):
                for y in range(mat_t.m):
                    mulmat[x][y] = sum([item[0] * item[1] for item in zip(self.rows[x], mat_t[y])])
        else:
            mulmat = Matrix(self.m,self.n)

            for x in range(self.m):
                for y in range(self.n):
                    mulmat[x][y] = self[x][y] * mat

        return mulmat


    @classmethod
    def _makeMatrix(cls, rows):

        m = len(rows)
        n = len(rows[0])
        if any([len(row) != n for row in rows[1:]]):
            raise Exception("inconsistent row length")
        mat = Matrix(m,n, init=False)
        mat.rows = rows

        return mat


    @classmethod
    def makeRandom(cls, m, n, low=0, high=10):
        obj = Matrix(m, n, init=False)
        for x in range(m):
            obj.rows.append([random.randrange(low, high) for i in range(obj.n)])

        return obj

    @classmethod
    def makeZero(cls, m, n):
        rows = [[0] * n for x in range(m)]
        return cls.fromList(rows)


    @classmethod
    def fromList(cls, listoflists):
        rows = listoflists[:]
        return cls._makeMatrix(rows)

    @classmethod
    def fromVector(cls, vec):
        return cls.fromList([i for i in vec.rows])