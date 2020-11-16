# In the 20×20 grid below, four numbers along a diagonal line have been marked in red.

number1 = "08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08"
number2 = "49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00"
number3 = "81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65"
number4 = "52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91"
number5 = "22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80"
number6 = "24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50"
number7 = "32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70"
number8 = "67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21"
number9 = "24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72"
number10 = "21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95"
number11 = "78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92"
number12 = "16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57"
number13 = "86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58"
number14 = "19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40"
number15 = "04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66"
number16 = "88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69"
number17 = "04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36"
number18 = "20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16"
number19 = "20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54"
number20 = "01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"


array = [number1.split(" "), number2.split(" "), number3.split(" "), number4.split(" "), number5.split(" "), number6.split(" "), number7.split(" "), number8.split(" "), number9.split(" "), number10.split(" "), number11.split(" "), number12.split(" "), number13.split(" "), number14.split(" "), number15.split(" "), number16.split(" "), number17.split(" "), number18.split(" "), number19.split(" "), number20.split(" ")]
# The product of these numbers is 26 × 63 × 78 × 14 = 1788696.

# What is the greatest product of four adjacent numbers in the same direction
#  (up, down, left, right, or diagonally) in the 20×20 grid?

for i in range(len(array)):
    for j in range(len(array[i])):
        array[i][j] = int(array[i][j])

def row_max(row):
    ans = 0
    for i in range(17):
        current = row[i] * row[i+1] * row[i+2] * row[i+3]
        if current > ans:
            ans = current
    return ans

def column_max(array):
    ans = 0
    for i in range(20):
        for j in range(17):
            # Since I am clculating the column product I need to take different rows before changing column
            # i will be the column value and j the row value as j changes before i
            # as array[0][0] is the correct first value but array[0][1] is the wrong second value
            # the correct second value is array[1][0].
            # And as we did for rows we stop at array[16][0] and move on to the next column
            current = array[j][i] * array[j+1][i] * array[j+2][i] * array[j+3][i]
            if current > ans:
                ans = current
    return ans

def right_diagonal_max(array):
    # We need to do this 16 x 16 times
    diagonalRightMax = 0
    for i in range(17):
        for j in range(17):
            current = array[i][j] * array[i+1][j+1] * array[i+2][j+2] * array[i+3][j+3]
            if current > diagonalRightMax:
                diagonalRightMax = current
                print("RIGHT", current, diagonalRightMax)
    return diagonalRightMax

def left_diagonal_max(array):
    # We also need to do this 16 x 16 times
    diagonalLeftMax = 0
    for i in range(17):
        for j in range(17):
            current = array[i][j + 3] * array[i + 1][j + 2] * array[i + 2][j + 1] * array[i + 3][j]
            if current > diagonalLeftMax:
                diagonalLeftMax = current
                print("LEFT", current, diagonalLeftMax)
    return diagonalLeftMax

def problem_eleven():
    # Finding row max
    answer = 0
    rowMax = 0
    for i in array:
        current = row_max(i)
        if current > rowMax:
            rowMax = current
    columnMax = column_max(array)
    diagonalRightMax = right_diagonal_max(array)
    diagonalLeftMax = left_diagonal_max(array)
    if rowMax > answer:
        answer = rowMax
    if columnMax > answer:
        answer = columnMax
    if diagonalLeftMax > answer:
        answer = diagonalLeftMax
    if diagonalRightMax > answer:
        answer = diagonalRightMax
    return answer

print(problem_eleven())