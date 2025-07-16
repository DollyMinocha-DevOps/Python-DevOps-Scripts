# *args (variable arguments) & **kwargs (keyword arguments)

# used when we are not sure about the number of arguments to be passed to a function.

def log(*argv, **kwargv):
  print(*argv)
  print(**kwargv)

log(1, 2, 3, env="Prod", status="Success")
