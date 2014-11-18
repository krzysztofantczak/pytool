import sys

from PySide import QtCore, QtGui
# from PySide.QtGui import QMessageBox

class ui:

    @staticmethod
    def test():

        print "[PROVIDER]\tui testingz"

    @staticmethod
    def init():

        app = QtGui.QApplication(sys.argv)
        # main_window = QtGui.MainWindowClass()
        # main_window.show()

        QtGui.QWidget()

        sys.exit(app.exec_())


    @staticmethod
    def alert(msg):

        msgBox = QtGui.QMessageBox()
        msgBox.setText(msg)
        msgBox.exec_()
