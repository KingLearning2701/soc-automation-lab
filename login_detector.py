failed_attempts = {}

with open("login_logs.txt", "r") as file:
    logs = file.readlines()

for entry in logs:
    user, status = entry.strip().split()

    if status == "FAILED":
        if user not in failed_attempts:
            failed_attempts[user] = 1
        else:
            failed_attempts[user] += 1

for user, count in failed_attempts.items():
    if count >= 3:
        print(f"⚠️ Suspicious activity detected for {user} ({count} failed attempts)")