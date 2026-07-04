import re
import string

def preprocess_text(text:str):

    # turn to lowercase
    text = text.lower()

    # remove html tags
    text = re.sub(r"<.*?>", " ", text)

    # remove punctuation
    text = text.translate(
        str.maketrans("", "", string.punctuation)
    )

    # remove digits
    text = re.sub(r"\d+", "", text)

    # remove spaces
    text = re.sub(r"\s+"," ", text)
    
    return text.strip()
