Assignment No 4
     Name :- Atharv Yadav                                                  Div:- B
     Batch:-T3                                                                      Roll No :- CO3B47
Title – Implementation of Tower of Hanoi Using State Space Search.

Program:-
def tower_of_hanoi(n, source, auxiliary, destination):
    if n == 0:
        return

    # Move n-1 disks from source to auxiliary
    tower_of_hanoi(n - 1, source, destination, auxiliary)

    # Move the largest disk to destination
    print(f"Move disk {n} from {source} -> {destination}")

    # Move n-1 disks from auxiliary to destination
    tower_of_hanoi(n - 1, auxiliary, source, destination)


# Main program
n = int(input("Enter number of disks: "))

print("\nTower of Hanoi using State Space Search:")
tower_of_hanoi(n, 'A', 'B', 'C')

print("\nMinimum number of moves:", 2**n - 1)

Output:-
Enter number of disks: 3

Tower of Hanoi using State Space Search:
Move disk 1 from A -> C
Move disk 2 from A -> B
Move disk 1 from C -> B
Move disk 3 from A -> C
Move disk 1 from B -> A
Move disk 2 from B -> C
Move disk 1 from A -> C

Minimum number of moves: 7

Process finished with exit code 0