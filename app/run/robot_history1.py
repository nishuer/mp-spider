from app.robot.toutiao_article import ToutiaoArticleRobot
from app.account import toutiao_account

robot = ToutiaoArticleRobot({
    "source": {
        "platform": "sohu",
        "category": "history"
    },
    "account": toutiao_account.history_15387579110,
    "profile_dir": "/Users/nishu/Library/Application Support/Firefox/Profiles/n0euj0fh.robot1"
})

robot.run()
