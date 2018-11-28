import difflib
from app.config.default import TITLE_SIMILARITY_SWITCH, TITLE_SIMILARITY_THRESHOLD
from app.extend.helper import titleSimilarityLog


def titleCompare(title, target_title):
    res = difflib.SequenceMatcher(None, title, target_title).quick_ratio()

    try:
        pass
        # titleSimilarityLog(title, target_title, res)
    finally:
        return (res < TITLE_SIMILARITY_THRESHOLD) if TITLE_SIMILARITY_SWITCH else True