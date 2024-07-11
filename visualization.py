import pandas as pd
import matplotlib.pyplot as plt

def visualize_contracts(filename='contracts.xlsx'):
    df = pd.read_excel(filename)
    plt.figure(figsize=(10, 6))
    plt.bar(df['total_dollars_obligated'], df['recipient_name'])
    plt.xlabel('Total Dollars Obligated')
    plt.ylabel('Recipient Name')
    plt.title('Contracts Awarded')
    plt.show()

visualize_contracts()
