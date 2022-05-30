from vn_telex.utils.TelexRule import TelexRule

VOWELS = {
    'a': ['á', 'à', 'ả', 'ã', 'ạ'],
    'e': ['é', 'è', 'ẻ', 'ẽ', 'ẹ'],
    'i': ['i', 'í', 'ỉ', 'ĩ', 'ị'],
    'y': ['ý', 'ỳ', 'ỷ', 'ỹ', 'ỵ'],
    'o': ['ó', 'ò', 'ỏ', 'õ', 'ọ'],
    'u': ['ú', 'ù', 'ủ', 'ũ', 'ụ'],
    'ư': ['ứ', 'ừ', 'ử', 'ữ', 'ự'],
}

CONSONANTS = {
    'q': ['ú', 'ù', 'ủ', 'ũ', 'ụ', 'u'],
    'g': ['í', 'ì', 'ỉ', 'ĩ', 'ị', 'i'],
}


def generate():
    rules = []
    for consonant_init in CONSONANTS.keys():
        for c_index in range(len(CONSONANTS[consonant_init]) - 1):
            base = consonant_init + CONSONANTS[consonant_init][c_index]
            for vowel in VOWELS.keys():
                if vowel != CONSONANTS[consonant_init][-1]:
                    modifier = vowel
                    result = consonant_init + CONSONANTS[consonant_init][-1] + VOWELS[vowel][c_index]
                    rules.append(TelexRule(base, modifier, result))
    return rules


if __name__ == '__main__':
    all_rules = generate()
    for i in range(len(all_rules)):
        print(f'{i}. {all_rules[i].base} + {all_rules[i].modifier} = {all_rules[i].result}')
