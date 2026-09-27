# Traffic AI Testing

test_cases = [
    {
        "name": "Normal Traffic",
        "roads": {
            "Road A": "low",
            "Road B": "medium",
            "Road C": "low",
            "Road D": "medium"
        }
    },

    {
        "name": "Blocked Road",
        "roads": {
            "Road A": "blocked",
            "Road B": "high",
            "Road C": "low",
            "Road D": "medium"
        }
    },

    {
        "name": "Multiple Blocked Roads",
        "roads": {
            "Road A": "blocked",
            "Road B": "blocked",
            "Road C": "high",
            "Road D": "low"
        }
    },

    {
        "name": "All Roads Blocked",
        "roads": {
            "Road A": "blocked",
            "Road B": "blocked",
            "Road C": "blocked"
        }
    }
]


def traffic_impact(roads):
    blocked_count = 0
    high_count = 0

    for status in roads.values():
        if status == "blocked":
            blocked_count += 1
        elif status == "high":
            high_count += 1

    if blocked_count >= 1:
        return "HIGH"
    elif high_count >= 1:
        return "MEDIUM"
    else:
        return "LOW"


def recommend_route(roads):
    priority = {
        "low": 1,
        "medium": 2,
        "high": 3
    }

    available = []

    for road, status in roads.items():
        if status != "blocked":
            available.append((road, status))

    if not available:
        return None

    available.sort(key=lambda x: priority[x[1]])

    return available[0][0]


for test in test_cases:

    roads = test["roads"]

    impact = traffic_impact(roads)
    route = recommend_route(roads)

    print("\n-------------------------")
    print("Test:", test["name"])
    print("Traffic Impact:", impact)
    print("Recommended Route:", route)