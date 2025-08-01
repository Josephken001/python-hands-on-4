'''
Task 3: Hotel Room Allocation
Hill View Hotel tracked room occupancy as follows:

rooms = {"101": "Alice", "102": "Bob", "103": "Charlie"}

During the evening:
- A new guest "Daisy" was checked into room 104.
- Room 102 was vacated after Bob checked out.
- A last-minute cancellation happened for the most recently allocated room just after the manager backed up the current allocation.
'''

# Initial room occupancy
rooms = {"101": "Alice", "102": "Bob", "103": "Charlie"}

# A new guest Daisy checks into room 104
rooms["104"] = "Daisy"
print(rooms)

# Room 102 is vacated (Bob checks out)
rooms.pop("102")

# Backup the current allocation before cancellation
backup_allocation = rooms.copy()

# Cancel the most recently allocated room (room 104)
rooms.pop("104")

# Show the results
print(" Backup Allocation:", backup_allocation)
print(" Current Allocation after cancellation:", rooms)

