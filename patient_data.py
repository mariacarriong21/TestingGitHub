import pandas as pd

patients = pd.read_csv("patients.csv")

print("Patient Data Explorer")
print("---------------------")

print("\nFirst 5 patients:")
print(patients.head())

print("\nDataset dimensions:")
print(patients.shape)

print("\nVariables:")
print(patients.columns.tolist())

print("\nPatient statistics:")
print("-------------------")

print("Average age:", patients["age"].mean())
print("Average heart rate:", patients["heart_rate"].mean())
print("Average systolic blood pressure:", patients["systolic_bp"].mean())
print("Average cholesterol:", patients["cholesterol"].mean())
print("Average glucose:", patients["glucose"].mean())

print("\nData types:")
print("-----------")
print(patients.dtypes)

print("\nMissing values:")
print("--------------")
print(patients.isnull().sum())

print("\nDuplicated rows:")
print("----------------")
print(patients.duplicated().sum())

import matplotlib.pyplot as plt

plt.hist(patients["age"], bins=5)

plt.title("Age distribution")
plt.xlabel("Age")
plt.ylabel("Number of patients")

plt.show()

plt.scatter(patients["age"], patients["cholesterol"])

plt.title("Age vs Cholesterol")
plt.xlabel("Age")
plt.ylabel("Cholesterol")

plt.show()