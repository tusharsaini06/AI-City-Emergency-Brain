print("AI City Emergency Brain")
print("Traffic AI Started")
import json

with open("traffic.json", "r") as file:
    roads = json.load(file)

blocked_roads = []

for road, status in roads.items():
    if status == "blocked":
        blocked_roads.append(road)

print("Blocked Roads:", blocked_roads)

available_roads = []

for road, status in roads.items():
    if status != "blocked":
        available_roads.append(road)

print("Available Roads:", available_roads)

priority = {
    "low": 1,
    "medium": 2,
    "high": 3
}

available_roads = []

for road, status in roads.items():
    if status != "blocked":
        available_roads.append((road, status))

available_roads.sort(key=lambda x: priority[x[1]])

recommended_route = available_roads[0][0]

print("Recommended Route:", recommended_route)

recommended_status = roads[recommended_route]

reason = (
    f"{recommended_route} has {recommended_status} traffic "
    f"and is not blocked."
)

print("Reason:", reason)

# Traffic Impact Prediction

blocked_count = 0
high_count = 0

for status in roads.values():
    if status == "blocked":
        blocked_count += 1
    elif status == "high":
        high_count += 1

if blocked_count >= 1 and high_count >= 1:
    traffic_impact = "HIGH"
elif blocked_count >= 1:
    traffic_impact = "HIGH"
elif high_count >= 1:
    traffic_impact = "MEDIUM"
else:
    traffic_impact = "LOW"

print("Traffic Impact:", traffic_impact)

# Affected Roads

affected_roads = []

for road, status in roads.items():
    if status == "high":
        affected_roads.append(road)

print("Affected Roads:", affected_roads)

# Final Traffic AI Result

result = {
    "traffic_impact": traffic_impact,
    "affected_roads": affected_roads,
    "recommended_route": recommended_route,
    "reason": reason
}

print("\nFinal Traffic AI Result:")
print(result)