'''

M901 - Project 2
Kylafi Christina-Theano
LT1200012

'''

#global variable (frequency dictionary)
token_frequencies = {}

#global variable (dictionary with all the versions(case sensitive) of same tokens)
token_versions = {}

def read_text(input_txt):
    '''
    Reads the input text and creates a token frequency dictionary

    Parameters:     input_txt: input text to split and tokenize to create the frequency dictionary     

    '''
    global token_frequencies

    #Χωρίζουμε το κείμενο με βάση το κενό
    tokens_txt_list = input_txt.split(" ")
    #Σε περίπτωση που το κείμενο που εισήχθη ήταν κενό ή περιείχε μόνο κενά
    tokens_txt_list = [i for i in tokens_txt_list if len(i)>0]

    #Εαν τελικά η λίστα με τα tokens είναι κενή - κείμενο μόνο με κενά, ή κενό κείμενο, τότε επιστρέφεται αρνητική τιμή, ώστε να τυπωθεί το κατάλληλο μήνυμα στο κεντρικό πρόγραμμα, το οποίο καλεί τη συνάρτηση
    if len(tokens_txt_list)==0:
        return -9
    else:
    #Αλλιώς, δημιουργείται set με όλα τα tokens, ώστε να υπολογιστεί η συχνότητά τους και να προστεθούν όλα τα ζευγάρια (token,frequency) στο λεξικό
        tokens_txt_set = set(tokens_txt_list)
        for i in tokens_txt_set:
            token_frequencies[i]=tokens_txt_list.count(i)


        #Initialization of the token versions dictionary described below
        #Δημιουργία λεξικού εκδοχών των tokens - προαιρετική χρήση
        create_token_version_dictionary(input_txt)

        return 9


def get_frequency(token):
    '''
    Finds the frequency of the given token

    Parameters:     token: token of which the frequency is found - if the token is on the text the tokens of which the frequency dictionary was initialized on

    Returns:        error_message(str): in case the dictionary is not yet initialized
                    0(int): if the token is not a key in the dictionary - was not in the text - frequency is 0
                    result(int): frequency of the token if the token is found in the dictionary

    '''
    global token_frequencies
    
    #Εαν το λεξικό δεν έχει αρχικοποιηθεί, επιστρέφεται το μήνυμα λάθους με τύπο str
    if token_frequencies=={}:
        error_message = "The frequency dictionary has not yet been initialized !"
        return error_message

    result = token_frequencies.get(token)

    #Εαν δε βρεθεί η εγγραφή επιστρέφεται η μηδενική συχνότητα του token που ζητήθηκε
    if result == None:
        return 0
    
    #Αλλιώς επιστρέφεται η συχνότητα του token
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
    for k,freq in zip(token_frequencies.keys(),token_frequencies.values()):
        tok_vers_k = token_versions.get(k.lower())
        #Εαν δεν υπάρχει ήδη η εγγραφή του token με τη λίστα των εκδοχών του ως τιμές, προστίθεται
        if tok_vers_k==None and freq>0:
            temp_version_list = [k]
            #όλες οι εκδοχές από το tokenized κείμενο, προστίθενται στη λίστα
            for i in tokenized_txt_set:
                if i.lower() == k.lower():
                    temp_version_list.append(i)
        
            token_versions[k.lower()] = list(set(temp_version_list))


def get_token_versions(token): 
    global token_versions
    
    #Εαν το λεξικό δεν υπάρχει ή είναι άδειο
    if token_versions=={}:
        return -9,[]

    else:
        tok_vers = token_versions.get(token)
        #Εαν δε βρέθηκε εγγραφή του token
        if tok_vers==None:
            return 0,[]
        else:
            return len(tok_vers),tok_vers


if __name__ == "__main__":

    #test case insensitive version
    test_txt = "How lala LalA lala TheAtina what how he she WHAT ThE tHe what WhaT"
    read_text(test_txt)

    #text token versions
    create_token_version_dictionary(test_txt)
    # print(token_versions)

    token = "what"
    freq = get_frequency(token)
    if type(freq) == str:
        print(f"\n{freq}\n")

    elif type(freq) == int and freq>0:
        vers_count, vers_list = get_token_versions(token.lower())
        print(f"\n> Frequency of token \"{token}\" is {freq}\nAll versions of token -> {vers_list}\n")
        
    else:
        print(f"\n> Token \"{token}\" not found !")
        vers_count, vers_list = get_token_versions(token.lower())
        if vers_count!=None and vers_count > 0:
            print(f"Other versions of token \"{token}\" : {vers_list}\n")


    # help(get_frequency) 