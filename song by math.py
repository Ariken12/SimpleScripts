import numpy as np
import math
import pyaudio as pa

step_of_arg = 10
begin_of_function = 0
end_of_function = 1000
# частота дискретизации
SAMPLE_RATE = 44100
# 16-ти битный звук (2 ** 16 -- максимальное значение для int16)
S_16BIT = 2 ** 16
# период звука = 1/частота
DURATION = 1

def function_math(x):
    #a = math.sin(x)*500+500
    a = int(500 * ((math.e ** (math.sin(3 * x / 100))) - (math.e ** (math.sin(x/100)))) / (x/100) + 800) if x != 0 else 10000
    return a


def generate_sample(freq, duration, volume):
    # амплитуда
    amplitude = np.round(S_16BIT * volume)
    # длительность генерируемого звука в сэмплах
    total_samples = np.round(SAMPLE_RATE * duration)
    # частоте дискретизации (пересчитанная)
    w = 2.0 * np.pi * freq / SAMPLE_RATE
    # массив сэмплов
    k = np.arange(0, total_samples)
    # массив значений функции (с округлением)
    return np.round(amplitude * np.sin(k * w))

p = pa.PyAudio()

stream = p.open(format=p.get_format_from_width(width=2),
                    channels=2, rate=SAMPLE_RATE, output=True)

for i in range(begin_of_function, end_of_function, step_of_arg):
    freq = function_math(i)
    stream.write(np.array(generate_sample(freq, DURATION, 0.05), dtype=np.int16))
    print(i, freq)

stream.stop_stream()
stream.close()
