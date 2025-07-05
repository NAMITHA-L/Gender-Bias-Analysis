import re

def clean_and_flatten(nested_lists):
    flat_list = []
    for sublist in nested_lists:
        for word in sublist:
            # Remove punctuation and lowercase
            word = re.sub(r"[^\w\s]", "", word).lower().strip()
            if word:  # Skip empty strings
                flat_list.append(word)
    return flat_list
