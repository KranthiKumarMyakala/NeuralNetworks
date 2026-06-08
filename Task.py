# # from sklearn.datasets import make_classification
# # from sklearn.model_selection import train_test_split
# # import numpy as np
# # import tensorflow as tf
# # import matplotlib.pyplot as plt

# # #splitting the data into train and test sets
# # x_train,x_test,y_train,y_test = train_test_split(x,y, test_size=0.2, random_state=2022)

# # #print the train and test split shapes
# # print("X train set: ", x_train.shape, "Xtest set: ", x_test.shape,
# #       "y train set: ", y_train.shape, "y test set: ", y_test.shape)

# # x,y = make_classification(n_samples=10000, n_informative=10, random_state=2022)

# # model = tf.keras.Sequential([
# #     tf.keras.layers.Dense(10, activation="relu", input_shape=(x_train.shape[1],)),
# #     tf.keras.layers.Dense(10, activation="relu"),
# #     tf.keras.layers.Dense(1, activation="sigmoid")
# # ])

# # model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# # history = model.fit(x_train, y_train, epochs=20, validation_data=(x_test, y_test), verbose=1)

# # #plot the loss of the models
# # fig, ax = plt.subplots(figsize=(12, 6))
# # plt.plot(history.history['loss'], label='train loss')
# # plt.plot(history.history['val_loss'], label='test loss')
# # plt.title('Loss')
# # plt.xlabel('Epochs')
# # plt.ylabel('Loss')
# # plt.xticks(np.arange(0, 20, 1))
# # plt.legend(['train loss', 'test loss'], loc='upper right')
# # plt.show()

# import tensorflow as tf
# import keras
# from keras.datasets import mnist
# from keras.models import Sequential
# from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
# from keras import backend as K

# #Load data
# (x_train, y_train), (x_test, y_test) = mnist.load_data()

# #Reshape input data to include the channel dimension
# x_train = x_train.reshape(x_train.shape[0], 28, 28, 1).astype('float32') / 255
# x_test = x_test.reshape(x_test.shape[0], 28, 28, 1).astype('float32') / 255

# #Convert labels to one-hot encoding
# y_train = keras.utils.to_categorical(y_train, 10)
# y_test = keras.utils.to_categorical(y_test, 10)

# def build_model(optimizer):
#     model = Sequential()
#     model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(28, 28, 1)))
#     model.add(Conv2D(64, (3, 3), activation='relu'))
#     model.add(MaxPooling2D(pool_size=(2, 2)))
#     model.add(Dropout(0.25))
#     model.add(Flatten())
#     model.add(Dense(128, activation='relu'))
#     model.add(Dropout(0.5))
#     model.add(Dense(10, activation='softmax'))

#     model.compile(loss=keras.losses.categorical_crossentropy,
#                   optimizer=optimizer,
#                   metrics=['accuracy'])
#     return model

#     optimizers = ['Adadelta', 'Adam', 'Adagrad', 'RMSprop', 'SGD']
# history_dict = {}

# for opt in optimizers:
#     print("Training with {}".format(opt))
#     model = build_model(opt)
#     history = model.fit(x_train, y_train,
#                         batch_size=64,
#                         epochs=10,
#                         verbose=1,
#                         validation_data=(x_test, y_test))
#     history_dict[opt] = history

#     import matplotlib.pyplot as plt

# # Plotting the training and validation accuracy for each optimizer
# plt.figure(figsize=(12, 6))
# for opt in optimizers:
#     plt.plot(history_dict[opt].history['accuracy'], label=f'{opt} Train Accuracy')

# plt.title('Training Accuracy for Different Optimizers')
# plt.xlabel('Epochs')
# plt.ylabel('Accuracy')
# plt.legend()
# plt.grid(True)
# plt.show()