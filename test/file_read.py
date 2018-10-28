import os

with open('%s/app/log/sohu_title.txt' % os.getcwd(), 'r') as f:
               try:
                f.readlines().index('1969年四位老帅密议国家安全')
               except ValueError:
                print(123)