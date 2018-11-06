from app.robot.toutiao_article import ToutiaoArticleRobot
from app.account import toutiao_account

robot = ToutiaoArticleRobot({
    "source": {
        "platform": "sohu",
        "category": "joke"
    },
    "account": toutiao_account.joke_15111461956,
    "profile_dir": r"C:\Users\admin\AppData\Roaming\Mozilla\Firefox\Profiles\ivft84z1.robot3",
})

robot.run()
