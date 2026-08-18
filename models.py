from abc import ABC, abstractmethod
from datetime import datetime


class User:
    def __init__(self, user_id, name, role):
        self.user_id = user_id
        self.name = name
        self.role = role

    def display_info(self):
        return f"{self.user_id} | {self.name} | {self.role}"


class DataAsset(ABC):
    def __init__(self, data_type, sensitivity):
        self.data_type = data_type
        self.sensitivity = sensitivity

    @abstractmethod
    def get_risk_value(self):
        pass


class PersonalData(DataAsset):
    def get_risk_value(self):
        return self.sensitivity * 2


class FinancialData(DataAsset):
    def get_risk_value(self):
        return self.sensitivity * 4


class CredentialData(DataAsset):
    def get_risk_value(self):
        return self.sensitivity * 5


class BreachIncident(ABC):
    def __init__(self, incident_id, title, affected_records, data_asset, discovered_by):
        self.incident_id = incident_id
        self.title = title
        self.affected_records = affected_records
        self.data_asset = data_asset
        self.discovered_by = discovered_by
        self.status = "OPEN"
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.timeline = []
        self.add_event("Incident created")

    @abstractmethod
    def breach_type(self):
        pass

    def add_event(self, event):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.timeline.append(f"{timestamp} - {event}")

    def update_status(self, status):
        self.status = status
        self.add_event(f"Status changed to {status}")

    def display(self):
        print("\n" + "=" * 55)
        print(f"Incident ID       : {self.incident_id}")
        print(f"Title             : {self.title}")
        print(f"Breach Type       : {self.breach_type()}")
        print(f"Affected Records  : {self.affected_records}")
        print(f"Exposed Data      : {self.data_asset.data_type}")
        print(f"Status            : {self.status}")
        print(f"Discovered By     : {self.discovered_by.name}")
        print(f"Created At        : {self.created_at}")
        print("=" * 55)


class CredentialBreach(BreachIncident):
    def breach_type(self):
        return "Credential Breach"


class DatabaseBreach(BreachIncident):
    def breach_type(self):
        return "Database Breach"


class PhishingBreach(BreachIncident):
    def breach_type(self):
        return "Phishing-related Breach"


class InsiderBreach(BreachIncident):
    def breach_type(self):
        return "Insider Data Exposure"
