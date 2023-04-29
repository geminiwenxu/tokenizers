# test_word.py

import pprint
from datetime import datetime

import morphemes_lib as morphemes


def find(word):
    # nltk.download('wordnet')
    startTime = datetime.now()

    pp = pprint.PrettyPrinter()

    results = morphemes.discover_segments(word)
    # print("segmentation:", type(results), len(results))
    # for item in results.items():
    # print(item)
    # print("---------------------")

    if morphemes.format_results(results, "") == word:
        final_results = morphemes.generate_final_results(results)
        # print(final_results)
        pp.pprint(final_results)
    else:
        result = morphemes.format_results(results, "+"), "failed"

    timeElapsed = datetime.now() - startTime

    # print('script: time elapsed (hh:mm:ss.ms) {}'.format(timeElapsed))
    return final_results


if __name__ == '__main__':
    result = find("deconstructed")
    print(result)