#find if both tree are simiar



def isSimilar(root1,root2):
    if root1==NULL and root2==NULL:
        return True
    if root1!=NULL or root2!=NULL:
        return False
    if root1.data==root2.data and isSimilar(root1.left,root2.left) and isSimilar(root1.right,root2.right)
        return True
    
    
