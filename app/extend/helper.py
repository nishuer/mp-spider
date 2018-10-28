import os
import logging

def titleRead(title):
    with open('%s/app/data/title_data.txt' % os.getcwd(), 'r') as f:
        try:
            f.readlines().index('%s\n' % title)
            return False
        except ValueError:
            return True


def titleWrite(title):
     with open('%s/app/data/title_data.txt' % os.getcwd(), 'w') as f:
        try:
            f.write('%s\n' % title)
        except Exception as e:
            logging.exception(e)