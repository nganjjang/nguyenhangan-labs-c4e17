#FOR MAC (2 dong dau tien):
import matplotlib
matplotlib.use('TkAgg')

from matplotlib import pyplot

#1. Prepare data:
machine_counts = [18, 4, 2]

#2. Prepare labels:
machine_names = ['PC', 'MAC', 'Linux']

#3. Draw pie chart:
pyplot.pie(machine_counts, labels=machine_names, autopct='%.1f%%', shadow=True, explode=[0, 0.2, 0])
pyplot.title('PC vs MAC vs Linux usage')
pyplot.axis('equal')


#4. Show:
pyplot.show()
