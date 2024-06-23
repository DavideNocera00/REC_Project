#!/usr/bin/python3
import sys
import time
import requests
    
param = sys.argv[1]

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


sys.exit(0)
