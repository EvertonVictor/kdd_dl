from sqlalchemy import create_engine, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import database.models.kddcup_dataset as kdd_model
import database.models.kddcup_dataset_clean as kdd_clean_model
#import numpy as np
import cupy as cp

cp.corrco

def main():


    Base = declarative_base()

    engine = create_engine('mysql+mysqlconnector://root:123456@localhost:3306/kdd', echo=False)
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    #determine_correlation(session)
    feature_scaling(session)

def feature_scaling(session):
    print("Feature scaling")
    features = [kdd_clean_model.kdd_dataset.duration, kdd_clean_model.kdd_dataset.protocol_type,
                kdd_clean_model.kdd_dataset.flag, kdd_clean_model.kdd_dataset.src_bytes,
                kdd_clean_model.kdd_dataset.dst_bytes,
                kdd_clean_model.kdd_dataset.land, kdd_clean_model.kdd_dataset.wrong_fragment,
                kdd_clean_model.kdd_dataset.urgent, kdd_clean_model.kdd_dataset.hot,
                kdd_clean_model.kdd_dataset.num_failed_logins,
                kdd_clean_model.kdd_dataset.logged_in, kdd_clean_model.kdd_dataset.num_compromised,
                kdd_clean_model.kdd_dataset.root_shell, kdd_clean_model.kdd_dataset.num_file_creations,
                kdd_clean_model.kdd_dataset.num_shells, kdd_clean_model.kdd_dataset.num_access_files,
                kdd_clean_model.kdd_dataset.num_outbound_cmds, kdd_clean_model.kdd_dataset.is_host_login,
                kdd_clean_model.kdd_dataset.diff_srv_rate, kdd_clean_model.kdd_dataset.srv_diff_host_rate,
                kdd_clean_model.kdd_dataset.dst_host_srv_diff_host_rate]

    max = (session.query(func.max(kdd_clean_model.kdd_dataset.duration)).one())[0]
    min = (session.query(func.min(kdd_clean_model.kdd_dataset.duration)).one())[0]
    avg = (session.query(func.avg(kdd_clean_model.kdd_dataset.duration)).one())[0]

    print(f"Query... Max {max} Min {min} Avg {avg}")
    session.query(kdd_clean_model.kdd_dataset).update({kdd_clean_model.kdd_dataset.duration : (kdd_clean_model.kdd_dataset.duration - avg)/(max - min)})
    session.commit()
    print("Comitado")



def determine_correlation(session):
    features = [kdd_model.kdd_dataset.duration, kdd_model.kdd_dataset.protocol_type, kdd_model.kdd_dataset.service,
                kdd_model.kdd_dataset.flag, kdd_model.kdd_dataset.src_bytes, kdd_model.kdd_dataset.dst_bytes,
                kdd_model.kdd_dataset.land, kdd_model.kdd_dataset.wrong_fragment, kdd_model.kdd_dataset.urgent,
                kdd_model.kdd_dataset.hot, kdd_model.kdd_dataset.num_failed_logins, kdd_model.kdd_dataset.logged_in,
                kdd_model.kdd_dataset.num_compromised, kdd_model.kdd_dataset.root_shell,
                kdd_model.kdd_dataset.su_attempted, kdd_model.kdd_dataset.num_root,
                kdd_model.kdd_dataset.num_file_creations, kdd_model.kdd_dataset.num_shells,
                kdd_model.kdd_dataset.num_access_files, kdd_model.kdd_dataset.num_outbound_cmds,
                kdd_model.kdd_dataset.is_host_login, kdd_model.kdd_dataset.is_guest_login, kdd_model.kdd_dataset.count,
                kdd_model.kdd_dataset.srv_count, kdd_model.kdd_dataset.serror_rate,
                kdd_model.kdd_dataset.srv_serror_rate, kdd_model.kdd_dataset.rerror_rate,
                kdd_model.kdd_dataset.srv_rerror_rate, kdd_model.kdd_dataset.same_srv_rate,
                kdd_model.kdd_dataset.diff_srv_rate, kdd_model.kdd_dataset.srv_diff_host_rate,
                kdd_model.kdd_dataset.dst_host_count, kdd_model.kdd_dataset.dst_host_srv_count,
                kdd_model.kdd_dataset.dst_host_same_srv_rate, kdd_model.kdd_dataset.dst_host_diff_srv_rate,
                kdd_model.kdd_dataset.dst_host_same_src_port_rate, kdd_model.kdd_dataset.dst_host_srv_diff_host_rate,
                kdd_model.kdd_dataset.dst_host_serror_rate, kdd_model.kdd_dataset.dst_host_srv_serror_rate,
                kdd_model.kdd_dataset.dst_host_rerror_rate, kdd_model.kdd_dataset.dst_host_srv_rerror_rate,
                kdd_model.kdd_dataset.attack_type]

    erased_features = []

    i = 0
    j = 1

    while i < len(features):
        col1 = session.query(features[i]).all()
        col1 = (np.asarray(col1)[:, 0]).astype(np.float)

        while j < len(features):
            col2 = session.query(features[j]).all()
            col2 = (np.asarray(col2)[:, 0]).astype(np.float)
            corrcoef = np.corrcoef(col1, col2)

            if abs(corrcoef[0][1]) > 0.5:
                print(f"Removendo {features[j]}")
                erased_features.append(features[j])
                features.remove(features[j])
            else:
                j = j + 1

        i = i + 1
        j = i + 1

    for feature in features:
        print("Features mantidas:")
        print(feature)

    for erased in erased_features:
        print("Features apagadas:")
        print(erased)

if __name__ == '__main__':
    main()