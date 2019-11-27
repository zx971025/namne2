#!/use/bin/env python
# _*_coding:utf_8 _*_

import jieba
from wordcloud import WordCloud
import numpy as np
import PIL.Image as image
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import time


class Setlable(QWidget):
    def __init__(self):
        super().__init__()
        self.setui()
        self.setWindowTitle('简单小程序-词云统计')
        self.resize(500, 300)

    def setui(self):
        self.gird = QGridLayout(self)
        self.combobox1 = QComboBox(self)
        self.filebutton = QPushButton(self)
        self.filebutton.setText('打开文件')
        self.filebutton.clicked.connect(self.filename)
        self.add_list = ['宋体', '楷体', '黑体']
        self.combobox1.addItems(self.add_list)
        self.gird.addWidget(self.filebutton, 1, 0)
        self.gird.addWidget(self.combobox1, 0, 0)

    def filename(self):
        self.openfile_name = QFileDialog.getOpenFileName(self, '选择文本文件', '', 'files(*.txt , *.txt)')
        time.sleep(1)
        self.openfile_name1 = QFileDialog.getOpenFileName(self, '选择后衬图片文件', '', 'files(*.png , *.jpg)')
        with open(self.openfile_name[0], 'r', encoding='utf-8') as fp:
            text = fp.read()
        word_list = jieba.cut(text)
        result = " ".join(word_list)
        mask = np.array(image.open(self.openfile_name1[0]))
        index = self.combobox1.currentIndex()
        if index == 0:
            wordcloud = WordCloud(mask=mask, font_path="C:\Windows\Fonts\simsun.ttc", background_color="white",
                                  width=100, height=700, max_words=2000).generate(text)
            wordcloud.to_file('9.png')
        elif index == 1:
            wordcloud = WordCloud(mask=mask, font_path="C:\Windows\Fonts\simkai.ttf", background_color="white",
                                  height=700).generate(text)
        elif index == 2:
            wordcloud = WordCloud(mask=mask, font_path="C:\Windows\Fonts\simhei.ttf", background_color="white",
                                  height=700).generate(text)
        image_produce = wordcloud.to_image()
        image_produce.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('3.ico'))
    main = Setlable()
    main.show()
    sys.exit(app.exec_())
