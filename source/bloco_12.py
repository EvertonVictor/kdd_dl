# plot_model(model, to_file='model.png')

# Plot training & validation accuracy values
plt.figure(figsize=(10,5))
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('Model accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper left')
plt.show()

# Plot training & validation loss values
plt.figure(figsize=(10,5))
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper left')
plt.show()

print(model.metrics_names)
print(h2)

print({
"CLEAN_DATASET":CLEAN_DATASET,
"DATASET_COMPLETO":DATASET_COMPLETO,
"CORRCOEF_THRESHOLD":CORRCOEF_THRESHOLD,
"BATCH_SIZE":BATCH_SIZE,
"EPOCHS":EPOCHS,
"SHUFFLE":SHUFFLE,
"VERBOSE":VERBOSE,
"VALIDATION_SPLIT":VALIDATION_PERCENTAGE,
"LEARNING_RATE":LEARNING_RATE,
"ACTIVATION_FN":ACTIVATION_FN,
"TEMPO": end_time-start_time})