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
    Exception to be risen in case of document error along with the proper message each time (eg. not found, lacking the proper extension, etc. )
    
    '''
    pass

class DictError(Exception):
    '''
    Exception to be risen in case of dictionary error (eg. not initialized)
    
    '''
    pass

class PathError(Exception):
    '''
    Exception to be risen in case of path error (eg. inexistent)
    
    '''
    pass


class FrequenciesGenerator:

    def __init__(self,folder_name):
        '''
        Class initialiser

        Parameters:     folder_name: string
                        The path of the dataset folder given by the user when creating an instance of the class
                        
        '''

        # Instance variables: source_folder and the dictionaries file_frequencies and total_frequencies
        self.source_folder = folder_name
        
        # Dictionary initialisation
        self.file_frequencies = {}
        self.total_frequencies = {}


    def tokenize(self, text):
        '''
        Performs text cleaning and splitting into tokens by employing regular expressions

        Parameters:     text: string
                        The text of a file from the given dataset to be tokenized

        Returns:        tokens: list
                        List of tokens after splitting the text using regex

        '''

        # Text cleaning using regular expressions
        text = re.sub(r"\s+"," ",text)      # Multiple whitespaces -> single space
        text = re.sub(r"- ","",text)        # Removes dash+space pattern
        text = re.sub(r"[-]{2,}","-",text)  # Removes multiple sequential dashes (keeps the 1st)
        text = re.sub(r"[_]{2,}","_",text)  # Removes multiple sequential underscores (keeps the 1st)
        # Basic token pattern comprising alphanumberic characters, dashes and underscores
        # The tokens are all in lower case so as to avoid case sensitive duplicates
        tokens = re.findall(r"[\w-]+", text.lower())
        
        # Removing sole occurrences of the two characters below, from the token list
        for char in ["-","_"]:
            if char in tokens:
                tokens.remove(char)


        return tokens


    def generate_frequencies(self, word_list):
        '''
        Creates a word frequency dictionary of the 'word_list' given by the user

        Parameters:     word_list: list
                        The list of words to be used for the creation of the frequency dictionary

        Returns:        freq_dict: dictionary
                        The frequency dictionary of the list of words given above

        '''
        # Initialization of the dictionary
        freq_dict = {}

        # In case the list is empty, an empty dictionary is returned, triggering an exception raise
        if len(word_list)==0:
            return freq_dict
        else:
            # Frequency dictionary creation using the token list from the text splitting
            for i in word_list:
                if i in freq_dict:
                # If the token is already in the dictionary, its frequency is increased by one
                    freq_dict[i] += 1
                else:
                # if the token is not included in the dictionary, it is added for the first time, with an inital frequency (value) of 1 (first occurrence in the list)
                    freq_dict[i] = 1

        return freq_dict


    def read_folder(self):
        '''
        Performs recursive traversing of the 'source_folder' given by the user when creating an instance of the 'FrequenciesGenerator' Class, to get the tokens from each document and the respective frequencies
       
        '''

        # Checks that the source_folder path exists, else it raises a PathError with the proper error message
        if not os.path.exists(self.source_folder):
            raise PathError(f"\n\nERROR: Folder '{self.source_folder} does not exist!'\n")

        # Recursive traversing of the given source_folder path
        for sub_d_path, d_names, files_d in os.walk(self.source_folder):
            # For each .txt file, tokenization is performed and then the dictionary of that specific file is created
            for f_name in files_d:
                # Possible exception(due to wrong file extension) handling with try/except
                try:
                    # Ensuring that only the .txt files are used, else a DocError exception with the proper error message (as exception argument) is raised
                    if not f_name.endswith('.txt'):
                        raise DocError(f"\n\nERROR: '{f_name}' is not a .txt file !\n")
            
                    # Each .txt file from the given dataset folder path (source_folder) is opened and tokenized
                    f_path = os.path.join(sub_d_path, f_name)
                    file_text_reader = open(f_path,"r")
                    file_text = file_text_reader.read()
                    
                    text_tokens = self.tokenize(file_text)
                    # In case of an error related to the file frequency dictionary, an exception is raised, along with a proper error message
                    if len(text_tokens)==0:
                        raise DocError(f"\nERROR: Something went wrong with the text tokenization of file '{f_name}' (file could be empty) !\n")
                    
                    file_text_reader.close()
                    
                    # The text_tokens list of the splitted text file are used to create the file frequency dictionary
                    token_freq = self.generate_frequencies(text_tokens)
                    
                    # In case of an error related to the file frequency dictionary, an exception is raised, along with a proper error message
                    if token_freq=={}:
                        raise DictError("\nERROR: Something went wrong with the dictionary !\n")
                        
                    # Finally, the file frequency dictionary is saved in the dictionary of file dictionaries, under the name of the respective file it represents (name as key) 
                    self.file_frequencies[f_name] = token_freq

                except (DocError,DictError) as dict_doc_error:
                    # Exceptions are handled by the handler, which prints the error message and allows the programme to continue running instead of exiting
                    print(f"{dict_doc_error.args[0]}")

                 
        # Traversing the file_frequencies dictionary and the respective file dictionaries in order to created the total_frequencies dictionary of the corpus tokens by merging all the file dictionaries into one (summing the frequencies of identical keys)
        for f_name in self.file_frequencies:
            for token in self.file_frequencies[f_name]:
                # Creation of the total_frequencies dictionary
                if token in self.total_frequencies:
                    # If token is already in the dictionary, the frequencies are added
                    self.total_frequencies[token]+= self.file_frequencies[f_name][token]
                else:
                    # If the token is not already included in the corpus token dictionary, it is added as a key, with the frequency from the file frequency dictionary being its initial value
                    self.total_frequencies[token]=self.file_frequencies[f_name][token]
                

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
            # Checks if token is included in the corpus
            if frequency==None:
                error_msg = f"\nERROR: Token '{token}' not found in corpus !\n"
        else:
            # If f_name is  given, then the frequency of the token in the particular document 'f_name' is returned

            # Check if file exists (if it is contained in the dictionary keys)
            if f_name not in self.file_frequencies.keys():
                error_msg = f"\nERROR: Filename '{f_name}' does not exist !\n"
            else:
                frequency = self.file_frequencies[f_name].get(token)
                # Checks if token is included in the given file
                if frequency==None:
                    error_msg = f"\nERROR: Token '{token}' not found in document '{f_name}' !\n"

        # If the given token is not found or the given filepath does not exist, a value of zero is returned, after the respective error message is printed
        if frequency == None:
            print(error_msg)
            frequency = 0
            return frequency
        
        # Else (if found in corpus/document), the frequency of the token is returned
        return frequency


    def calculate_similarity(self, file_a, file_b):
        '''
        Calculates the Jaccard similarity between 2 files a,b ( |intersection(a,b)| / |union(a,b)| )

        Parameters:     file_a: string
                        The name of the 1st file to be compared

                        file_b: int
                        The name of the 2nd file to be compared with the 1st, file_a

        Returns:        file_similarity: int
                        The value of the Jaccard similarity (percentage) between the two files, file_a & file_b

        '''
        # initial value of the similatiry is zero
        file_similarity = 0
        
        # Possible exception(due to non-existent file) handling with try/except
        try:
            # Check if given file paths exist
            for f_n in [file_a,file_b]:
                # If not, raise the DocError with a proper error message as an exception argument
                if f_n not in self.file_frequencies.keys():
                    raise DocError(f"\nERROR: Filename '{f_n}' does not exist !\n")
            
            # The token sets of the two files
            file_a_tokens_set = set(self.file_frequencies[file_a].keys())
            file_b_tokens_set = set(self.file_frequencies[file_b].keys())

            # The cardinality of the intersection and the union of the two token sets calculated above
            common_tokens = len(file_a_tokens_set.intersection(file_b_tokens_set))
            total_tokens = len(file_a_tokens_set.union(file_b_tokens_set))
            
            # Jaccard similarity formula ( percentage )
            file_similarity = (common_tokens/(total_tokens))*100.0

        except DocError as d_error:
            # If DocError exception has been raised in the try clause above, then the specific error message that was defined (exception argument) is printed
            print(d_error.args[0])

        # If everything went well, the similarity percentage between the two files is returned
        return file_similarity



if __name__ == "__main__":
    
    freqGen = FrequenciesGenerator("../data/test_data_901_final_project/")
    freqGen.read_folder()

