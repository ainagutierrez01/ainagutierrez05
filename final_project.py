# -*- coding: utf-8 -*-
"""final project.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-39M-CHfII_jmLzclfhUokaByyVoT3oy

# From source to sound: The impact of speaker enclosures and environment on audio transmission

## Acoustic Engineering 2024-2025

Rita Cots Forteza (U218913), Aina Gutiérrez Llaó (U213911), Pau Noguera Mulet (U213916), Xavier Riera Feliu de la Peña (U214387)

##### Functions imported

Uploading all the functions needed from previous seminars
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy

import numpy as np
import matplotlib.pyplot as plt
import IPython.display as ipd
from scipy.io.wavfile import read
from scipy.io.wavfile import write

from scipy.fft import fft
from scipy import signal as signal

import soundfile as sf

#We load all the packages that will be used
!git clone https://github.com/pzinemanas/sis1lab.git
import os
import numpy as np
import librosa
import soundfile as sf
import IPython.display as ipd
from scipy import signal
import matplotlib.pyplot as plt

from sis1lab.util import load_audio, plot_signals, plot_spectrogram, plot_mean_spectrogram

from IPython.display import Audio

from google.colab import drive
drive.mount('/content/drive')

def FFTvisualize(xx, Nfft, fs, fourier = False):
    """
    Visualizes the spectrum of a given signal using FFT.

    Parameters:
    xx (numpy.ndarray): The input signal in the temporal domain.
    Nfft (int): The number of points used in the FFT.
    fs (int): The sampling frequency in Hz.

    Returns:
    None: Displays the plot of the spectrum.
    """
    if fourier == True:
      zz = np.abs(np.fft.fft(xx, n=Nfft))
    else:
      zz = xx

    plt.figure(figsize=(15,5))

    xf = np.arange(0, fs, fs/Nfft)

    plt.plot(xf, zz)
    plt.title('Full Spectrum')
    plt.xlabel('Frequency (Hz)'), plt.ylabel('Energy')

    plt.figure(figsize=(15,5))
    plt.plot(xf[Nfft//2:], zz[Nfft//2:])
    plt.title('Half Spectrum')
    plt.xlabel('Frequency (Hz)'), plt.ylabel('Energy')

def FFTvisualize2(xx, Nfft, fs, fourier = False):
    """
    Visualizes the spectrum of a given signal using FFT.

    Parameters:
    xx (numpy.ndarray): The input signal in the temporal domain.
    Nfft (int): The number of points used in the FFT.
    fs (int): The sampling frequency in Hz.

    Returns:
    None: Displays the plot of the spectrum.
    """
    if fourier == True:
      zz = np.abs(np.fft.fft(xx, n=Nfft))
    else:
      zz = xx

    plt.figure(figsize=(15,5))

    xf = np.arange(0, fs, fs/Nfft)

    plt.plot(xf, zz)
    plt.title('Full Spectrum')
    plt.xlabel('Frequency (Hz)'), plt.ylabel('Energy')

    plt.figure(figsize=(15,5))
    plt.xlim([0, 10000])
    #plt.ylim([0, 730])
    plt.plot(xf, zz)
    plt.title('Half Spectrum')
    plt.xlabel('Frequency (Hz)'), plt.ylabel('Energia')

def FFTvisualize_multi(signals, NFFT, fs_list, labels, title, fourier = False):

    plt.figure(figsize=(15, 5))

    for xx, fs, label in zip(signals, fs_list, labels):
        if fourier:
            zz = np.abs(np.fft.fft(xx, n = NFFT))
        else:
            zz = xx

        xf = np.arange(0, fs, fs / NFFT)  # Frequency axis
        plt.plot(xf[:NFFT//2], zz[:NFFT//2], label = label)

    plt.title(title)
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Energy')
    plt.legend()
    plt.show()

"""##### Laser Sound uploaded"""

filepath_og = "/content/drive/Shareddrives/enginyeria acutica (yupii)/seminari 3/original_laser.wav"
note_og_laser, note_fs_og = load_audio(filepath_og)

print("The Original Laser Sound is:")
Audio(note_og_laser, rate = note_fs_og)

print("The sample rate is: ", note_fs_og)

NFFT = 48000
FFTvisualize(note_og_laser, NFFT, note_fs_og, True)

