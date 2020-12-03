import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import keras
from keras import backend as K
from keras.models import Sequential
from keras.layers import Activation
from keras.layers.core import Dense
from keras.optimizers import Adam
from keras.metrics import categorical_crossentropy
from keras.utils import plot_model
from keras import optimizers
from keras.utils import to_categorical
import time