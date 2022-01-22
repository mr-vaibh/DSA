class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
    
    def add_child(self, child):
        child.parent = self
        self.children.append(child)
    
    def get_level(self):
        level = 1
        while self.parent:
            self = self.parent
            level += 1
        return level
    
    def print_tree(self, level=None):
        print(self.data)

        if level < self.get_level():
            return
        
        for child in self.children:
            spaces = ' ' * self.get_level() * 4
            print(spaces + '|--', end='')
            child.print_tree(level)


root = TreeNode('Electronics')

laptop = TreeNode('Laptop')
laptop.add_child(TreeNode('Mac'))
laptop.add_child(TreeNode('Lenovo'))
laptop.add_child(TreeNode('Dell'))
laptop.add_child(TreeNode('HP'))

smartphone = TreeNode('Smart Phone')
smartphone.add_child(TreeNode('iPhone'))
smartphone.add_child(TreeNode('Vivo'))
smartphone.add_child(TreeNode('OnePlus'))
smartphone.add_child(TreeNode('Redmi'))

tv = TreeNode('Television')
tv.add_child(TreeNode('Samsung'))
tv.add_child(TreeNode('Sony'))
tv.add_child(TreeNode('LG'))
tv.add_child(TreeNode('Toshiba'))

root.add_child(laptop)
root.add_child(smartphone)
root.add_child(tv)


root.print_tree(2)