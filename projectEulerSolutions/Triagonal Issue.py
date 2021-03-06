# Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:

# Triangle	 	    Tn=n(n+1)/2	 	    1, 3, 6, 10, 15, ...
# Pentagonal	 	Pn=n(3n−1)/2	 	1, 5, 12, 22, 35, ...
# Hexagonal	 	    Hn=n(2n−1)	 	    1, 6, 15, 28, 45, ...

# It can be verified that T285 = P165 = H143 = 40755.

# Find the next triangle number that is also pentagonal and hexagonal.

def triagonal_array(n, start):
    array = []
    for i in range(start, n + 1):
        array.append( i * ( i + 1 ) / 2 )
    return array

def pentagonal_array(n):
    array = []
    for i in range(n):
        array.append( i * ( (3*i) - 1 ) / 2 )
    return array

def hexagonal_array(n):
    array = []
    for i in range(n):
        array.append( i * ( (2*i) - 1 ) )
    return array

def solution_next(n):
    # T285 is already a solution therefore, we must start at 286 
    # Return an array of possibilities
    t_array = triagonal_array(n, 286)
    t_array_original = t_array
    p_array = pentagonal_array(n)
    h_array = hexagonal_array(n)
    index_ans = 0
    for i in p_array:
        t_array.append(i)
    for i in h_array:
        t_array.append(i)
    total = sorted(t_array)
    for i in range(len(total) - 2):
        if (total[i] == total[i+1]) and (total[i] == total[i + 2]):
            index_ans = t_array.index(total[i])
            return total[i]
    return False


print(solution_next(100000))