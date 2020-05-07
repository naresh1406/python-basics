class Solution:
    def checkValidString(self, s):
        return self.checkValidStringUtil(s, 0, 0)

    def checkValidStringUtil(self, s, index, balanced):
        if balanced < 0:
            return False
        if index == len(s):
            return balanced == 0
        if s[index] == '(':
            return self.checkValidStringUtil(s, index + 1, balanced + 1)
        elif s[index] == ')':
            return self.checkValidStringUtil(s, index + 1, balanced - 1)
        else:
            return (self.checkValidStringUtil(s, index + 1, balanced) or
                    self.checkValidStringUtil(s, index + 1, balanced + 1) or
                    self.checkValidStringUtil(s, index + 1, balanced - 1))


def main():  # main function to initialize instance and call methods
    print(Solution().checkValidString("()"))
    print(Solution().checkValidString("(*)"))
    print(Solution().checkValidString("(*))"))
    print(Solution().checkValidString("*)("))


if __name__ == '__main__':  # to run the main function
    main()
