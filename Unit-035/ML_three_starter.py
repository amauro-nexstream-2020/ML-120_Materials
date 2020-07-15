import numpy as np
from keras.models import Sequential
from keras.layers.core import Dense
from datetime import datetime
import tensorflow as tf
from tensorflow import keras


# Step 1: Create input (training) data

# Rock     == 0
# Paper    == 1
# Scissors == 2
# [Player1, Player2] --> [P1,P2]
training_data = np.array([[0,0],[0,1],[0,2], <PUT DATA HERE> ], "float32")
print(training_data.shape)


# Step 2: Create corresponding output (target) data

# 1 for whoever wins - [P1,P2], where  [0,0] is tie
target_data = np.array([[0,0], [0,1], [1,0], <PUT DATA HERE> ]) 
print(target_data.shape)


# Step 3: Create the neural network
model = keras.Sequential([
      keras.layers.Dense(10, input_dim=2, activation='relu'),
      keras.layers.Dense(10, activation='relu'),
      keras.layers.Dense(10, activation='relu'),
      keras.layers.Dense(2, activation='sigmoid')
])


# Step 4: Compile the neural network
model.compile(loss='mean_squared_error',
              optimizer='adam',
              metrics=['accuracy'])



# Step 5: Feed the neural network the training and target data
model.fit(training_data, target_data, epochs=1000)


# Step 6: Output unrounded and rounded predictions of the model
pred = model.predict(training_data).round()

print("Model's Unrounded Prediction: \n" + pred)
print("Model's Rounded Prediction: \n" + pred.round())
print("Model's Target Data: \n" + target_data)

comparison = pred.round == target_data
if(comparison.all()):
   print('The model is correct!')
else:
   print('The model is not correct!')
