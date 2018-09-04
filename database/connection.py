from sqlalchemy import create_engine, Column, Integer, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import numpy as np

Base = declarative_base()

class kdd_dataset(Base):
    __tablename__ = "kdd_dataset_clean"

    id = Column('id', Integer, primary_key=True)
    duration = Column('duration', Float)
    protocol_type = Column('protocol_type', Integer)
    service = Column('service', Integer)
    flag = Column('flag', Integer)
    src_bytes = Column('src_bytes', Float)
    dst_bytes = Column('dst_bytes', Float)
    land = Column('land', Float)
    wrong_fragment = Column('wrong_fragment', Float)
    urgent = Column('urgent', Float)
    hot = Column('hot', Float)
    num_failed_logins = Column('num_failed_logins', Float)
    logged_in = Column('logged_in', Float)
    num_compromised = Column('num_compromised', Float)
    root_shell = Column('root_shell', Float)
    su_attempted = Column('su_attempted', Float)
    num_root = Column('num_root', Float)
    num_file_creations = Column('num_file_creations', Float)
    num_shells = Column('num_shells', Float)
    num_access_files = Column('num_access_files', Float)
    num_outbound_cmds = Column('num_outbound_cmds', Float)
    is_host_login = Column('is_host_login', Float)
    is_guest_login = Column('is_guest_login', Float)
    count = Column('count', Float)
    srv_count = Column('srv_count', Float)
    serror_rate = Column('serror_rate', Float)
    srv_serror_rate = Column('srv_serror_rate', Float)
    rerror_rate = Column('rerror_rate', Float)
    srv_rerror_rate = Column('srv_rerror_rate', Float)
    same_srv_rate = Column('same_srv_rate', Float)
    diff_srv_rate = Column('diff_srv_rate', Float)
    srv_diff_host_rate = Column('srv_diff_host_rate', Float)
    dst_host_count = Column('dst_host_count', Float)
    dst_host_srv_count = Column('dst_host_srv_count', Float)
    dst_host_same_srv_rate = Column('dst_host_same_srv_rate', Float)
    dst_host_diff_srv_rate = Column('dst_host_diff_srv_rate', Float)
    dst_host_same_src_port_rate = Column('dst_host_same_src_port_rate', Float)
    dst_host_srv_diff_host_rate = Column('dst_host_srv_diff_host_rate', Float)
    dst_host_serror_rate = Column('dst_host_serror_rate', Float)
    dst_host_srv_serror_rate = Column('dst_host_srv_serror_rate', Float)
    dst_host_rerror_rate = Column('dst_host_rerror_rate', Float)
    dst_host_srv_rerror_rate = Column('dst_host_srv_rerror_rate', Float)
    attack_type = Column('attack_type', Integer)


engine = create_engine('mysql+mysqlconnector://root:123456@localhost:3306/kdd', echo=False)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)

features = [kdd_dataset.duration,kdd_dataset.protocol_type,kdd_dataset.service,kdd_dataset.flag,kdd_dataset.src_bytes,kdd_dataset.dst_bytes,kdd_dataset.land,kdd_dataset.wrong_fragment,kdd_dataset.urgent,kdd_dataset.hot,kdd_dataset.num_failed_logins,kdd_dataset.logged_in,kdd_dataset.num_compromised,kdd_dataset.root_shell,kdd_dataset.su_attempted,kdd_dataset.num_root,kdd_dataset.num_file_creations,kdd_dataset.num_shells,kdd_dataset.num_access_files,kdd_dataset.num_outbound_cmds,kdd_dataset.is_host_login,kdd_dataset.is_guest_login,kdd_dataset.count,kdd_dataset.srv_count,kdd_dataset.serror_rate,kdd_dataset.srv_serror_rate,kdd_dataset.rerror_rate,kdd_dataset.srv_rerror_rate,kdd_dataset.same_srv_rate,kdd_dataset.diff_srv_rate,kdd_dataset.srv_diff_host_rate,kdd_dataset.dst_host_count,kdd_dataset.dst_host_srv_count,kdd_dataset.dst_host_same_srv_rate,kdd_dataset.dst_host_diff_srv_rate,kdd_dataset.dst_host_same_src_port_rate,kdd_dataset.dst_host_srv_diff_host_rate,kdd_dataset.dst_host_serror_rate,kdd_dataset.dst_host_srv_serror_rate,kdd_dataset.dst_host_rerror_rate,kdd_dataset.dst_host_srv_rerror_rate,kdd_dataset.attack_type]
erased_features = []
session = Session()

i = 0
j = 1

while i < len(features):
    col1 = session.query(features[i]).all()
    col1 = (np.asarray(col1)[:, 0]).astype(np.float)

    while j < len(features):
        print(f"Rodando {features[i]} e {features[j]}")
        col2 = session.query(features[j]).all()
        col2 = (np.asarray(col2)[:, 0]).astype(np.float)
        corrcoef = np.corrcoef(col1, col2)

        if abs(corrcoef[0][1]) > 0.5:
            print(f"Apagando {features[j]}")
            features.remove(features[j])
        else:
            j = j + 1

    i = i + 1
    j = i + 1

for feature in features:
    print(feature)
