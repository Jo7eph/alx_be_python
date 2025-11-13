# daily_reminder.py
# A simple daily reminder using match-case, loops, and conditional statements

# Prompt the user for input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Loop to ensure correct priority input
while priority not in ("high", "medium", "low"):
    print("Invalid priority. Please enter high, medium, or low.")
    priority = input("Priority (high/medium/low): ").lower()

# Loop to ensure correct time-bound input
while time_bound not in ("yes", "no"):
    print("Invalid input. Please enter yes or no.")
    time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process task based on priority
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"

# Modify reminder if task is time-bound
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += ". Consider completing it when you have free time."

# Print the reminder
print("\nReminder:", reminder)
