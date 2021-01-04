'''
 
Christina-Theano Kylafi
M901 - Final Project
LT1200012

'''
import os 
import re

class FrequenciesGenerator:

    def __init__(self,folder_name):

        self.source_folder = folder_name
        self.file_frequencies = {}
        self.total_frequencies = {}

    #check regex for better splitting
    def tokenize_text(self, text):
        # tokens = text.split(" ")
        # tokens = re.findall(r"[^\s.,\[\]():]+", text.lower())
        
        text = re.sub(r"-\r","",text)
        text = re.sub(r"-\n","",text)
        tokens = re.findall(r"[\w-]+", text.lower())

        return tokens

    def generate_frequencies(self, word_list):
        freq_dict = {}
        if len(word_list)==0:
            return -9
        else:
            for i in word_list:
                if i in freq_dict:
                    freq_dict[i] += 1
                else:
                    freq_dict[i] = 1

        return freq_dict


    def read_folder(self):
        counter = 0
        for sub_d_path, d_names, files_d in os.walk(self.source_folder):
            for f_name in files_d:
                f_path = os.path.join(sub_d_path, f_name)
                # print(f_path)
                # counter+=1
                file_text = open(f_path,"r").read()
                text_tokens = self.tokenize_text(file_text)
                token_freq = self.generate_frequencies(text_tokens)

                self.file_frequencies[f_name] = token_freq

        for f_name in self.file_frequencies:
            # file_dir = self.file_frequencies[f_name]
            for token in self.file_frequencies[f_name]:
                if token in self.total_frequencies:
                    self.total_frequencies[token]+= self.file_frequencies[f_name][token]
                else:
                    self.total_frequencies[token]=1
                
            # print(f_name)
        # print(counter)

    def get_frequency(self, token, f_name=None):
        '''
        Finds the frequency of the given token

        Parameters:     token: token of which the frequency is found - if the token is on the text the tokens of which the frequency dictionary was initialized on

        Returns:        error_message(str): in case the dictionary is not yet initialized
                        0(int): if the token is not a key in the dictionary - was not in the text - frequency is 0
                        result(int): frequency of the token if the token is found in the dictionary

        '''

        if f_name is None:
            result = self.total_frequencies.get(token)
        else:
            result = self.file_frequencies[f_name].get(token)

        #Εαν δε βρεθεί η εγγραφή επιστρέφεται η μηδενική συχνότητα του token που ζητήθηκε
        if result == None:
            return -9
        
        #Αλλιώς επιστρέφεται η συχνότητα του token
        return result


    def calculate_similarity(self, file_a, file_b):
        file_a_tokens = len(self.file_frequencies[file_a])
        file_b_tokens = len(self.file_frequencies[file_b])
        
        file_a_tokens_set = set(self.file_frequencies[file_a].values())
        file_b_tokens_set = set(self.file_frequencies[file_b].values())
        
        common_tokens = len(file_a_tokens_set.intersection(file_b_tokens_set))

        file_similarity = common_tokens/(file_a_tokens+file_b_tokens)

        return file_similarity



if __name__ == "__main__":
    
    freqGen = FrequenciesGenerator("../data/test_data_901_final_project/")
    freqGen.read_folder()
    # print(freqGen.calculate_similarity("Chapter8.pdf.txt","Chapter12.pdf.txt"))

    # print(freqGen.get_frequency("ενότητα:","Chapter8.pdf.txt"))

    # print(freqGen.file_frequencies)
    # print(freqGen.total_frequencies)

    # f_out = open("./file_frequencies.txt","wb+")
    # f_out.write(freqGen.file_frequencies)


