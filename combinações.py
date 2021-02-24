#This is a progrim which, given a list of items, will calculate and display all the possible combinations of a given size
import copy
from collections import OrderedDict
class item:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return str(self.name)
class comb:
    def __init__(self):
        self.items=[]
    def __str__(self):
        string='{ '
        for x in self.items:
            string += str(x)+", "
        string=string.rstrip(", ")+" }"
        return string
    def adde(self, item):
        self.items.append(item)

def printconj(conj):
    string = "combs: "
    for x in conj:
        string += str(x) + "+"
    string = string.rstrip("+")
    print(string)
            
size = int(input("Qual o tamanho das combinações?\n"))
elements, combs = [], []#elements is the list of items for the combinations, while combs is the matrix for the sake of calculating the combinations
combs.append([])
print("Agora insira os elementos das combinações:")
while True:
    try:
        elements.append(item(input()))
    except EOFError:
        break
n = len(elements)
#size is the number of columns necessary to calculate the combinations
if size < n: size = n - size
else: size = 0
#now to create the matrix with the necessary size
for i in range(n+1):
    combs.append([])
    for j in range(size+1):
        combs[i].append([])
for j in range(size+1):
    for i in range(j,n+1):
        if i > j:#if it's below the main diagonal
            combs[i][j] = copy.deepcopy(combs[i-1][j])#the current cell receives a copy of the cell directly above
            if not combs[i][j]:
                combs[i][j].append(comb())#otherwise, it receives an empty combination
            for k in combs[i][j]:
                k.adde(elements[i-1])#now every combination in that cell will have the appropriate element concatenated with them
        if j > 0:
            combs[i][j] += copy.deepcopy(combs[i-1][j-1])#in the end, the cell will have all the combinations from the cell diagonal to it added to it
printconj(combs[n][size])#to display the combinations, print the combinations of the cell in the last line and column

