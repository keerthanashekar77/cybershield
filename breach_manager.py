class BreachManager:
    def __init__(self):
        self.incidents = []

    def add_incident(self, incident):
        self.incidents.append(incident)

    def find_incident(self, incident_id):
        for incident in self.incidents:
            if incident.incident_id == incident_id:
                return incident
        return None

    def list_incidents(self):
        if not self.incidents:
            print("\nNo incidents found.")
            return

        print("\n========== SECURITY INCIDENTS ==========")
        for incident in self.incidents:
            print(
                f"{incident.incident_id} | "
                f"{incident.breach_type()} | "
                f"{incident.status}"
            )

    def update_incident_status(self, incident_id, status):
        incident = self.find_incident(incident_id)
        if incident:
            incident.update_status(status)
            print("Incident status updated.")
        else:
            print("Incident not found.")

    def show_timeline(self, incident_id):
        incident = self.find_incident(incident_id)
        if not incident:
            print("Incident not found.")
            return

        print("\n========== INCIDENT TIMELINE ==========")
        for event in incident.timeline:
            print(event)
