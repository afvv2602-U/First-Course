from tkinter.tix import Tree


class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None
    
    def add_child(self,child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level +=1
            p = p.parent
        return level

    def print_tree(self):
        print(self.data)
        for child in self.children:
            print(child.data)
        # spaces = ' ' * self.get_level() * 3
        # prefix = spaces + '|--' if self.parent else ""
        # print(prefix + self.data)
        # if self.children:
        #     for child in self.children:
        #         child.print_tree()

    
def build_product_tree():
    root = TreeNode('Nilupul (CEO)')

    cto = TreeNode('Chinmay (CTO)')
    vishwa = TreeNode ('Vishwa (Infrastructure head)')
    # vishwa.add_child(TreeNode('Dhaval (Cloud Manager)'))
    # vishwa.add_child(TreeNode('Abhijit (App Manager)'))
    cto.add_child(TreeNode(vishwa))

    hr = TreeNode('Gels (HR Head)')
    # hr.add_child(TreeNode('Peter (Recruitment Manager)'))
    # hr.add_child(TreeNode('Policy Manager'))

    root.add_child(TreeNode(cto))
    root.add_child(TreeNode(hr))
    return root


if __name__ == '__main__':
    root = build_product_tree()
    root.print_tree()
    pass
