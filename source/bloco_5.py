#Substitui os valores no dataset que sao string por numeros
dataset = dataset.replace(
    {"protocol_type": protocol_type_dict,
     "service": service_dict,
     "flag": flag_dict,
     "attack": attack_dict}
)

dataset = dataset.apply(pd.to_numeric)