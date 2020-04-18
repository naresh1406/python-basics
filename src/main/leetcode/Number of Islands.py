class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0

        r = len(grid)
        c = len(grid[0])
        count = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] is "1":
                    self.dfs(grid, i, j, r, c)
                    count += 1

        return count

    def dfs(self, grid, i, j, r, c):
        if 0 <= i < r and 0 <= j < c and grid[i][j] == "1":
            grid[i][j] = '#'
            self.dfs(grid, i + 1, j, r, c)
            self.dfs(grid, i - 1, j, r, c)
            self.dfs(grid, i, j + 1, r, c)
            self.dfs(grid, i, j - 1, r, c)
        else:
            return


def main():  # main function to initialize instance and call methods
    # print(Solution().numIslands(
    #     [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"],
    #      ["0", "0", "0", "0", "0"]]))  # 1
    #
    # print(Solution().numIslands(
    #     [["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"],
    #      ["0", "0", "0", "1", "1"]]))  # 3

    print(Solution().numIslands(
        [["0", "1", "0"], ["1", "0", "1"], ["0", "1", "0"]]  # 4
    ))


if __name__ == '__main__':  # to run the main function
    main()
