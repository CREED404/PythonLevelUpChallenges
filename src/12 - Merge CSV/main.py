import csv

def merge_csv(input_array, output):
  all_headers = []

  # Get all unique header values
  for filename in input_array:
    with open(filename, "r") as f:
      reader = csv.DictReader(f)
      all_headers.extend(h for h in reader.fieldnames if h not in all_headers)

  # Write on read; line-by-line
  with open(output, "w") as output_file:
    # Creates a csv with the specified headers
    writer = csv.DictWriter(output_file, fieldnames=all_headers)
    writer.writeheader()

    for filename in input_array:
      with open(filename, "r") as input_file:
        reader = csv.DictReader(input_file)
        for row in reader:
          # Writes to csv and handles missing headers automatically
          writer.writerow(row)