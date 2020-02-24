# a binary tree with operations
from DataStructures.stack import *
from Other import globals
from DataStructures.mySet import mySet

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
    if tree is None:
        return None
    if tree.left is None and tree.right is None:
        print(tree.data)

    left = printTree(tree.left)
    right = printTree(tree.right)

    if tree.data == "&&":
        print("&&")
    elif tree.data == "||":
        print("||")
    elif tree.data == "!":
        print("!")

def evaluateTree(tree):
    if tree is None:
        return None
    if tree.left is None and tree.right is None:
        value = globals.trie.isWord(tree.data)
        if value[0]:
            tempSet = mySet()
            for paths in value[1].wordShowing:
                tempSet.add(paths)
            return tempSet
        else:
            return mySet()

    left_tree = evaluateTree(tree.left)
    right_tree = evaluateTree(tree.right)

    if tree.data == "&&":
        return left_tree.__and__(right_tree)
    elif tree.data == "||":
        return left_tree.__or__(right_tree)
    elif tree.data == "!":
        return left_tree.komlpement(globals.listEl)
