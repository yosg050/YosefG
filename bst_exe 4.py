
class Node:
    def __init__(self, x):
        self.x = x
        self.right = None
        self.left = None

class BST:
    def __init__(self, html_file="bst.html"):
        self.root = None
        self.html_file = html_file

    def _css(self, file):
        file.write("<style>\n"
          "* {\n  margin: 0; padding: 0; font-family: Arial;\n}\n"
          ".tree {\n  display: flex; justify-content: center;\n}\n"
          ".tree ul {\n  padding-top: 20px; position: relative;\n}\n"
          ".tree li {\n  float: left; text-align: center; list-style-type: none;\n"
          "  position: relative; padding: 20px 5px 0 5px;\n}\n"
          ".tree li::before, .tree li::after {\n  content: '';\n"
          "  position: absolute; top: 0; right: 50%;\n"
          "  border-top: 1px solid #777; width: 50%; height: 20px;\n}\n"
          ".tree li::after {\n  right: auto; left: 50%; border-left: 1px solid #777;\n}\n"
          ".tree li:only-child::after, .tree li:only-child::before {\n  display: none;\n}\n"
          ".tree li:first-child::before, .tree li:last-child::after {\n  border: 0 none;\n}\n"
          ".tree li:last-child::before {\n  border-right: 1px solid #777;\n}\n"
          ".tree ul ul::before {\n  content: ''; position: absolute; top: 0; left: 50%;\n"
          "  border-left: 1px solid #777; width: 0; height: 20px;\n}\n"
          ".node {\n  border: 1px solid #777; padding: 10px 20px; color: #666;\n"
          "  font-size: 12px; display: inline-block;\n}\n"
          ".null {\n  border: none; border-top: 1px solid #777; padding: 10px 20px;\n"
          "  color: #666; display: inline-block;\n}\n"
          "</style>\n")

    def _html(self, file, node):
        file.write("<li>\n")

        if not node:
            file.write("<span class=\"null\"></span>\n")
            file.write("</li>\n")
            return
        
        file.write(f"<span class=\"node\">{node.x}</span>\n")
        file.write("<ul>\n")
        self._html(file, node.left)
        self._html(file, node.right)
        file.write("</ul>\n")
        file.write("</li>\n")

    def html(self):
        with open(self.html_file, "w") as file:
            file.write("<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n")
            self._css(file)
            file.write("</head>\n<body>\n<div class=\"tree\">\n<ul>\n")
            self._html(file, self.root)
            file.write("</ul>\n</div>\n</body>\n</html>\n")
        print(f"BST printed to {self.html_file}")

    def add_node(self, node):
        if not self.root:
            self.root = node
            return
        temp = self.root
        while True:
            if node.x <= temp.x:
                if not temp.left:
                    temp.left = node
                    break
                temp = temp.left
            else:
                if not temp.right:
                    temp.right = node
                    break
                temp = temp.right

    def _max_node(self, node):
        if not node or not node.right:
            return node
        max_node = self._max_node(node.right)
        return max_node

    def max_node(self):
        node =  self._max_node(self.root)
        if node:
            print(node.x)
        else:
            print("Empty Tree")     

    def find_node(self, x):
        temp = self.root
        prev = temp
        while temp:
            if x == temp.x:
                return prev
            if x < temp.x:
                if not temp.left:
                    return False
                prev = temp
                temp = temp.left
                continue
            if x > temp.x:
                if not temp.right:
                    return False
                prev = temp
                temp = temp.right
                continue

    def _depth(self, temp):
        if temp is None:
            return 0
        return max(self._depth(temp.left), self._depth(temp.right)) + 1
    
    def depth(self):
        depth_print = self._depth(self.root)
        print("maximum depth:", depth_print)

    def _count_nodes(self, node, num):
        if not node:
            return num
        
        num += 1
        if node.left:
            num = self._count_nodes(node.left, num) 
        if node.right:
            num = self._count_nodes(node.right, num)
        return num

    def count_nodes(self):
        sum = self._count_nodes(self.root, 0)
        print("number of nodes: ", sum)

    def remove_node(self, x):
        temp = self.root
        prev = temp
        while temp:
            if x < temp.x:
                if not temp.left:
                    return False
                prev = temp
                temp = temp.left
                continue
            if x > temp.x:
                if not temp.right:
                    return False
                prev = temp
                temp = temp.right
                continue
            # Found!
            if not temp.left and not temp.right:
                # temp has no sub trees
                if prev.left is temp:
                    prev.left = None
                elif prev.right is temp:
                    prev.right = None
                else:
                    self.root = None
            elif temp.left and not temp.right:
                # temp has only a left sub tree
                if prev.left is temp:
                    prev.left = temp.left
                elif prev.right is temp:
                    prev.right = temp.left
                else:
                    self.root = temp.left
            elif not temp.left and temp.right:
                # temp has only a right sub tree
                if prev.left is temp:
                    prev.left = temp.right
                elif prev.right is temp:
                    prev.right = temp.right
                else:
                    self.root = temp.right
            else:
                # temp has two sub trees...
                # get the max from the left sub tree
                max_node = self._max_node(temp.left)
                # override x with max_node.x
                temp.x = max_node.x
                # now search and remove the node with x = max_node.x
                # that node does not have a right sub tree
                x = max_node.x
                prev = temp
                temp = temp.left
                continue
            # Found
            return True
        # Empty tree
        assert self.root is None
        return False
   
    def _print_tree(self, node):
        if not node:
            return
        self._print_tree(node.left)
        print(node.x, end=" ")
        self._print_tree(node.right)
        
    def print_tree(self):
        self._print_tree(self.root)
        print("")

    def _print_reverse(self, node):
        if not node:
            return
        self._print_reverse(node.right)
        print(node.x, end=" ")
        self._print_reverse(node.left)        

    def print_reverse(self):
        self._print_reverse(self.root)
        print("")
        
bst = BST()
x_list = [4, 6, 9, 11, 13, 5, 24, 2, 5, 7, 8, 3, 15, 16, 6]
for i in x_list:
    bst.add_node(Node(i))


while True:
    op = input("Enter operation: ").split()
    try:
        if op[0] == "end":
            break
        elif op[0] == "add":
            bst.add_node(Node(int(op[1])))
        elif op[0] == "remove":
            bst.remove_node(int(op[1]))
        elif op[0] == "max":
            node = bst.max_node()
        elif op[0] == "find":
            node = bst.find_node(int(op[1]))
            print(node,"\n",node.x)
        elif op[0] == "depth":
            bst.depth()
        elif op[0]== "count":
            bst.count_nodes()
        elif op[0] == "print":
            if op[1] == "1":
                bst.print_tree()
            elif op[1] ==  "reverse" or op[1] == "2": 
                bst.print_reverse()
        elif op[0] == "html":
            bst.html()
        else:
            raise
    except:
        print("Invalid Operation!")