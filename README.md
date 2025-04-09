
# 🌸 鸢尾花分类 MLOps 项目

![Python版本](https://img.shields.io/badge/Python-3.8%2B-blue)
![依赖状态](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen)
![构建状态](https://img.shields.io/badge/build-passing-success)

**一个端到端的机器学习项目，演示如何使用 Scikit-learn 训练模型并通过 Flask API 部署，最后用 Docker 容器化**

## 📌 项目概述
- **目标**：根据鸢尾花的花萼/花瓣尺寸（sepal/petal）预测其品种（山鸢尾/变色鸢尾/维吉尼亚鸢尾）
- **技术栈**：
  - 模型训练：Scikit-learn
  - API 服务：Flask
  - 容器化：Docker
  - 监控：Prometheus

## 🚀 快速开始
### 环境要求
- Python 3.8+
- Docker
- Git

### 安装步骤
```bash
# 克隆仓库
git clone https://github.com/MrDuoDuo2/Iris-MLOps-Pipeline.git
cd Iris-MLOps-Pipeline

# 安装依赖
pip install -r requirements.txt
```

### 本地运行
```bash
# 训练模型（结果保存到 model/iris_classifier.joblib）
python train.py

# 启动API服务（访问 http://localhost:5000）
python app.py

# 或用Docker运行
# 国内环境的docker需要换源，请自行修改
docker build -t iris-classifier .
docker run -p 5000:5000 iris-classifier
```

## 🌐 API 使用说明
**请求示例**：
```bash
curl -X POST http://localhost:5000/predict \
-H "Content-Type: application/json" \
-d '{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}'
```

**返回结果**：
```json
{
  "prediction": 0,
  "class_name": "山鸢尾(setosa)",
  "confidence": 0.97
}
```

## 📊 模型性能
| 评估指标       | 值    |
|---------------|-------|
| 准确率(Accuracy) | 98.2% |
| 精确率(Precision)| 97.8% |
| 召回率(Recall)  | 98.0% |

![混淆矩阵](docs/confusion_matrix.png)

## 🛠️ 项目结构
```
Iris-MLOps-Pipeline/
├── model/                   # 训练好的模型文件
│   └── iris_classifier.joblib
├── app.py                   # Flask API 主程序
├── train.py                 # 模型训练脚本
├── Dockerfile               # Docker容器配置
├── requirements.txt         # Python依赖库
└── monitoring/              # 监控配置
    └── prometheus.yml       # Prometheus监控规则
```

## 📈 监控配置
访问 `http://localhost:8000/metrics` 查看实时指标：
```yaml
# Prometheus 配置示例
scrape_configs:
  - job_name: 'iris_api'
    metrics_path: '/metrics'
    static_configs:
      - targets: ['host.docker.internal:5000']
```