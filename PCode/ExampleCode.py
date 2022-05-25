import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import GUI.MainGUI
import Handle
import Main
from Sub import Assistance_01
import pandas as pd

class SampleCode:
    def __init__(self,GUI : Main.MainClass):
        self.df = pd.read_csv('OBS_ASOS_ANL_20220525163546.csv', encoding='cp949')
        self.GUI = GUI
        GUI.Main_Button_LineTextChange.clicked.connect(lambda : self.Clicked_Button_LineTextChange())
        GUI.Main_Button_GraphShow.clicked.connect(lambda : self.Clicked_Button_GraphShow())
        GUI.Main_ListWidget_RegionSelect.itemClicked.connect(lambda : self.Clicked_ListWidget_RegionSelect_Item())

        self.Initial_ListWidget_RegionSelect()
        for i in ['가','나','다']:
            GUI.Main_ComboBox_RegionList.addItem(i)

        self.Ass = Assistance_01.Assistance()

    def Clicked_Button_LineTextChange(self):
        msg = self.GUI.Main_LineText_LineText01.text()
        self.GUI.Main_Label_Label01.setText(msg)
    def Clicked_Button_GraphShow(self):
        print(self.GUI.Main_ComboBox_RegionList.currentText())
    def Initial_ListWidget_RegionSelect(self):
        Region_List = list(set(self.df['지점명'].to_list()))
        Region_List.sort()
        for i in Region_List:
            self.GUI.Main_ListWidget_RegionSelect.addItem(i)
    def Clicked_ListWidget_RegionSelect_Item(self):
        선택한지점 = self.GUI.Main_ListWidget_RegionSelect.currentItem().text()
        TempDataFrame = self.df.set_index("지점명")
        CurrentDataFrame = TempDataFrame.loc[선택한지점]
        DatePeriod = str(CurrentDataFrame.iat[0,1]) + "-" + str(CurrentDataFrame.iat[-1,1])
        print(DatePeriod)
        self.GUI.Main_Label_year.setText(DatePeriod)
        OutDataFrame = CurrentDataFrame.set_index("일시")["평균기온(°C)"]

        self.Ass.DrawGraphInVertical(self.GUI.Main_VerticalLayout_ShowGraph,OutDataFrame,선택한지점)



