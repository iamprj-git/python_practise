import queue
class node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
    def insert(self,value):
        if value <=self.value:
            if self.left is None:
                self.left=node(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right=node(value)
            else:
                self.right.insert(value)
   
   
    #for inorder traversal

'''def dfs(root,search_node):
    if root.value == search_node:
        return True
    elif root.left is not None:
        dfs(root.left,search_node)
    elif root.right is not None:
        dfs(root.right,search_node)'''

#to find parent node 

def queue_on_parent_Node(root):
    queue=[]
    def traverse(node,parent,is_left):
        if node is None:
            return 
        if is_left is True:
            queue.append(parent)
        
        traverse(node.left,node,True)
        if node.left is None:
            traverse(node.right,node,True)
        else:
            traverse(node.right,node,False)

    traverse(root,None,False)
    return queue
#remaining part
    '''def distance(self,root,root_node):
        #to check there is root_node or not:
        #to find node
        root=self.dfs(root,root_node)'''
    
            
root=node(5)
root.insert(7)
root.insert(4)
root.insert(2)
root.insert(8)
root.insert(6)
root.insert(9)
root.insert(1)
root.insert(3)
print("distance travelled by node for given target::")
'''if dfs(root,10) is True:
    print("there is node found :")
else:
    print("Not found:")'''
#printing parent_queue
parent_queue=queue_on_parent_Node(root)
while parent_queue:
    x = parent_queue.pop(0)
    print(x.value if x else None)