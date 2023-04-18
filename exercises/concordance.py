from collections import defaultdict, Counter
from typing import List, Tuple

def tokenize_file(path: str) -> List[str]:
    with open(path, 'r') as file:
        words = [w.lower() for w in file.read().split()]
    return words

def get_most_common(words: List[str]) -> List[Tuple[str, int]]:
    # concordance = defaultdict(int)
    # for word in words:
    #     concordance[word] += 1
    
    # result = list(concordance.items())
    # result.sort(key=lambda t: t[1], reverse=True)
    # return result[:10]

    counter = Counter(words)
    return counter.most_common(10)


print(get_most_common(tokenize_file('holmes.txt')))   