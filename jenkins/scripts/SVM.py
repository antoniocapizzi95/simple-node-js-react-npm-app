class Unbuffered(object):
   def __init__(self, stream):
       self.stream = stream
   def write(self, data):
       self.stream.write(data)
       self.stream.flush()
   def writelines(self, datas):
       self.stream.writelines(datas)
       self.stream.flush()
   def __getattr__(self, attr):
       return getattr(self.stream, attr)

import sys
sys.stdout = Unbuffered(sys.stdout)

from sklearn import svm

train_data = [[0, 0, 0, 0, 0, 1, 0, 0], [0, 1, 0, 0, 0, 1, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1], [0, 3, 0, 0, 0, 1, 0, 0], [0, 11, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 4]]
test_data = [[0, 0, 0, 0, 0, 132, 0, 0], [0, 1, 0, 0, 0, 1, 0, 0]]


clf = svm.OneClassSVM(nu=0.1, kernel="rbf", gamma=0.1)
clf.fit(train_data)

pred_test = clf.predict(test_data)

from sklearn.neighbors import LocalOutlierFactor
clf = LocalOutlierFactor(n_neighbors=10, novelty=True, contamination=0.1)
clf.fit(train_data)
y_pred_test = clf.predict(test_data)
if -1 in y_pred_test:
    print("anomaly detected")
else:
    print("no anomalies")