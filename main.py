import requests
import json
import matplotlib.pyplot as plt

# Make the API request
url = 'https://api.nasa.gov/neo/rest/v1/feed'
params = {
    'start_date': '2015-09-07',
    'end_date': '2015-09-08',
    'api_key': 'DEMO_KEY'  # Use your API key here
}
headers = {'accept': 'application/json'}

response = requests.get(url, params=params, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()

    # Extract relevant data
    neo_data = data['near_earth_objects']['2015-09-08']
    miss_distances = [float(neo['close_approach_data'][0]['miss_distance']['miles']) for neo in neo_data]
    relative_velocities = [float(neo['close_approach_data'][0]['relative_velocity']['miles_per_hour']) for neo in neo_data]
    estimated_diameters_max = [float(neo['estimated_diameter']['feet']['estimated_diameter_max']) for neo in neo_data]

    # Create the plot
    plt.figure(figsize=(10, 6))
    for i in range(len(neo_data)):
        plt.scatter(miss_distances[i], relative_velocities[i], s=estimated_diameters_max[i]*10, alpha=0.75)
        plt.text(miss_distances[i], relative_velocities[i], neo_data[i]['name'], fontsize=8, ha='right')

    plt.xlabel('Miss Distance (miles)')
    plt.ylabel('Relative Velocity (miles/hour)')
    plt.title('NEO Data: Miss Distance vs Relative Velocity')
    plt.grid(True)
    plt.tight_layout()
    plt.show()
else:
    print(f"Error in request: {response.status_code}")
