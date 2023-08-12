import json

# Read JSON data from file
def read_json_file(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

# Write JSON data to file
def write_json_file(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

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