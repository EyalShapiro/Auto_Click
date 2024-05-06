import pyautogui
import time


class AutoClicker:
    def __init__(self, time_click=0.1, loc="RIGHT", limit=None):
        self.time_click = time_click
        self.loc = loc
        self.limit = limit

    def start_clicking(self):
        time.sleep(5)  # Delay for 5 seconds before starting
        self.click()

    def click(self):
        if self.limit is None:
            self.click_infinite()
        else:
            self.click_limited()

    def click_infinite(self):
        while True:
            time.sleep(self.time_click)
            print("Click", self.loc)
            self.except_location_click()

    def click_limited(self):
        for _ in range(self.limit):
            time.sleep(self.time_click)
            print("Click", self.loc)
            self.except_location_click()

    def except_location_click(self):
        try:
            pyautogui.click(button=self.loc)
        except pyautogui.FailSafeException:
            print("Failsafe exception occurred. Exiting...")
            exit()
