# Prompt the user tp input the integers in seconds

sec = int(input("Enter the integers in seconds: "))

# Compute the remaining seconds and minutes

minutes = sec // 60
secs = sec % 60

# Display Result

print(sec, "is", secs, "Seconds ", minutes, "Minutes")
