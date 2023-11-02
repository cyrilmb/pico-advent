
def decode(message_file):
    # First initialize an empty dictionary and list
    d = {} 
    s = []

    # This opens the file as variable 'text' and use a loop on each line
    with open(message_file) as text: # Using 'with' will close the file after reading, saving memory
        for line in text:
        (key, val) = line.split() # Each line is split into a key-value pair
        d[int(key)] = val # Then added to the dictionary 'd'

    # Each item in the dictionary is sorted by numercial value and stored in the list 's'
    s = sorted(d.items())

    # This function loops through a list and adds pieces of it to a new list
    def divide(l, n):
        result = [] # New empty list
        start = 0
        while start < len(l): # The function loops for the length of the given list
            result.append(l[start:start + n]) # Adds the sublist with lenght 'n' from list 'l' to the new list
            start += n
            n += 1
        return result

    n = 1
    pyramid = divide(s, n) # Call the divide function using the sorted list to create a new list in pyramid form

    last_words = [sublist[-1] for sublist in pyramid] # Takes the last tuple of each sublist in pyramid and adds to new list

    sentence = ' '.join([sublist[-1] for sublist in last_words]) # Takes the last element of each tuple and joins them into a single string, seperated by a space

    return sentence