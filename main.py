# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QApplication,QMainWindow,QStyleFactory,QFileDialog,QMessageBox
from user_interface.mainwindow import Ui_MainWindow
from PyQt5.QtCore import pyqtSlot
from utils import audio_utils as au
from utils import mi_band as mb
import shutil



import sys
import os

class App(QMainWindow):
    def __init__(self):
        super(App, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup()
        
    def setup(self):
        self.ui.progressBar.hide()
        self.update_audio()
        self.thread_play = None
        
        if not os.path.exists('data_lagu'):
            os.mkdir('data_lagu')
        
        self.ui.add.clicked.connect(self.addfile)
        self.ui.delete_2.clicked.connect(self.delete_file)
        self.ui.mi_band.clicked.connect(self.connect_mi_band)
        self.ui.play.clicked.connect(self.play_audio)
        self.ui.next.clicked.connect(self.next_audio)
        self.ui.prev.clicked.connect(self.prev_audio)
        
        self.file_active = None
        
        self.ui.play_list.currentItemChanged.connect(self.changefile)
        
        
    def addfile(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"Open audio File", "","Audio Files (*.wav)", options=options)
        
        if fileName:
            name = fileName.split("/")[-1].split('.')[0].replace(' ','_')
            if os.path.isdir(os.path.join('data_lagu',name)):
                buttonReply = QMessageBox.question(self, 'File already exist', f"Are you sure rewrite \"{name}\"?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if buttonReply == QMessageBox.Yes:
                    self.delete_audio(name)
                    self.thread = au.init_audio(fileName,parent = self)
                    self.thread.ind.connect(self.progress)
                    self.thread.start()
                    
                else:
                    return
                
            else:
                self.thread = au.init_audio(fileName,parent = self)
                self.thread.ind.connect(self.progress)
                self.thread.start()
    
    def delete_file(self):
        if self.ui.play_list.currentItem() is not None:
            name = self.ui.play_list.currentItem().text().split(' ')[-1]
            self.delete_audio(name)
            
    def next_audio(self):
        n = (self.ui.play_list.currentRow()+1)%self.ui.play_list.count()
        self.ui.play_list.setCurrentRow(n)
        
    def prev_audio(self):
        n = (self.ui.play_list.currentRow()-1)%self.ui.play_list.count()
        self.ui.play_list.setCurrentRow(n)
        
    def play_audio(self,n):
        if self.ui.play.text() == 'PLAY':
            self.ui.play.setText('STOP')
            self.dissable_widget(False,mode = 'play')
            if self.ui.play_list.currentItem() is not None:
                name = self.file_active.split(' ')[-1]
                file_path = os.path.join('data_lagu',name)
                self.thread_play = au.play_audio(file_audio=file_path,parent=self)
                self.thread_play.start()
            
        else:
            self.thread_play.stop()
            self.thread_play.quit()
            self.dissable_widget(True,mode = 'play')
            self.ui.play.setText('PLAY')
            
    def changefile(self):
        self.ui.label_play.setText(self.ui.play_list.currentItem().text())
        self.file_active = self.ui.play_list.currentItem().text()
        
    def update_audio(self):
        self.ui.play_list.clear()
        list_audio =  os.listdir('data_lagu/')
        for n, file in enumerate (list_audio):
            self.ui.play_list.addItem(str(n+1) + '. '+file)
        
    def delete_audio(self,name):
        filepath = os.path.join(os.getcwd(),'data_lagu',name)
        buttonReply = QMessageBox.question(self, 'Delete Audio File', f"Are you sure delete \"{name}\"?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            shutil.rmtree(filepath)
        else:
            pass
        self.update_audio()
        
    def dissable_widget(self, state, mode = 'init'):
        self.ui.delete_2.setEnabled(state)
        self.ui.mi_band.setEnabled(state)
        self.ui.prev.setEnabled(state)
        self.ui.next.setEnabled(state)
        self.ui.play_list.setEnabled(state)
        if mode == 'init':
            self.ui.play.setEnabled(state)
        else:
            self.ui.add.setEnabled(state)
    
    def connect_mi_band(self):
        self.thread_mi = mb.MiBand(parent = self)
        self.thread_mi.value.connect(self.mi_value)
        self.thread_mi.start()
        
    @pyqtSlot(int)
    def mi_value(self,n):
        if n < 60:
            self.ui.lcd_heart.setStyleSheet("""QLCDNumber {
                                                background-color: white; 
                                                color: yellow; }""")
        elif n > 100:
            self.ui.lcd_heart.setStyleSheet("""QLCDNumber { 
                                                color: red;
                                                background-color: white; }""")
        else :
            self.ui.lcd_heart.setStyleSheet("""QLCDNumber { 
                                                color: green; 
                                                background-color: white; }""")
        self.ui.lcd_heart.display(n)
        
        if self.thread_play is not None:
            self.thread_play.change_heart_value(n)
        
    @pyqtSlot(int)
    def progress(self,n):
        if n == 0 :
            self.ui.progressBar.show()
            self.dissable_widget(False)
            
        elif n == 100:
            self.ui.progressBar.hide()
            self.ui.progressBar.setValue(0)
            self.update_audio()
            self.dissable_widget(True)
            
        self.ui.progressBar.setValue(n)
        
        
if __name__ == "__main__":

    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create('Fusion'))
    Dialog = App()
    Dialog.show()
    Dialog.setWindowTitle("Audio TSM")
    result = app.exec_()
    sys.exit(result)