import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay
import matplotlib.pyplot as plt
import joblib


# Define the path to the data directory
data_path = "assets/data/Training/"

# Define the list of movement types
movement_types = ["choodan_ooke", "choodan_zooki", "jodan_ooke", "jodan_zooki", "gedan_ooke", "gedan_zooki", "random"]

# Load the data into a pandas dataframe
data = pd.DataFrame(columns=["movement_type", "x_gyro", "y_gyro", "z_gyro", "x_acc", "y_acc", "z_acc"])

for movement_type in movement_types:
    folder_path = data_path + movement_type + "/"
    gyro_csv_files = [f for f in os.listdir(folder_path) if f.endswith("_gyro.csv")]
    accl_csv_files = [f for f in os.listdir(folder_path) if f.endswith("_acc.csv")]

    for gyro_file in gyro_csv_files:
        gyro_filename = gyro_file[:-9]  # Strip the "_gyro.csv" suffix from the filename
        matching_accl_files = [f for f in accl_csv_files if f.startswith(gyro_filename)]
        if len(matching_accl_files) == 0:
            continue
        accl_file = matching_accl_files[0]

        df1 = pd.read_csv(folder_path + gyro_file, header=None)  
        df2 = pd.read_csv(folder_path + accl_file, header=None)
        
        # Make sure that the two dataframes have the same number of rows
        min_rows = min(len(df1), len(df2))
        df1 = df1[:min_rows]
        df2 = df2[:min_rows]
        
        # Combine the dataframes and add the movement type column
        df1.columns = ["x_gyro", "y_gyro", "z_gyro"]
        df2.columns = ["x_acc", "y_acc", "z_acc"] # Add a prefix to the column names of the accelerometer dataframe

        df = pd.concat([df1, df2], axis=1)

        df["movement_type"] = movement_type
        # Append the dataframe to the main data dataframe
        data = pd.concat([data, df], ignore_index=True)

if data.empty:
    print("No data found!")
    exit()

# Split the data into training and testing sets
X = data.drop("movement_type", axis=1)
y = data["movement_type"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
X_train.columns = X_train.columns.astype(str)

print(X_train)
# Train a support vector machine (SVM) model
svm = SVC()
svm.fit(X_train, y_train)

# Make predictions on the testing set and calculate accuracy
y_pred = svm.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
confusionMatrix = confusion_matrix(y_test,y_pred)
# print(f"Confusion Matrix:\n{confusion_matrix(y_test,y_pred)}\n")
print(f"Confusion Matrix:\n{confusionMatrix}\n")
print("Accuracy: {:.2f}%\n".format(accuracy * 100))
print(f"Classification Report:\n{classification_report(y_test,y_pred)}\n")

# ConfusionMatrixDisplay(svm, X_test, y_test)
displayPlot = ConfusionMatrixDisplay(confusion_matrix=confusionMatrix, display_labels=svm.classes_)
displayPlot.plot()
plt.show()

# Save the SVM model to a file
joblib.dump(svm, "./assets/data/Model/model.pkl")