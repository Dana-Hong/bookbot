def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        lower_case_string = file_contents.lower()
        word_count = get_word_count(lower_case_string)
        char_dict = get_char_dict(lower_case_string)
        filtered_char_dict = get_filtered_char_dict(char_dict)
        sorted_chars = get_sorted_char_list(filtered_char_dict)

        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{word_count} words found in the document \n")

        print_report(sorted_chars)

def get_char_dict(contents):
    char_count_dict = {}
    for i in range(0, len(contents)):
        char = contents[i]
        if char in char_count_dict:
            char_count_dict[f"{char}"] += 1
        else:
            char_count_dict[f"{char}"] = 1

    return char_count_dict

def get_filtered_char_dict(char_dict):
    filtered_dict = {}
    for char in char_dict:
        if char.isalpha():
            filtered_dict[char] = char_dict[char]

    return filtered_dict


def get_sorted_char_list(filtered_dict):
    def get_count(list_element):
        return list_element[1]

    sorted_list = []
    for char in filtered_dict:
        sorted_list.append((char, filtered_dict[char]))
    sorted_list = sorted(sorted_list, reverse=True, key=get_count)

    # desc_list = list(filtered_dict.values()).sort(reverse=True)
    # result = {i: filtered_dict[i] for i in desc_list}
    return sorted_list

def get_word_count(doc):
    return len(doc.split())

def print_report(char_list):
    for item in char_list:
        char = item[0]
        count = item[1]
        print(f"The '{char}' character was found {count} times")

main()
