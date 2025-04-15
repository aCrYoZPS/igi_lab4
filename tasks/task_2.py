import re
import string
import zipfile
from core.file_io import read_txt


def task_2():
    text = read_txt()
    sentences_regex = "[.?!]"
    dot_sentences_regex = "[.]"
    excl_sentences_regex = "[!]"
    quest_sentences_regex = "[?]"
    word_regex = r"\w+"
    sentences_content_regex = r"\s*([^!.?\n\r]+)"
    smileys_regex = r"[;:]{1}-*([\(\)\[\]])\1*"
    phones_regex = r"\+37529[0-9]{7}"
    target_words_regex = r"\b\w[][aoiueyAOIUEY][^aoiueyAOIUEY]\w*\b"
    whitespace_bound_words_regex = r" *\w+ *"
    word_combination_regex = r"([^,\s]+(?:\s[^,\s]+)+),?"
    result: str = ""

    result += f"Total sentences: {len(re.findall(sentences_regex, text))}\n"
    result += f"Dot sentences: {len(re.findall(dot_sentences_regex, text))}\n"
    result += f"Excl sentences: {len(re.findall(excl_sentences_regex, text))}\n"
    result += f"Quest sentences: {len(re.findall(quest_sentences_regex, text))}\n"

    sentences = re.findall(sentences_content_regex, text)
    mean_word_len = 0
    words = re.findall(word_regex, text)

    for word in words:
        mean_word_len += len(word)

    mean_sentence_len = mean_word_len / len(sentences)
    result += f"Mean sentence len: {mean_sentence_len}\n"

    mean_word_len /= len(words)
    result += f"Mean word len: {mean_word_len}\n"

    smileys = re.finditer(smileys_regex, text, re.MULTILINE)
    smileys_number = 0
    for smiley in smileys:
        # print(smiley.group())
        smileys_number += 1

    result += f"Number of smileys: {smileys_number}\n"

    result += "Phones starting with 29:\n"
    for phone in re.findall(phones_regex, text):
        result += f"{phone}\n"

    input_str = input("Input a string to be analyzed:\n")
    result += f"\nAnalyzed string: {input_str}\n"

    result += "Words with second vowel and third consonant:\n"
    for word in re.findall(target_words_regex, input_str):
        result += f"{word}\n"

    whitespace_bound_words = re.findall(whitespace_bound_words_regex, input_str)
    result += f"Whitespace bound words: {len(whitespace_bound_words)}\n"

    result += "Letter counts:\n"
    for ch in string.ascii_letters:
        number = len(re.findall(ch, input_str))
        if number > 0:
            result += (f"{ch}: {number}\n")

    word_combinations = re.findall(word_combination_regex, input_str)
    word_combinations.sort()
    result += "Sorted word combinations:\n"
    for word_combination in word_combinations:
        result += f"{word_combination}\n"

    with open("result.txt", "w") as file:
        file.write(result)

    zip_file = zipfile.ZipFile("archive.zip", "w")
    zip_file.write("result.txt")
    print(zip_file.infolist())
    zip_file.close()
