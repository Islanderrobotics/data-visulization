

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("/Users/williammckeon/Sync/youtube videos/dataanalysis/housing.csv")

data.hist(figsize=(15-2,9.375-2))
plt.show()
data["total_rooms"].hist()
plt.show()
for i in data.columns:
    print(i)
data.plot(kind = "scatter",x = "total_rooms",y = "total_bedrooms",figsize=(20,10),alpha=None,label = "what")
plt.show()
data.plot(kind = "line",x = "total_rooms",y = "total_bedrooms",figsize=(20,10),alpha=0.1)
plt.show()
'''from PyQt5 import QtWidgets
import sys
screen = app.primaryScreen()
Traceback (most recent call last):
  File "<input>", line 1, in <module>
NameError: name 'app' is not defined
app = QtWidgets.QApplication(sys.argv)
screen = app.primaryScreen()
size = screen.size()
rint('Size: %d x %d' % (size.width(), size.height()))
Traceback (most recent call last):
  File "<input>", line 1, in <module>
NameError: name 'rint' is not defined
print('Size: %d x %d' % (size.width(), size.height()))
Size: 1440 x 900
print(size.width()/96)
15.0
print(size.height()/96)
9.375
'''