# Python code to flat a nested array of integers
  
# input
nestedArray = [" N O T - I N T", 788, 8, [36, 74, [1345, 20.6]], 987, 48, [90, [10,[1, 2, 3, 4, [5, [6, [" N O T - I N T", 7, [8, [9, 10.9898767]]]]]]]]]
  
# output
output = []
  
# function used to flatten nested arrays (removing non integers values) 
def flatten(nestedArray):
    for n in nestedArray:
        if isinstance(n, list):    #type(n) == list:
            flatten(n)
        elif isinstance(n, int):   #type(n) == int:
                output.append(n)
  
print ('Nested array: ', nestedArray)
flatten(nestedArray)
print ('Flatted array: ', output)