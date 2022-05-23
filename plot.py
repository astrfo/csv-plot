import pandas as pd
import matplotlib.pyplot as plt

def plot():
    data = pd.read_csv('total.csv')
    plt.plot(data, label=data.columns)
    plt.legend()
    plt.savefig('multi_arm.png')
    plt.show()