class Math:
    PI = 22 / 7

    @staticmethod
    def min(x, y):
        if x < y:
            return x
        else:
            return y

    @staticmethod
    def max(x, y):
        if x > y:
            return x
        else:
            return y

    @staticmethod
    def abs(x):
        if x < 0:
            return -x
        else:
            x

    @staticmethod
    def square(x):
        return x * x

    @staticmethod
    def gcd(x, y):
        if y == 0:
            return x
        return Math.gcd(y, x % y)


print(Math.PI)
print(Math.min(2, 3))
print(Math.max(2, 3))
print(Math.abs(-2))
print(Math.square(2))
print(Math.gcd(2, 3))
