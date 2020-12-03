# Teste do modelo
h2 = model.evaluate(
    x=test_samples,
    y=test_labels,
    verbose=VERBOSE,
)
# plot_model(model, to_file='model.png' ,show_shapes=True, show_layer_names=True, expand_nested=True, dpi=200)