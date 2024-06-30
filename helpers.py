def print_rows(rows, col = 'name'):
    for [idx,row] in enumerate(rows):
        print(f"{idx+1}. {row[col]}")
        
def pretty_print(data):
    header = data[0].keys()
    print("   ".join(header))
    for row in data:
        str_row = []
        for head in header:
            if row[head] is None:
                str_row.append('')
            elif isinstance(row[head], bool):
                str_row.append(str(row[head]))
            else:
                str_row.append(row[head])
        print("   ".join(str_row))