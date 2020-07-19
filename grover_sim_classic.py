import matplotlib.pyplot as plt
import numpy as np
import string
import hashlib
from math import sqrt, pi
from collections import OrderedDict
from statistics import mean
def ShowGraph(amplitude_value, n):
    y_position = np.arange(n)
    plt.bar(y_position, amplitude_value.values(), align='center', color='g')
    plt.xticks(y_position, amplitude_value.keys())
    plt.ylabel('Amplitude Value')
    plt.title('Grovers Algorithm')
    plt.show()

def GetOracle(xvalue):
    return hashlib.sha256(bytes(xvalue, 'utf-8')).hexdigest()

def ExecuteGrover(target, objects, nvalue, rounds):
    y_pos = np.arange(nvalue)
    amplitude = OrderedDict.fromkeys(objects, 1/sqrt(nvalue))
    for i in range(0, rounds, 2):
        for k, v in amplitude.items():
            if GetOracle(k) == target:
                amplitude[k] = v * -1
        average = mean(amplitude.values())
        for k, v in amplitude.items():
            if GetOracle(k) == target:
                amplitude[k] = (2 * average) + abs(v)
                continue
            amplitude[k] = v-(2*(v-average))
    return amplitude

target_algorithm = '3'
objects_grover = ('4', '5', '3', '7','9','11','97')
number = len(objects_grover)
amplitude_grover = OrderedDict.fromkeys(objects_grover, 1/sqrt(number))

amplitude_grover[target_algorithm] = amplitude_grover[target_algorithm] * -1
print(amplitude_grover)
average_grover = mean(amplitude_grover.values())
print("Mean is {}".format(average_grover))
for k, v in amplitude_grover.items():
    if k == target_algorithm:
        amplitude_grover[k] = (2 * average_grover) + abs(v)
        continue
    amplitude_grover[k] = v-(2*(v-average_grover))
print(amplitude_grover)

needle_value = "2d711642b726b04401627ca9fbac32f5c8530fb1903cc4db02258717921a4881"
haystack_value = string.ascii_lowercase
num = len(haystack_value)
num_rounds = int((pi / 4) * sqrt(num))
print("number of rounds are {}".format(num_rounds))
ShowGraph(ExecuteGrover(needle_value, haystack_value, num, num_rounds), num)