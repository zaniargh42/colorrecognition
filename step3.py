labels=[]
labels_name={'black':0,
 'blue':1,
 'brown':2,
 'green':3,
 'grey':4,
 'orange':5,
 'pink':6,
 'purple':7,
 'red':8,
 'silver':9,
 'white':10,
 'yellow':11}
for i in label:
    labels.append(labels_name[i])

labels = np.array(labels)
