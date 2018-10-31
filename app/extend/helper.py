import os
import logging

def titleRead(title, fileName):
    with open('%s/app/data/title_%s_data.txt' % (os.getcwd(), fileName), 'r') as f:
        try:
            f.readlines().index('%s\n' % title)
            return False
        except ValueError:
            return True


def titleWrite(title, fileName):
     with open('%s/app/data/title_%s_data.txt' % (os.getcwd(), fileName), 'a') as f:
        try:
            f.write('%s\n' % title)
        except Exception as e:
            logging.exception(e)