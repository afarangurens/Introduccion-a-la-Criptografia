import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

celsius_entries = np.array([-40, -10, 0, 8, 15, 22, 38], dtype=float)
fahrenheit_expected_outputs = np.array([-40, 14, 32, 46, 59, 72, 100], dtype=float)

layer = tf.keras.layers.Dense(units=1, input_shape=[1])
model = tf.keras.Sequential([layer])

model.compile(
    optimizer=tf.keras.optimizers.Adam(0.1),
    loss='mean_squared_error'
)

print("Training started")

history = model.fit(celsius_entries, fahrenheit_expected_outputs, epochs=1000)

print("Training finished")


plt.xlabel("# Generation")
plt.ylabel("Loss magnitude")
plt.plot(history.history["loss"])
plt.show()

res = model.predict([100.0])

print("Res=" + str(res))
