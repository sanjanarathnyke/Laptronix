# Laptop Price Predictor

![App Screenshot](images/image.png)

A web application that predicts laptop prices using machine learning. Enter your laptop's specifications and get an instant price estimate in EUR and LKR!

## Features

- Predicts laptop prices based on brand, type, CPU, GPU, RAM, weight, and features.
- Supports currency toggle between EUR and LKR.
- Modern, responsive UI with Tailwind CSS.
- Powered by Flask and a trained scikit-learn model.

## Machine Learning Approach

This app uses **supervised learning** with a **Random Forest Regressor** to predict laptop prices based on historical data.

## Getting Started

### Prerequisites

- Python 3.10+
- pip

### Installation

1. **Clone the repository:**
   ```sh
   git clone <your-repo-url>
   cd <your-repo-folder>
   ```

2. **Create and activate a virtual environment (optional):**
   ```sh
   python -m venv env
   env\Scripts\activate
   ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Ensure the model file exists:**
   - The trained model should be at `Model/predictor.pickle`.

5. **Run the app locally:**
   ```sh
   python app.py
   ```
   - Visit [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

## Project Structure

```
.
├── app.py
├── requirements.txt
├── Model/
│   └── predictor.pickle
├── templates/
│   └── index.html
├── images/
│   └── image.png
└── ...
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
