import os
import datetime
import random
import subprocess

# Define the cake pattern using a 7x52 grid (GitHub contribution graph)
cake_pattern = [
    "  | | | | | | | | | | | | | | | | | | | |  ",  # 20 candles (week 1)
    "  ██████████████████████████████████████  ",  # Cake top (week 2)
    "  ██████████████████████████████████████  ",  # Cake middle (week 3)
    "  ██████████████████████████████████████  ",  # Cake middle (week 4)
    "  ██████████████████████████████████████  ",  # Cake bottom (week 5)
]

# Start date (1 year ago, aligned to a Sunday)
start_date = datetime.date.today() - datetime.timedelta(days=365)

# Ensure repo has an index.html file
with open("index.html", "w") as f:
    f.write("<h1>Happy Birthday, baby!</h1>")

subprocess.run(["git", "add", "index.html"])
subprocess.run(["git", "commit", "-m", "Added birthday message"])
subprocess.run(["git", "push", "origin", "main"])

# Loop through the past year to make commits based on the pattern
for week in range(len(cake_pattern[0])):  # Iterate weeks (columns)
    for day in range(len(cake_pattern)):  # Iterate days (rows)
        if cake_pattern[day][week] == "█" or cake_pattern[day][week] == "|":
            commit_date = start_date + datetime.timedelta(weeks=week, days=day)

            for _ in range(random.randint(3, 7)):  # Random commit intensity
                with open("cake.txt", "a") as f:
                    f.write(f"Commit on {commit_date}\n")

                subprocess.run(["git", "add", "cake.txt"])
                subprocess.run(["git", "commit", "--date", commit_date.strftime("%Y-%m-%d"), "-m", "Birthday cake commit"])

# Push everything
subprocess.run(["git", "push", "origin", "main"])

print("🎂 Birthday cake is now on your GitHub contributions graph!")
