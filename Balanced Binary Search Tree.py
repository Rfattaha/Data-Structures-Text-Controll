# Read the text file and store it to Array
import time
st = time.time()

f = open("words.txt", "r")

fileRead = f.read()

text_Arr = fileRead.split("\n")

f.close()

text = "Me spll rite"

text = text.split()


i = 0
while i < len(text):
    text[i] = text[i].lower()
    i += 1

startPoint = len(text_Arr) / 2
startPoint = round(startPoint)


Bbst_st = time.time()

class rootNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def insert(Node,data):
    if Node == None:
        return rootNode(data)
    while Node != None:
       if data < Node.data and Node.left == None:
           Node.left = rootNode(data)
           break
       if  data < Node.data and Node.left != None:
           Node = Node.left
           pass
       if data > Node.data and Node.right == None:
           Node.right = rootNode(data)  
           Node = Node.right
           break
       if data > Node.data and Node.right != None:
           Node = Node.right
           pass
    return True

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)


def search(Node,data):
    flag = 0
    while Node != None:
        if data == Node.data:
            flag = 1
            break
        if Node.right == None and Node.left == None:
            break
        if data < Node.data:
            Node = Node.left
            continue
        if data > Node.data:
            Node = Node.right
            continue
    if flag > 0 :
        print(data," is spelled correctly")
    else: 
        print(data," is misspelled")   

root = None

leftSide = startPoint - 1
rightSide = startPoint + 1
root = insert(root, text_Arr[startPoint])
while leftSide > 0 and rightSide < len(text_Arr):
    if leftSide >= 0:
        insert(root,text_Arr[leftSide])
        leftSide -= 1
    if rightSide < len(text_Arr):
        insert(root,text_Arr[rightSide])
        rightSide +=1
    
print()

for i in text:
    search(root,i)

print()

time.sleep(3)

Bbst_et = time.time()

Bbst_elapsed_time = Bbst_et - Bbst_st - 3

print('Execution time:', Bbst_elapsed_time, 'seconds')