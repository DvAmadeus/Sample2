import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigCanvas
class Assistance:
    def __init__(self):
        pass
    def DrawGraphInVertical(self,Vertical,DataFrame,NAME="NULL"):
        for i in range(Vertical.count()):
            Vertical.itemAt(i).widget().deleteLater()
        self.fig = plt.Figure()
        self.canvas = FigCanvas(self.fig)
        self.ax = self.fig.add_subplot(111)
        Vertical.addWidget(self.canvas)

        self.ax.set_title(NAME,fontname="Malgun Gothic")
        plt.rc('font', family="Malgun Gothic")


        DataFrame.plot(ax=self.ax)


        self.canvas.show()