import os

d=os.listdir('.')
i=8
for file in d:
    if 'Snipaste' in file:
        #print(file)
        suffix=file[file.find('.'):]
        #print(suffix)
        cmd='rename {} {}'.format(file,str(i)+suffix)
        print(cmd)
        os.system(cmd)
        i+=1
        
