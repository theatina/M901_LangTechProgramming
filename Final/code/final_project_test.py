'''
 
Christina-Theano Kylafi
M901 - Final Project
LT1200012

'''

import final_project as fpro

freqGen = fpro.FrequenciesGenerator("../data/test_data_901_final_project/")
freqGen.read_folder()
print(freqGen.calculate_similarity("Chapter8.pdf.txt","Chapter12.pdf.txt"))

# print(freqGen.get_frequency("ενότητα:","Chapter8.pdf.txt"))

# print(freqGen.file_frequencies)
# print(freqGen.total_frequencies)

# f_out = open("./file_frequencies.txt","wb+")
# f_out.write(freqGen.file_frequencies)

