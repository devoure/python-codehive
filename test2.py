import shelve

variable = shelve.open('myvariables')
variable['utd']
print(variable['utd'])
variable.close()
