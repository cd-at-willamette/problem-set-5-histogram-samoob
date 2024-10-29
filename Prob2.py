
##################################################
# Name: Sivana
# Collaborators:
# Estimate of time spent (hr): 20 mins, I finished my code on Monday 
#but for some reason I would get "you must be on the branch to edit" error
#and i only fixed it by changing my account settings
##################################################
def is_magic_square(array: list[list[int]]) -> bool:
    
    n = len(array)
    for row in array:
        if len(row) != n:  # if any row is not the same length as n
            return False
    #season 6 puerto rican parade 30 thirdy rock cleveland tina are you a model youre so skinny
    
    magic_sum = sum(array[0])
    
    
    for row in array:
        if sum(row) != magic_sum:
            return False
    
    
    for col in range(n):
        col_sum = sum(array[row][col] for row in range(n))
        if col_sum != magic_sum:
            return False
    
    
    primary_diagonal_sum = sum(array[i][i] for i in range(n))
    if primary_diagonal_sum != magic_sum:
        return False
    
    
    secondary_diagonal_sum = sum(array[i][n-1-i] for i in range(n))
    if secondary_diagonal_sum != magic_sum:
        return False
    
    
    return True


small = [[8, 1, 6], [3, 5, 7], [4, 9, 2]]
print(is_magic_square(small))  # expected output: True

