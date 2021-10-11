# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def traverse(self, l, dep):
        self.maxdep = max(self.maxdep, dep)

        for e in l:
            if e.isInteger():
                v = e.getInteger()
                self.sum += v
                self.sumdep += dep * v
            else:
                self.traverse(e.getList(), dep + 1)

    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        self.sum = 0
        self.sumdep = 0
        self.maxdep = 0
        self.traverse(nestedList, 0)
        return (self.maxdep + 1) * self.sum - self.sumdep
