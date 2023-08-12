import json

# Read JSON data from file
def read_json_file(filename):
    file = open(filename, 'r')
    try:
        data = json.load(file)
    finally:
        file.close()
    return data

# Write JSON data to file
def write_json_file(filename, data):
    file = open(filename, 'w')
    try:
        json.dump(data, file, indent=4)
    finally:
        file.close()

# Add a new country to the JSON data
def add_country(filename, country, population):
    data = read_json_file(filename)
    new_country = {
        "country": country,
        "population": population
    }
    data.append(new_country)
    write_json_file(filename, data)

# Delete a country from the JSON data
def delete_country(filename, country):
    data = read_json_file(filename)
    data = [item for item in data if item["country"] != country]
    write_json_file(filename, data)

# Example usage
filename = "Countries.json"
add_country(filename, "Africa", 212559417)
delete_country(filename, "China")

# Print updated data
updated_data = read_json_file(filename)
print(json.dumps(updated_data, indent=4))