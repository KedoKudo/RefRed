# -*- coding: utf-8 -*-
#@PydevCodeAnalysisIgnore

# Form implementation generated from reading ui file 'designer//compare_widget.ui'
#
# Created: Mon Aug 31 09:02:32 2015
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(851, 718)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter = QtGui.QSplitter(Form)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.frame_7 = QtGui.QFrame(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.frame_7)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.comparePlot = MPLWidget(self.frame_7)
        self.comparePlot.setObjectName("comparePlot")
        self.verticalLayout_6.addWidget(self.comparePlot)
        self.widget_6 = QtGui.QWidget(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_15 = QtGui.QHBoxLayout(self.widget_6)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.compareList = QtGui.QTableWidget(self.widget_6)
        self.compareList.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.compareList.setSelectionBehavior(QtGui.QAbstractItemView.SelectItems)
        self.compareList.setObjectName("compareList")
        self.compareList.setColumnCount(3)
        self.compareList.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.compareList.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.compareList.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.compareList.setHorizontalHeaderItem(2, item)
        self.horizontalLayout_15.addWidget(self.compareList)
        self.frame_8 = QtGui.QFrame(self.widget_6)
        self.frame_8.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_10 = QtGui.QVBoxLayout(self.frame_8)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.pushButton = QtGui.QPushButton(self.frame_8)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_10.addWidget(self.pushButton)
        self.pushButton_2 = QtGui.QPushButton(self.frame_8)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_10.addWidget(self.pushButton_2)
        self.horizontalLayout_15.addWidget(self.frame_8)
        self.verticalLayout.addWidget(self.splitter)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL("pressed()"), Form.open_file)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("pressed()"), Form.clear_plot)
        QtCore.QObject.connect(self.compareList, QtCore.SIGNAL("itemChanged(QTableWidgetItem*)"), Form.draw)
        QtCore.QObject.connect(self.compareList, QtCore.SIGNAL("cellDoubleClicked(int,int)"), Form.edit_cell)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.compareList, self.pushButton_2)
        Form.setTabOrder(self.pushButton_2, self.pushButton)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.compareList.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("Form", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.compareList.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("Form", "Color", None, QtGui.QApplication.UnicodeUTF8))
        self.compareList.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("Form", "Label", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Form", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("Form", "Open", None, QtGui.QApplication.UnicodeUTF8))

from .mplwidget import MPLWidget
