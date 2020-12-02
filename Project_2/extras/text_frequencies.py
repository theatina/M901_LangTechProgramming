'''

Kylafi Christina-Theano

'''
import exercise2 as ex2
#global variable (frequency dictionary)
token_frequencies = {}
clean_dict = {}

#global variable (dictionary with all the versions of same tokens)
token_versions = {}

def read_text(input_txt):
    '''
    Reads the input text and creates a token frequency dictionary

    Parameters:     input_txt: input text to split and tokenize to create the frequency dictionary     

    '''
    global token_frequencies

    tokens_txt_list = input_txt.split(" ")
    tokens_txt_set = set(tokens_txt_list)

    for i in tokens_txt_set:
       token_frequencies[i]=tokens_txt_list.count(i)


def get_frequency(token):
    '''
    Finds the frequency of the given token

    Parameters:     token: token of which the frequency is found - if the token is on the text the tokens of which the frequency dictionary was initialized on

    Returns:        error_message(str): in case the dictionary is not yet initialized
                    0(int): if the token is not a key in the dictionary - was not in the text - frequency is 0
                    result(int): frequency of the token if the token is found in the dictionary

    '''
    global token_frequencies
    
    if token_frequencies=={}:
        error_message = "The frequency dictionary has not yet been initialized !"
        return error_message

    result = token_frequencies.get(token)

    if result == None:
        # print("\nToken \"%s\" not found !\n"%(token))
        return 0
    
    return result

#Δημιούργησα τις case insensitive εκδοχές των συναρτήσεων, σε περίπτωση που χρειαζόμαστε τις συχνότητες των λέξεων χωρίς ενδιαφέρον προς τα κεφαλαία - μικρά γράμματα, συνεπώς τα tokens αποθηκεύονται όλα μικρά, και η αναζήτηση της συχνότητας γίνεται αντίστοιχα με το token αφού περάσει από επεξεργασία που οι χαρακτήρες γίνονται lower case με τη χρήση της string method "lower()" 
#Επίσης μια άλλη υλοποίηση που θα μπορούσε να γίνει, είναι η εύρεση όλων των διαφορετικών εκδοχών της λέξης που αναζητώ, για παράδειγμα εαν γίνει αναζήτηση της λέξης the, να επιστραφούν εαν υπάρχουν όλες οι διαφοροποιήσεις ως προς τα μικρα/κεφαλαία γράμματα
def read_text_case_insensitive(input_txt):
    '''
    Reads the input text and creates a token frequency dictionary (case insensitive version of function "read_text()")

    Parameters:     input_txt: input text to split and tokenize to create the frequency dictionary     

    '''

    global token_frequencies

    tokens_txt_list = input_txt.lower().split(" ")
    tokens_txt_set = set(tokens_txt_list)

    for i in tokens_txt_set:
       token_frequencies[i]=tokens_txt_list.count(i)

def get_frequency_case_insensitive(token):
    '''
    Finds the frequency of the given token (case insensitive version of function "get_frequency()")

    Parameters:     token: token of which the frequency is found - if the token is on the text the tokens of which the frequency dictionary was initialized on

    Returns:        -9: in case the dictionary is not yet initialized
                    None: if the token is not a key in the dictionary - was not in the text
                    frequency of the token: if the token is found in the dictionary

    '''
    global token_frequencies
    
    if token_frequencies=={}:
        error_message = "The frequency dictionary has not yet been initialized !"
        return error_message

    result = token_frequencies.get(token.lower())

    if result == None:
        return 0
    
    return result

def create_token_version_dictionary(text):
    '''
    This function can work along with both case sensitive and case insensitive version of functions "read_text()" and "get_frequency()" and creates a dictionary of all the different versions of each token found in the text.
    The structure of the version dictionary is independent of the version of the frequency dictionary, as the keys of the version dictionary, are the exact keys in lower case 
     
    as those in the frequency dictionary. When using the case sensitive version, the version dictionary consists of pairs of keys and values, corresponding to the actual tokens of the text and their different versions, respectively. When using the case insensitive version, the version dictionary is more "concentrated" and consists of pairs of keys and values corresponding to the unique lower case occurence of each token of the text (key) and a list of the total versions of the token found in it (value).

    '''
    global token_versions
    global token_frequencies
    
    tokenized_txt_set = set(text.split(" "))
    # print(token_frequencies)
    for k,freq in zip(token_frequencies.keys(),token_frequencies.values()):
        # print(k,freq)
        if freq > 0:
            temp_version_list = [k]
            for i in tokenized_txt_set:
                if i.lower() == k.lower():
                    temp_version_list.append(i)
            
            token_versions[k.lower()] = list(set(temp_version_list))

def clean_dictionary(text): 

    global clean_dict

    tokens_txt_list = text.split(" ")
    tokens_txt_unique_list = list(set(text.split(" ")))

    counter = 0
    for i in tokens_txt_unique_list:
        isalnum = i.isalnum()
        if isalnum==False and i!="-":
            # print(i)
            new_str = "".join([ char for char in i if char.isalnum() ])
            tokens_txt_unique_list[counter] = new_str
            # print(new_str)
            # print(tokens_txt_list[counter])
        counter+=1

    tokens_txt_set = set(tokens_txt_unique_list)
    # print(len(tokens_txt_list))

    for i in tokens_txt_set:
       clean_dict[i]=tokens_txt_list.count(i)

    return 9 

def text_cleaning_replace(text): 
    for i in text:
        isalnum = i.isalnum()
        if isalnum==False and i not in ["-",".",",",":"]:
            text = text.replace(i," ")

    sentences = text.split(".")
    counter = 1
    for i in sentences:
        print(f"{counter}. {i}.")
        counter+=1

    

if __name__ == "__main__":

    text_cleaning_replace(ex2.text)
    exit()

    read_text(ex2.text)
    clean_dictionary(ex2.text)
    print(len(clean_dict), len(token_frequencies))
    print(clean_dict['the'])

    sort_clean_dict = [(key,value) for (key,value) in sorted(clean_dict.items(), key=lambda x: x[1], reverse=True)]

    sort_tok_freqs = [(key,value) for (key,value) in sorted(token_frequencies.items(), key=lambda x: x[1], reverse=True)]

    n=9
    print(f"\n{n} Most Frequent tokens:\nToken ( Frequency )\n")
    count = 1
    for i,j in zip(sort_tok_freqs[:n],sort_clean_dict[:n]):
        print(f"{count}. {i[0]} ( {i[1]} ) -- {j[0]} ( {j[1]} ) \n")
        count+=1


    exit()




    #test case insensitive version
    test_txt = "How lala LalA lala TheAtina what how he she WHAT ThE tHe what WhaT"
    # read_text(test_txt)
    # print(token_frequencies)

    #text token versions
    # create_token_version_dictionary(test_txt)
    # print(token_versions)

    token = 'hOw'
    freq = get_frequency(token)
    if type(freq) == str:
        print("\n%s\n"%(freq))

    elif type(freq) == int and freq>0:
        print("\n> Frequency of token \"%s\" is %d\nAll versions of token -> %s\n"%(token,freq,token_versions.get(token.lower())))
        
    else:
        print("\n> Token \"%s\" not found !\n"%(token))
        version_count = token_versions.get(token.lower())
        if version_count!=None and len(version_count) > 0:
            print("Other versions of token \"%s\" : %s\n"%(token, version_count))




    # help(get_frequency) 