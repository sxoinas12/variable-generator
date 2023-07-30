import sys

from word_processor.generators import Generator
from word_processor.parsers import JavascriptParser
from word_processor.strategies import back_and_forth_strategy


def calculate_names(text: str):
    generator = Generator(text=text, strategy=back_and_forth_strategy, parser=JavascriptParser())

    generator.suggest()

    presentation = generator.present()

    print('\n\n'.join(presentation))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    calculate_names(sys.argv[1])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
