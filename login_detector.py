logins = [
    "user1 SUCCESS",
    "user2 FAILED",
    "user2 FAILED",
    "user2 FAILED",
    "user3 SUCCESS"
]

failed_attempts = {}

for entry in logins:
    user, status = entry.split()

    if status == "FAILED":
        if user not in failed_attempts:
            failed_attempts[user] = 1
        else:
            failed_attempts[user] += 1

for user, count in failed_attempts.items():
    if count >= 3:
        print(f"⚠️ Suspicious activity detected for {user}")