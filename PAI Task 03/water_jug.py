def water_puzzle(jugA_max, jugB_max, target, jugA=0, jugB=0, steps=0, visited=None):
    if visited is None:
        visited = set()
    if (jugA, jugB) in visited:
        return float('inf')
    visited.add((jugA, jugB))
    if jugA == target or jugB == target:
        return steps
    possible_moves = [
        (jugA_max, jugB),
        (jugA, jugB_max),
        (0, jugB),
        (jugA, 0),
        (jugA - min(jugA, jugB_max - jugB), jugB + min(jugA, jugB_max - jugB)),
        (jugA + min(jugB, jugA_max - jugA), jugB - min(jugB, jugA_max - jugA))
    ]
    return min(water_puzzle(jugA_max, jugB_max, target, a, b, steps + 1, visited) for a, b in possible_moves)
jug1_capacity = 4
jug2_capacity = 3
desired_amount = 2
result = water_puzzle(jug1_capacity, jug2_capacity, desired_amount)
print(f"Minimum steps required: {result}" if result != float('inf') else "No solution possible.")
