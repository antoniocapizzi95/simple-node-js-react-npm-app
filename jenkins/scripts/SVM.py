def sendAlert(message):
    from slacker import Slacker
    slack = Slacker('xoxb-607836096374-607542930759-do64JYEYnRtR7fM7rhG97s63')
    slack.chat.post_message('#research',message)


from sklearn import svm

train_data = [[0, 0, 0, 0, 0, 1, 0, 0], [0, 1, 0, 0, 0, 1, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1], [0, 3, 0, 0, 0, 1, 0, 0], [0, 11, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 4]]
test_data = [[0, 0, 0, 0, 0, 0, 0, 17], [0, 1, 0, 0, 0, 1, 0, 0]]


clf = svm.OneClassSVM(nu=0.1, kernel="rbf", gamma=0.1)
clf.fit(train_data)

pred_test = clf.predict(test_data)

from sklearn.neighbors import LocalOutlierFactor
clf = LocalOutlierFactor(n_neighbors=10, novelty=True, contamination=0.1)
clf.fit(train_data)
y_pred_test = clf.predict(test_data)
if -1 in y_pred_test:
    sendAlert('Anomaly detected')
