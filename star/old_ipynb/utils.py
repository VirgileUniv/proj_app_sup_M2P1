

PATH_TRAIN = 'data/stars_train_new.csv'
PATH_TEST = 'data/stars_test_new.csv'
NJOBS = 1

SEED = 1234


import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split



def load_data(test_size=None, train_size=None, test=False, random_state=SEED) :
    '''
    load the data make train/test split

    Parameters
    ----------
    test_size : float or int, default=None
        If float, should be between 0.0 and 1.0 and represent the proportion
        of the dataset to include in the test split. If int, represents the
        absolute number of test samples. If None, the value is set to the
        complement of the train size. If ``train_size`` is also None, it will
        be set to 0.25.

    train_size : float or int, default=None
        If float, should be between 0.0 and 1.0 and represent the
        proportion of the dataset to include in the train split. If
        int, represents the absolute number of train samples. If None,
        the value is automatically set to the complement of the test size.
    
    test : bool, default=False
        if True load the test data of the project (labels unknown)
        if False load the train data

    Returns
    -------
    splitting : list, length=4 if not test, else length=2
        List containing train-test split of the data contained in the PATH file
    '''
    if test : 
        data = pd.read_csv(PATH_TEST)
        X = data.drop(columns=['obj_ID'])
        
        return train_test_split(X, test_size=test_size, train_size=train_size, random_state=random_state)
    
    else :
        data = pd.read_csv(PATH_TRAIN)
        X, Y = data.drop(columns=['obj_ID', 'label']).to_numpy(dtype=float), data['label'].to_numpy(dtype=int)
    
        return train_test_split(X, Y, test_size=test_size, train_size=train_size, random_state=random_state)


def dict_equality(d1, d2) : 
    shared_items = [k for k in d1.keys() if k in d2.keys() and np.all(d1[k] == d2[k])]
    return len(shared_items) == max(len(d1.keys()), len(d2.keys()))