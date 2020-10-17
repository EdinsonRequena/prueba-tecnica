class Triangle:
    '''
    returns the area of ​​a triangle when its vertices A and B are equal
    '''
    def __init__(self, a, b, c):
        '''
        :type a: int
        :type b: int
        :type c: int
        :rtype: None
        '''
        self.a = a
        self.b = b
        self.c = c


    def execute(self):
        '''
        :rtype: str
        :rtype opetation: method
        '''
        if self.a != self.b:
            print('Vertices A and B are not equal')
        else:
            self.operation()


    def operation(self):
        '''
        :type base: int
        :type altura: int
        :rtype area: int
        '''
        base = self.c
        height = self.b
        area = (base*height) / 2

        print(area)


def main():
    '''
    :type a: int
    :type b: int
    :type c: int
    rtype triangle: object
    '''
    a = int(input('Vertice A: '))
    b = int(input('Vertice B: '))
    c = int(input('Vertice C: '))

    triangle = Triangle(a,b,c)
    triangle.execute()

if __name__ == "__main__":
    main()
