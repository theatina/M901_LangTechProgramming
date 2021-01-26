'''
 
Christina-Theano Kylafi
M901 - Final Project
LT1200012

'''

import final_project as fpro

freqGen = fpro.FrequenciesGenerator("../data/test_data_901_final_project/")
freqGen.read_folder()

#1 Check function calculate_similarity() 
# file_1 = "Chapter12.pdf.txt"
# file_2 = "Chapter8.pdf.txt"
# print(f"\n> Similarity between files '{file_1} & '{file_2}': {freqGen.calculate_similarity(file_1,file_2):.2f}%\n")


#2 Check function get_frequency() 
# token = "ενότητα"
# file_name = "Chapter8.pdf.txt"
# print(f"\n> Frequency of token '{token}' in '{file_name}': {freqGen.get_frequency(token,file_name)}\n")
# print(f"> Frequency of token '{token}' in the corpus: {freqGen.get_frequency(token)}\n")
