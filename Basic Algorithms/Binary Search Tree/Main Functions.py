# данный класс является недееспособным с точки зрения добавления элементов,

class node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return 'Node [' + str(self.data) + ']'


# /* класс, описывающий само дерево */
class Tree:
    def __init__(self):
        self.root = None  # корень дерева

    # /* функция для добавления узла в дерево */
    def newNode(self, data):
        return node(data, None, None)

    # Дальше, все функции расширяют класс Tree.

    # /* функция для вычисления высоты дерева */
    def height(self, node):
        if node == None:
            return 0
        else:
            lheight = self.height(node.left)
            rheight = self.height(node.right)

            if lheight > rheight:
                return (lheight + 1)
            else:
                return (rheight + 1)

    #    /* функция для зеркального отражения дерева */
    def mirror_tree(self, node):
        if node.left and node.right:
            node.left, node.right = node.right, node.left
            self.mirror_tree(node.right)
            self.mirror_tree(node.left)
        else:
            if node.left == None and node.right:
                return self.mirror_tree(node.right)
            if node.right == None and node.left:
                return self.mirror_tree(node.left)

    #    /* функция для проверки наличия узла */
    def lookup(self, node, target):
        if node == None:
            return 0
        else:
            if target == node.data:
                return 1
            else:
                if target < node.data:
                    return self.lookup(node.left, target)
                else:
                    return self.lookup(node.right, target)

    # /* функция для вычисления ширины дерева */
    def get_max_width(self, root):
        maxWdth = 0
        i = 1
        width = 0;
        h = self.height(root)
        while (i < h):
            width = self.getWidth(root, i)
            if (width > maxWdth):
                maxWdth = width;
            i += 1
        return maxWdth;

    def getWidth(self, root, level):
        if root == None:
            return 0
        if level == 1:
            return 1
        elif level > 1:
            return self.getWidth(root.left, level - 1) + self.getWidth(root.right, level - 1)

    # /* функция для распечатки элементов на определенном уровне дерева */
    def printGivenLevel(self, root, level):
        if root == None:
            return
        if level == 1:
            print("%d " % root.data)
        elif level > 1:
            self.printGivenLevel(root.left, level - 1);
            self.printGivenLevel(root.right, level - 1);

    # /* функция для распечатки дерева */
    def printLevelOrder(self, root):
        h = self.height(self.root)
        i = 1
        while (i <= h):
            self.printGivenLevel(self.root, i)
            i += 1


# Сравнение бинарных деревьев Вынесите её за пределы класса только)

def sameTree(a, b):
    if a == None and b == None:
        return 1
    elif a and b:
        return (
                a.data == b.data and
                sameTree(a.left, b.left) and
                sameTree(a.right, b.right)
        )
    return 0


# Количество узлов в бинарном дереве
# Вычислить количество узлов в бинарном дереве также можно с помощью рекурсии.
# Хотя с точки зрения производительности и принципов ООП, правильнее встроить счетчик в сам объект.
def size(node):
    if node == None: return 0;
    return (size(node.left) + 1 + size(node.right));
