from app.robot.toutiao_article import ToutiaoArticleRobot
from app.account import toutiao_account

robot = ToutiaoArticleRobot({
    "source": {
        "platform": "sohu",
        "category": "history"
    },
    "account": toutiao_account.history_15387579110,
    "profile_dir": r"C:\Users\admin\AppData\Local\Google\Chrome\User Data\Profile 2"
})

robot.run()
