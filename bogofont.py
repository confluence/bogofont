import fontforge
import string
import argparse
import random

parser = argparse.ArgumentParser(prog='bogofont', description='A fontforge script for creating an obfuscating font')
parser.add_argument('input_font', help="Path to the input font.")
parser.add_argument('output_font', help="Path to the output font.")
parser.add_argument('-l', '--letters', type=int, help="The number of letters to use. Default 13; min 1; max 26.", default=13)
parser.add_argument('-d', '--digits', type=int, help="The number of digits to use. Default 5; min 1; max 10.", default=5)
args = parser.parse_args()

num_chars = min(max(args.letters, 1), 26)
num_digits = min(max(args.letters, 1), 10)

lower_chars = (random.sample(string.ascii_lowercase, num_chars) * (26 // num_chars + 1))[:26]
upper_chars = [c.upper() for c in lower_chars]
digits = (random.sample(string.digits, num_digits) * (10 // num_digits + 1))[:10]

random.shuffle(lower_chars)
random.shuffle(upper_chars)
random.shuffle(digits)

mapping = {}
mapping.update({k: v for k, v in zip(string.ascii_lowercase, lower_chars)})
mapping.update({k: v for k, v in zip(string.ascii_uppercase, upper_chars)})
mapping.update({k: v for k, v in zip(string.digits, digits)})

font = fontforge.open(args.input_font)

font.selection.all()
font.copy()

copy = fontforge.font()
copy.selection.all()
copy.paste()

for char in (*string.ascii_lowercase, *string.ascii_uppercase, *string.digits):
    copy.selection.select(mapping[char])
    copy.copy()
    font.selection.select(char)
    font.paste()

font.familyname = f"{font.familyname} Bogo"
font.fullname =  f"{font.fullname} Bogo"
font.fontname =  f"{font.fontname}Bogo"
font.generate(args.output_font)
font.close()
