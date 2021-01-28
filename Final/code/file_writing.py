'''
 
Christina-Theano Kylafi
M901 - Final Project
LT1200012

'''

from collections import Counter
import final_project as fpro

freqGen = fpro.FrequenciesGenerator("./test_data_901_final_project/")
freqGen.read_folder()


'''

Writing details and stats to files

'''

tokens_sorted = sorted(freqGen.total_frequencies, key=freqGen.total_frequencies.get, reverse=True)
freqs_sorted = sorted(freqGen.total_frequencies.values(), reverse=True)
count_freq_distr = Counter(freqs_sorted)
count_freq_distr_list = count_freq_distr.values()
temp = 1

total_tokens = len(freqGen.total_frequencies.keys())
f_corpus_stats = open("./corpus_stats.txt","w")
f_corpus_stats.write(f"Total tokens in corpus: {total_tokens}\n\n")
for i in count_freq_distr.keys():
    if temp==len(count_freq_distr.values()):
        lowest_freq = count_freq_distr[i]
        f_corpus_stats.write(f"Frequency: {i} | count: {lowest_freq}\n")
    elif temp==len(count_freq_distr.values())-1:
        lowest_freq2 = count_freq_distr[i]
        f_corpus_stats.write(f"Frequency: {i} | count: {lowest_freq2}\n")
    elif temp==len(count_freq_distr.values())-2:
        lowest_freq3 = count_freq_distr[i]
        f_corpus_stats.write(f"Frequency: {i} | count: {lowest_freq3}\n")
    
    temp+=1

maxim = -1
f_corpus_stats.write(f"\n\nFile   :   Number of tokens\n")
for i in freqGen.file_frequencies.keys():
    doc_dict_tokens = len(freqGen.file_frequencies[i])
    if doc_dict_tokens>maxim:
        maxim = doc_dict_tokens
    f_corpus_stats.write(f"\n{i}: {doc_dict_tokens}")

f_corpus_stats.close()


f_tot_freq = open("./total_frequencies.txt","w")
f_tot_freq.write(f"Corpus Dictionary\n\n")
counter=1
for tok,freq in zip(tokens_sorted, freqs_sorted ):
    f_tot_freq.write(f"{counter}. {tok}: {freq}\n")
    counter+=1

f_tot_freq.close()

