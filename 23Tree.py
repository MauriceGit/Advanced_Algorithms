#!/usr/bin/python
# -*- coding: utf-8 -*-


class Tree23:
    def __init__(self):
        # ([maxLeft, maxRight], [pointerLeftChild, pointerRightChild], elem)
        self.treeInstance = None

    def _isLeaf(self, tree):
        return tree[0] == []

    def _newLeaf(self, elem):
        return ([], [], elem)

    def _max(self, tree):
        if self._isLeaf(tree):
            return tree[2]
        return max(tree[0])

    def _nodeFromChildrenList(self, children):
        newNode = ([],[],0)
        for i in range(len(children)):
            newNode[0].append(self._max(children[i]))
            newNode[1].append(children[i])
        return newNode

    def _multipleNodesFromChildrenList(self, children):

        cLen = len(children)
        if cLen == 0:
            return [self._nodeFromChildrenList(children)]

        if cLen <= 3:
            return [self._nodeFromChildrenList(children)]

        if 4 <= cLen <= 6:
            half = cLen/2
            c1 = self._nodeFromChildrenList(children[:half])
            c2 = self._nodeFromChildrenList(children[half:])
            return [c1, c2]

        if 7 <= cLen <= 9:
            third = cLen/3
            c1 = self._nodeFromChildrenList(children[:third])
            c2 = self._nodeFromChildrenList(children[third:2*third])
            c3 = self._nodeFromChildrenList(children[2*third:])
            return [c1, c2, c3]

        print "should never get here."

    def _insertInto(self, tree, elem):
        biggest = -1
        subTree = -1
        for i in range(len(tree[0])):
            # smallest child bigger than elem
            if (subTree == -1 and tree[0][i] > elem) or (tree[0][i] > elem and tree[0][i] < tree[0][subTree]):
                subTree = i
            if tree[0][i] > biggest:
                biggest = i
        if subTree == -1:
            return biggest
        return subTree


    def _distributeFourChildren(self, c1, c2, c3, c4):
        child1 = ([], [], 0)
        child1[0].append(self._max(c1))
        child1[1].append(c1)
        child1[0].append(self._max(c2))
        child1[1].append(c2)

        child2 = ([], [], 0)
        child2[0].append(self._max(c3))
        child2[1].append(c3)
        child2[0].append(self._max(c4))
        child2[1].append(c4)

        newRoot = ([], [], 0)
        newRoot[0].append(self._max(child1))
        newRoot[1].append(child1)
        newRoot[0].append(self._max(child2))
        newRoot[1].append(child2)

        return newRoot

    def _insertRec(self, tree, elem):
        if self._isLeaf(tree):
            return [tree, self._newLeaf(elem)]
        subTree = self._insertInto(tree, elem)
        newChildren = self._insertRec(tree[1][subTree], elem)
        if len(newChildren[0]) == 1:
            tree[0][subTree] = self._max(newChildren[0])
            tree[1][subTree] = newChildren[0]
            return [tree]
        if len(tree[0]) == 2:
            tree[0][subTree] = self._max(newChildren[0])
            tree[1][subTree] = newChildren[0]
            tree[0].append(self._max(newChildren[1]))
            tree[1].append(newChildren[1])
            return [tree]

        del tree[0][subTree]
        del tree[1][subTree]
        tmpRoot = self._distributeFourChildren(tree[1][0], tree[1][1], newChildren[0], newChildren[1])

        return [tmpRoot[1][0], tmpRoot[1][1]]

    def insert(self, elem):

        if self.treeInstance == None:
            self.treeInstance = self._newLeaf(elem)
            return

        if self._isLeaf(self.treeInstance):
            newRoot = ([], [], 0)
            newChild = self._newLeaf(elem)
            newRoot[0].append(self.treeInstance[2])
            newRoot[1].append(self.treeInstance)
            newRoot[0].append(newChild[2])
            newRoot[1].append(newChild)
            self.treeInstance = newRoot
            return

        subTree = self._insertInto(self.treeInstance, elem)
        newChildren = self._insertRec(self.treeInstance[1][subTree], elem)

        if len(newChildren) == 1:
            self.treeInstance[0][subTree] = self._max(newChildren[0])
            self.treeInstance[1][subTree] = newChildren[0]
            return

        # we get two new children and have one old (subTree is overwritten).
        if len(self.treeInstance[0]) == 2:
            # overwrite old child
            self.treeInstance[0][subTree] = self._max(newChildren[0])
            self.treeInstance[1][subTree] = newChildren[0]
            # add new child
            self.treeInstance[0].append(self._max(newChildren[1]))
            self.treeInstance[1].append(newChildren[1])
            return

        # delete old child
        del self.treeInstance[0][subTree]
        del self.treeInstance[1][subTree]

        newRoot = self._distributeFourChildren(self.treeInstance[1][0], self.treeInstance[1][1], newChildren[0], newChildren[1])

        # set new root as global root
        self.treeInstance = newRoot

    def _deleteFrom(self, tree, elem):
        subTree = -1
        for i in range(len(tree[0])):
            # smallest child bigger or equal than elem
            if (subTree == -1 and tree[0][i] >= elem) or (tree[0][i] >= elem and tree[0][i] < tree[0][subTree]):
                subTree = i
        return subTree

    def _deleteRec(self, tree, elem):

        allLeaves = True
        for c in tree[1]:
            allLeaves = allLeaves and self._isLeaf(c)
        if allLeaves:
            newChildren = []
            for c in tree[1]:
                if c[2] != elem:
                    newChildren.append(c)
            return newChildren

        deleteFrom = self._deleteFrom(tree, elem)
        if deleteFrom == -1:
            return tree[1]

        oldChildren = tree[1][:deleteFrom] + tree[1][deleteFrom+1:]
        oldGrandchildren = []
        for c in oldChildren:
            for i in range(len(c[1])):
                oldGrandchildren.append(c[1][i])

        children = self._deleteRec(tree[1][deleteFrom], elem)

        nodes = self._multipleNodesFromChildrenList(oldGrandchildren + children)
        return nodes

    def delete(self, elem):

        if self.treeInstance == None or self._isLeaf(self.treeInstance) and self.treeInstance[2] == elem:
            self.treeInstance = None
            return

        children = self._deleteRec(self.treeInstance, elem)

        if len(children[0]) == 1:
            self.treeInstance = children[0]
            return

        self.treeInstance = self._nodeFromChildrenList(children)

    def _findInTree(self, tree, elem):
        if tree == None:
            return None
        if self._isLeaf(tree):
            if tree[2] == elem:
                return tree
            else:
                return None

        subTree = self._deleteFrom(tree, elem)

        return self._findInTree(tree[1][subTree], elem)

    def find(self, elem):
        return self._findInTree(self.treeInstance, elem)

    def _minmaxDepth(self, tree):
        if tree == None:
            return (0, 0)
        if self._isLeaf(tree):
            return (1, 1)

        depths = ([], [])

        for i in range(len(tree[1])):
            tmpDepth = self._minmaxDepth(tree[1][i])
            depths[0].append(tmpDepth[0]+1)
            depths[1].append(tmpDepth[1]+1)

        return (min(depths[0]), max(depths[1]))

    def depths(self):
        return self._minmaxDepth(self.treeInstance)

    def invariant(self):
        depths = self.depths()
        return depths[0] == depths[1]

    def _pprint(self, tree):
        if self._isLeaf(tree):
            print tree[2],
            return
        for i in range(len(tree[1])):
            self._pprint(tree[1][i])

    def pprint(self):
        print "Elements:",
        self._pprint(self.treeInstance)
        print ""

if __name__ == '__main__':

    tree = Tree23()

    print "Invariant:", tree.invariant()

    print "________________________ INSERT ___________________________"
    print "insert 4"
    tree.insert(4)
    print "insert 3"
    tree.insert(3)
    print "insert 5"
    tree.insert(5)
    print "insert 6"
    tree.insert(6)
    print "insert 7"
    tree.insert(7)
    tree.pprint()
    print "Invariant:", tree.invariant()

    print "________________________ FIND _____________________________"
    print "find 7"
    print tree.find(7)
    print "find 8"
    print tree.find(8)
    print "find 3"
    print tree.find(3)
    tree.pprint()
    print "Invariant:", tree.invariant()

    print "________________________ DELETE ___________________________"
    print "delete 5"
    tree.delete(5)
    print "delete 4"
    tree.delete(4)
    tree.pprint()
    print "delete 8"
    tree.delete(8)
    tree.pprint()
    print "delete 7"
    tree.delete(7)
    tree.pprint()

    print "Invariant:", tree.invariant()





