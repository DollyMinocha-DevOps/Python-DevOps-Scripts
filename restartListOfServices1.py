# Function to restart a list of services (e.g. Nginx, mysql, etc)
def restart_service(services):
  for service in services:
    print(f"Restarting{service}...")
