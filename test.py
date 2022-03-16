import os, shelve

shelfile = shelve.open('myvariables')
utdplayers = ['Ororo', 'Bruno', 'Degea']
shelfile['utd'] = utdplayers
shelfile.close()




