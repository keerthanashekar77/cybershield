class RiskEngine:
    def calculate_score(self, incident):
        sensitivity_score = incident.data_asset.get_risk_value()
        records = incident.affected_records

        if records <= 100:
            record_multiplier = 1
        elif records <= 1000:
            record_multiplier = 2
        elif records <= 10000:
            record_multiplier = 3
        else:
            record_multiplier = 4

        return sensitivity_score * record_multiplier

    def get_severity(self, score):
        if score >= 50:
            return "CRITICAL"
        elif score >= 30:
            return "HIGH"
        elif score >= 15:
            return "MEDIUM"
        return "LOW"
