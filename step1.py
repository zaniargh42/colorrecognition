#first step to build the model is to prepare the data. the data must be in the shape of an numpy array.

imageaddress=[]
label=[]
for x in os.listdir('the path of the files/'+'train/'):
    for y in os.listdir('the path of the files/'+'train/'+ x):
        imageaddress.append('the path of the files/'+'train/'+ x+'/'+y)
        label.append(x)
    
#now we have a list named imageaddress that includs addresses of all files and a list named labels that has the label of any image.
# this is a new comment to test the git/////momo