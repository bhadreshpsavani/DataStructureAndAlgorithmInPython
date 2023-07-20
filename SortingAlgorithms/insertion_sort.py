""" Insertion Sort


"""

A = [1, 4, 74, 48, 5, 7, 2]

for i in range(1, len(A)):
    stab = A[i] # Fix a pointer
    j = i-1 # get index of previous Number
    while j >= 0 and A[j]>stab: # until reaches front limitd
        A[j+1] = A[j]
        j-=1
    A[j+1] = stab

print(A)