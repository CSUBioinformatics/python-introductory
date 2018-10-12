import sys
import re

PHONE_REGEX = re.compile(r'[0-9]{3}-([0-9]{3}-[0-9]{4})')
ACC_REGEX = re.compile(r'[A-Z]{2,3}_[0-9]{6,7}\.?[0-9]?')
TIME_REGEX = re.compile(r'[0-9]+:[0-9]+:[0-9]+\s[A-Z][SD]T')


def load_csv(file):
    with open(file, 'r') as f:
        data = f.read()
        for line in data.split('\n')[1:]:
            if not line:
                continue
            entries = line.split(',')
            phone_number = PHONE_REGEX.findall(entries[2])
            if phone_number:
                print(phone_number)
            acc = ACC_REGEX.findall(entries[2])
            if acc:
                print(acc)
            time = TIME_REGEX.findall(entries[2])
            if time:
                print(time)




if __name__ == '__main__':
    load_csv(sys.argv[1])
