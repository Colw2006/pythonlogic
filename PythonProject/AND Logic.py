score = float(input("Enter your test score: "))
attendance = float(input("Enter your attendance percentage: "))

if score >= 70 and attendance >= 80:
    print("You pass the course.")
else:
    print("You do not pass the course.")