"""# ***ANALYSIS OF THE RECORDINGS***


---

### Recordings uploaded and trimmed:

First enclosure, insonorized room, sound recorder
"""

filepath = "/content/drive/Shareddrives/enginyeria acutica (yupii)/Gravacions LAB/Gravadora Bona/1r altaveu (Sala Insonoritzada).wav"
pr_inso_grav, pr_inso_grav_fs = load_audio(filepath)


print("The sample rate is", pr_inso_grav_fs)

Audio(pr_inso_grav, rate = pr_inso_grav_fs)

#plot_signals(pr_inso_grav, pr_inso_grav_fs)

t_start = 4.846

sample_start = int(t_start * pr_inso_grav_fs)
sample_end = sample_start + len(note_og_laser)

pr_inso_grav_trimmed = pr_inso_grav[sample_start:sample_end]

print("The first speaker enclousre in the insonorized room Trimmed is:")
Audio(pr_inso_grav_trimmed, rate = note_fs_og)

sf.write('pr_inso_grav_trimmed .wav', pr_inso_grav_trimmed, note_fs_og)
# plot_signals(pr_inso_grav_trimmed, note_fs_og)

NFFT = 44100

FFTvisualize(pr_inso_grav_trimmed, NFFT, pr_inso_grav_fs, True)

"""Second enclosure, insonorized room, sound recorder"""

filepath = "/content/drive/Shareddrives/enginyeria acutica (yupii)/Gravacions LAB/Gravadora Bona/2n altaveu (Sala Insonoritzada).wav"
sg_inso_grav, sg_inso_grav_fs = load_audio(filepath)

print("The sample rate is", sg_inso_grav_fs)

Audio(sg_inso_grav, rate = sg_inso_grav_fs)

#plot_signals(sg_inso_grav, sg_inso_grav_fs)

t_start = 4.268

sample_start = int(t_start * sg_inso_grav_fs)
sample_end = sample_start + len(note_og_laser)

sg_inso_grav_trimmed = sg_inso_grav[sample_start:sample_end]


print("The second speaker enclousre in the insonorized room Trimmed is:")
Audio(sg_inso_grav_trimmed, rate = note_fs_og)

sf.write('sg_inso_grav_trimmed.wav', sg_inso_grav_trimmed, note_fs_og)
#plot_signals(sg_inso_grav_trimmed, note_fs_og)

NFFT = 44100

FFTvisualize(sg_inso_grav_trimmed, NFFT, sg_inso_grav_fs, True)

"""Third enclosure, insonorized room, sound recorder"""

filepath = "/content/drive/Shareddrives/enginyeria acutica (yupii)/Gravacions LAB/Gravadora Bona/3r altaveu (Sala Insonoritzada).wav"
tr_inso_grav, tr_inso_grav_fs = load_audio(filepath)

print("The sample rate is", tr_inso_grav_fs)

Audio(tr_inso_grav, rate = tr_inso_grav_fs)

#plot_signals(tr_inso_grav, tr_inso_grav_fs)

t_start = 3.98

sample_start = int(t_start * tr_inso_grav_fs)
sample_end = sample_start + len(note_og_laser)

tr_inso_grav_trimmed = tr_inso_grav[sample_start:sample_end]


print("The third speaker enclousre in the insonorized room Trimmed is:")
Audio(tr_inso_grav_trimmed, rate = note_fs_og)

sf.write('tr_inso_grav_trimmed.wav', tr_inso_grav_trimmed, note_fs_og)
#plot_signals(tr_inso_grav_trimmed, note_fs_og)

NFFT = 44100

FFTvisualize(tr_inso_grav_trimmed, NFFT, tr_inso_grav_fs, True)

"""Fourth enclosure, insonorized room, sound recorder"""

filepath = "/content/drive/Shareddrives/enginyeria acutica (yupii)/Gravacions LAB/Gravadora Bona/4t altaveu (Sala Insonoritzada).wav"
qrt_inso_grav, qrt_inso_grav_fs = load_audio(filepath)

print("The sample rate is", qrt_inso_grav_fs)

Audio(qrt_inso_grav, rate = qrt_inso_grav_fs)

#plot_signals(qrt_inso_grav, qrt_inso_grav_fs)

t_start = 5.34

