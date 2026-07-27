from services.data_loader import DataLoader
from datetime import datetime


class IncidentService:


    def __init__(self):

        self.loader = DataLoader()

        self.incidents = self.loader.get_incidents()



    def get_incident(self, incident_id):

        for incident in self.incidents:

            if incident["incident_id"] == incident_id:
                return incident


        return None



    def check_status(self, incident_id):

        incident = self.get_incident(incident_id)

        if incident:
            return incident["status"]

        return "Incident not found"



    def create_incident(
            self,
            shipment_id,
            severity,
            description
    ):

        incident = {

            "incident_id":
                f"INC{len(self.incidents)+1:03}",

            "shipment_id": shipment_id,

            "severity": severity,

            "description": description,

            "status": "Open",

            "created_at":
                str(datetime.now().date())

        }


        self.incidents.append(incident)


        return incident



    def escalate_incident(self, incident_id):

        incident = self.get_incident(incident_id)


        if incident:

            incident["severity"] = "Critical"

            return incident


        return "Incident not found"