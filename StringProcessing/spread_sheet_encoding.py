def spreadsheet_encode_column(col_str):
    num = 0
    count = len(col_str) - 1

    for c in col_str:
        num   += 26**count * (ord(c) - ord('A') +1)
        count += 1

    return num

print(spreadsheet_encode_column("X"))  # X * 26^0
print(spreadsheet_encode_column("AA")) # A * 26^1  + A * 26^0
print(spreadsheet_encode_column("ZZ"))

# print(ord('X') - ord('A') + 1)