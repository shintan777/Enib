import os
root ='Training Data Set'
lis = os.listdir(root)

os.system('mkdir Data')

for folders in lis:
    #folder_name = '\ '.join(folders.split())
    #print(folders)
    for filename in os.listdir(root +'/' + folders):
        #print(filename)
        new_file = '_'.join(folders.split()) + '_' + filename
        print(new_file)
        #cmd = 'cp ' + root  + folder_name + '/' + filename + ' Data/' + '_'.join(folder_name.split('\ ')) + '_' + filename
        cmd = 'cp Training\ Data\ Set' + '/' + folders + '/' + filename + ' Data/' + '_'.join(folders.split()) + '_' + filename
        print(cmd)
        os.system(cmd)
    #print(folders)
