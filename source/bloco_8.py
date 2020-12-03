input_shape = (train_samples.shape[1],)

# Criacao do modelo
model = Sequential([
    Dense(15, input_shape=input_shape, activation=ACTIVATION_FN),
    Dense(15, activation=ACTIVATION_FN),
    Dense(15, activation=ACTIVATION_FN),
    Dense(15, activation=ACTIVATION_FN),
    Dense(15, activation=ACTIVATION_FN),
    Dense(len(attack_values), activation='softmax'),
])