# -*- coding: utf-8 -*-
import os
import wave
import sys
import time
import psutil

import scipy.io.wavfile as wavfile
from shutil import copyfile

from PyQt5.QtCore import QThread, pyqtSignal
# PyAudio Library
import pyaudio


class WavePlayerLoop(QThread) :
  """
  A simple class based on PyAudio to play wave loop.

  It's a threading class. You can play audio while your application
  continues to do its stuff. :)
  """

  CHUNK = 1024

  def __init__(self,filepath,loop=True) :
    """
    Initialize `WavePlayerLoop` class.

    PARAM:
        -- filepath (String) : File Path to wave file.
        -- loop (boolean)    : True if you want loop playback. 
                               False otherwise.
    """
    super(WavePlayerLoop, self).__init__()
    self.filepath = os.path.abspath(filepath)
    self.loop = loop

    # Open Wave File
    self.wf = wave.open(self.filepath, 'rb')

  def run(self):
    player = pyaudio.PyAudio()

    # Open Output Stream (basen on PyAudio tutorial)
    stream = player.open(format = player.get_format_from_width(self.wf.getsampwidth()),
        channels = self.wf.getnchannels(),
        rate = self.wf.getframerate(),
        output = True)

    # PLAYBACK LOOP
    data = self.wf.readframes(self.CHUNK)
    while self.loop :
      stream.write(data)
      data = self.wf.readframes(self.CHUNK)
      if data == '' : # If file is over then rewind.
        self.wf.rewind()
        data = self.wf.readframes(self.CHUNK)

    stream.close()
    player.terminate()


  def play(self) :
    """
    Just another name for self.start()
    """
    self.start()

  def stop(self) :
    """
    Stop playback. 
    """
    self.loop = False


  def getDuration(self) :
    """ 
    in ms. 
    """
    return (self.wf.getnframes() / self.wf.getframerate()) * 1000



class init_audio(QThread):
    ind = pyqtSignal(int)
    def __init__(self, file_original,parent=None):
        super(init_audio, self).__init__(parent)
        self.file_original = file_original
        
    def run(self):
        file_original = self.file_original
        base_path = 'data_lagu'
        name = file_original.split("/")[-1].split('.')[0].replace(' ','_')
        
        file_path = os.path.join(base_path,name)
        if not os.path.exists(file_path):
            os.mkdir(file_path)
            
        run_path = os.path.join(file_path,"run")
        if not os.path.exists(run_path):
            os.mkdir(run_path)
            
        track_path = os.path.join(file_path,"track")
        if not os.path.exists(track_path):
            os.mkdir(track_path)
            
        if os.path.isfile(file_original) == 0: #if false
            return
    
        player = WavePlayerLoop(file_original)
        
        length_original = player.getDuration()
        start_length = 0
        devide = 5000
    
        i = 0
        fs, data = wavfile.read(file_original)
        
        while start_length <= length_original:
            self.ind.emit(int(100*i/(length_original//devide)))
            
            end_length = (start_length) + (devide)
            start = float(fs) * (start_length/1000)
            end = float(fs) * (end_length/1000)
          
            start_length = end_length
    
            mid_secs = data[int(start):int(end)]
            wavfile.write(track_path+'/' + str(i) + "-n" + ".wav", fs, mid_secs)
            i = i + 1
        
        count = i
        i = 0
        
        file_out_wsola = os.path.join(os.getcwd(),run_path,f"wsola_{name}.wav")
        file_wsola = "audiotsm-master/examples/audiotsmcli.py"
        
        while 1:
            self.ind.emit(int(100*i/count))
            current_file = os.path.join(os.getcwd(),track_path,str(i)+"-n"+".wav")

            if os.path.isfile(current_file) == 0: #if false
                break
            
            os.system("python " + file_wsola + " -s 1.5 -o " + file_out_wsola + " " + current_file)
            copyfile(file_out_wsola, track_path+'/'  + str(i) + "-f" + ".wav")
            
            os.system("python " + file_wsola + " -s 0.5 -o " + file_out_wsola + " " + current_file)
            copyfile(file_out_wsola, track_path+'/' + str(i) + "-s" + ".wav")
            
            i += 1
            
            
class play_audio(QThread):
    def __init__(self, file_audio,parent=None):
        super(play_audio, self).__init__(parent)
        
        self.files = []
        self.players = [[],[],[]]
        self.filepath = file_audio
        self.heart_value = 40
        self.stop_loop = False
        
    def run(self):
        i = 0
        while 1:
            current_file = os.path.join(self.filepath ,"track" , str(i) + "-s" + ".wav")
            if os.path.isfile(current_file) == 0: #if false
                break
            self.players[0].append(WavePlayerLoop(current_file))
    
    
            current_file = os.path.join(self.filepath ,"track" , str(i) + "-n" + ".wav")
            if os.path.isfile(current_file) == 0: #if false
                break
            self.players[1].append(WavePlayerLoop(current_file))
            
            current_file = os.path.join(self.filepath ,"track" , str(i) + "-f" + ".wav")
            if os.path.isfile(current_file) == 0: #if false
                break
            self.players[2].append(WavePlayerLoop(current_file))
            
            i += 1
    
        i = 0
        while not self.stop_loop:
#            self.heart_value = (self.heart_value+5)%120
            
            heartrate = self.get_heart_value()
            if(heartrate < 60):
                speed = 2
                current_file = os.path.join(self.filepath ,"track" , str(i) + "-s" + ".wav")
                #m = open("fast.txt", "r")
            elif(heartrate > 100):
                speed = 0
                current_file = os.path.join(self.filepath ,"track" , str(i) + "-f" + ".wav")
                #m = open("slow.txt", "r")
            else:
                speed = 1
                current_file = os.path.join(self.filepath ,"track" , str(i) + "-n" + ".wav")
                #m = open("normal.txt", "r")
    
            #mi = m.read()
    
            #if(mi == ''):
           #     mi = 0
    
            start_mi_band = float(0)
            end_mi_band = time.time()
    
            delay_mi_band = end_mi_band - start_mi_band
    
            with open("delay_mi_band.txt", "a") as myFile:
                myFile.write(str(delay_mi_band * 1000) + '\n')
    
            self.files.append(current_file)
    
            a = time.time()
            
            length = self.players[speed][i].getDuration()
            self.players[speed][i].play()
    
            b = time.time()
    
            start_time = time.time()
            current_time = time.time()
    
            diff = 0
    
            while diff * 1000 <= length:
                current_time = time.time()
                diff = (current_time - start_time) #second
                #print(player)
                print("speed " + str(speed) + " | " + "file-" + str(i) + " : " + str(diff * 1000) + " | delay : " + str((b - a) * 1000))
                
            self.players[speed][i].stop()
    
            i = i + 1
            
            if i > len(self.players[0])-1:
                break
    
        data = []
        for file in self.files:
            w = wave.open(file, 'rb')
            data.append( [w.getparams(), w.readframes(w.getnframes())] )
            w.close()
    
        output = wave.open(self.filepath + "/result.wav", 'wb')
        output.setparams(data[0][0])
    
        for d in data:
            output.writeframes(d[1])
    
        output.close()
        
    def change_heart_value(self, val):
        self.heart_value = val
    
    def get_heart_value(self):
        return self.heart_value
    
    def stop(self):
        self.stop_loop = True