sample_start = int(t_start * qrt_inso_grav_fs)
sample_end = sample_start + len(note_og_laser)

qrt_inso_grav_trimmed = qrt_inso_grav[sample_start:sample_end]


print("The fourth speaker enclousre in the insonorized room Trimmed is:")
Audio(qrt_inso_grav_trimmed, rate = note_fs_og)

sf.write('qrt_inso_grav_trimmed.wav', qrt_inso_grav_trimmed, note_fs_og)
#plot_signals(qrt_inso_grav_trimmed, note_fs_og)

NFFT = 44100

FFTvisualize(qrt_inso_grav_trimmed, NFFT, qrt_inso_grav_fs, True)

"""Fifth enclosure, insonorized room, sound recorder"""

filepath = "/content/drive/Shareddrives/enginyeria acutica (yupii)/Gravacions LAB/Gravadora Bona/5e altaveu (Sala Insonoritzada).wav"
cinq_inso_grav, cinq_inso_grav_fs = load_audio(filepath)

print("The sample rate is", cinq_inso_grav_fs)

Audio(cinq_inso_grav, rate = cinq_inso_grav_fs)

#plot_signals(cinq_inso_grav, cinq_inso_grav_fs)

t_start = 7.54

sample_start = int(t_start * cinq_inso_grav_fs)
sample_end = sample_start + len(note_og_laser)

cinq_inso_grav_trimmed = cinq_inso_grav[sample_start:sample_end]


print("The fifth speaker enclousre in the insonorized room Trimmed is:")
Audio(cinq_inso_grav_trimmed, rate = note_fs_og)

sf.write('cinq_inso_grav_trimmed.wav', cinq_inso_grav_trimmed, note_fs_og)
#plot_signals(cinq_inso_grav_trimmed, note_fs_og)

NFFT = 44100

FFTvisualize(cinq_inso_grav_trimmed, NFFT, cinq_inso_grav_fs, True)

"""First enclosure, library room, sound recorder"""

filepath = "/content/drive/Shareddrives/enginyeria acutica (yupii)/Gravacions LAB/Gravadora Bona/1r altaveu (Sala Biblio).wav"
note_1biblio_grav, note_fs1biblio_grav = load_audio(filepath)

print("The sample rate is", note_fs1biblio_grav)

print("The 1 biblio sound_grav is:")
Audio(note_1biblio_grav, rate=note_fs1biblio_grav)

#plot_signals(note_1biblio_grav, note_fs1biblio_grav)

t_start = 4.99

sample_start = int(t_start * note_fs1biblio_grav)
sample_end = sample_start + len(note_og_laser)

note_1biblio_grav_trimmed= note_1biblio_grav[sample_start:sample_end]

print("The iPhone Laser Sound Trimmed is:")
Audio(note_1biblio_grav_trimmed, rate = note_fs_og)

sf.write('trimmed_1bibliograv_sound.wav', note_1biblio_grav_trimmed, note_fs_og)
#plot_signals(note_1biblio_grav_trimmed,note_fs_og)

NFFT = 44100
FFTvisualize(note_1biblio_grav_trimmed, NFFT, note_fs_og, True)

"""Second enclosure, library room, sound recorder"""

filepath = "/content/drive/Shareddrives/enginyeria acutica (yupii)/Gravacions LAB/Gravadora Bona/2n altaveu (Sala Biblio).wav"
note_2biblio_grav, note_fs2biblio_grav = load_audio(filepath)

print("The sample rate is", note_fs2biblio_grav)

print("The 2 biblio sound_grav is:")
Audio(note_2biblio_grav, rate=note_fs2biblio_grav)

#plot_signals(note_2biblio_grav, note_fs2biblio_grav)

t_start = 4.792

sample_start = int(t_start * note_fs2biblio_grav)
sample_end = sample_start + len(note_og_laser)

note_2biblio_grav_trimmed= note_2biblio_grav[sample_start:sample_end]

print("The 2nd biblio record Sound Trimmed is:")
Audio(note_2biblio_grav_trimmed, rate = note_fs_og)

sf.write('trimmed_2bibliograv_sound.wav', note_2biblio_grav_trimmed, note_fs_og)
#plot_signals(note_2biblio_grav_trimmed,note_fs_og)

