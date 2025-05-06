import pyaudio
import wave
import matplotlib.pyplot as plt
import numpy as np
import threading
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from pygame import mixer

class VoiceRecorder():
    def __init__(self, frames_per_buffer=3200, format=pyaudio.paInt16, channels=1, rate=16000):
        self.frames_per_buffer = frames_per_buffer
        self.format = format
        self.rate = rate
        self.channels = channels
        self.frames = []
        self.pa = pyaudio.PyAudio()
        self.stream = None
        self.is_recording = False  
        self.remaining_time = 0
        mixer.init()

    def start_recording(self, seconds=8):

        self.is_recording = True
        self.frames = []
        self.remaining_time = seconds

        threading.Thread(target=self.record, args=(self.remaining_time,)).start()

    def record(self, seconds):
        self.stream = self.pa.open(
            format=self.format,
            channels=self.channels,
            rate=self.rate,
            input=True,
            frames_per_buffer=self.frames_per_buffer
        )

        print("Start Recording...")
        second_tracking = 0
        second_count = 0

        for i in range(0, int(self.rate / self.frames_per_buffer * seconds)):
            if not self.is_recording: 
                self.remaining_time  = seconds - second_count
                break
            data = self.stream.read(self.frames_per_buffer)
            self.frames.append(data)
            second_tracking += 1
            if second_tracking == self.rate / self.frames_per_buffer:
                second_count += 1
                second_tracking = 0
                print(f'Time left: {seconds - second_count} seconds')

        self.stop_recording() 

    def pause_button(self):
        if self.is_recording:
            self.is_recording = False
            print("Recording Paused.")
        else:
            self.is_recording = True
            print("Recording Resumed.")
            threading.Thread(target=self.record, args=(self.remaining_time,)).start()

    def stop_recording(self):

        if not self.is_recording:
            return

        self.is_recording = False  
        if self.stream is not None:
            self.stream.stop_stream()
            self.stream.close()
            self.stream = None  

    def save_recording(self, filename='output/voice_record.wav'):
        obj = wave.open(filename, 'wb')
        obj.setnchannels(self.channels)
        obj.setsampwidth(self.pa.get_sample_size(self.format))
        obj.setframerate(self.rate)
        obj.writeframes(b''.join(self.frames))
        obj.close()

    def plot_recording(self, frame, filename='output/voice_record.wav'):

        file_name = wave.open(filename, 'rb')  
        sample_freq = file_name.getframerate()
        frames = file_name.getnframes()
        signal_wave = file_name.readframes(-1)
        file_name.close()

        time = frames / sample_freq
        audio_array = np.frombuffer(signal_wave, dtype=np.int16)
        times = np.linspace(0, time, num=frames)

        fig, ax = plt.subplots(figsize=(6,4))
        ax.plot(times, audio_array)
        ax.set_title('Visual Representation', color='gray')
        ax.set_ylabel('Signal Wave', color='gray')
        ax.set_xlabel('Time (s)', color='gray')
        fig.patch.set_alpha(0)
        ax.set_facecolor('none')
        ax.grid(visible=True)
        ax.tick_params(axis='x', colors='gray')
        ax.tick_params(axis='y', colors='gray')

        for widget in frame.winfo_children():
            widget.destroy()

        plot_canvas = FigureCanvasTkAgg(fig, master=frame)
        plot_canvas.get_tk_widget().pack()
        plot_canvas.draw()

    def play_audio(self):
        mixer.music.load('output/voice_record.wav')
        mixer.music.play()

    def stop_audio(self):
        mixer.music.stop()

    def pause_audio(self):
        mixer.music.pause()
    
    def unpause_audio(self):
        mixer.music.unpause()

