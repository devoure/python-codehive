import zipfile, os
path = os.getcwd()
filepath = path + '/randquiz_2.zip'
zipfile = zipfile.ZipFile(filepath)
zipfile.extractall()
zipfile.close()
