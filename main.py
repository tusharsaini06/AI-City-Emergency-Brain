import json
from traffic_module import get_traffic_result

print("AI City Emergency Brain")
print("Traffic AI Started")

# Load traffic data
with open("traffic.json", "r") as file:
    roads = json.load(file)

# Run Traffic AI
result = get_traffic_result(roads)

# Display result
print("\nFinal Traffic AI Result:")

print("Traffic Impact:", result["traffic_impact"])
print("Affected Roads:", result["affected_roads"])
print("Recommended Route:", result["recommended_route"])
print("Reason:", result["reason"])