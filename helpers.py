from tabulate import tabulate

def print_rows(rows, col = 'name'):
    for [idx,row] in enumerate(rows):
        print(f"{idx+1}. {row[col]}")
        
def pretty_print_old(data):
    header = list(data[0].keys())
    # header.remove("id")
    print("   ".join(header))
    for [idx,row] in enumerate(data):
        str_row = []
        for head in header:
            if head == 'id':
                str_row.append(str(idx+1))
            elif row[head] is None:
                str_row.append('')
            # elif isinstance(row[head], bool):
            #     str_row.append(str(row[head]))
            # elif isinstance(row[head], int):
            #     str_row.append(str(row[head]))
            else:
                str_row.append(str(row[head]))
        print("   ".join(str_row))
        
def pretty_print(data):
    print_list =[{k: v for k, v in d.items() if k != 'id'} for d in data]
    print(
        tabulate(print_list, headers="keys", showindex=range(1, len(data)+1))
        )