"""Third encloser, biblio room, sound recorder"""

filepath = "/content/drive/Shareddrives/enginyeria acutica (yupii)/Gravacions LAB/Gravadora Bona/3r altaveu (Sala Biblio).wav"
note_3biblio_grav, note_fs3biblio_grav = load_audio(filepath)

print("The sample rate is", note_fs3biblio_grav)

print("The 3 biblio sound_grav is:")
Audio(note_3biblio_grav, rate=note_fs3biblio_grav)

#plot_signals(note_3biblio_grav, note_fs3biblio_grav)

t_start = 4.093

sample_start = int(t_start * note_fs3biblio_grav)
sample_end = sample_start + len(note_og_laser)

note_3biblio_grav_trimmed= note_3biblio_grav[sample_start:sample_end]

print("The 3rd biblio record Sound Trimmed is:")
Audio(note_3biblio_grav_trimmed, rate = note_fs3biblio_grav)

sf.write('trimmed_3bibliograv_sound.wav', note_3biblio_grav_trimmed, note_fs_og)
#plot_signals(note_3biblio_grav_trimmed,note_fs_og)

"""Fourth encloser, biblio room, sound recorder"""

filepath = "/content/drive/Shareddrives/enginyeria acutica (yupii)/Gravacions LAB/Gravadora Bona/4t altaveu (Sala Biblio).wav"
note_4biblio_grav, note_fs4biblio_grav = load_audio(filepath)

print("The sample rate is", note_fs4biblio_grav)

print("The 4 biblio sound_grav is:")
Audio(note_4biblio_grav, rate=note_fs4biblio_grav)

#plot_signals(note_4biblio_grav, note_fs4biblio_grav)

t_start = 4.148

sample_start = int(t_start * note_fs4biblio_grav)
sample_end = sample_start + len(note_og_laser)

note_4biblio_grav_trimmed= note_4biblio_grav[sample_start:sample_end]

print("The 4th biblio record Sound Trimmed is:")
Audio(note_4biblio_grav_trimmed, rate = note_fs4biblio_grav)

sf.write('note_4biblio_grav_trimmed.wav', note_4biblio_grav_trimmed, note_fs_og)
#plot_signals(note_4biblio_grav_trimmed,note_fs_og)

"""Fifth encloser, biblio room, sound recorder"""

filepath = "/content/drive/Shareddrives/enginyeria acutica (yupii)/Gravacions LAB/Gravadora Bona/5e altaveu (Sala Biblio).wav"
note_5biblio_grav, note_fs5biblio_grav = load_audio(filepath)

print("The sample rate is", note_fs5biblio_grav)

print("The 5th biblio sound_grav is:")
Audio(note_5biblio_grav, rate=note_fs5biblio_grav)

#plot_signals(note_5biblio_grav, note_fs5biblio_grav)

t_start = 3.831

sample_start = int(t_start * note_fs5biblio_grav)
sample_end = sample_start + len(note_og_laser)

note_5biblio_grav_trimmed= note_5biblio_grav[sample_start:sample_end]

print("The 5th biblio record Sound Trimmed is:")
Audio(note_5biblio_grav_trimmed, rate = note_fs5biblio_grav)

sf.write('note_5biblio_grav_trimmed.wav', note_5biblio_grav_trimmed, note_fs_og)
#plot_signals(note_5biblio_grav_trimmed,note_fs_og)

"""First encloser, biblio room, phone recorder"""

filepath = "/content/drive/Shareddrives/enginyeria acutica (yupii)/Gravacions LAB/Gravadora Mobil/recortats/1r Altaveu (Sala Biblio) - mobil.wav"
pr_biblio_phone, pr_biblio_phone_fs = load_audio(filepath)

print("The sample rate is", pr_biblio_phone_fs)

print("The first enclousure biblio sound with the phone is:")
Audio(pr_biblio_phone, rate=pr_biblio_phone_fs)

#plot_signals(pr_biblio_phone, pr_biblio_phone_fs)

"""First encloser, insonorized room, phone recorder"""

filepath = "/content/drive/Shareddrives/enginyeria acutica (yupii)/Gravacions LAB/Gravadora Mobil/recortats/1r Altaveu (Sala Insonoritzada) - Mobil.wav"
pr_inso_phone, pr_inso_phone_fs = load_audio(filepath)

