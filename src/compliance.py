required_rules = [
    "set service ssh",
    "set service ntp"
]

routers = ["R1", "R2", "R3"]

report = []

for router in routers:

    report.append(f"\nChecking {router}")

    print(f"\nChecking {router}")

    with open(f"../configs/{router}.txt", "r") as file:
        config = file.read()

    for rule in required_rules:

        if rule in config:
            print(f"PASS: {rule}")
            report.append(f"PASS: {rule}")
        else:
            print(f"FAIL: {rule}")
            report.append(f"FAIL:{rule}")

with open("../reports/compliance_report.txt", "w") as file:
    file.write("\n".join(report))
