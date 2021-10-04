#WRITE YOUR CODE IN THIS FILE
def hasL(w):
    for i in range(0, len(w)):
        print(w[i])
        if w[i] == "l":
            return True
    return False
        

print(hasL("alabama"))