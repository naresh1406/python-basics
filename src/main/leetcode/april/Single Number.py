class Solution:
    def singleNumber(self, nums) -> int:
        x = 0
        for i in range(len(nums)):
            x = x ^ nums[i]
        return x


def main():
    print(Solution().singleNumber([1, 2, 2]))


if __name__ == '__main__':
    main()
