import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from PIL import Image, ImageTk
from ttkbootstrap.dialogs import Messagebox
from VoiceRecorder import VoiceRecorder

class VoiceRecorderGUI():
    def __init__(self):
        self.root = ttk.Window()
        self.style = ttk.Style()
        self.theme_names = self.style.theme_names()
        self.root.title('Voice Recorder')
        self.root.geometry("600x400")
        self.vr = VoiceRecorder()

        self.header = ttk.Frame(self.root, padding=(10, 10, 10, 0))
        self.header.pack(fill=X, expand=YES)

        main_icon = Image.open('assets/images/mic.png').resize((30, 30))
        img = ImageTk.PhotoImage(main_icon)
        panel = ttk.Label(self.header, image=img)
        panel.image = img
        panel.pack(side=LEFT)

        mic_on = Image.open('assets/images/microphone_icon.png').resize((250, 250))
        self.mic_on_icon = ImageTk.PhotoImage(mic_on)
        mic_off = Image.open('assets/images/microphone_slash_icon.png').resize((250, 250))
        self.mic_off_icon = ImageTk.PhotoImage(mic_off)
        
        ttk.Label(self.header, text="Voice Recorder", font="-size 24 -weight bold").pack(side=LEFT)

        self.theme_choices = ttk.Combobox(
            master=self.header,
            text=self.style.theme.name,
            values=self.theme_names,
            state=READONLY
        )
        self.theme_choices.pack(side=RIGHT)

        ttk.Label(self.header, text="Themes: ", font="-size 12 -weight bold").pack(side=RIGHT)
        self.theme_choices.current(self.theme_names.index(self.style.theme.name))
        self.theme_choices.bind('<<ComboboxSelected>>', self.change_theme)

        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(fill=BOTH)

        self.voice_recorder_frame = ttk.LabelFrame(self.main_frame, text='Audio Recorder')
        self.voice_recorder_frame.pack(side=LEFT, fill=BOTH, expand=YES, padx=5, pady=5)

        self.mic_panel = ttk.Label(self.voice_recorder_frame, image=self.mic_off_icon)
        self.mic_panel.pack()

        self.start_button = ttk.Button(self.voice_recorder_frame, text='Start', bootstyle='primary', command=self.handle_recording)
        self.start_button.pack(side=LEFT, expand=YES, pady=10)
        self.pause_button = ttk.Button(self.voice_recorder_frame, text='Pause', bootstyle='secondary', command=self.handle_pause)
        self.pause_button.pack(side=LEFT, expand=YES, pady=10)
        self.stop_button = ttk.Button(self.voice_recorder_frame, text='Stop', bootstyle='danger', command=self.handle_stop_recording)
        self.stop_button.pack(side=LEFT, expand=YES, pady=10)
        self.save_button = ttk.Button(self.voice_recorder_frame, text='Save', bootstyle='success', command=self.handle_save_recording)
        self.save_button.pack(side=LEFT, expand=YES, pady=10)
        self.plot_button = ttk.Button(self.voice_recorder_frame, text='Plot', bootstyle='info', command=self.handle_plotting)
        self.plot_button.pack(side=LEFT, expand=YES, pady=10)

        self.audio_player_frame = ttk.LabelFrame(self.main_frame, text='Audio Player')
        self.audio_player_frame.pack(fill=BOTH, padx=5, expand=YES, pady=5)

        self.pause_audio_button = ttk.Button(self.audio_player_frame, text='Pause', bootstyle='secondary', command=self.vr.pause_audio)
        self.pause_audio_button.pack(side=LEFT, expand=YES, pady=10)
        self.unpause_audio_button = ttk.Button(self.audio_player_frame, text='Unpause', bootstyle='warning', command=self.vr.unpause_audio)
        self.unpause_audio_button.pack(side=LEFT, expand=YES, pady=10)
        self.play_audio_button = ttk.Button(self.audio_player_frame, text='Play', bootstyle='primary', command=self.vr.play_audio)
        self.play_audio_button.pack(side=LEFT, expand=YES, pady=10)
        self.stop_audio_button = ttk.Button(self.audio_player_frame, text='Stop', bootstyle='danger', command=self.vr.stop_audio)
        self.stop_audio_button.pack(side=LEFT, expand=YES, pady=10)

        self.plot_frame = ttk.LabelFrame(self.main_frame, text='Visual Representation', width=400, height=400)
        self.plot_frame.pack(side=RIGHT,fill=BOTH, padx=5, pady=5)

    def handle_pause(self):
        self.vr.pause_button()
        if self.vr.is_recording:
            self.mic_panel.configure(image=self.mic_on_icon)
            self.pause_button.config(text='Pause', bootstyle='secondary')
        else:
            self.mic_panel.configure(image=self.mic_off_icon)
            self.pause_button.config(text='Resume', bootstyle='warning')

    def handle_recording(self):

        if self.vr.is_recording:
            Messagebox.show_error("Already recording!")
            return
        
        Messagebox.show_info("Recording start")
        self.mic_panel.configure(image=self.mic_on_icon)
        self.vr.start_recording()

    def handle_stop_recording(self):
        self.vr.stop_recording()
        self.mic_panel.configure(image=self.mic_off_icon)
        Messagebox.show_info("Recording stopped!")

    def handle_save_recording(self):
        confirm = Messagebox.yesno("Do you want to save your recording?")

        if confirm == "Yes":
            self.vr.save_recording()
        else:
            return

    def handle_plotting(self):
        confirm = Messagebox.yesno("Do you want to plot the recording?")

        if confirm == "Yes":
            self.vr.plot_recording(self.plot_frame)
        else:
            return

    def change_theme(self, event):
        theme = self.theme_choices.get()
        self.style.theme_use(theme)
        self.theme_choices.selection_clear()