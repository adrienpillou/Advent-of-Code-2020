def get_combinations(word:list):
    combinations = []
    
    if 'X' in word:
        floating_index = 0
        floating_bits = []
        while floating_index < len(word):
            i = word.index('X', floating_index, len(word))
            floating_bits.append(i)
            floating_index = i+1

        truth = []
        state = False
        for l in range(1, 2**len(floating_bits)):
            new_word = word.copy()
            state = False
            for n in floating_bits:
                if l%(2**(floating_bits.index(n)+1)) == 0:
                    state = not state
                if state:
                    new_word[n] = '1'
                else:
                    new_word[n] = '0'
                truth.append(new_word)
        return truth
        for w in truth:
            if not w in combinations:
                combinations.append(w)
        return combinations
    else : return word

def truth(lines, weight):
    state = False
    for l in range(lines):
        if (l%(2**weight)) == 0:
            state = not state   
        print (int(state))

# Python3 implementation of the  
# above approach  
  
# Function to print the output  
def printTheArray(arr, n):  
    for i in range(0, n):  
        print(arr[i], end = " ")
    print() 
  
# Function to generate all binary strings  
def generateAllBinaryStrings(n, arr, i):  
  
    if i == n: 
        printTheArray(arr, n)  
        return
      
    # First assign "0" at ith position  
    # and try for all other permutations  
    # for remaining positions  
    arr[i] = 0
    generateAllBinaryStrings(n, arr, i + 1)  
  
    # And then assign "1" at ith position  
    # and try for all other permutations  
    # for remaining positions  
    arr[i] = 1
    generateAllBinaryStrings(n, arr, i + 1)  
  
# Driver Code  
if __name__ == "__main__":  

    #n = 3
    #arr = [None] * n  
    ## Print all binary strings  
    #generateAllBinaryStrings(n, arr, 0)
  
# This code is contributed  
# by Rituraj Jain
