# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

def even_next(n):
    return n / 2

def odd_next(n):
    return (3*n) + 1

def next_value(n):
    if n % 2 == 0:
        return even_next(n)
    else:
        return odd_next(n)

def collatz(n):
    array = [n]
    answer = n
    while answer != 1:
        answer = next_value(answer)
        array.append(answer)
    return array

def longest_collatz():
    max = []
    answer = 0
    for i in range(1000000):
        if i == 0:
            pass
        else:
            print(i)
            current = collatz(i)
            if len(current) > len(max):
                max = current
                answer = i
    return answer

print(longest_collatz())