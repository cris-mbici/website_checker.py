import csv # Imports the module to read csv files
import requests # Allows you to make requests to these websites

while True:
  user_ready = input("Are you ready to initiate the website checker?(y/n) ")
  if user_ready == "y":
     print("Checking websites...")
     break
  elif user_ready == "n":
     print("Terminating program...")
     quit()
     break
  else:
     print("Please enter a valid input...")
     continue


#Now we need to open the file in read mode
with open("test_sites.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader: #Basically saying for every row in the file, run the commands that follow
        url = row[0]

        try:
          response = requests.get(url, timeout=5)
          #I tried to include the most common response codes here
          if response.status_code == 200: #Our webiste exists
            print(f"{url} is ONLINE")
          elif response.status_code == 404: #Our website couldn't be found
            print(f"{url} is NOT FOUND")
          elif response.status_code == 403: #Our webiste doesn't allow requests
            print(f"{url} is BLOCKED")
          elif response.status_code == 429: #Our website has DDoS protection and we triggered it
            print(f"{url} is RATE LIMITED (doesn't allow too many requests)")
          else:
            print(f"{url} returned status code {response.status_code} ") #Just outright prints the response code

        except requests.exceptions.RequestException: #Error handling
           print(f"{url} is OFFLINE")