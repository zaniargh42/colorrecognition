#step 4
# train_test spliting

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)

# step5
#calculates the class weights
from sklearn.utils import class_weight

class_weights = class_weight.compute_class_weight('balanced',np.unique(label),label)

# step6
# converting labelsets to categorical sets

y_train = keras.utils.to_categorical(y_train,num_classes=8)
y_test = keras.utils.to_categorical(y_test, num_classes=8)
