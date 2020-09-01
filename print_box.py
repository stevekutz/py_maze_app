# Print box of arbitrary num row, col

rows = int(input(" Please enter num rows: "))
cols = int(input(" Please enter num columns: "))


print(f'  rows: {rows}  cols: {cols}')

i = 1

while( i < rows):
    j = 1
    while(j <= cols):
        if (i == 1 or i == rows or j == 1 or j == cols):
            print('*', end = '')
        else:
            print(' ', end  = '')    
        j = j + 1
    i = i + 1
    print()            