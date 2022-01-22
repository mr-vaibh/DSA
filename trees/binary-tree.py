class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def add_child(self, data):
        if data == self.data:
            return

        if data < self.data:
            # add in left
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinaryTreeNode(data)
        else:
            # add in right
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinaryTreeNode(data)
    
    def search(self, value):
        if self.data == value:
            return True
        
        # might be in left
        if value < self.data:
            if self.left:
                return self.left.search(value)
            else:
                return False
        
        # might be in right
        if value > self.data:
            if self.right:
                return self.right.search(value)
            else:
                return False

    def find_min(self):
        if self.left is None:
            return self.data
        
        return self.left.find_min()

    def find_max(self):
        if self.right is None:
            return self.data
        
        return self.right.find_max()

    def calculate_sum(self):
        # validate elements int or float
        if not (isinstance(self.data, int) or isinstance(self.data, float)):
            return None
        
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        
        return self.data + left_sum + right_sum
    
    def delete(self, value):
        if self.data > value:
            if self.left:
                self.left = self.left.delete(value)
        elif self.data < value:
            if self.right:
                self.right = self.right.delete(value)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            
            min_value = self.right.find_min()
            self.data = min_value
            self.right = self.right.delete(min_value)
            
            # Same functionality
            # max_value = self.left.find_min()
            # self.data = max_value
            # self.left = self.left.delete(max_value)

        return self

    def in_order_traversal(self):
        elements = []

        # visit left tree
        if self.left:
            elements += self.left.in_order_traversal()

        # visit root
        elements.append(self.data)

        # visit right tree
        if self.right:
            elements += self.right.in_order_traversal()

        return elements
    
    def post_order_transversal(self):
        elements = []

        # visit left tree
        if self.left:
            elements += self.left.post_order_transversal()
        
        # visit right tree
        if self.right:
            elements += self.right.post_order_transversal()
        
        # visit root
        elements.append(self.data)

        return elements
    
    def pre_order_transversal(self):
        elements = []

        # visit root
        elements.append(self.data)

        # visit left tree
        if self.left:
            elements += self.left.pre_order_transversal()
        
        # visit right tree
        if self.right:
            elements += self.right.pre_order_transversal()
        
        return elements

def build_tree(array):
    root = BinaryTreeNode(array[0])

    for i in array:
        root.add_child(i)
    
    return root

numbers = [34, 46, 43, 6, 575, 4, 7, 54, 57, 98, 98, 98, 98]
countries = ['India', 'UK', 'USA', 'Singapore', 'Pakistan', 'Germany', 'Australia', 'Australia']

numbers_tree = build_tree(numbers)
countries_tree = build_tree(countries)

print(numbers_tree.in_order_traversal())
print(numbers_tree.post_order_transversal())
print(numbers_tree.pre_order_transversal())
print(numbers_tree.search(34))
print(numbers_tree.search(4))
print(numbers_tree.find_min())
print(numbers_tree.find_max())
print(numbers_tree.calculate_sum())
numbers_tree.delete(575)

print(countries_tree.in_order_traversal())
print(countries_tree.post_order_transversal())
print(countries_tree.pre_order_transversal())
print(countries_tree.search('India'))
print(countries_tree.search('UK'))
print(countries_tree.find_min())
print(countries_tree.find_max())
print(countries_tree.calculate_sum())
countries_tree.delete('USA')