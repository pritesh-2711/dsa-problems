def move(n, source, target, auxiliary):
    """Move n disks from source to target using auxiliary as a temporary storage.
    The function prints the steps required to move the disks from the source to the target.
    """
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    move(n - 1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    move(n - 1, auxiliary, target, source)

move(5, 'A', 'C', 'B')

# Output:
# Move disk 1 from A to C
# Move disk 2 from A to B
# Move disk 1 from C to B
# Move disk 3 from A to C
# Move disk 1 from B to A
# Move disk 2 from B to C
# Move disk 1 from A to C
# Move disk 4 from A to B
# Move disk 1 from C to B
# Move disk 2 from C to A
# Move disk 1 from B to A
# Move disk 3 from C to B
# Move disk 1 from A to C
# Move disk 2 from A to B
# Move disk 1 from C to B
# Move disk 5 from A to C
# Move disk 1 from B to A
# Move disk 2 from B to C
# Move disk 1 from A to C
# Move disk 3 from B to A
# Move disk 1 from C to B
# Move disk 2 from C to A
# Move disk 1 from B to A
# Move disk 4 from B to C
# Move disk 1 from A to C
# Move disk 2 from A to B
# Move disk 1 from C to B
# Move disk 3 from A to C
# Move disk 1 from B to A
# Move disk 2 from B to C
# Move disk 1 from A to C