from typing import List


class Solution:
    def countBits(self, num: int) -> List[int]:
        a = [0] * (num + 1)

        for i in range(num + 1):
            if i % 2 == 0:
                a[i] = a[i // 2]
            else:
                a[i] = a[i // 2] + 1

        return a

    def countBitsAnding(self, num: int) -> List[int]:
        a = [0] * (num + 1)

        for i in range(num + 1):
            n = i
            count = 0
            while n > 0:
                n = n & (n - 1)
                count += 1
            a[i] = count

        return a


def main():  # main function to initialize instance and call methods
    print(Solution().countBits(5))
    print(Solution().countBitsAnding(5))


if __name__ == '__main__':  # to run the main function
    main()
