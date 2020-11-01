from collections import Counter
import sklearn
import sklearn.datasets as datasets
from imblearn.over_sampling import SMOTE, BorderlineSMOTE, ADASYN, SVMSMOTE, SMOTENC, KMeansSMOTE
from imblearn.under_sampling import ClusterCentroids, RandomUnderSampler, NearMiss
from sklearn.datasets import load_iris, make_classification, load_digits
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

DTC = DecisionTreeClassifier()
# iris = datasets.load_breast_cancer()# 近乎平衡
iris = load_iris()
X = iris.data[:, :2]
y = iris.target
# X, y = make_classification(n_classes=2, class_sep=2,
#                            weights=[0.9, 0.1], n_informative=10,
#                            n_redundant=1, flip_y=0,
#                            n_features=20, n_clusters_per_class=2,
#                            n_samples=500, random_state=10)
for i in range(len(y)):
    if y[i] != 1:
        y[i] = 0
    i += 1
kf = sklearn.model_selection.RepeatedKFold(n_splits=10, n_repeats=100)
f1_origin_list = []
f1_smote_list = []
f1_under_list = []
recall_origin_list = []
recall_smote_list = []
recall_under_list = []
precision_origin_list = []
precision_smote_list = []
precision_under_list = []
print("origin", Counter(y))
plt.scatter(X[y == 0, 0], X[y == 0, 1], color='g', marker='+', label="majority")
plt.scatter(X[y == 1, 0], X[y == 1, 1], color='b', marker='*', label="minority")
plt.legend()
plt.title('origin')
plt.xlabel('sepal length')
plt.ylabel('sepal width')
plt.show()
# X = iris.data
for train, test in kf.split(X):
    X_train = X[train]
    Y_train = y[train]
    X_test = X[test]
    Y_test = y[test]
    DTC.fit(X_train, Y_train)
    f1_nosmote = sklearn.metrics.f1_score(y_pred=DTC.predict(X=X_test), y_true=Y_test, zero_division=0)
    recall_nosmote = sklearn.metrics.recall_score(y_pred=DTC.predict(X=X_test), y_true=Y_test, zero_division=0)
    precision_nosmote = sklearn.metrics.precision_score(y_pred=DTC.predict(X=X_test), y_true=Y_test, zero_division=0)
    f1_origin_list.append(f1_nosmote)
    recall_origin_list.append(recall_nosmote)
    precision_origin_list.append(precision_nosmote)

X = iris.data[:, :2]
y = iris.target
over = SMOTE()
# smote = BorderlineSMOTE()
# smote = ADASYN()
# smote = SVMSMOTE()
# smote = KMeansSMOTE()
X, y = over.fit_sample(X=X, y=y)
print("SMOTE", Counter(y))
plt.scatter(X[y == 0, 0], X[y == 0, 1], color='g', marker='+', label="majority")
plt.scatter(X[y == 1, 0], X[y == 1, 1], color='b', marker='*', label="minority")
plt.legend()
plt.title(over)
plt.xlabel('sepal length')
plt.ylabel('sepal width')
plt.show()
# X = iris.data
for train, test in kf.split(X):
    X_train = X[train]
    Y_train = y[train]
    X_test = X[test]
    Y_test = y[test]
    DTC = DecisionTreeClassifier()
    DTC.fit(X_train, Y_train)
    f1_smote = sklearn.metrics.f1_score(y_pred=DTC.predict(X=X_test), y_true=Y_test, zero_division=0)
    recall_smote = sklearn.metrics.recall_score(y_pred=DTC.predict(X=X_test), y_true=Y_test, zero_division=0)
    precision_smote = sklearn.metrics.precision_score(y_pred=DTC.predict(X=X_test), y_true=Y_test, zero_division=0)
    f1_smote_list.append(f1_smote)
    recall_smote_list.append(recall_smote)
    precision_smote_list.append(precision_smote)

X = iris.data[:, :2]
y = iris.target
under = ClusterCentroids()
under = RandomUnderSampler()  # 随机欠采样
under = NearMiss(version=2)
X, y = under.fit_sample(X=X, y=y)
print("cc", Counter(y))
plt.scatter(X[y == 0, 0], X[y == 0, 1], color='g', marker='+', label="majority")
plt.scatter(X[y == 1, 0], X[y == 1, 1], color='b', marker='*', label="minority")
plt.legend()
plt.title(under)
plt.xlabel('sepal length')
plt.ylabel('sepal width')
plt.show()
# X = iris.data
for train, test in kf.split(X):
    X_train = X[train]
    Y_train = y[train]
    X_test = X[test]
    Y_test = y[test]
    DTC = DecisionTreeClassifier()
    DTC.fit(X_train, Y_train)
    f1_under = sklearn.metrics.f1_score(y_pred=DTC.predict(X=X_test), y_true=Y_test, zero_division=0)
    recall_under = sklearn.metrics.recall_score(y_pred=DTC.predict(X=X_test), y_true=Y_test, zero_division=0)
    precision_under = sklearn.metrics.precision_score(y_pred=DTC.predict(X=X_test), y_true=Y_test, zero_division=0)
    f1_under_list.append(f1_under)
    recall_under_list.append(recall_under)
    precision_under_list.append(precision_under)

plt.title("F1-Score")
plt.boxplot([f1_origin_list, f1_smote_list, f1_under_list], labels=['origin', 'over', 'under'])
plt.show()
plt.savefig("resampling-f1-score")
plt.title("resampling-recall")
plt.boxplot([recall_origin_list, recall_smote_list, recall_under_list], labels=['origin', 'over', 'under'])
plt.show()
plt.title("resampling-precision")
plt.boxplot([precision_origin_list, precision_smote_list, precision_under_list], labels=['origin', 'over', 'under'])
plt.show()
