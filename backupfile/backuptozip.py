#! /usr/bin/python
'''
A python script that will backup a folder into a zip folder
'''

import zipfile, os

def backuptozip(folder):

    folder = os.path.abspath(folder)

    number = 1
    while True:
        zipfilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipfilename):
            break
        number = number + 1
    print('Creating backup for {}'.format(zipfilename))
    backupzip = zipfile.ZipFile(zipfilename, 'w')

    for foldername , subfolder, filenames in os.walk(folder):
        print('Backup files in folder {}'.format(foldername))
        backupzip.write(foldername)
        for a in filenames:
            newbase = os.path.basename(folder) + '_'
            if a.startswith(newbase) and a.endswith('.zip'):
                continue
            backupzip.write(os.path.join(foldername, a))
    backupzip.close()
    print('Done Backing Up')
path = os.getcwd()
backuptozip(path+'/randquiz')


