# from sklearn.datasets import make_classification
# from sklearn.model_selection import train_test_split
# import numpy as np
# import tensorflow as tf
# import matplotlib.pyplot as plt

# #splitting the data into train and test sets
# x_train,x_test,y_train,y_test = train_test_split(x,y, test_size=0.2, random_state=2022)

# #print the train and test split shapes
# print("X train set: ", x_train.shape, "Xtest set: ", x_test.shape,
#       "y train set: ", y_train.shape, "y test set: ", y_test.shape)

# x,y = make_classification(n_samples=10000, n_informative=10, random_state=2022)

# model = tf.keras.Sequential([
#     tf.keras.layers.Dense(10, activation="relu", input_shape=(x_train.shape[1],)),
#     tf.keras.layers.Dense(10, activation="relu"),
#     tf.keras.layers.Dense(1, activation="sigmoid")
# ])

# model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# history = model.fit(x_train, y_train, epochs=20, validation_data=(x_test, y_test), verbose=1)

# #plot the loss of the models
# fig, ax = plt.subplots(figsize=(12, 6))
# plt.plot(history.history['loss'], label='train loss')
# plt.plot(history.history['val_loss'], label='test loss')
# plt.title('Loss')
# plt.xlabel('Epochs')
# plt.ylabel('Loss')
# plt.xticks(np.arange(0, 20, 1))
# plt.legend(['train loss', 'test loss'], loc='upper right')
# plt.show()