from flask import Flask, render_template, request
import pickle
import numpy as np

# Initialize Flask application
app = Flask(__name__)

def prediction(lst):
    """Load the model and predict the price for the given feature list."""
    filename = 'model/predictor.pickle'
    try:
        with open(filename, 'rb') as file:
            model = pickle.load(file)
        pred_value = model.predict([lst])
        return pred_value
    except FileNotFoundError:
        print("Error: predictor.pickle not found in model/ directory.")
        return [0]
    except Exception as e:
        print(f"Prediction error: {e}")
        return [0]

@app.route('/', methods=['POST', 'GET'])
def index():
    """Handle GET and POST requests for the main page."""
    pred_value = 0
    if request.method == 'POST':
        try:
            # Collect form inputs
            ram = request.form['ram']
            weight = request.form['weight']
            company = request.form['company']
            typename = request.form['typename']
            opsys = request.form['opsys']
            cpu = request.form['cpuname']
            gpu = request.form['gpuname']
            touchscreen = request.form.getlist('touchscreen')
            ips = request.form.getlist('ips')

            # Initialize feature list
            feature_list = []

            # Add numeric and boolean features
            feature_list.append(int(ram))
            feature_list.append(float(weight))
            feature_list.append(1 if touchscreen else 0)  # 1 if checked, else 0
            feature_list.append(1 if ips else 0)  # 1 if checked, else 0

            # Define all categories as per training data
            company_list = ['Acer', 'Apple', 'Asus', 'Chuwi', 'Dell', 'Fujitsu', 'Google', 'HP',
                            'Huawei', 'LG', 'Lenovo', 'MSI', 'Mediacom', 'Microsoft', 'Razer',
                            'Samsung', 'Toshiba', 'Vero', 'Xiaomi']
            typename_list = ['2 in 1 Convertible', 'Gaming', 'Netbook', 'Notebook', 'Ultrabook', 'Workstation']
            opsys_list = ['Linux', 'Mac', 'Windows', 'other']
            cpu_list = ['AMD', 'Intel Core i3', 'Intel Core i5', 'Intel Core i7', 'other']
            gpu_list = ['AMD', 'Intel', 'Nvidia']

            # One-hot encoding function
            def traverse_list(lst, value):
                for item in lst:
                    feature_list.append(1 if item.lower() == value.lower() else 0)

            # Apply one-hot encoding in the correct order
            traverse_list(company_list, company)
            traverse_list(typename_list, typename)
            traverse_list(opsys_list, opsys)
            traverse_list(cpu_list, cpu)
            traverse_list(gpu_list, gpu)

            # Verify feature list length (should be 41)
            if len(feature_list) != 41:
                print(f"Error: Expected 41 features, got {len(feature_list)}")
                print(f"Feature list: {feature_list}")
                return render_template('index.html', pred_value=0, error="Feature mismatch error.")

            # Make prediction
            pred_value = prediction(feature_list)
            pred_value = np.round(pred_value[0], 2) * 221  # Convert euros to LKR

        except ValueError as ve:
            print(f"Input error: {ve}")
            return render_template('index.html', pred_value=0, error="Invalid input. Please check your entries.")
        except Exception as e:
            print(f"General error: {e}")
            return render_template('index.html', pred_value=0, error="An error occurred. Please try again.")

    return render_template('index.html', pred_value=pred_value)

if __name__ == '__main__':
    app.run(debug=True)