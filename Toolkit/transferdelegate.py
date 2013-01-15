#!/usr/bin/python

from PySide import QtCore, QtGui


class TransferDelegate (QtGui.QStyledItemDelegate):

	def __init__ (self, parent = None):
		QtGui.QStyledItemDelegate.__init__ (self, parent)

	def paint (self, painter, option, index):
		style = QtGui.QApplication.style()

		if index.column() == 1:
			progressbar = QtGui.QStyleOptionProgressBarV2()
			progressbar.minimum = 0
			progressbar.maximum = 100
			progressbar.textVisible = True
			progressbar.textAlignment = QtCore.Qt.AlignCenter
			progressbar.text = "%d%%" % index.data()
			progressbar.progress = index.data()
			progressbar.rect = option.rect

			style.drawControl (QtGui.QStyle.CE_ProgressBar, progressbar, painter)

		else:
			label = QtGui.QStyleOptionViewItemV4 (option)
			label.text = index.data()
			label.displayAlignment = QtCore.Qt.AlignCenter

			style.drawControl (QtGui.QStyle.CE_ItemViewItem, label, painter)

	def createEditor (self, parent, option, index):
		pass
