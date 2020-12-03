start_time = time.time()

# Treinamento do modelo
history = model.fit(
    x=train_samples, 
    y=train_labels, 
    batch_size=BATCH_SIZE, 
    epochs=EPOCHS,
    shuffle=SHUFFLE, #Mistura os dados
    verbose=VERBOSE,
    validation_split=VALIDATION_PERCENTAGE #Porcentagem dos dados de treino que serao usadas para validacao
)

end_time = time.time()