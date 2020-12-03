sgd = optimizers.SGD(lr=LEARNING_RATE)
model.compile(loss='mean_squared_error', optimizer=sgd)

model.compile(
    optimizer=sgd,
    loss='mean_squared_error', 
    metrics=['accuracy'],
)