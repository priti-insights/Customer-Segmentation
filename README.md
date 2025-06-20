# 🧑‍🤝‍🧑 Customer Segmentation App

This is a **Customer Segmentation** web app built with:
- 🐍 Python & Scikit-learn
- 🎨 Streamlit for a beautiful and interactive UI
- 📊 Pandas, Matplotlib, and Seaborn for data handling & visualization

---

## ✨ Features
- 🧠 Input customer features (Gender, Age, Annual Income, Spending Score).
- ⚡ Instantly predict the customer segment (e.g. "Average" or "Best").
- 🎨 Interactive, responsive layout with color-coded results.
- 📂 Pre-trained `customer.pkl` model for instant predictions.

---

## 📂 Project Structure
```
Customer-Segmentation/
├─ customer.py         # Streamlit app file
├─ customer.pkl        # Saved trained model
├─ requirements.txt    # Dependencies
├─ README.md           # Documentation
```

---

## 🚀 Getting Started
1. **Clone this repository:**
   ```bash
   git clone https://github.com/your-username/Customer-Segmentation.git
   cd Customer-Segmentation
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the app:**
   ```bash
   streamlit run customer.py
   ```

---

## 🧠 Model Training
If you’d like to retrain the model:
1. Modify the training script (e.g. `train_model.py`)
2. Run:
   ```bash
   python train_model.py
   ```
3. Save the updated model as `customer.pkl`

---

## 🎯 Contributing
Contributions are welcome — feel free to open an issue or submit a pull request!

---

## 📄 License
This project is licensed under the MIT License — see the `LICENSE` file for details.

---

💖 **Happy segmenting!**
