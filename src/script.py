import numpy as np
from os import walk
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import numpy as np
from scipy.signal import resample
def read_file(f):
    with open(f) as file:
        text = file.read()
    lines = text.split('\n')
    if lines[len(lines) - 1] == '':
        del lines[len(lines)-1]
    all_lines_formatted = []
    for line in lines:
        line_formatted = []
        for item in line.split(' '):
            if item:
                line_formatted.append(float(item))
        all_lines_formatted.append(line_formatted)
    matrix = np.array(all_lines_formatted)
    return matrix.T
classes = [
    'I-I-',
    'I-M-',
    'IMP-',
    'I-P-',
    'L-L-',
    'M-M-',
    'M-R-',
    'R-L-',
    'R-R-',
    'T-I-',
    'T-L-',
    'T-M-',
    'T-R-',
    'T-T-'
]
root_dir = './../dataset/'
persons = []
for (dirpath, dirnames, filenames) in walk(root_dir):
    for dir_name in dirnames:
        print('Person: ' + dir_name)
        for (dirpath, dirnames, filenames) in walk(root_dir + dir_name):
            trials=[]
            for i in range(4):
                data_classes = []
                for classe in classes:
                    data_classes.append(read_file(root_dir + dir_name + '/' + classe + str(i+1) + '.txt'))
                trials.append(np.array(data_classes))
            persons.append(np.array(trials))
            break
print("Finish")

from scipy.signal import resample
dt = resample(person[0, 1, 1, :], 1000)
print(dt.shape)
d = list()
for e in range(8):
    # distribuindo os 40.000 dados em 5 segundos
    for i, t in enumerate(np.linspace(0, 10, 40000)):
        # testando a 1ª amostra das 189 disponíveis (0)
        d.append([e, t, person[0][1][e][i]])
d = np.array(d)
print(d.shape)

d = resample(d, 1000)
print(d.shape)

x, y, z = d[:,0], d[:,1], d[:,2]
print(x.shape, y.shape)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_trisurf(x, y, z, cmap=cm.inferno, linewidth=1)
ax.set_xlabel('Canais')
ax.set_ylabel('Tempo (seg.)')
ax.set_zlabel('Microvolts')
#fig.colorbar(surf)
fig.tight_layout()
plt.show()