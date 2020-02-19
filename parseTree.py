# a binary tree with operations
from stack import *

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def createParseTree(postfixNotation):
    postfixNotation = postfixNotation.split()
    tempStack = Stack()

    for word in postfixNotation:
        if word != "&&" and word != "||" and word != "!":
            # kreiranje novog cvora jer je trenutni token
            # rec za pretragu (levo ili desno dete)
            tempNode = TreeNode(word)
            tempStack.push(tempNode)
            # stavljamo na stek da bismo mogli kasnije
            # da koristimo za skupovne operacije

        else:
            if word != "!":
                tempNode = TreeNode(word)
                tempNode.right = tempStack.pop()
                tempNode.left = tempStack.pop()
            else:
                tempNode = TreeNode(word)
                tempNode.left = tempStack.pop()

            tempStack.push(tempNode)

    return tempStack.pop()

def printTree(tree):
    root = tree
    print(tree.data)

    while tree.left is not None:
        print(tree.left.data)
        tree = tree.left
    tree = root
    while tree.right is not None:
        print(tree.right.data)
        tree = tree.right
