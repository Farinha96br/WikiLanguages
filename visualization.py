import numpy as np
import matplotlib.pyplot as plt




data = np.load('pt_50k.npy', allow_pickle=True)
print(data.shape)  # print the first 5 rows to check the structure
print(data[:5])
# the number of links per page is in the second column (index 1)
link_counts = data[:, 1]
def plot_link_distribution(link_counts):
    plt.figure(figsize=(10, 6))
    plt.hist(link_counts, bins=100)  # log scale for better visibility
    plt.title('Distribution of Number of Links per Wikipedia Page')
    #plt.xlabel('Number of Links')
    #plt.ylabel('Frequency (log scale)')
    plt.grid(True)
    plt.show()


plot_link_distribution(link_counts)