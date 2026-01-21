# 🍎 FruitSense - AI-powered Fruit Classifier

---

## 🔍 Project Goal
FruitSense is designed to predict the **type of fruit** based on its physical attributes using **machine learning models**. It provides a user-friendly interface for real-time predictions, making it an excellent tool for learning and demonstrating the power of AI in classification tasks.

---

## 📖 Overview
The project leverages **fruit datasets** to train and evaluate machine learning models. It uses a Streamlit-based web app for deployment, enabling real-time predictions. By integrating preprocessing, model training, and deployment, FruitSense showcases a complete machine learning workflow.

---

## 🔄 **Project Workflow**

### **1️⃣ Data Preprocessing**
- **Data Loading:** Loaded the dataset containing fruit features.
- **Feature Selection:** Selected relevant features for classification.
- **Feature Scaling:** Applied `StandardScaler` to normalize input values.
- **Data Preparation:** Prepared the data for model training and evaluation.

---

### **2️⃣ Model Building**
- Trained a machine learning classification model using **scikit-learn**.
- Optimized the model for better prediction accuracy.
- Saved the trained model and scaler using `joblib` for deployment.

---

### **3️⃣ Evaluation Metrics**
- **Accuracy:** The primary metric used to evaluate the model. The accuracy score represents the proportion of correctly classified fruit types out of the total predictions made. For this project, the model achieved an accuracy of **87%** on the test dataset, indicating high reliability in predictions.
- **Confusion Matrix:** Analyzed the confusion matrix to understand the distribution of true positives, true negatives, false positives, and false negatives across different fruit types.
- **Precision and Recall:** Calculated precision and recall for each fruit type to ensure balanced performance, especially for underrepresented classes.
- **F1-Score:** Used the F1-score to balance precision and recall, ensuring the model performs well across all classes.

---

### **4️⃣ Deployment**
- Built an interactive web application using **Streamlit**.
- Loaded the trained model and scaler in the app.
- Enabled real-time predictions based on user input.
- Designed a simple and intuitive UI for end users.

---

## 🛠 **Tech Stack**

- **Python**
- **Pandas** – Data handling and manipulation
- **NumPy** – Numerical computations
- **Scikit-learn** – Model training and evaluation
- **Joblib** – Model and scaler serialization
- **Streamlit** – Web application and deployment interface

---

## 📂 Project Structure
```
FruitSense/
├── dataset                          # Dataset used for training
├── .gitignore                       # Files/directories to exclude from Git tracking
├── LICENSE                          # Allows reuse, with attribution, no warranty
├── README.md                        # Project documentation
├── app.py                           # Streamlit app script
├── fruit_classifier.ipynb           # Jupyter notebook for data processing and model training
├── model.pkl                        # Trained machine learning model
├── requirements.txt                 # Project dependencies
└── scaler.pkl                       # Pre-fitted StandardScaler object for input normalization
```

---

## ✨ **Features**

- Predicts fruit type based on physical attributes
- Real-time predictions through a web interface
- Lightweight and easy to run locally
- Beginner-friendly and well-structured ML workflow

---

## 🚀 **Future Enhancements**

- Add more fruit categories and features
- Integrate image-based fruit classification
- Improve evaluation with additional metrics like precision and recall
- Deploy the app on a cloud platform for public access
- Add data visualization for better insights

---

## 🧪 **How to Run Locally**

```
# Clone the repository
git clone https://github.com/yourusername/FruitSense.git

# Navigate to the project directory
cd FruitSense

# Install the dependencies
pip install -r requirements.txt
```

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 📬 Contact

<p>

  <a href="mailto:aradhyaray99@gmail.com"><img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" /></a>
  <a href="www.linkedin.com/in/rayaradhya"><img src="https://img.shields.io/badge/LinkedIn-blue?style=for-the-badge&logo=linkedin&logoColor=white" /></a>
  <a href="https://github.com/AradhyaRay05"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" /></a>
</p>

---

Thanks for visiting ! Feel free to explore my other repositories and connect with me. 🚀