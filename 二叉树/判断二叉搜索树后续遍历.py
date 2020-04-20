class Solution:
    '''
    输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
    如果是则输出Yes,否则输出No。
    假设输入的数组的任意两个数字都互不相同。

    思路： 1、判断输入为空、二叉树只有左子树、二叉树只有右子树的情况 
        2、使用index分割左右子树 
        3、使用递归判断左右子树是否为后序遍历
    '''
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if len(sequence) <= 0:
            return False
        root = sequence[-1]
        length = len(sequence)
        if min(sequence)>root or max(sequence)<root:
            return True #二叉树只有一个子树的情况下是后序遍历

        index = 0
        for i in range(length-1): #用index分割左右子树
            index = i
            if sequence[i] > root:
                break 
        #由于默认sequence[index]>root所以可以从index+1开始
        for j in range(index+1 ,length-1):
            if sequence[j] < root:
                return False

        left = True
        right = True
        if index > 0: #存在左子树，递归左子树
            left = self.VerifySquenceOfBST(sequence[:index])
        if index < length-1: #存在右子树，递归右子树
            right = self.VerifySquenceOfBST(sequence[index:length-1])
        return left&right #只有当左右子树都为后序遍历时，结果为后序遍历
