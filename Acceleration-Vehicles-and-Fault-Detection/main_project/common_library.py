import numpy as np
import sys 
import keras 
import librosa 
import os 
import pandas as pd 
import seaborn as sns
import tensorflow as tf
import matplotlib.pyplot as plt
import random 
import warnings
import time 
import ast
import pickle
#from sklearn.externals import joblib
from keras.models import load_model
from sklearn.model_selection import cross_val_score,StratifiedKFold
from sklearn.metrics import multilabel_confusion_matrix
from libsvm.svmutil import *
from sklearn.multiclass import OneVsRestClassifier
from sklearn.metrics import make_scorer
from scipy.io.wavfile import read
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.metrics import accuracy_score
from sklearn.model_selection import StratifiedKFold, GridSearchCV
from sklearn.model_selection import KFold
from datetime import datetime
from sklearn.svm import SVC
from sklearn.utils import shuffle
from sklearn.datasets import make_classification
from sklearn.preprocessing import label_binarize
from sklearn.multioutput import MultiOutputClassifier
from sklearn.datasets import make_multilabel_classification
from sklearn.multiclass import OneVsOneClassifier
from scipy import sparse
from sklearn.svm import LinearSVC
from sklearn.metrics import make_scorer
from scipy.stats import loguniform
from skmultilearn.problem_transform import BinaryRelevance
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.metrics import balanced_accuracy_score
from sklearn.metrics import jaccard_score, hamming_loss