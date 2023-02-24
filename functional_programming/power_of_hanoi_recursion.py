def hanoi(disks, source, helper, destination):
    # base condition
    if disks == 1:
        print(f"Disk {disks} moves from tower {source} to tower {destination}.")
        return
    
    # recursive function return is calling itself
    hanoi(disks -1, source, destination, helper)
    print(f"Disk {disks} moves from tower {source} to tower {destination}.")
    hanoi(disks-1, helper, source,destination)
    
disks = int(input('Number of disks to be displaced: '))

# Actual function call
"""Tower A is the source
   Towe B is the helper
   Tower C is the destination
 """
hanoi(disks, 'A', 'B', 'C')
    
    