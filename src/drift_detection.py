routers = ["R1", "R2", "R3"]

with open("../baseline/golden_config.txt") as file:
    baseline = file.read().splitlines()

report = []

for router in routers:

    report.append(f"\nChecking {router}")

    with open(f"../configs/{router}.txt") as file:
        config = file.read()

    drift_found = False

    for rule in baseline:

        if rule in config:
            report.append(f"PASS: {rule}")
        else:
            report.append(f"DRIFT: Missing {rule}")
            drift_found = True
    if not drift_found:
        report.append("NO DRIFT DETECTED")

with open("../reports/drift_report.txt", "w") as file:
    file.write("\n".join(report))

print("Drift report generated.")
