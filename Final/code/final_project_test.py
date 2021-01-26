'''
 
Christina-Theano Kylafi
M901 - Final Project
LT1200012

'''
from collections import Counter
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
print(f"Total words in corpus: {len(freqGen.total_frequencies.keys())}")
# print(freqGen.file_frequencies)
# print(freqGen.total_frequencies)

tokens_sorted = sorted(freqGen.total_frequencies, key=freqGen.total_frequencies.get, reverse=True)
freqs_sorted = sorted(freqGen.total_frequencies.values(), reverse=True)
count_freq_distr = Counter(freqs_sorted)
count_freq_distr_list = count_freq_distr.values()
temp = 1

for i in count_freq_distr.values():
    if temp==len(count_freq_distr.values()):
        print(f"Lower frequency count: {i}")
    
    temp+=1
# for i in count_freq_distr.keys():
#     print(f"{i}: {count_freq_distr[i]}")

counter=1
for tok,freq in zip(tokens_sorted, freqs_sorted ):
    print(f"{counter}. {tok}: {freq}")
    counter+=1


# f_out = open("./file_frequencies.txt","wb+")
# f_out.write(freqGen.file_frequencies)

