from pprint import pprint as pp  # noqa

import requests

####################
# Configure Requests
####################
session = requests.Session()
BASE_URL = "http://0.0.0.0:5560/fhir"
headers = {
    "User-Agent": "Jasper FHIR Client",
    "Content-Type": "application/fhir+json;charset=utf-8",
    "Accept": "application/fhir+json;charset=utf-8",
}
session.headers.update(headers)

##################
# Create a Patient
##################
patient1 = {
    "resourceType": "Patient",
    "id": "fc345f70-a76d-4088-a838-3f6f22cdafda",
    "name": [{"family": "Beahan", "given": ["Roscoe"]}],
    "gender": "male",
    "birthDate": "1971-08-09",
    "address": [{"city": "Boston", "state": "MA", "postalCode": "02215"}],
}

response = session.put(f"{BASE_URL}/Patient/{patient1['id']}", json=patient1)
# should create a new Patient
assert response.status_code == 201

##################
# Create a Patient
##################
patient2 = {
    "resourceType": "Patient",
    "id": "68935564-9414-49e6-a96a-6f6cb1a3fc61",
    "name": [{"family": "Beahan", "given": ["Margarette"]}],
    "gender": "female",
    "birthDate": "1974-03-14",
    "address": [{"city": "Boston", "state": "MA", "postalCode": "02215"}],
}
response = session.put(f"{BASE_URL}/Patient/{patient2['id']}", json=patient2)
# should create a new Patient
assert response.status_code == 201

########################
# Fetch Patient Resource
########################
# run in REPL
# resp = session.get(f"{BASE_URL}/Patient/{patient1['id']}")
# resp = session.get(f"{BASE_URL}/Patient/{patient2['id']}")

####################################
# Search for Patients by family name
####################################
# run in REPL
# resp = session.get(f"{BASE_URL}/Patient?family=Beahan")
