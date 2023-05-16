import csv

def merge_csv(input_array, output):
  dict_array = []
  all_headers = set()

  # Iterate for every input csv file
  for filename in input_array:
    with open(filename, "r") as f:
      # Convert CSV to list of dict
      reader = csv.DictReader(f)
      dict = list(reader)
      dict_array.append(dict)

      # Collect all possible headers in a set
      all_headers.update(dict[0].keys())
  
  combined_dict = []
  # Iterate for every list
  for array in dict_array:
    # Find missing headers
    current_headers = set(array[0].keys())
    missing_headers = all_headers.symmetric_difference(current_headers)
    
    for dict in array:
      # If any header missing, then add it with an empty value
      for header in missing_headers:
        dict[header] = ""

      # Save it to single list
      combined_dict.append(dict)
  
  # Write list to CSV
  with open(output, "w") as f:
    writer = csv.DictWriter(f, fieldnames=combined_dict[0].keys())
    writer.writeheader()
    for row in combined_dict:
      writer.writerow(row)