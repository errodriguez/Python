#! /usr/bin/env python

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def getHeight(self,root):
        stack = [root]
        graph = {id(root):{'depth':0}}
        node = root
        while node:
            next_node = None
            for child in [c for c in (node.right, node.left) if c is not None]:
                stack.append(child)
                graph[id(child)] = {'depth':graph[id(node)]['depth'] + 1}
                next_node = child
            if next_node is None and len(stack):
                next_node = stack.pop()
            node = next_node
        return max([item['depth'] for item in list(graph.values())])
                   
          # return 1 + max(self.getHeight(node.left),self.getHeight(node.right)) if node else -1  

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height)