# This is a python program to find permutation and combination

# Function definition to find factorial

def fact(x):
    
    p = 1
    
    for i in range(1, x + 1):
        p *= i
    return p

# Function definition to find combination
    
def nCr(n, r):
    
    ncr = fact(n) // (fact(r) * fact(n - r))
    
    print("\n" + str(n) + "C" + str(r) + ' = ' + str(ncr) + "\n")
    
# Function definition to find permutation
    
def nPr(n, r):
    
    npr = fact(n) // fact(n - r)
    
    print(str(n) + "P" + str(r) + ' = ' + str(npr) + "\n")
    

# Function call to find combination
    

nCr(11,7)

# Function call to find permutation

nPr(11,7)
