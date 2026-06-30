weld_points = [0.1, 0.3, 0.5]

def weld_sequence(points):
    for p in points:
        print(f"Moving to weld position {p}")
        print("Welding at speed=18, length=12")

weld_sequence(weld_points)

# Note:
# Simulated welding sequence.
# Structure used in robotic welding cells in automotive manufacturing.
