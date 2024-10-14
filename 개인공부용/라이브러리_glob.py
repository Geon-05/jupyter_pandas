from glob import glob
import os

now = os.getcwd()
print(now,'------------------------')

files = glob('./개인공부용/data/*.csv')

print(files)