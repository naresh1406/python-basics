# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root is None:
            return 0
        left_height = self.height(root.left)
        right_height = self.height(root.right)

        left_diameter = self.diameterOfBinaryTree(root.left)
        right_diameter = self.diameterOfBinaryTree(root.right)

        return max(left_height + right_height, left_diameter, right_diameter)

    def height(self, root: TreeNode) -> int:
        if root is None:
            return 0
        left_height = self.height(root.left)
        right_height = self.height(root.right)

        return max(left_height, right_height) + 1


def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    res = Solution().diameterOfBinaryTree(root)
    print(res)


if __name__ == '__main__':
    main()