print("The sample rate is", pr_inso_phone_fs)

print("The first enclousure in the insonorized room recorded with the phone is:")
Audio(pr_inso_phone, rate=pr_inso_phone_fs)

#plot_signals(pr_inso_phone, pr_inso_phone_fs)

NFFT = 48000
FFTvisualize(pr_inso_phone, NFFT, pr_inso_phone_fs, True)

"""Second enclosure, library room, phone recorder"""

filepath = "/content/drive/Shareddrives/enginyeria acutica (yupii)/Gravacions LAB/Gravadora Mobil/recortats/2n Altaveu (Sala Biblio) - Mobil.wav"
sg_biblio_phone, sg_biblio_phone_fs = load_audio(filepath)

print("The sample rate is", sg_biblio_phone_fs)

print("The second enclousure in the library room recorded with the phone is:")
Audio(sg_biblio_phone, rate=sg_biblio_phone_fs)

#plot_signals(sg_biblio_phone, sg_biblio_phone_fs)

"""Second enclosure, insonorized room, phone recorder"""

filepath = "/content/drive/Shareddrives/enginyeria acutica (yupii)/Gravacions LAB/Gravadora Mobil/recortats/2n Altaveu (Sala Insonoritzada) - Mobil.wav"
sg_inso_phone, sg_inso_phone_fs = load_audio(filepath)

print("The sample rate is", sg_inso_phone_fs)

print("The second enclousure in the insonorized room recorded with the phone is:")
Audio(sg_inso_phone, rate=sg_inso_phone_fs)

#plot_signals(sg_biblio_phone, sg_biblio_phone_fs)

"""Third enclosure, library room, phone recorder"""

filepath = "/content/drive/Shareddrives/enginyeria acutica (yupii)/Gravacions LAB/Gravadora Mobil/recortats/3r Altaveu (Sala Biblio) - Mobil.wav"
tr_biblio_phone, tr_biblio_phone_fs = load_audio(filepath)

print("The sample rate is", tr_biblio_phone_fs)

print("The third enclousure in the library room recorded with the phone is:")
Audio(tr_biblio_phone, rate=tr_biblio_phone_fs)

#plot_signals(sg_biblio_phone, sg_biblio_phone_fs)

"""Third enclosure, insonorized room, phone recorder"""

filepath = "/content/drive/Shareddrives/enginyeria acutica (yupii)/Gravacions LAB/Gravadora Mobil/recortats/3r Altaveu (Sala Insonoritzada) - Mobil.wav"
tr_inso_phone, tr_inso_phone_fs = load_audio(filepath)

print("The sample rate is", tr_inso_phone_fs)

print("The third enclousure in the insonorized room recorded with the phone is:")
Audio(tr_inso_phone, rate=tr_inso_phone_fs)

#plot_signals(sg_biblio_phone, sg_biblio_phone_fs)

"""Fourth enclosure, library room, phone recorder"""

filepath = "/content/drive/Shareddrives/enginyeria acutica (yupii)/Gravacions LAB/Gravadora Mobil/recortats/4t Altaveu (Sala Biblio) - Mobil.wav"
qrt_biblio_phone, qrt_biblio_phone_fs = load_audio(filepath)

print("The sample rate is", qrt_biblio_phone_fs)

print("The fourth enclousure in the library room recorded with the phone is:")
Audio(qrt_biblio_phone, rate=qrt_biblio_phone_fs)

#plot_signals(qrt_biblio_phone, qrt_biblio_phone_fs)

"""Fourth enclosure, insonorized room, phone recorder"""

filepath = "/content/drive/Shareddrives/enginyeria acutica (yupii)/Gravacions LAB/Gravadora Mobil/recortats/4t Altaveu (Sala Insonoritzada) - Mobil.wav"
qrt_inso_phone, qrt_inso_phone_fs = load_audio(filepath)

print("The sample rate is", qrt_inso_phone_fs)

print("The fourth enclousure in the insonorized room recorded with the phone is:")
Audio(qrt_inso_phone, rate=qrt_inso_phone_fs)

#plot_signals(qrt_inso_phone, qrt_inso_phone_fs)

"""Fifth enclosure, library room, phone recorder"""

