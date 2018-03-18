import sys
from sample.strings_example import StringsExamples

if __name__ == "__main__":
    args = sys.argv[1:]
    print (StringsExamples.count_words(args[0]))