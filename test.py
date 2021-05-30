def helper(node, lower=float("-inf"), upper=float("inf")):
 
    if not node:
        return "uhu"
    
    val = node
    if val <= lower or val >= upper:
        print("here")
        return "yoo"
    
    if not helper(node, val, upper):
        print("there")
        return "booo"
        
    

print(helper(10))

