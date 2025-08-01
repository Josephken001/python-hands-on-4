"""
Task 1: Music Concert Ticketing System
During the Jos Summer Music Concert, ticket sales were recorded as follows:

tickets = {"VIP": 50, "Regular": 150, "Student": 75}

Later in the day:
- A new "Backstage" experience with 10 tickets was introduced.
- The "Student" category sold out completely.
- The team wanted to keep a record of the day’s sales before preparing for next week’s concert.
"""

# Initial ticket sales
tickets = {"VIP": 50, "Regular": 150, "Student": 75}

# Add the new "Backstage" experience
tickets["Backstage"] = 10
print(tickets)

# Remove the "Student" category (sold out)
tickets.pop("Student")
print(tickets)

# Keep a record of the day’s sales
sales_record = tickets.copy()

# Show the results
print(" Tickets after updates:", tickets)
print(" Record of the day’s sales:", sales_record)

