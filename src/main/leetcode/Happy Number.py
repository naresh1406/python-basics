class Solution:
    def isHappy(self, n: int) -> bool:
        hash_set = set()
        while n not in hash_set:
            hash_set.add(n)
            x = n
            n = 0
            while x > 0:
                n += (x % 10) * (x % 10)
                x = (int)(x / 10)

        return n == 1


def main():  # main function to initialize instance and call methods
    print(Solution().isHappy(19))


if __name__ == '__main__':  # to run the main function
    main()
