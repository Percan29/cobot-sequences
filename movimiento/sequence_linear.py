points = [0.2, 0.4, 0.6, 0.8]

def linear_sequence(points):
    for p in points:
        print(f"Moving to position {p}")
        print("Action: maintaining linear path")

linear_sequence(points)

# Note:
# Typical linear movement sequence used in UR, KUKA, and FANUC cobots.
# Represents continuous motion between defined points.
