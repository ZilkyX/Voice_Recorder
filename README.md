🎙️ Voice Recorder & Time-Domain Visualization App
A Voice Recorder and Time-Domain Visualization desktop application built with Python and the ttkbootstrap library, featuring a modern UI with multiple theme options such as darkly, solar, cyborg, and more for a personalized appearance. This app lets you record your voice and visualize the waveform in graphical form. Control playback with play, pause, unpause, and stop functionality using pygame.mixer.

🧩 Features
🎤 Voice Recording
Capture your voice directly through your system’s microphone.

The audio is recorded in real-time and saved as a .wav file using the wave module.

The recording is designed to be lightweight and responsive, making it ideal for quick voice clips, testing, or audio input for further analysis.

Recording starts with a simple button click.

The sample rate and duration are predefined but can be modified in the code.

Saved .wav files are stored locally in the same directory.

📊 Time-Domain Visualization
After recording, the waveform of your voice is automatically plotted using matplotlib.

This time-domain representation shows how the amplitude of your voice signal varies over time.

Displays a clear and interactive plot of the waveform.

Useful for understanding the shape, silence gaps, and dynamics of the recorded audio.

The plot updates only after a new recording is made.

Visualization is embedded within the GUI using matplotlib’s FigureCanvasTkAgg.

⏯️ Playback Controls
Playback functionality is handled using pygame.mixer, enabling smooth control of the recorded audio:

Play: Begins audio playback of the most recent recording.

Pause: Temporarily halts playback at the current position.

Stop: Stops the playback.

Unpause: Resumes playback from the paused position.

This ensures a seamless review of the recorded clip directly from the GUI without needing external media players.

🎨 Themed User Interface
The entire application is styled using ttkbootstrap, a modern UI library built on top of Tkinter.

It provides a clean and professional interface with built-in support for theme switching.

Offers a selection of over 5+ prebuilt themes (e.g., darkly, solar, superhero, cyborg, morph).

Buttons, labels, frames, and the waveform plot integrate seamlessly with the selected theme.

This makes the app not only functional but visually appealing and customizable to user preferences.

📸 Screenshots
![Litera Theme Screenshot](assets/output_images/Screenshot%202025-05-06%20215517.png)
![Darkly Theme Screenshot](assets/output_images/Screenshot%202025-05-06%20215548.png)
![Superhero Theme Screenshot](assets/output_images/Screenshot%202025-05-06%20215610.png)
![Vapor Theme Screenshot](assets/output_images/Screenshot%202025-05-06%20215629.png)
