rows = input("Enter the number of rows: ")
rows = int(rows)
start = rows - 1
end = rows + 1
i = 1
while i <= rows + (rows - 1):
    j = 1
    while j <= rows + (rows - 1):
        if start < j < end:
            print("*", end="")
        else:
            print(" ", end="")
        j = j + 1
    if i < rows:
        start = start - 1
        end = end + 1
    else:
        start = start + 1
        end = end - 1
    i = i + 1
    print()