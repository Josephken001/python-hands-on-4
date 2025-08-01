"""
Task 2: Airport Luggage Tracker
At Jos Airport, the luggage department tracked passengers and their luggage weights:

luggage = [("Alice", 23),( "Bob", 18), ("Charlie", 25)]

- you need to map each user to its corresponding luggage weight value.

Before the flight took off:
- A late passenger "Daisy" checked in with 20kg of luggage.
- Bob’s luggage went missing.
- The staff prepared a daily report before resetting for the next flight.
"""

# Initial luggage list
luggage = [("Alice", 23),( "Bob", 18), ("Charlie", 25)]

# Convert the list into a dictionary for easy tracking
luggage_dict = dict(luggage)
print(luggage_dict)

# Add Daisy and her luggage weight
print(">>>>>> Adding 'Daisy' and her luggage")
luggage_dict["Daisy"] = 20
print(luggage_dict)

# Remove Bob (his luggage went missing)
print(">>>> Removing Bob")
luggage_dict.pop("Bob")
print(luggage_dict)

# Prepare the daily report (make a copy before reset)
daily_report = luggage_dict.copy()

# Show the results
print("Daily Luggage Report:", daily_report)

