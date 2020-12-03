#Separa os dados entre treino e teste
train, test = np.split(dataset.sample(frac=1), [int(TRAIN_PERCENTAGE * len(dataset))])

train_samples = train.drop(['attack'], axis=1)
train_labels = to_categorical(train[['attack']].to_numpy(), num_classes=len(attack_values))

test_samples = test.drop(['attack'], axis=1)
test_labels = to_categorical(test[['attack']].to_numpy(), num_classes=len(attack_values))