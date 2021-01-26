#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
 
Christina-Theano Kylafi
M901 - Final Project
LT1200012

'''
import os 
import re


class DocError(Exception):
    '''
    Exception to be risen in case of document error along with the proper message each time
    
    '''
    pass


class FrequenciesGenerator:

    def __init__(self,folder_name):
        '''
        Class initialiser

        Parameters:     folder_name: string
                        The path of the dataset folder
                        
        '''

        # Instance variables: source_folder and the dictionaries file_frequencies and total_frequencies
        self.source_folder = folder_name
        
        # Dictionary initialisation
        self.file_frequencies = {}
        self.total_frequencies = {}


    def tokenize_text(self, text):
        '''
        Text tokenizer for text cleaning and splitting into tokens

        Parameters:     text: string
                        The text of a file from the given dataset
                        
        '''

        # Text cleaning using regular expressions
        text = re.sub(r"\s+"," ",text)      # multiple whitespaces -> single space
        text = re.sub(r"- ","",text)        # removes dash+space pattern
        text = re.sub(r"[-]{2,}","-",text)  # removes multiple sequential dashes (keeps the 1st)
        text = re.sub(r"[_]{2,}","_",text)  # removes multiple sequential underscores (keeps the 1st)
        # basic token pattern comprising alphanumberic characters, dashes and underscores
        tokens = re.findall(r"[\w-]+", text.lower())
        
        for char in ["-","_"]:
            if char in tokens:
                tokens.remove(char)

        return tokens

    def generate_frequencies(self, word_list):
        '''
        Finds the frequency of the given token

        Parameters:     token: string
                        token of which the frequency is found - if the token is included in either the document 'f_name' (if given) or the whole corpus

        Returns:        frequency: int
                        frequency of the token if the token is found in the respective dictionary or 0 if the token is not found or the document 'f_name' given, does not exist

        '''

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
        '''
        Finds the frequency of the given token

        Parameters:     token: string
                        token of which the frequency is found - if the token is included in either the document 'f_name' (if given) or the whole corpus

        Returns:        frequency: int
                        frequency of the token if the token is found in the respective dictionary or 0 if the token is not found or the document 'f_name' given, does not exist

        '''

        for sub_d_path, d_names, files_d in os.walk(self.source_folder):
            for f_name in files_d:
                try:
                    # Ensuring that only the .txt files are used
                    if not f_name.endswith('.txt'):
                        raise DocError(f"\nERROR: '{f_name}' is not a .txt file !\n")
                
                except DocError as doc_error:
                    print(f"{doc_error.args[0]}")

                else:
                    f_path = os.path.join(sub_d_path, f_name)
                    file_text_reader = open(f_path,"r")
                    file_text = file_text_reader.read()
                    text_tokens = self.tokenize_text(file_text)
                    file_text_reader.close()
                    token_freq = self.generate_frequencies(text_tokens)
                    self.file_frequencies[f_name] = token_freq
            
            for d in d_names:
                print(d)

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

        Parameters:     token: string
                        token of which the frequency is found - if the token is included in either the document 'f_name' (if given) or the whole corpus

        Returns:        frequency: int
                        frequency of the token if the token is found in the respective dictionary or 0 if the token is not found or the document 'f_name' given, does not exist

        '''

        frequency = None
        
        # If f_name is not given, then the frequency of the token in the corpus is returned
        if f_name is None:
            frequency = self.total_frequencies.get(token)
            if frequency==None:
                error_msg = f"\nERROR: Token '{token}' not found !\n"
        else:
            # If f_name is  given, then the frequency of the token in the particular document 'f_name' is returned

            # Check if file exists (if it is contained in the dictionary keys)
            if f_name not in self.file_frequencies.keys():
                error_msg = f"\nERROR: Filename '{f_name}' does not exist !\n"
            else:
                frequency = self.file_frequencies[f_name].get(token)

        # If the given token is not found, a value of zero is returned
        if frequency == None:
            print(error_msg)
            frequency = 0
            return frequency
        
        # Else, the frequency of the token is returned
        return frequency


    def calculate_similarity(self, file_a, file_b):
        '''
        Finds the frequency of the given token

        Parameters:     token: string
                        token of which the frequency is found - if the token is included in either the document 'f_name' (if given) or the whole corpus

        Returns:        frequency: int
                        frequency of the token if the token is found in the respective dictionary or 0 if the token is not found or the document 'f_name' given, does not exist

        '''

        file_similarity = 0
        
        try:
            for f_n in [file_a,file_b]:
                if f_n not in self.file_frequencies.keys():
                    raise DocError(f"\nERROR: Filename '{f_n}' does not exist !\n")

            # file_a_tokens = len(self.file_frequencies[file_a].keys())
            # file_b_tokens = len(self.file_frequencies[file_b].keys())
            
            file_a_tokens_set = set(self.file_frequencies[file_a].keys())
            file_b_tokens_set = set(self.file_frequencies[file_b].keys())
            common_tokens = len(file_a_tokens_set.intersection(file_b_tokens_set))
            total_tokens = len(file_a_tokens_set.union(file_b_tokens_set))
            
            file_similarity = (common_tokens/(total_tokens))*100.0

        except DocError as d_error:
            print(d_error.args[0])

        return file_similarity



if __name__ == "__main__":
    
    freqGen = FrequenciesGenerator("../data/test_data_901_final_project/")
    freqGen.read_folder()

