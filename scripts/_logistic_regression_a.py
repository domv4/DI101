import matplotlib.pyplot as plt
from sklearn import datasets
cancer = datasets.load_breast_cancer()
cancer_x = cancer.data[:100]
cancer_y = cancer.target[:100]
x = cancer_x[:, :2] 
y = cancer_y
plt.figure(figsize=(12,6))
plt.style.use('seaborn')
plt.scatter(x[:, 0], x[:, 1], c=y, cmap=plt.cm.Set1, edgecolor="k")