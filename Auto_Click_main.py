import pyautogui
import time


######################################################


def Click_Infinite(time_click, loc):  # בלי מקבלה
    """
    time_click מחכה לפי
    והזה לוחצה פעם אחת
    פעולה רקורסיבית ואינסופי
    """
    time.sleep(time_click)
    print("Click", loc)
    Except_Location_Click(loc)
    Click_Infinite(time_click, loc)
    # return Click_Infinite(time_click, loc)


def Click_Limits(time_click, loc, limit):  # הם מקבלה
    """
    time_clickמחכה לפי
    והזה לוחצה פעם אחת
    בנוסף יש כמות לחיצות
     פעולה רקורסיבית ונגמרת לפי
    limit
    """
    if limit > 0:
        time.sleep(time_click)
        Except_Location_Click(loc)
        print("Click", loc, ":", end=" ")
        print(limit)
        limit -= 1
        Click_Limits(time_click, loc, limit)
        # return Click_Limits(time_click, loc, limit)
    else:
        print("__-Exit-__")
        return None


def Click(time_click, loc, limit=None):
    """מכלית להן להלכת
    return Click_Infinite: הם אין מגבלת לחיצות אז הפעולה הולכת
    return Click_Limits: יש מגלת לחיצות אז הפעולה הולכת"""
    if limit is None:
        return Click_Infinite(time_click, loc)  # אין מגבלת לחיצות
    else:
        return Click_Limits(time_click, loc, limit)  # יש מגלת לחיצות


def Except_Location_Click(loc):
    """בודקה את לחצן אני בחרה
    אם לא מהבירה
    It defaults to ``PRIMARY``
    """
    try:
        pyautogui.click(button=loc)
    except ValueError:
        print(ValueError)
        pyautogui.click()


######################################################


def Input_Variables(time_click=None, loc=None, limit=None):
    # הכניסה משתנים
    time_click = input("Enetr Click interval time :")
    loc = input(
        "Enetr Click Choosing a place ``LEFT``, ``MIDDLE``, ``RIGHT`` \n\t enter:"
    )
    limit = int(input("Enetr the click limits "))
    print(time_click, loc, limit, sep=",")
    print("/n ---------------")
    return time_click, loc, limit


def main():
    # time_click, loc, limit = Input_Variables()
    # time.sleep(5)
    # Click(time_click, loc)
    # Click(time_click, loc, limit)
    time.sleep(2)
    Click(0.1, "RIGHT", 600)


if __name__ == "__main__":
    main()
