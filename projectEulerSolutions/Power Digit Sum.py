# def power_digit_sum(x, n)
#     answer = 0
#     first = x ** n
#     second = first.to_s.split("")
#     second.each do |i|
#         i = i.to_i
#         answer = answer + i
#     end
#     return answer
# end

def splitString(word):
    return [char for char in word]

def power_digit_sum(x, n):
    answer = 0
    first = x ** n
    second = str(first)
    second = splitString(second)
    for i in second:
        answer = answer + int(i)
    return answer

print(power_digit_sum(2, 1000))