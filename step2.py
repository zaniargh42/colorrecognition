npdata=[]
for i in imageaddress: 
    # load the image
    image = Image.open(i)
    # convert image to numpy array
    data = asarray(image)
    npdata.append(data)
    
data = np.array(npdata)
