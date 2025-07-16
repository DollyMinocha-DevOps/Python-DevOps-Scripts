# Function to restart a list of services (e.g. Nginx, mysql, etc)

def restart_service(services):
  for service in services:
    print(f"Restarting{service}...")
    # os.system(f"systemctl restart {service}")

# usign subrpocess.run

import subprocess
def restart_service(services):
  for service in services:
    print(f"Restarting {service}...")
    result = subprocess.run(
          ["systemctl", "restart", service], 
          capture_output=True,
          text=True
    )
    if result.returncode == 0:
      print(f"{service} restarted successfully")
    else:
      print(f"Failed to restart {service}: {result.stderr}")

#This fucntion demonstrates how Python can be used to automate operational tasks in DevOps,
#like restarting mulitple services in a loop. It's simple, reusable, and easily extendable to handle errors or logs
#For Production scripts, using subprocess.run can allow logging with the logging module. It is better to use subprocess.run instead of os.system beacuse its safer and gives
#better error handling
