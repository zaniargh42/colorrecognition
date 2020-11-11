from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)

# the code is not perfectly clear here. but it works! you can do it by yourself. it's too easy

from collections import Counter

a=Counter(labels).keys() # equals to list(set(words))
b=Counter(labels).values() # counts the elements' frequency
a=[5, 6, 2, 0, 3, 4, 1, 7]
b=[318, 341, 681, 334, 704, 686, 651, 306]
c=[]
for i in b:
  c.append(1-(i/sum(b)))

cweight={0:0.9169,
        1:0.8380,
        2:0.8306,
        3:0.8249,
        4:0.8293,
        5:0.9209,
        6:0.9151,
        7:0.9238}