filepath = "/content/drive/Shareddrives/enginyeria acutica (yupii)/Gravacions LAB/Gravadora Mobil/recortats/5e Altaveu (Sala Biblio) - Mobil.wav"
cinq_biblio_phone, cinq_biblio_phone_fs = load_audio(filepath)

print("The sample rate is", cinq_biblio_phone_fs)

print("The fifth enclousure in the library room recorded with the phone is:")
Audio(cinq_biblio_phone, rate=cinq_biblio_phone_fs)

#plot_signals(cinq_biblio_phone, cinq_biblio_phone_fs)

"""Fifth enclosure, insonorized room, phone recorder"""

filepath = "/content/drive/Shareddrives/enginyeria acutica (yupii)/Gravacions LAB/Gravadora Mobil/recortats/5e Altaveu (Sala Insonoritzada) - Mobil.wav"
cinq_inso_phone, cinq_inso_phone_fs = load_audio(filepath)

print("The sample rate is", cinq_inso_phone_fs)

print("The fifth enclousure in the insonorized room recorded with the phone is:")
Audio(cinq_inso_phone, rate=cinq_inso_phone_fs)

#plot_signals(cinq_inso_phone, cinq_inso_phone)

"""### Spectrums ploted

##### Spectrums of all enclosures in Biblio Room (Phone recording):
"""

signals = [pr_biblio_phone, sg_biblio_phone, tr_biblio_phone, qrt_biblio_phone, cinq_biblio_phone]

fs_list = [pr_biblio_phone_fs, sg_biblio_phone_fs, tr_biblio_phone_fs, qrt_biblio_phone_fs, cinq_biblio_phone_fs]

labels = ['1st enclosure', '2nd enclosure', '3rd enclosure', '4th enclosure', '5th enclosure']

FFTvisualize_multi(signals, NFFT, fs_list, labels, "Spectrum of the 5 enclosures in the Library Room (Phone Recorder)",True)

"""##### Spectrums of all enclosures in Biblio Room (Good recorder):"""

note_1biblio_grav, note_fs1biblio_grav

signals = [note_1biblio_grav, note_2biblio_grav, note_3biblio_grav, note_4biblio_grav, note_5biblio_grav]

fs_list = [note_fs1biblio_grav, note_fs2biblio_grav, note_fs3biblio_grav, note_fs3biblio_grav, note_fs4biblio_grav, note_fs5biblio_grav]

labels = ['1st enclosure', '2nd enclosure', '3rd enclosure', '4th enclosure', '5th enclosure']

FFTvisualize_multi(signals, NFFT, fs_list, labels, "Spectrum of the 5 enclosures in the Library Room (Good Recorder)",True)

"""##### Spectrums of all enclosures in SoundProof Room (Phone Recorder):"""

signals = [pr_inso_phone, sg_inso_phone, tr_inso_phone, qrt_inso_phone, cinq_inso_phone]

fs_list = [pr_inso_phone_fs, sg_inso_phone_fs, tr_inso_phone_fs, qrt_inso_phone_fs, cinq_inso_phone_fs]

labels = ['1st enclosure', '2nd enclosure', '3rd enclosure', '4th enclosure', '5th enclosure']

FFTvisualize_multi(signals, NFFT, fs_list, labels, "Spectrum of the 5 enclosures in the Soundproof Room (Phone Recorder)", True)

"""##### Spectrums of all enclosures in SoundProof Room (Good Recorder):"""

signals = [pr_inso_grav_trimmed, sg_inso_grav_trimmed, tr_inso_grav_trimmed, qrt_inso_grav_trimmed, cinq_inso_grav_trimmed]

fs_list = [pr_inso_grav_fs, sg_inso_grav_fs, tr_inso_grav_fs, qrt_inso_grav_fs, cinq_inso_grav_fs]

labels = ['1st enclosure', '2nd enclosure', '3rd enclosure', '4th enclosure', '5th enclosure']

FFTvisualize_multi(signals, NFFT, fs_list, labels, "Spectrum of the 5 enclosures in the Soundproof Room (Good Recorder)", True)

"""# ***Transfer functions***

### ***Comparing rooms***
"""

NFFT = 44100
Y_f = np.abs(np.fft.fft(note_og_laser, n=NFFT))

"""Transfer function insonorized room"""

