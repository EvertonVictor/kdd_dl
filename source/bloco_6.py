#Apaga as colunas que tem correlacao entre elas que seja maior que CORRCOEF_THRESHOLD
if CLEAN_DATASET:
    excluded = list()
    
    for index_1 in range(len(column_names)-1):
        for index_2 in range(len(column_names)-1):
            if column_names[index_1] not in excluded and column_names[index_2] not in excluded and index_1 != index_2:
                corrcoef = np.corrcoef(dataset[column_names[index_1]], dataset[column_names[index_2]])

                if abs(corrcoef[0][1]) > CORRCOEF_THRESHOLD:
                    excluded.append(column_names[index_2])
                
    dataset = dataset[dataset.columns.difference(excluded)]