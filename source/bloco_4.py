#Pega os valores  unicos das colunas que tem string
protocol_type_values = dataset.protocol_type.unique()
service_values = dataset.service.unique()
flag_values = dataset.flag.unique()
attack_values = dataset.attack.unique()

#Transforma as strings em numeros
protocol_type_dict = dict(zip(protocol_type_values, range(len(protocol_type_values))))
service_dict = dict(zip(service_values, range(len(service_values))))
flag_dict = dict(zip(flag_values, range(len(flag_values))))
attack_dict = dict(zip(attack_values, range(len(attack_values))))