PR_INSO_GRAV = np.abs(np.fft.fft(pr_inso_grav_trimmed, n=NFFT))

H_f_insonorized = Y_f / PR_INSO_GRAV
H_f_insonorized = H_f_insonorized / np.max(np.abs(H_f_insonorized))


# # Keep the same length as the original signal
H_f_insonorized = H_f_insonorized[:note_fs_og]

# Plot the H_f magnitude
FFTvisualize(H_f_insonorized, NFFT, note_fs_og)

"""Transfer function library room"""

NOTE_1BIBLIO_GRAV = np.abs(np.fft.fft(note_1biblio_grav_trimmed, n=NFFT))

H_f_library = Y_f / NOTE_1BIBLIO_GRAV

# Plot the H_f magnitude
FFTvisualize(H_f_library, NFFT, note_fs_og)

"""### ***Comparing enclosures***

Transfer function second enclosure
"""

SG_INSO_GRAV = np.abs(np.fft.fft(sg_inso_grav_trimmed, n=NFFT))

H_f_second = PR_INSO_GRAV / SG_INSO_GRAV

# Plot the H_f magnitude
FFTvisualize(H_f_second, NFFT, note_fs_og)

"""Transfer function third enclosure"""

TR_INSO_GRAV = np.abs(np.fft.fft(tr_inso_grav_trimmed, n=NFFT))

H_f_third = PR_INSO_GRAV / TR_INSO_GRAV

# Plot the H_f magnitude
FFTvisualize(H_f_third, NFFT, note_fs_og)

"""Transfer function fourth enclosure"""

QRT_INSO_GRAV = np.abs(np.fft.fft(qrt_inso_grav_trimmed, n=NFFT))

H_f_fourth = PR_INSO_GRAV / QRT_INSO_GRAV

# Plot the H_f magnitude
FFTvisualize(H_f_fourth, NFFT, note_fs_og)

"""Transfer function fifth enclosure"""

CINQ_INSO_GRAV = np.abs(np.fft.fft(cinq_inso_grav_trimmed, n=NFFT))

H_f_fifth = PR_INSO_GRAV / CINQ_INSO_GRAV

# Plot the H_f magnitude
FFTvisualize(H_f_fifth, NFFT, note_fs_og)

"""All 5 spectrums for the Transer Function"""

signals = [H_f_insonorized, H_f_second, H_f_third, H_f_fourth, H_f_fifth]

fs_list = [note_fs_og, note_fs_og, note_fs_og, note_fs_og, note_fs_og,]

labels = ['1st enclosure', '2nd enclosure', '3rd enclosure', '4th enclosure', '5th enclosure']

FFTvisualize_multi(signals, NFFT, fs_list, labels, "Spectrum of Transfer Function of the 5 enclosures in the Sound Room (Good Recorder)")

"""### ***Comparing quality sound***

Spectrum of the first enclosure in the insonorized room recorded with the phone
"""

FFTvisualize2(pr_inso_phone, NFFT, note_fs_og, True)

FFTvisualize2(pr_inso_grav_trimmed, NFFT, note_fs_og, True)

pr_inso_phone_fs = 44100
PR_INSO_PHONE = np.abs(np.fft.fft(pr_inso_phone, n=NFFT))

H_f = PR_INSO_GRAV / PR_INSO_PHONE

# Compute the impulse response h(t) using the inverse Fourier Transform
h_t_1 = np.fft.ifft(H_f)

# Normalize the filtered output to prevent clipping
h_t_1 = h_t_1 / np.max(np.abs(h_t_1))

# We short the impulse response to avoid duplication problems
h_t = h_t_1[:40000]

# Apply the computed impulse response as a filter to the dry sound x(t) using convolution (np.convolve)
filtered_output_1 = np.convolve(pr_inso_phone, h_t)

# Normalize the filtered output to prevent clipping
filtered_output_1 = filtered_output_1 / np.max(np.abs(filtered_output_1))

# Keep the same length as the original signal
filtered_output_1 = filtered_output_1[:len(pr_inso_phone)]


Audio(filtered_output_1.real, rate = pr_inso_phone_fs)

sf.write("filtered_output.wav", filtered_output_1.real, samplerate = pr_inso_phone_fs)

"""Original Impulse Response Plot:"""

