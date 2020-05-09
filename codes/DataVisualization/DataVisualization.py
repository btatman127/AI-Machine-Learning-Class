import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Patch

# read csv
X = pd.read_csv("congress-terms.csv", thousands=',')

# form data frame from csv
df = pd.DataFrame(X)
# only for the state of Wyoming
df = df.loc[df['state'] == 'WY']

# make smaller data frames from the original, one for each type of marker
df_D = df.loc[df['party'] == 'D']
df_R = df.loc[df['party'] == 'R']
df_O = df.loc[df['party'] != 'D'].loc[df['party'] != 'R']
df_list = [df_D, df_R, df_O]
markers = ['*', '^', '.']

# make scatter plot (each data frame with its corresponding marker)
fig, ax = plt.subplots()
for d, m in zip(df_list, markers):
    # determine color based on dictionary
    color = d['chamber'].replace({'house': 'b', 'senate': 'r'})
    ax.scatter(d['congress'], d['age'], c=color, marker=m)

# title and labels
ax.set_title('Congress Terms')
ax.set_xlabel('nth Congress')
ax.set_ylabel('Age')

# make legend for different markers and colors
legend_elements = [Line2D([0], [0], marker='*', color='w', label='Democrats',
                          markerfacecolor='k', markersize=15),
                   Line2D([0], [0], marker='^', color='w', label='Republicans',
                          markerfacecolor='k', markersize=15),
                   Line2D([0], [0], marker='.', color='w', label='Other Party',
                          markerfacecolor='k', markersize=15),
                   Patch(facecolor='blue', edgecolor='k',
                         label='House'),
                   Patch(facecolor='red', edgecolor='k',
                         label='Senate')]
ax.legend(handles=legend_elements, loc='best')

plt.tight_layout()
plt.show()
