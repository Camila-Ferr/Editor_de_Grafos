import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

employees_df = pd.DataFrame({
    '1': [20, 22, 29, 20, 20, 21],
    '2': [65, 75, 80, 60, 63, 70],
    '3': [1.6, 1.7, 1.85, 1.69, 1.8, 1.75],
    '4': [3200, 3500, 4000, 2090, 2500, 3600],
    '5': [3200, 3500, 4000, 2090, 2500, 3600],
    '6': [3200, 3500, 4000, 2090, 2500, 3600],
    '7': [3200, 3500, 4000, 2090, 2500, 3600],
    '8': [3200, 3500, 4000, 2090, 2500, 3600],
    '9': [3200, 3500, 4000, 2090, 2500, 3600],
    '10': [3200, 3500, 4000, 2090, 2500, 3600]

})

correlacao = employees_df.corr(method='pearson')


plt.figure(figsize=(8, 6))
sns.heatmap(correlacao, annot=True)


plt.savefig("teste")

print(correlacao)