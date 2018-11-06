from app.extend import helper
import os

with open('%s/app/data/title_%s_data.txt' % (os.getcwd(), "history"), 'r', encoding='utf8') as f:
    try:
        f.readlines().index('%s\n' % "叛徒中他是升官最快的，官至中统二把手，晚年说的5字显出心虚123")
        print("Flase")
    except Exception as e:
        print(e)