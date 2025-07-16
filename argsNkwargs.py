# *args (variable arguments) & **kwargs (keyword arguments)

def log(*argv, **kwargv):
  print(*argv)
  print(**kwargv)

log(1, 2, 3, env="Prod", status="Success")
