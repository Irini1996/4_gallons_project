# 4 Gallon Bucket Problem

# The objective of this project is to develop a program that can solve the problem of 2 kids fetching 4 gallons of water from a stream, using only an unmarked 3-gallon bucket, and an unmarked 5-gallon bucket, in less than 15 steps.



def solve(a=0, b=0, seen=set(), path=[]):
    if a + b == 4: # Goal: stop when the two buckets together hold exactly 4 gallons
        return path
    seen.add((a, b)) # Remember the current state (to avoid visiting it again)           

    steps = [
        ("Fill A",  (5, b)),
        ("Fill B",  (a, 3)),
        ("Empty A", (0, b)),
        ("Empty B", (a, 0)),
        ("A->B",    (max(0, a-(3-b)), min(3, a+b))),
        ("B->A",    (min(5, a+b), max(0, b-(5-a))))
    ]

    for name, (new_a, new_b) in steps:   # Try each possible move
        if (new_a, new_b) not in seen:  # Only continue if this state has not been seen before
            solution = solve(new_a, new_b, seen, path + [(name, (new_a, new_b))]) #Recursive call: continue searching from the new state
            if solution:
                return solution

#run and print the steps
for i, (act, state) in enumerate(solve(), 1):
    print(f"{i}) {act} -> {state}")



