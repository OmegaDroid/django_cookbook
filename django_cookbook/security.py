import os
import random
import string


def generate_secret_key(dir):
    """
    If 'secret.txt' exists in dir the contents is read and returned as the secret key.
    If 'secret.txt' does not exist in dir a key is generated and stored in 'secret.txt'.

    :param dir: The directory to search for 'secret.txt'

    :return: The generated key
    """
    fileName = os.path.join(dir, 'secret.txt')
    try:
        return open(fileName).read().strip()
    except FileNotFoundError:
        key = ''.join([random.SystemRandom().choice("{}{}{}".format(string.ascii_letters, string.digits, string.punctuation)) for i in range(50)])
        with open(fileName, 'w') as f:
            f.write(key)
        return key