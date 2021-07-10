"""
Develop Rectangle class with following content:
    2 private fields type of float `side_a` and `side_b` (sides А and В of the rectangle);
    One constructor with two optional parameters a and b (parameters specify rectangle sides). Side А of a rectangle
    defaults to 4, side В - 3. Raise ValueError if received parameters are less than or equal to 0;
    Method `get_side_a`, returning value of the side А;
    Method `get_side_b`, returning value of the side В;
    Method `area`, calculating and returning the area value;
    Method `perimeter`, calculating and returning the perimeter value;
    Method `is_square`, checking whether current rectangle is square or not. Returns True if the shape is square and
    False in another case;
    Method `replace_sides`, swapping rectangle sides.

Develop class ArrayRectangles, in which declare:
    Private attribute `rectangle_array` (list of rectangles);
    One constructor that creates a list of rectangles with length `n` filled with `None` and that receives an
    arbitrary amount of objects of type `Rectangle` or a list of objects of type `Rectangle` (the list must be
    unpacked inside the constructor so that there will be no nested arrays). If both objects and length are passed,
    at first creates a list with received objects and then add the required number of Nones to achieve the
    desired length. If `n` is less than the number of received objects, the length of the list will be equal to the
    number of objects;
    Code like ArrayRectangles(Rectangle(),[Rectangle(),Rectangle()]) should be valid;
    Method `add_rectangle` that adds a rectangle of type `Rectangle` to the array on the nearest free place and
    returning True, or returning False, if there is no free space in the array;
    Method `number_max_area`, that returns order number (index) of the first rectangle with the maximum area value
    (numeration starts from zero);
    Method `number_min_perimeter`, that returns order number (index) of the first rectangle with the minimum area value
    (numeration starts from zero);
    Method `number_square`, that returns the number of squares in the array of rectangles
"""


class Rectangle:

    def __init__(self, a: float = 4.0, b: float = 3.0):
        self.__side_a = a
        self.__side_b = b
        if self.__side_a <= 0 or self.__side_b <= 0:
            raise ValueError

    @property
    def side_a(self):
        return self.__side_a

    @property
    def side_b(self):
        return self.__side_b

    def get_side_a(self):
        return self.__side_a

    def get_side_b(self):
        return self.__side_b

    def area(self):
        area = self.__side_a * self.__side_b
        return area

    def perimeter(self):
        perimeter = 2 * self.__side_a + 2*self.__side_b
        return perimeter

    def is_square(self):
        if self.__side_a == self.__side_b:
            return True
        return False

    def replace_sides(self):
        self.__side_a , self.__side_b = self.__side_b, self.__side_a


class ArrayRectangles(Rectangle):

    def __init__(self, *args, n: int = 0):
        super().__init__()
        self.n = n
        self.__rectangle_array = []
        if self.n and len(args) > 0:
            self.__rectangle_array = [obj for obj in args]
            if self.n > len(self.__rectangle_array):
                for i in range(n-len(self.__rectangle_array)):
                    self.__rectangle_array.append(None)
        if len(args) == 0:
            self.list_of_rectangles = [None for _ in range(n)]

    def add_rectangle(self):
        pass

    def number_max_area(self):
        return max([rectangle.area() for rectangle in self.__rectangle_array])

    def number_min_perimeter(self):
        return min([rectangle.perimeter() for rectangle in self.__rectangle_array])

    def number_square(self):
        count = 0
        for rectangle in self.__rectangle_array:
            if rectangle.is_square():
                count += 1
        return count
