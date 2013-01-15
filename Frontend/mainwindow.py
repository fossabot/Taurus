#!/usr/bin/python

import sys, os, time
from PySide import QtCore, QtGui
from ctypes import pythonapi, c_void_p, py_object

import gobject

from UI import Ui_MainWindow
from Frontend import MergeExam, NewConvert, SaveSplit, LoadError
from Backend import Player, VideoSplitter, VideoMerger, MediaFileChecker, Transcoder
from Toolkit import TransferDelegate, MergeDelegate, time2str, str2time


TransTaskProcessing, TransTaskFinished, TransTaskDeleted, TransTaskVerifying = xrange (4)
MergeTaskProcessing, MergeTaskFinished, MergeTaskDeleted = xrange (3)
SplitNotChosen, SplitAdjustStart, SplitAdjustStop = xrange (3)


class MainWindow (QtGui.QMainWindow):

	def __init__ (self, username, edited, transferred, lastsplittime, lastsplitfile, lastsplitpath,
			lastmergepath, lasttransferpath, parent = None):
		QtGui.QMainWindow.__init__ (self, parent)

		self.username = username
		self.edited = edited
		self.transferred = transferred
		self.lastsplittime = lastsplittime
		self.lastsplitfile = lastsplitfile
		self.lastsplitpath = lastsplitpath
		self.lastmergepath = lastmergepath
		self.lasttransferpath = lasttransferpath

		self.ui = Ui_MainWindow()
		self.ui.setupUi (self)
		self.setWindowFlags (QtCore.Qt.FramelessWindowHint)

		self.setWindowTitle (self.tr ("Cartoon Encoding and Uploading Platform"))
		self.setWindowIcon (QtGui.QIcon (':/images/icon.png'))

		self.createActions()
		self.createplayer()
		self.createmerger()
		self.createUIdetails()
		self.creategobject()

		self.transcoding = []
		self.translisting = TransTaskProcessing
		self.checkers = []
		self.splitchoose = SplitNotChosen
		self.updatelineeditblocked = False
		self.playerfile = None

		self.leftclicked = False

	def createActions (self):
		self.restact = QtGui.QAction (self.tr ("&Restore"), self, triggered = self.showNormal)
		self.minact = QtGui.QAction (self.tr ("Mi&nimize"), self, triggered = self.showMinimized)
		self.maxact = QtGui.QAction (self.tr ("Ma&ximize"), self, triggered = self.showMaximized)
		self.quitact = QtGui.QAction (self.tr ("&Quit"), self, triggered = QtGui.qApp.quit)

		self.trayicon = QtGui.QSystemTrayIcon (QtGui.QIcon (':/images/icon.png'))

		self.trayiconmenu = QtGui.QMenu (self)
		self.trayiconmenu.addAction (self.minact)
		self.trayiconmenu.addAction (self.maxact)
		self.trayiconmenu.addAction (self.restact)
		self.trayiconmenu.addSeparator()
		self.trayiconmenu.addAction (self.quitact)

		self.trayiconmenu.setStyleSheet ("QMenu {background-color: rgba(255, 255, 255, 255); border: 1px solid black;} QMenu::item {background-color: transparent;} QMenu::item:selected {background-color: rgba(0, 100, 255, 128);}")

		self.trayicon.setToolTip (self.tr ("Minimize to system tray. Right click this icon and choose Quit to close."))
		self.trayicon.setContextMenu (self.trayiconmenu)

		self.trayicon.show()

		self.trayicon.activated.connect (self.trayiconactivated)

	def createUIdetails (self):

		self.ui.transview.setModel (self.transfermodel (self))
		self.ui.transview.setRootIsDecorated (False)
		self.ui.transview.setAlternatingRowColors (True)
		self.ui.transview.setItemDelegate (TransferDelegate (self))
		self.ui.transview.setContextMenuPolicy (QtCore.Qt.CustomContextMenu)

		self.ui.mergeview.setModel (self.mergemodel (self))
		self.ui.mergeview.setRootIsDecorated (False)
		self.ui.mergeview.setAlternatingRowColors (True)
		self.ui.mergeview.setItemDelegate (MergeDelegate (self))

		self.ui.stackedWidget.setCurrentIndex (0)

		self.ui.lineeditstarttime.installEventFilter (self)
		self.ui.lineeditendtime.installEventFilter (self)

		self.ui.labelvideoedit.setText (self.tr ("Video Edit: %d") % (self.edited))
		self.ui.labelvideoconvert.setText (self.tr ("Video Transfer: %d") % (self.transferred))
		if self.lastsplittime is not None:
			self.ui.labellastrecordtime.setText (self.lastsplittime)
		if self.lastsplitfile is not None:
			self.ui.labellastsavefile.setText (self.lastsplitfile)
		if self.lastmergepath is not None:
			self.ui.lineeditsaveblank.setText (self.lastmergepath)

		self.ui.buttoncancelbrowse.hide()

		self.ui.labelfilmtitle.setAlignment (QtCore.Qt.AlignHCenter)

	def creategobject (self):
		gobject.threads_init()
		self.mainloop = gobject.MainLoop()
		self.context = self.mainloop.get_context()

		self.contexttimer = QtCore.QTimer (QtGui.QApplication.instance())
		self.contexttimer.timeout.connect (self.contexthandler)
		self.contexttimer.start (1)

	def contexthandler (self):
		while self.context.pending():
			QtGui.qApp.processEvents()
			self.context.iteration()

	@QtCore.Slot (QtCore.QPoint)
	def on_transview_customContextMenuRequested (self, point):
		menu = QtGui.QMenu (self)
		menu.addAction (QtGui.QAction (self.tr ("Start"), self, triggered = self.on_buttontransbegin_clicked))
		menu.addAction (QtGui.QAction (self.tr ("Pause"), self, triggered = self.on_buttontranspause_clicked))
		menu.addAction (QtGui.QAction (self.tr ("Delete"), self, triggered = self.on_buttontransdelete_clicked))
		menu.exec_ (QtGui.QCursor.pos())

	@QtCore.Slot (unicode, unicode)
	def newmerged (self, username, path):
		self.edited += 1
		self.ui.labelvideoedit.setText (self.tr ("Video Edit: %d") % (self.edited))
		self.lastmergepath = path
		self.ui.lineeditsaveblank.setText (self.lastmergepath)

	@QtCore.Slot (unicode, unicode, unicode, unicode)
	def newsplitted (self, username, time, filename, path):
		self.edited += 1
		self.ui.labelvideoedit.setText (self.tr ("Video Edit: %d") % (self.edited))
		self.lastsplittime = time
		self.ui.labellastrecordtime.setText (self.lastsplittime)
		self.lastsplitfile = filename
		self.ui.labellastsavefile.setText (self.lastsplitfile)
		self.lastsplitpath = path

	@QtCore.Slot (unicode, unicode)
	def newtransferred (self, username, path):
		self.transferred += 1
		self.ui.labelvideoconvert.setText (self.tr ("Video Transfer: %d") % (self.transferred))
		self.lasttransferpath = path

	@QtCore.Slot (int)
	def trayiconactivated (self, event):
		if event == QtGui.QSystemTrayIcon.Trigger:
			if self.isHidden():
				self.ui.buttonmaximize.setIcon (QtGui.QIcon (':/images/maximize.png'))
				self.showNormal()
			else:
				self.ui.buttonmaximize.setIcon (QtGui.QIcon (':/images/maximize.png'))
				self.hide()

	@QtCore.Slot()
	def on_buttonminimize_clicked (self):
		self.showMinimized()

	@QtCore.Slot()
	def on_buttonmaximize_clicked (self):
		if self.isMaximized():
			self.ui.buttonmaximize.setIcon (QtGui.QIcon (':/images/maximize.png'))
			self.showNormal()
		else:
			self.ui.buttonmaximize.setIcon (QtGui.QIcon (':/images/restore.png'))
			self.showMaximized()

	@QtCore.Slot()
	def on_buttonclose_clicked (self):
		self.ui.buttonmaximize.setIcon (QtGui.QIcon (':/images/maximize.png'))
		self.hide()
		self.trayicon.showMessage (self.tr ("Cartoon Encoding and Uploading Platform"),
				self.tr ("Minimize to system tray. Right click this icon and choose Quit to close."),
				QtGui.QSystemTrayIcon.Information, 10000)

	def transfermodel (self, parent):
		model = QtGui.QStandardItemModel (0, 4, parent)
		model.setHorizontalHeaderLabels ([self.tr ("Cartoon Name"), self.tr ("Transfer Progress"), self.tr ("Status"), self.tr ("Output Path")])
		return model

	def mergemodel (self, parent):
		model = QtGui.QStandardItemModel (0, 4, parent)
		model.setHorizontalHeaderLabels ([self.tr ("File Name"), self.tr ("Duration"), self.tr ("Resolution"), self.tr ("Status")])
		return model

	def createplayer (self):

		winid = self.ui.frame_2.winId()
		pythonapi.PyCObject_AsVoidPtr.restype = c_void_p
		pythonapi.PyCObject_AsVoidPtr.argtypes = [py_object]
		self.windowId = pythonapi.PyCObject_AsVoidPtr (winid)

		self.ui.frame_2.mouseMoveEvent = self.mouseMoveEvent
		self.ui.frame_2.mousePressEvent = self.mousePressEvent
		self.ui.frame_2.mouseReleaseEvent = self.frameMouseRelease

		self.player = Player (self.windowId, self.ui.sliderseek.minimum(), self.ui.sliderseek.maximum(), self.ui.slidervolume.minimum(), self.ui.slidervolume.maximum())

		self.ui.buttonplayerplay.clicked.connect (self.player.playclicked)
		self.ui.buttonplayerstop.clicked.connect (self.player.stopclicked)
		self.ui.buttonplayerbackward.clicked.connect (self.player.backwardclicked)
		self.ui.buttonplayerforward.clicked.connect (self.player.forwardclicked)
		self.ui.buttonvolume.clicked.connect (self.player.muteornot)
		self.ui.sliderseek.valueChanged.connect (self.player.sliderseekvalue)
		self.ui.slidervolume.valueChanged.connect (self.player.slidervolumevalue)

		self.player.playurisignal.connect (self.player.playuri)
		self.player.updatelabelduration.connect (self.updatelabelduration)
		self.player.updatesliderseek.connect (self.updatesliderseek)
		self.player.updateslidervolume.connect (self.updateslidervolume)
		self.player.updatelineedit.connect (self.updatelineedit)
		self.player.setbuttonplay.connect (self.playersetbuttonplay)
		self.player.setbuttonpause.connect (self.playersetbuttonpause)
		self.player.setloopsignal.connect (self.player.setloop)

		self.player.startworker()

	@QtCore.Slot()
	def on_buttonloadfile_clicked (self):

		self.playerfile = QtGui.QFileDialog.getOpenFileName (self, self.tr ("Open"), QtGui.QDesktopServices.storageLocation (QtGui.QDesktopServices.MoviesLocation))[0]
		if self.playerfile:
			self.player.playurisignal.emit (self.playerfile)
			self.ui.labelfilmtitle.setText (QtCore.QFileInfo (self.playerfile).fileName())

	@QtCore.Slot (unicode)
	def updatelabelduration (self, text):
		self.ui.labelduration.setText (text)

	@QtCore.Slot (int)
	def updatesliderseek (self, value):
		self.ui.sliderseek.blockSignals (True)
		self.ui.sliderseek.setValue (value)
		self.ui.sliderseek.blockSignals (False)

	@QtCore.Slot (unicode)
	def updatelineedit (self, text):
		if self.updatelineeditblocked:
			return

		if self.splitchoose == SplitNotChosen:
			return
		elif self.splitchoose == SplitAdjustStart:
			self.ui.lineeditstarttime.setText (text)
		elif self.splitchoose == SplitAdjustStop:
			self.ui.lineeditendtime.setText (text)

	@QtCore.Slot (int)
	def updateslidervolume (self, value):
		self.ui.slidervolume.blockSignals (True)
		self.ui.slidervolume.setValue (value)
		self.ui.slidervolume.blockSignals (False)

		self.on_slidervolume_valueChanged (value)

	@QtCore.Slot (int)
	def on_slidervolume_valueChanged (self, value):

		volmax = self.ui.slidervolume.maximum()
		volmin = self.ui.slidervolume.minimum()

		if value == 0:
			self.ui.buttonvolume.setIcon (QtGui.QIcon (':/images/mute.png'))
		elif value < (volmin + (volmax - volmin) / 3):
			self.ui.buttonvolume.setIcon (QtGui.QIcon (':/images/volume.png'))
		elif value < (volmin + (volmax - volmin) * 2 / 3):
			self.ui.buttonvolume.setIcon (QtGui.QIcon (':/images/weakvolume.png'))
		else:
			self.ui.buttonvolume.setIcon (QtGui.QIcon (':/images/strongvolume.png'))

	@QtCore.Slot()
	def playersetbuttonplay (self):
		self.ui.buttonplayerplay.setIcon (QtGui.QIcon (':/images/play.png'))

	@QtCore.Slot()
	def playersetbuttonpause (self):
		self.ui.buttonplayerplay.setIcon (QtGui.QIcon (':/images/pause2.png'))

	@QtCore.Slot()
	def on_buttoncancelbrowse_clicked (self):
		self.player.setloopsignal.emit (0, 0)

		self.ui.buttoncancelbrowse.hide()
		self.ui.buttonpreview.show()

		self.updatelineeditblocked = False
		self.ui.lineeditstarttime.setEnabled (True)
		self.ui.lineeditendtime.setEnabled (True)
		
	@QtCore.Slot()
	def on_buttonpreview_clicked (self):

		self.updatelineeditblocked = True
		self.ui.lineeditstarttime.setEnabled (False)
		self.ui.lineeditendtime.setEnabled (False)

		starttime = str2time (self.ui.lineeditstarttime.text())
		stoptime = str2time (self.ui.lineeditendtime.text())
		if starttime < 0 or stoptime <= starttime:
			msg = QtGui.QMessageBox()
			msg.setInformativeText (self.tr ("Start time or stop time invalid."))
			msg.exec_()
			self.on_buttoncancelbrowse_clicked()
			return

		self.player.setloopsignal.emit (self.ui.lineeditstarttime.text(), self.ui.lineeditendtime.text())

		self.ui.buttonpreview.hide()
		self.ui.buttoncancelbrowse.show()

	def createmerger (self):

		self.merger = VideoMerger (self.username, self)

		self.merger.appendtasksignal.connect (self.merger.appendtask)
		self.merger.switchrowsignal.connect (self.merger.switchrow)
		self.merger.removerowsignal.connect (self.merger.removerow)
		self.merger.updatemodel.connect (self.updatemergemodel)
		self.merger.startsignal.connect (self.merger.startworker)
		self.merger.cancelsignal.connect (self.merger.quitworker)

	@QtCore.Slot()
	def on_buttonplus_clicked (self):

		files = QtGui.QFileDialog.getOpenFileNames (self, self.tr ("Open"),
				QtGui.QDesktopServices.storageLocation (QtGui.QDesktopServices.MoviesLocation))[0]
		model = self.ui.mergeview.model()

		while len (files) > 0:
			newfile = QtCore.QFileInfo (files.pop (0))

			row = model.rowCount()
			model.insertRow (row)

			model.setData (model.index (row, 0), newfile.fileName())
			model.setData (model.index (row, 3), (0, self.tr ("Not Started")))

			self.ui.labelmerge.setText (self.tr ("There are %d video clips to be merged.") % (row + 1))

			checker = MediaFileChecker (newfile.absoluteFilePath(), len (self.checkers))
			checker.discoveredsignal.connect (self.mediafilediscovered)
			checker.finished.connect (checker.deleteLater)
			checker.startworker()
			self.checkers.append ({"worker": checker, "operation": "Merge", "params": (newfile.absoluteFilePath(), row)})

	@QtCore.Slot()
	def on_buttonup_clicked (self):
		row = self.ui.mergeview.currentIndex().row()
		model = self.ui.mergeview.model()

		if row <= 1:
			return
		
		model.insertRow (row - 1, model.takeRow (row))
		self.merger.switchrowsignal.emit (row, row - 1)
		self.ui.mergeview.setCurrentIndex (model.index (row - 1, 0))

	@QtCore.Slot()
	def on_buttondown_clicked (self):
		row = self.ui.mergeview.currentIndex().row()
		model = self.ui.mergeview.model()

		if row >= model.rowCount() - 1:
			return

		model.insertRow (row + 1, model.takeRow (row))
		self.merger.switchrowsignal.emit (row, row + 1)
		self.ui.mergeview.setCurrentIndex (model.index (row + 1, 0))

	@QtCore.Slot()
	def on_buttondelete_clicked (self):
		row = self.ui.mergeview.currentIndex().row()
		self.ui.mergeview.model().takeRow (row)
		self.merger.removerowsignal.emit (row)

		rownum = self.ui.mergeview.model().rowCount()
		self.ui.labelmerge.setText (self.tr ("There are %d video clips to be merged.") % rownum)

	@QtCore.Slot()
	def on_buttonstart_clicked (self):
		filename = self.ui.lineeditfilenameblank.text()
		path = self.ui.lineeditsaveblank.text()

		if not os.path.exists (path) or not os.path.isdir (path):
			msg = QtGui.QMessageBox()
			msg.setInformativeText (self.tr ("Save destination invalid."))
			msg.exec_()
			return

		outputfile = QtCore.QFileInfo (os.path.join (path, filename))
		dstfile = outputfile.absolutePath()
		i = 0
		while os.path.exists (dstfile):
			i += 1
			dstfile = os.path.join (outputfile.absolutePath(), outputfile.baseName() + "-%02d.%s" % (i, outputfile.suffix()))
		os.close (os.open (dstfile, os.O_CREAT))

		self.merger.startsignal.emit (dstfile, outputfile.absolutePath())

	@QtCore.Slot()
	def on_buttoncancel_clicked (self):
		self.merger.cancelsignal.emit()

	@QtCore.Slot()
	def on_buttonexamine_clicked (self):
		exam = MergeExam (self.ui.lineeditfilenameblank.text(), self.ui.lineeditsaveblank.text())
		exam.move (self.pos() + self.rect().center() - exam.rect().center())
		exam.exec_()

	@QtCore.Slot (int, int)
	def updatemergemodel (self, row, value):
		model = self.ui.mergeview.model()
		rownum = model.rowCount()

		if row >= rownum:
			for i in xrange (rownum):
				model.setData (model.index (i, 3), (100, self.tr ("Finished")))
			return

		if value is not None:
			print "%d %d" % (value, model.data (model.index (row, 3))[0])
			if model.data (model.index (row, 3))[0] < value:
				if value < 100:
					model.setData (model.index (row, 3), (value, self.tr ("Processing...")))
				else:
					model.setData (model.index (row, 3), (100, self.tr ("Finished")))

			for i in xrange (row):
				model.setData (model.index (i, 3), (100, self.tr ("Finished")))

	@QtCore.Slot (unicode)
	def on_lineeditleadertitle_textChanged (self, text):
		self.ui.checkboxleadertitle.setChecked (True)

	@QtCore.Slot()
	def on_buttonsave_clicked (self):
		if not self.playerfile:
			return

		starttime = str2time (self.ui.lineeditstarttime.text())
		stoptime = str2time (self.ui.lineeditendtime.text())
		duration = stoptime - starttime
		if starttime < 0 or duration <= 0:
			msg = QtGui.QMessageBox()
			msg.setInformativeText (self.tr ("Start time or stop time invalid."))
			msg.exec_()
			return

		ss = SaveSplit (self.lastsplitpath)
		ss.move (self.pos() + self.rect().center() - ss.rect().center())
		if not ss.exec_() == QtGui.QDialog.Accepted:
			return

		outputname = os.path.join (ss.splitpath, ss.splitfile)

		if self.ui.checkboxleadertitle.isChecked():
			title = self.ui.lineeditleadertitle.text()
		else:
			title = None

		time = "%s -- %s" % (time2str (starttime), time2str (stoptime))

		outputfile = QtCore.QFileInfo (outputname)

		if outputfile.suffix() == "":
			outputname += ".%s" % (QtCore.QFileInfo (self.playerfile).suffix())
			outputfile = QtCore.QFileInfo (outputname)

		dstname = outputfile.absoluteFilePath()
		i = 0
		while os.path.exists (dstname):
			i += 1
			dstname = os.path.join (outputfile.absolutePath(), outputfile.baseName() + "-%02d.%s" % (i, outputfile.suffix()))
		os.close (os.open (dstname, os.O_CREAT))
		dstfile = QtCore.QFileInfo (dstname)

		checker = MediaFileChecker (self.playerfile, len (self.checkers))
		checker.discoveredsignal.connect (self.mediafilediscovered)
		checker.finished.connect (checker.deleteLater)
		checker.startworker()
		self.checkers.append ({"worker": checker, "operation": "Split",
			"params": [(self.playerfile, dstfile.absoluteFilePath(), starttime, duration, title, ss.totranscode, self),
				(self.username, time, dstfile.absolutePath(), dstfile.fileName())]})

	@QtCore.Slot (int, tuple)
	def updatetransmodel (self, row, value):
		model = self.ui.transview.model()
		rownum = model.rowCount()

		if row >= rownum:
			return

		if value[0] is not None:
			if model.data (model.index (row, 1)) < value[0]:
				model.setData (model.index (row, 1), value[0])

			if value[0] >= 100:
				self.transcoding [row] ["status"] = TransTaskFinished
				model.setData (model.index (row, 2), self.tr ("Finished"))

				if self.translisting == TransTaskProcessing:
					self.ui.transview.setRowHidden (row, QtCore.QModelIndex(), True)
				else:
					self.ui.transview.setRowHidden (row, QtCore.QModelIndex(), False)

		if value[1] is not None:
			model.setData (model.index (row, 2), value[1])

	def closeEvent (self, event):
		if self.trayicon.isVisible():
			self.hide()
			event.ignore()

	@QtCore.Slot()
	def on_buttontransnew_clicked (self):

		model = self.ui.transview.model()

		nc = NewConvert (self.lasttransferpath)
		if nc.exec_() == QtGui.QDialog.Accepted:

			files = nc.files
			newpath = nc.transferpath

			while len (files) > 0:
				newfile = QtCore.QFileInfo (files.pop (0))
				row = model.rowCount()
				model.insertRow (row)

				model.setData (model.index (row, 0), newfile.fileName())
				model.setData (model.index (row, 1), 0)
				model.setData (model.index (row, 2), self.tr ("Verifying File Parameters..."))

				model.setData (model.index (row, 3), newpath)

				dstfile = os.path.join (newpath, newfile.baseName() + ".mp4")
				i = 0
				while os.path.exists (dstfile):
					i += 1
					dstfile = os.path.join (newpath, newfile.baseName() + "-%02d.mp4" % i)
				os.close (os.open (dstfile, os.O_CREAT))

				checker = MediaFileChecker (newfile.absoluteFilePath(), len (self.checkers))
				checker.discoveredsignal.connect (self.mediafilediscovered)
				checker.finished.connect (checker.deleteLater)
				checker.startworker()
				self.checkers.append ({"worker": checker, "operation": "Transcode",
					"params": (newfile.absoluteFilePath(), dstfile, self.username, newpath, row, self)})
				self.transcoding.append ({"worker": None, "status": TransTaskVerifying})

	@QtCore.Slot (unicode)
	def addtranscode (self, filename):
		model = self.ui.transview.model()
		newfile = QtCore.QFileInfo (filename)
		row = model.rowCount()
		model.insertRow (row)

		model.setData (model.index (row, 0), newfile.fileName())
		model.setData (model.index (row, 1), 0)
		model.setData (model.index (row, 2), self.tr ("Transcoding..."))
		model.setData (model.index (row, 3), newfile.absolutePath())

		dstfile = os.path.join (newfile.absolutePath(), newfile.baseName() + ".mp4")
		i = 0
		while os.path.exists (dstfile):
			i += 1
			dstfile = os.path.join (newfile.absolutePath(), newfile.baseName() + "-%02d.mp4" % i)
		os.close (os.open (dstfile, os.O_CREAT))

		transcode = Transcoder (newfile.absoluteFilePath(), dstfile, self.username, newfile.absolutePath(), row, self)

		transcode.playsignal.connect (transcode.play)
		transcode.pausesignal.connect (transcode.pause)
		transcode.removesignal.connect (transcode.remove)
		transcode.updatemodel.connect (self.updatetransmodel)
		transcode.finished.connect (transcode.deleteLater)

		transcode.startworker()
		self.transcoding.append ({"worker": transcode, "status": TransTaskProcessing})

	@QtCore.Slot()
	def on_buttontransbegin_clicked (self):
		for i in xrange (self.ui.transview.model().rowCount()):
			if self.transcoding [i] ["status"] == TransTaskProcessing:
				self.transcoding [i] ["worker"].playsignal.emit()

	@QtCore.Slot()
	def on_buttontranspause_clicked (self):
		for i in xrange (self.ui.transview.model().rowCount()):
			if self.transcoding [i] ["status"] == TransTaskProcessing:
				self.transcoding [i] ["worker"].pausesignal.emit()

	@QtCore.Slot()
	def on_buttontransdelete_clicked (self):
		row = self.ui.transview.currentIndex().row()
		if self.transcoding [row] ["status"] == TransTaskProcessing:
			self.transcoding [row] ["worker"].removesignal.emit()
		self.transcoding [row] ["status"] = TransTaskDeleted
		self.ui.transview.setRowHidden (row, QtCore.QModelIndex(), True)

	@QtCore.Slot()
	def on_listWidget_itemClicked (self):
		self.translisting = self.ui.listWidget.currentRow()

		for row in xrange (self.ui.transview.model().rowCount()):
			if self.transcoding [row] ["status"] == self.translisting:
				self.ui.transview.setRowHidden (row, QtCore.QModelIndex(), False)
			else:
				self.ui.transview.setRowHidden (row, QtCore.QModelIndex(), True)

	@QtCore.Slot()
	def on_buttonbrowse_clicked (self):
		self.ui.lineeditsaveblank.setText (QtGui.QFileDialog.getExistingDirectory (self, self.tr ("Select output directory")))

	@QtCore.Slot()
	def on_MovieEdit_clicked (self):
		self.ui.stackedWidget.setCurrentIndex (0)

	@QtCore.Slot()
	def on_FormatConvert_clicked (self):
		self.ui.stackedWidget.setCurrentIndex (1)

	@QtCore.Slot()
	def on_buttonvideomerge_clicked (self):
		self.ui.stackedWidget_2.setCurrentIndex (1)

	@QtCore.Slot()
	def on_buttonvideointerceptpage_clicked (self):
		self.ui.stackedWidget_2.setCurrentIndex (0)

	@QtCore.Slot (int, bool, dict)
	def mediafilediscovered (self, row, verified, params):

		if row >= len (self.checkers):
			return

		checker = self.checkers[row]

		if not verified:
			le = LoadError()
			le.move (self.pos() + self.rect().center() - le.rect().center())
			le.exec_()

		if checker["operation"] == "Merge":

			mergerow = checker["params"][1]
			model = self.ui.mergeview.model()

			if not verified:
				model.setData (model.index (mergerow, 1), "%s" % (self.tr ("Video Source Criteria Not Met")))
				model.setData (model.index (mergerow, 2), "")
				try:
					os.remove (checker["params"][0])
				except:
					pass
			else:
				model.setData (model.index (mergerow, 1), "%s" % (time2str (params["length"])))
				model.setData (model.index (mergerow, 2), "%d X %d" % (params["videowidth"], params["videoheight"]))

			self.merger.appendtasksignal.emit (params, *checker["params"])

		elif checker["operation"] == "Split":

			if not verified:
				try:
					os.remove (checker["params"][0][1])
				except:
					pass
				return

			self.splitter = VideoSplitter (params, *checker["params"][0])
			self.splitter.finished.connect (self.splitter.deleteLater)
			self.splitter.addtranscode.connect (self.addtranscode)
			self.splitter.startworker (*checker["params"][1])

		elif checker["operation"] == "Transcode":

			transrow = checker["params"][4]

			if not verified:
				self.transcoding [transrow]["status"] = TransTaskDeleted
				self.ui.transview.setRowHidden (transrow, QtCore.QModelIndex(), True)
				try:
					os.remove (checker["params"][1])
				except:
					pass
				return

			transcode = Transcoder (*checker["params"])

			transcode.playsignal.connect (transcode.play)
			transcode.pausesignal.connect (transcode.pause)
			transcode.removesignal.connect (transcode.remove)
			transcode.updatemodel.connect (self.updatetransmodel)
			transcode.finished.connect (transcode.deleteLater)

			transcode.startworker()
			self.transcoding [transrow]["worker"] = transcode
			self.transcoding [transrow]["status"] = TransTaskProcessing

	def eventFilter (self, obj, event):
		if event.type() == QtCore.QEvent.FocusIn and not self.updatelineeditblocked:
			if obj == self.ui.lineeditstarttime:
				self.splitchoose = SplitAdjustStart
			elif obj == self.ui.lineeditendtime:
				self.splitchoose = SplitAdjustStop

		return QtGui.QWidget.eventFilter (self, obj, event)

	def mouseMoveEvent (self, event):
		super (MainWindow, self).mouseMoveEvent (event)

		if self.leftclicked == True:

			if self.isMaximized():
				self.ui.buttonmaximize.setIcon (QtGui.QIcon (':/images/maximize.png'))

				origsize = self.rect().size()
				self.showNormal()
				newsize = self.rect().size()

				xfactor = float (newsize.width()) / origsize.width()
				yfactor = float (newsize.height()) / origsize.height()

				self.startdragging.setX (self.startdragging.x() * xfactor)
				self.startdragging.setY (self.startdragging.y() * yfactor)

			self.move (event.globalPos() - self.startdragging)

	def mousePressEvent (self, event):
		super (MainWindow, self).mousePressEvent (event)
		if event.button() == QtCore.Qt.LeftButton:
			self.leftclicked = True
			self.startdragging = event.globalPos() - self.pos()
			self.clickedpos = event.globalPos()

	def mouseReleaseEvent (self, event):
		super (MainWindow, self).mouseReleaseEvent (event)
		self.leftclicked = False

	def mouseDoubleClickEvent (self, event):
		super (MainWindow, self).mouseDoubleClickEvent (event)
		self.on_buttonmaximize_clicked()

	def frameMouseRelease (self, event):
		super (MainWindow, self).mouseReleaseEvent (event)
		if event.button() == QtCore.Qt.LeftButton and event.globalPos() == self.clickedpos:
			self.leftclicked = False
			self.ui.buttonplayerplay.clicked.emit()

	def resizeEvent (self, event):
		pixmap = QtGui.QPixmap (self.size())
		painter = QtGui.QPainter()
		painter.begin (pixmap)
		painter.fillRect (pixmap.rect(), QtCore.Qt.white)
		painter.setBrush (QtCore.Qt.black)
		painter.drawRoundRect (pixmap.rect(), 3, 3)
		painter.end()

		self.setMask (pixmap.createMaskFromColor (QtCore.Qt.white))
