#!/usr/bin/python3
import sys
import time
import requests
    
param = sys.argv[1]

# Define your JWT token
jwt_token = "eyJhbGciOiJIUzI1NiJ9.eyJyb2xlIjoiQWRtaW5pc3RyYXRvciIsInVzZXJJZCI6IjY2NWYzMmM2ZDM3YmM0MjA5NTY1N2FmNiIsInN1YiI6Im1hdHRlby5kZXZpdGlzQGdtYWlsLmNvbSIsImlhdCI6MTcxODk2NDA4NSwiZXhwIjoxNzE5MDAwMDg1fQ.EEFqcAiTH0LEvoRHkbaoh0ZkmsXxiR7cAbGl5fRtxwI"

# Define the headers
headers = {
    "Authorization": f"Bearer {jwt_token}"
}

print(f"{sys.argv[1]}")
start_time = time.time()  # Record the start time
print("Timer started.")

# business logic
var = 0
for i in range(10):
	var = var + i
	time.sleep(1)
	print(f"{var}")

end_time = time.time()  # Record the end time
print("Timer stopped.")

elapsed_time = int(end_time - start_time)  # Calculate the difference
print(f"Elapsed time: {elapsed_time} seconds")

res = 60 - elapsed_time
time.sleep(res)

#url = f"http://resources-service:8080/api/resources/updateAvailability/{param}"

# Send the PUT request without JSON payload
#response = requests.put(url, headers=headers)

# Check the response status code and print the response
#if response.status_code == 200:
#    print("Request was successful.")
#else:
#    print(f"Failed to send request. Status code: {response.status_code}")

#print("Response content:", response.content.decode())

sys.exit(0)
