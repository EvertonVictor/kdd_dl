# Flag para remocao das colunas correlacionadas.
CLEAN_DATASET = True

# Flag para decisao de qual versao do dataset usar
DATASET_COMPLETO = False

# Caminho para o dataset
# Endereco para download: http://kdd.ics.uci.edu/databases/kddcup99/kddcup99.html
# Backup: http://web.archive.org/web/*/http://kdd.ics.uci.edu/databases/kddcup99/kddcup99.html
if DATASET_COMPLETO:
    DATASET_PATH = "D:/UNIFEI/TCC/kdd_dl/dataset/kddcup.data.corrected"   
    # Treino 98%, Validacao 1%, Teste 1%
    # https://stackoverflow.com/a/13613316
    TRAIN_PERCENTAGE = 0.98
    VALIDATION_PERCENTAGE = 0.01
    TEST_PERCENTAGE = 0.01
else:
    DATASET_PATH = "D:/UNIFEI/TCC/kdd_dl/dataset/kddcup.data_10_percent_corrected"
    # Treino 80%, Validacao 10%, Teste 10%
    TRAIN_PERCENTAGE = 0.8
    VALIDATION_PERCENTAGE = 0.1
    TEST_PERCENTAGE = 0.1
    
## Threshold de correlacao para exclusao das colunas do dataset
CORRCOEF_THRESHOLD = 0.5

## Ignora os warnings de divisao por NaN
np.seterr(divide='ignore', invalid='ignore')


EPOCHS = 200 # Quantas vezes os dados serao corridos completamente
BATCH_SIZE = 1024 # Quantas linhas do dataset serao lidas por vez
SHUFFLE = True # Mistura os dados antes do treino
VERBOSE = 1 # 0 - Desativa os logs durante o treino, 1 - Imprime os logs durante o treino
LEARNING_RATE = 0.01 # Taxa de aprendizado
ACTIVATION_FN = "relu" # Funcao de ativacao