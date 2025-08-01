"""
Task 4: Tech Conference Registration
The Jos Tech Conference registered participants under ticket categories:

participants = {"VIP": "Alice", "Regular": "Bob", "Student": "Charlie"}

During the first day:
- A "Guest" participant named "Daisy" joined.
- The "Student" participant canceled their registration.
- The organizers created a record for the day before removing the most recently added participant from the live system.
"""

# print(participants_snapshot)
# print(participants)

# Initial participants
participants = {"VIP": "Alice", "Regular": "Bob", "Student": "Charlie"}

# Add a "Guest" participant Daisy
participants["Guest"] = "Daisy"
print(participants)

# Remove the "Student" participant (cancelled registration)
participants.pop("Student")
print(participants)

# Create a record for the day
day_record = participants.copy()

# Remove the most recently added participant ("Guest") from the live system
participants.pop("Guest")

# Show the results
print("Day Record:", day_record)
print("Current Live System:", participants)


