
import wave
import numpy as np

def generate_sine_wave(frequency, sample_rate, duration):
    num_samples = duration * sample_rate
    t = np.linspace(0, duration, num_samples, False)
    waveform = np.sin(2 * np.pi * frequency * t)
    return waveform

def save_wave_to_file(waveform, file_name, sample_rate):
    nchannels = 1
    sampwidth = 2  # 2 bytes (16 bits) per sample
    nframes = len(waveform)
    comptype = "NONE"
    compname = "not compressed"
    waveform_normalized = np.int16((waveform / waveform.max()) * 32767)

    with wave.open(file_name, 'w') as wave_file:
        wave_file.setparams((nchannels, sampwidth, sample_rate, nframes, comptype, compname))
        wave_file.writeframes(waveform_normalized.tobytes())

def generate_and_save_harmonics(fundamental_freq, num_harmonics=16, sample_rate=44100, duration=4):
    for n in range(1, num_harmonics + 1):
        harmonic_freq = fundamental_freq * n
        waveform = generate_sine_wave(harmonic_freq, sample_rate, duration)
        file_name = f"{fundamental_freq}_{n}th_{harmonic_freq}.wav"
        save_wave_to_file(waveform, file_name, sample_rate)

# Example usage with a fundamental frequency of 78 Hz
generate_and_save_harmonics(78)
