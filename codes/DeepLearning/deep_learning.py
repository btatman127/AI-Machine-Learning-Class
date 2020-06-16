import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import itertools
from tensorflow import keras


def unpickle(file):
    """Adapted from the CIFAR page: http://www.cs.utoronto.ca/~kriz/cifar.html"""
    import pickle
    with open(file, 'rb') as fo:
        return pickle.load(fo, encoding='bytes')


# Read the data
data_dir = 'cifar-10-batches-py/' #my laptop
# batches 1,2,3,4 are training sets
train = [unpickle(data_dir + 'data_batch_{}'.format(i)) for i in [1, 2, 3, 4]]
X_train = np.stack([t[b'data'] for t in train])
X_train = tf.transpose(tf.reshape(X_train, [-1, 3, 32, 32]), (0, 2, 3, 1))
y_train = list(itertools.chain(*[t[b'labels'] for t in train]))
y_train = np.array(y_train)

# batch 5 is validation set
batch5 = unpickle(data_dir + 'data_batch_5')
X_valid = batch5[b'data']
X_valid = tf.transpose(tf.reshape(X_valid, [-1, 3, 32, 32]), (0, 2, 3, 1))
y_valid = np.array(batch5[b'labels'])

labels = unpickle(data_dir + 'batches.meta')[b'label_names']

# https://www.pyimagesearch.com/2018/12/31/keras-conv2d-and-convolutional-layers/
# ^ good source to understand what is happening here
model = keras.models.Sequential()
model.add(keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))
model.add(keras.layers.MaxPooling2D((2, 2)))
model.add(keras.layers.Conv2D(64, (3, 3), activation='relu'))
model.add(keras.layers.MaxPooling2D((2, 2)))
model.add(keras.layers.Conv2D(64, (3, 3), activation='relu'))
model.add(keras.layers.Flatten())
model.add(keras.layers.Dense(64, activation='relu'))
# there are 10 classes
model.add(keras.layers.Dense(10))

model.compile(loss=keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              optimizer=keras.optimizers.Adam(learning_rate=0.001),
              metrics=["accuracy"])

# Train the network
model.fit(X_train, y_train, epochs=30, validation_data=(X_valid, y_valid))

# Test the network on one image
predictions = model.predict_classes(X_train)

i = 42
plt.imshow(X_train[i])
# prediction
print(f'{predictions[i]}: {labels[predictions[i]]}')
# correct answer
print(f'{y_train[i]}: {labels[y_train[i]]}')
plt.show()
