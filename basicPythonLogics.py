# Simple FOR Loop - iterates over a sequence(list, tuple, string, range)
for i in range(5):
  print(i)


# Simple WHILE Loop - repeats until a condition is False
count = 0
while count < 5:
  print(count)
  count += 1
  

# BREAK and CONTINUE 
for i in range(10):
  if i == 5:
    break # Exit Loop
  if i % 2 == 0:
    continue
  print(i)
  

# Function with return values
def greet(name):
  return(f"Hello{name}")

print(greet("DevOps")

      
# Default Parameters in Fucntions
def deploy(app="Nginx"):
  print(f"deploying{app})

deploy()            # Deploying Nginx
deploy(Apache)      # Deploying Apache

