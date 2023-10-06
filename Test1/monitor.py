import psutil
import json
import datetime

# Define the service names and their respective hosts
service_hosts = {
    "httpd": "host1",
    "rabbitMQ": "host2",
    "postgreSQL": "host3"
}

# Define the application name
application_name = "rbcapp1"

# Create a dictionary to store service status
service_status = {}

# Check the status of each service on its host
for service, host in service_hosts.items():
    try:
        # Use the psutil library to check if the service process is running on the host
        if psutil.ssh.service_running(service, host=host):
            service_status[service] = "UP"
        else:
            service_status[service] = "DOWN"
    except Exception as e:
        service_status[service] = "ERROR"
        print(f"Error checking status of {service} on {host}: {str(e)}")

# Determine the overall application status
application_status = "UP" if "DOWN" not in service_status.values() else "DOWN"

# Create a JSON object
data = {
    "service_name": application_name,
    "service_status": application_status,
    "timestamp": str(datetime.datetime.now())
}

# Write JSON object to a file
file_name = f"{application_name}-status-{data['timestamp']}.json"
with open(file_name, "w") as json_file:
    json.dump(data, json_file, indent=4)

print(f"JSON file '{file_name}' created.")
