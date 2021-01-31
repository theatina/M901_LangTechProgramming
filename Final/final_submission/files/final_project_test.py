#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
 
Christina-Theano Kylafi
M901 - Final Project
LT1200012

'''

import final_project as fpro
import argparse

# The programme can be run as " python ./final_project_test --source <dataset_source_folder_path> " or as " python ./final_project_test ", where the default path of the dataset folder is " ./test_data_901_final_project/ "
parser = argparse.ArgumentParser()
parser.add_argument("--source", type=str, default="./test_data_901_final_project/")
args = parser.parse_args()


# Creates an instance of class FrequenciesGenerator and calls read_folder function
print(f"\nCreating a FrequenciesGenerator instance...\n(source: '{args.source}')\n")
freqGen = fpro.FrequenciesGenerator(args.source)
freqGen.read_folder()


# 1 Checks function ' calculate_similarity() '
file_1 = "Chapter1.pdf.txt"
file_2 = "Chapter10.pdf.txt"
print(f"> Similarity between files '{file_1} & '{file_2}': {freqGen.calculate_similarity(file_1,file_2):.2f}%\n")


# 2 Checks ' function get_frequency() ' 
token = "το"
file_name = "Chapter9.pdf.txt"
print(f"> Frequency of token '{token}' in '{file_name}': {freqGen.get_frequency(token,file_name)}\n")
print(f"> Frequency of token '{token}' in the corpus: {freqGen.get_frequency(token)}\n")
