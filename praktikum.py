import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load Dataset
data = pd.read_csv('nilai_siswa.csv')
# print(data.head())
# print(data.info())
# print(data.describe())

print("Rata Rata:", data['Nilai'].mean())
print("Median:", data['Nilai'].max())
print("Modus:", data['Nilai'].mode()[0])

matematika = data[data['Matpel'] == 'Matematika']
print(matematika)

Inggris = data[data['Matpel'] == 'Bahasa Inggris']
print(Inggris)

# Indonesia = data[data['Matpel'] == 'Bahasa Indonesia']
# print(Indonesia)

data.groupby('Matpel')['Nilai'].agg({'mean','min'})

rata = data.groupby('Matpel')['Nilai'].mean()
rata.plot(kind='bar', color=['blue', '#ff7f0c', '#2ca02c', '#d62728', '#9467bd'])
plt.title('Rata-rata Nilai Siswa per Matpel')
plt.xlabel('Mata Pelajaran')
plt.ylabel('Nilai Rata-Rata')
plt.show()

sns.boxplot(x='Matpel', y='Nilai', data=data)
plt.title('sebaran Nilai per Mata Pelajaran')
plt.tight_layout()
plt.show()
