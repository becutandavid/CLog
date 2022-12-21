import numpy as np
import pandas as pd

TIME_INTERVAL_ = "300s"


def filter_(x, list_av):
    if x in list_av:
        return True
    else:
        return False


def create_dataset(dataset, valid_experiments):
    dataset["to_drop"] = dataset.test_id.apply(lambda x: filter_(x, valid_experiments))
    data = dataset[dataset.to_drop is True]
    data = data.drop(["to_drop"], axis=1)
    return data


normal_data = pd.read_csv("data/output/extracted_sequences_300s_new.csv")
normal_data = normal_data.drop(["Unnamed: 0"], axis=1)
abnormal_data = pd.read_csv("data/output/extracted_sequences_300s_new.csv")
abnormal_data = abnormal_data.drop(["Unnamed: 0"], axis=1)

experiments_normal = np.unique(normal_data.test_id)
experiments_abnormal = np.unique(abnormal_data.test_id)

SIZE_E_NORMAL = len(experiments_normal)
SIZE_E_ABNORMAL = len(experiments_abnormal)

# TRAIN
SIZE_E_NORMAL_TRAIN = int(0.59 * SIZE_E_NORMAL)
SIZE_E_NORMAL_VALID = int(0.5 * (1 - 0.59) * SIZE_E_NORMAL)

train_indecies_normal = np.random.choice(experiments_normal, size=SIZE_E_NORMAL_TRAIN, replace=False)
valid_indecies_normal = np.random.choice(
    list(set(experiments_normal).difference(set(train_indecies_normal))), size=SIZE_E_NORMAL_VALID, replace=False
)
test_indecies_normal = np.array(
    list(set(experiments_normal).difference(set(train_indecies_normal)).difference(set(valid_indecies_normal)))
)
assert (
    train_indecies_normal.shape[0] + valid_indecies_normal.shape[0] + test_indecies_normal.shape[0] == SIZE_E_NORMAL
), "Indecies are lost"

# VALID
SIZE_E_ABNORMAL_VALID = int(0.5 * SIZE_E_ABNORMAL)
valid_indecies_abnormal = np.random.choice(experiments_abnormal, size=SIZE_E_ABNORMAL_VALID, replace=False)
test_indecies_abnormal = np.array(list(set(experiments_abnormal).difference(set(valid_indecies_abnormal))))
assert valid_indecies_abnormal.shape[0] + test_indecies_abnormal.shape[0] == SIZE_E_ABNORMAL, "Indecies are lost"


train_normal = create_dataset(normal_data, train_indecies_normal)
valid_normal = create_dataset(normal_data, valid_indecies_normal)
test_normal = create_dataset(normal_data, test_indecies_normal)

valid_abnormal = create_dataset(abnormal_data, valid_indecies_abnormal)
test_abnormal = create_dataset(abnormal_data, test_indecies_abnormal)

path = "data/"
train_normal.to_csv(path + "train_valid_test_splits/train_normal_" + TIME_INTERVAL_ + ".csv", index=False)
valid_normal.to_csv(path + "train_valid_test_splits/valid_normal_" + TIME_INTERVAL_ + ".csv", index=False)
test_normal.to_csv(path + "train_valid_test_splits/test_normal_" + TIME_INTERVAL_ + ".csv", index=False)

valid_abnormal.to_csv(path + "train_valid_test_splits/valid_abnormal_" + TIME_INTERVAL_ + ".csv", index=False)
test_abnormal.to_csv(path + "train_valid_test_splits/test_abnormal_" + TIME_INTERVAL_ + ".csv", index=False)
