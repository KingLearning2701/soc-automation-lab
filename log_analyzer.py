# Simple SOC Log Analyzer
# Detects suspicious login attempts

failed_logins = [
    "user1 - failed login from 192.168.1.10",
    "admin - failed login from 192.168.1.15",
    "user2 - successful login from 192.168.1.20",
    "admin - failed login from 192.168.1.15",
    "guest - failed login from 192.168.1.30"
]

suspicious_ips = {}

for log in failed_logins:
    if "failed login" in log:
        ip = log.split("from ")[1]

        if ip in suspicious_ips:
            suspicious_ips[ip] += 1
        else:
            suspicious_ips[ip] = 1

print("Suspicious IP Report\n")

for ip, count in suspicious_ips.items():
    if count >= 2:
        print(f"⚠️ Possible brute force attack from {ip} ({count} attempts)")
    else:
        print(f"Failed login from {ip}")