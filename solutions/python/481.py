def multiplication_table(rows,cols):
    table = []
    for row in range(1, rows + 1):
        table.append([])
        for col in range(1, cols + 1):
            table[-1].append(row * col)
    return table