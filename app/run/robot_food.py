from app.robot.toutiao_article import ToutiaoArticleRobot
from app.account import toutiao_account

robot = ToutiaoArticleRobot({
    "source": {
        "platform": "sohu",
        "category": "food"
    },
    "account": toutiao_account.food_18707496278,
    "profile_dir": r"C:\Users\admin\AppData\Roaming\Mozilla\Firefox\Profiles\b3282adm.robot2",
})
