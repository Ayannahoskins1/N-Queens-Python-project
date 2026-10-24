def safe(stack, row, col):
    for r, c in stack:
        if c == col:
            return False
        if abs(r - row) == abs(c - col):
            return False
    return True


def n_queens(n):
    stack = []
    row = 0
    col = 0

    while row < n:
        while col < n:
            if safe(stack, row, col):
                stack.append((row, col))
                row += 1
                col = 0
                break
            col += 1
        else:
            if len(stack) == 0:
                return None

            row, col = stack.pop()
            col += 1

    return stack


def print_board(n, stack):
    for row in range(n):
        for col in range(n):
            if (row, col) in stack:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()


n = int(input("Enter N: "))

answer = n_queens(n)

if answer is None:
    print("No solution")
else:
    print_board(n, answer)