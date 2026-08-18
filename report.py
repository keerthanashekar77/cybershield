class ReportGenerator:
    def generate(self, incident, risk_score, severity):
        print("\n")
        print("=" * 60)
        print("           DATA BREACH INCIDENT REPORT")
        print("=" * 60)
        print(f"Incident ID      : {incident.incident_id}")
        print(f"Title            : {incident.title}")
        print(f"Breach Type      : {incident.breach_type()}")
        print(f"Records Affected : {incident.affected_records}")
        print(f"Exposed Data     : {incident.data_asset.data_type}")
        print(f"Risk Score       : {risk_score}")
        print(f"Severity         : {severity}")
        print(f"Current Status   : {incident.status}")
        print("\nIncident Timeline")
        for event in incident.timeline:
            print(f" - {event}")
        print("=" * 60)
