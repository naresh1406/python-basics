from typing import List


class Solution:

    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        n = len(s)
        count = 0
        for i in range(len(shift)):
            if shift[i][0] == 0:
                count += shift[i][1]
            else:
                count -= shift[i][1]

        if count > 0:
            s = s[count % n:] + s[:count % n]
        else:
            count = -count
            s = s[n - count % n:] + s[:n - count % n]

        return s


def main():
    print(Solution().stringShift("abc", [[0, 1], [1, 2]]))
    print(Solution().stringShift("abcdefg", [[1, 1], [1, 1], [0, 2], [1, 3]]))
    print(Solution().stringShift("abcdefg", [[1, 1], [1, 1], [0, 2], [1, 3]]))


if __name__ == '__main__':
    main()
