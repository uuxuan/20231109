def output(a, b):
    square = a ** 2
   
    def addition(a, b):
        return a + b
    
    add = addition(a, b)
    return add + 5

result = output(5, 10)
print(result)