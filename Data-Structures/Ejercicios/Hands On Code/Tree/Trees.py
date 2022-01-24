class TreeNode:
    def __init__(self, data):
        self.data = data 
        self.children=[]
        self.parent= None 
   
    def add_child(self,child):
        child.parent = self
        self.children.append(child)

    def print_tree(self):
        spaces='   '*self.get_level() 
        print(spaces + self.data)
        if self.children:   
            for child in self.children:
                child.print_tree()

    def get_level(self):
        level = 0 
        p = self.parent
        while p:
            level += 1
            p=p.parent
        return level
    
def build_product_tree():
    root = TreeNode('David Herrero (CEO)')

    software = TreeNode('Adrian Fernandez-Vaillo (Analista)')
    software.add_child(TreeNode('Daniel Doral (Diseñador Web)'))
    software.add_child(TreeNode('Pablo Pereira (Diseñador Web)'))
    software.add_child(TreeNode('Mario Galisteo (Desarrollador Android / IOS)'))
    
    design = TreeNode('Galo Martin (Concept Artist)')
    design.add_child(TreeNode('Pablo Castillo (Diseñador Grafico)'))
    design.add_child(TreeNode('Elena Martin (Diseñadora Grafica)'))
    design.add_child(TreeNode('Pedro Garcia (Animador 3D)'))

    sound = TreeNode('Beyond Pandara (Grupo Musical)')
    sound.add_child(TreeNode('Gonzalo Armin (Cantante / Compositor)'))
    sound.add_child(TreeNode('Mario Galisteo (Guitarrista)'))
    sound.add_child(TreeNode('Pablo Pereira (Violinista / Compositor)'))
    sound.add_child(TreeNode('Carlos Muñoz (Productor / Pianista)'))

    root.add_child(software)
    root.add_child(design)
    root.add_child(sound)
    return root 

if __name__ == '__main__':
    root = build_product_tree()
    root.print_tree()
    print(root.get_level())
    pass
