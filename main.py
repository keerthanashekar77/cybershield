from models import (
    User, PersonalData, FinancialData, CredentialData,
    CredentialBreach, DatabaseBreach, PhishingBreach, InsiderBreach
)
from breach_manager import BreachManager
from risk_engine import RiskEngine
from report import ReportGenerator

manager = BreachManager()
risk_engine = RiskEngine()
report_generator = ReportGenerator()

analyst = User("A001", "Security Analyst", "SECURITY_ANALYST")


def create_incident():
    print("\n========== CREATE INCIDENT ==========")
    incident_id = input("Incident ID: ")
    title = input("Incident title: ")

    try:
        records = int(input("Number of affected records: "))
        if records <= 0:
            print("Number of records must be greater than 0.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    print("\nSelect exposed data:")
    print("1. Personal Data")
    print("2. Financial Data")
    print("3. Credential Data")
    data_choice = input("Choice: ")

    if data_choice == "1":
        data_asset = PersonalData("Personal Information", 5)
    elif data_choice == "2":
        data_asset = FinancialData("Financial Information", 8)
    elif data_choice == "3":
        data_asset = CredentialData("Credentials", 10)
    else:
        print("Invalid choice.")
        return

    print("\nSelect breach type:")
    print("1. Credential Breach")
    print("2. Database Breach")
    print("3. Phishing-related Breach")
    print("4. Insider Data Exposure")
    breach_choice = input("Choice: ")

    breach_classes = {
        "1": CredentialBreach,
        "2": DatabaseBreach,
        "3": PhishingBreach,
        "4": InsiderBreach
    }
    breach_class = breach_classes.get(breach_choice)

    if not breach_class:
        print("Invalid breach type.")
        return

    incident = breach_class(
        incident_id, title, records, data_asset, analyst
    )
    manager.add_incident(incident)

    score = risk_engine.calculate_score(incident)
    severity = risk_engine.get_severity(score)
    incident.add_event(f"Risk assessed as {severity} (Score: {score})")

    print("\nIncident successfully created.")
    print(f"Risk Score: {score}")
    print(f"Severity: {severity}")


def view_incident():
    incident_id = input("\nEnter Incident ID: ")
    incident = manager.find_incident(incident_id)

    if incident:
        incident.display()
        score = risk_engine.calculate_score(incident)
        severity = risk_engine.get_severity(score)
        print(f"Risk Score : {score}")
        print(f"Severity   : {severity}")
    else:
        print("Incident not found.")


def update_status():
    incident_id = input("\nEnter Incident ID: ")
    print("\n1. OPEN")
    print("2. INVESTIGATING")
    print("3. CONTAINED")
    print("4. RESOLVED")
    choice = input("Choice: ")

    statuses = {
        "1": "OPEN",
        "2": "INVESTIGATING",
        "3": "CONTAINED",
        "4": "RESOLVED"
    }
    status = statuses.get(choice)

    if status:
        manager.update_incident_status(incident_id, status)
    else:
        print("Invalid status.")


def generate_report():
    incident_id = input("\nEnter Incident ID: ")
    incident = manager.find_incident(incident_id)

    if not incident:
        print("Incident not found.")
        return

    score = risk_engine.calculate_score(incident)
    severity = risk_engine.get_severity(score)
    report_generator.generate(incident, score, severity)


def main():
    while True:
        print("\n" + "=" * 55)
        print("       CYBERSHIELD - BREACH RESPONSE SYSTEM")
        print("=" * 55)
        print("1. Create Breach Incident")
        print("2. View All Incidents")
        print("3. View Incident")
        print("4. Update Incident Status")
        print("5. View Incident Timeline")
        print("6. Generate Incident Report")
        print("7. Exit")

        choice = input("\nEnter choice: ")

        if choice == "1":
            create_incident()
        elif choice == "2":
            manager.list_incidents()
        elif choice == "3":
            view_incident()
        elif choice == "4":
            update_status()
        elif choice == "5":
            manager.show_timeline(input("\nEnter Incident ID: "))
        elif choice == "6":
            generate_report()
        elif choice == "7":
            print("\nExiting CyberShield...")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
