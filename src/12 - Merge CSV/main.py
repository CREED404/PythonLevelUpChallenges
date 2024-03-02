def merge_csv(list_to_csvs: list[str]=["csv1.csv", "csv2.csv"], output_csv: str="output.csv"):
    csvs = []
    headers = []
    columns=[]
    
    for path in list_to_csvs:
        with open(path ,"r", encoding="utf-8") as f:
            csvs.append([line for line in f.read().split("\n") if line])
    
    for csv in csvs:
        headers.append({i:x for i ,x in enumerate(csv[0].split(","))})
    headerToUse = list(set([name for header in headers for _, name in header.items()]))
    
    for header in headerToUse:
        rows=[]
        for csv_index, csv in enumerate(csvs):
            for i in range(1,len(csv)):
                row=csv[i].split(",")
                found=False
                for item_index, item in enumerate(row):
                    if header == headers[csv_index][item_index]:
                        found = True
                        break
                rows.append(item if item else None) if found else rows.append(None)          
        columns.append(rows)

    csv = ""
    row_count = len(columns[0])
    col_count = len(headerToUse)

    for i, header in enumerate(headerToUse):
        csv+=f"{header}{"\n" if i == col_count-1 else ","}"

    for index, _ in enumerate(columns[0]):
        for i in range(col_count):
            csv += columns[i][index] if columns[i][index] else ""
            if i == col_count-1:
                csv+="\n" if index != row_count-1 else ""
            else:
                csv+=","

    with open(output_csv, "w", encoding="utf-8") as f:
        f.write(csv)
