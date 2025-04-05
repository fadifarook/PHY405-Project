from scipy.io.wavfile import write
import numpy as np
import matplotlib.pyplot as plt

# Parameters
samplerate = 44100  # Sampling rate
freq1 = 25  # First tone frequency
freq2 = 50  # Second tone frequency
duration = 1000 / np.gcd(freq1, freq2)  # A long signal for testing
t = np.linspace(0, duration, int(samplerate * duration), endpoint=False)

# Generate the wave
amplitude = np.iinfo(np.int16).max / 4
data = amplitude * (np.sin(2 * np.pi * freq1 * t) + np.sin(2 * np.pi * freq2 * t))

# Save the audio file
write("two_tone.wav", samplerate, data.astype(np.int16))


# Plot the first two cycles
plt.plot(t, data)
plt.xlim(0, 2 * 1 / np.gcd(freq1, freq2))
plt.xlabel("Time [s]")
plt.ylabel("Audio Signal")
plt.savefig("Two Tone")
