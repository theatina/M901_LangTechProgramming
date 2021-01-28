#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
 
Christina-Theano Kylafi
M901 - Final Project
LT1200012

'''

import final_project as fpro
import argparse

# The programme can be run as " python ./final_project_test --source <dataset_source_folder_path> " or as " python ./final_project_test ", where the default path of the dataset folder is " ../test_data_901_final_project/ "
parser = argparse.ArgumentParser()
parser.add_argument("--source", type=str, default="./test_data_901_final_project/")
args = parser.parse_args()


freqGen = fpro.FrequenciesGenerator(args.source)
freqGen.read_folder()

# 1 Check function calculate_similarity() 
file_1 = "Chapter12.pdf.txt"
file_2 = "Chapterdf8.pdf.txt"
print(f"\n> Similarity between files '{file_1} & '{file_2}': {freqGen.calculate_similarity(file_1,file_2):.2f}%")


# 2 Check function get_frequency() 
token = "και"
file_name = "Chapteasdfr8.pdf.txt"
print(f"> Frequency of token '{token}' in '{file_name}': {freqGen.get_frequency(token,file_name)}\n")
print(f"> Frequency of token '{token}' in the corpus: {freqGen.get_frequency(token)}\n")
