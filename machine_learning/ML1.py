from sklearn import datasets
iris_dataset = datasets.load_iris()

print(iris_dataset['data'][0:10])