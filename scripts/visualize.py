import matplotlib.pyplot as plt

def plot_vitals(vitals):
    labels = list(vitals.keys())
    values = list(vitals.values())

    plt.bar(labels, values, color=['blue', 'green', 'red'])
    plt.title("Patient Vitals")
    plt.ylabel("Value")
    plt.show()
