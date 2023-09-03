from sklearn import datasets, svm

iris = datasets.load_iris()
# print(iris.data)
# print(iris.data.shape)

# num = len(iris.data)
# print(num)

clf = svm.SVC(gamma='auto')
clf.fit(iris.data, iris.target)

print(clf.predict([[1.4, 1.8, 3.9, 0.5]]))