plt.plot(h_t_1)
plt.title("IR not shortened")

"""Shorted Impulse Response Plot (without duplication interferience):"""

plt.plot(h_t)
plt.title("IR shortened")

plt.plot(filtered_output_1)
plt.title("Plot Filtered Output")

"""### ***Interferences Analysis***

##### Recordings Trimmed
"""

filepath = "/content/drive/Shareddrives/enginyeria acutica (yupii)/Gravacions LAB/interferences/wav/60degrees.wav"
note_60degrees, fs_60degrees = load_audio(filepath)

print("The 60 degrees audio is:")
Audio(note_60degrees, rate = fs_60degrees)

#plot_signals(note_60degrees, fs_60degrees)

t_start = 1.77

sample_start = int(t_start * fs_60degrees)
sample_end = sample_start + int(6.5 * fs_60degrees)

trimmed_60degrees = note_60degrees[sample_start:sample_end]


print("The 60 degrees audio trimmed is:")
Audio(trimmed_60degrees, rate = fs_60degrees)

sf.write('trimmed_60degrees.wav', trimmed_60degrees, fs_60degrees)
#plot_signals(trimmed_60degrees, fs_60degrees)

filepath = "/content/drive/Shareddrives/enginyeria acutica (yupii)/Gravacions LAB/interferences/wav/90degrees.wav"
note_90degrees, fs_90degrees = load_audio(filepath)

print("The 90 degrees audio is:")
Audio(note_90degrees, rate = fs_90degrees)

#plot_signals(note_90degrees, fs_90degrees)

t_start = 3.34

sample_start = int(t_start * fs_90degrees)
sample_end = sample_start + int(6.5 * fs_90degrees)

trimmed_90degrees = note_90degrees[sample_start:sample_end]


print("The 90 degrees audio trimmed is:")
Audio(trimmed_90degrees, rate = fs_90degrees)

sf.write('trimmed_90degrees.wav', trimmed_90degrees, fs_90degrees)
#plot_signals(trimmed_90degrees, fs_90degrees)

filepath = "/content/drive/Shareddrives/enginyeria acutica (yupii)/Gravacions LAB/interferences/wav/moving.wav"
note_moving, fs_moving = load_audio(filepath)

print("The moving audio is:")
Audio(note_moving, rate = fs_moving)

#plot_signals(note_moving, fs_moving)

t_start = 1.12

sample_start = int(t_start * fs_moving)
sample_end = sample_start + int(6.5 * fs_moving)

trimmed_moving = note_moving[sample_start:sample_end]


print("The moving audio trimmed is:")
Audio(trimmed_moving, rate = fs_moving)

sf.write('trimmed_moving.wav', trimmed_moving, fs_moving)
#plot_signals(trimmed_moving, fs_moving)

"""##### Signal Plots"""

plot_signals([trimmed_90degrees, trimmed_60degrees], fs_60degrees, name = ["90º recording", "60º recording"])

plot_signals(trimmed_moving, fs_moving, name = "Moving recording")

"""##### Spectrograms"""

ff_60, tt_60, specref_60 = signal.spectrogram(trimmed_60degrees, fs_60degrees, nperseg=1024)

plt.figure(figsize=(12,10))
plot_spectrogram(ff_60, tt_60, specref_60)
plt.title("Spectrogram - 60 Degrees")
plt.xlabel('Time (s)')
plt.ylabel('Frequency (Hz)')
plt.ylim(0, 15000)
plt.show()

ff_90, tt_90, specref_90 = signal.spectrogram(trimmed_90degrees, fs_90degrees, nperseg=1024)

plt.figure(figsize=(12,10))
plot_spectrogram(ff_90, tt_90, specref_90)
plt.title("Spectrogram - 90 Degrees")
plt.xlabel('Time (s)')
plt.ylabel('Frequency (Hz)')
plt.ylim(0, 15000)
plt.show()

ff_moving, tt_moving, specref_moving = signal.spectrogram(trimmed_moving, fs_moving, nperseg=1024)

plt.figure(figsize=(12,10))
plot_spectrogram(ff_moving, tt_moving, specref_moving)
plt.title("Spectrogram - Moving")
plt.xlabel('Time (s)')
plt.ylabel('Frequency (Hz)')
plt.ylim(0, 15000)
plt.show()