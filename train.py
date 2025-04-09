import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib  # 用于保存模型

#加载模型
iris = load_iris()
# print(iris.target)
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = iris.target


# 2. 划分训练集/测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)


# 3. 训练模型
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# 4. 评估模型
print("Test Accuracy:", model.score(X_test, y_test))

# 5. 保存模型
joblib.dump(model, "model/iris_classifier.joblib")