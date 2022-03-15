import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


def scrap_data():#get all entries of quest containing Virtue Points
    driver = webdriver.Chrome("./chromedriver.exe")
    driver.get("https://lostarkcodex.com/us/quests/virtuepointsreward/")
    driver.find_element(By.XPATH,"//*[@id='QuestsTable_length']/label/select").click()
    driver.find_element(By.XPATH, "//*[@id='QuestsTable_length']/label/select/option[6]").click()
    f = open("VirtueQuest.txt", "w")
    for i in range(3):
        table = driver.find_element(By.XPATH, "//*[@id='QuestsTable']/tbody")
        rows = table.find_elements(By.TAG_NAME, "tr")
        for row in rows:
            id = row.find_elements(By.TAG_NAME, "td")[0]  # note: index start from 0, 1 is col 2
            QuestName = row.find_elements(By.TAG_NAME, "td")[2]
            string = "Quest Id: " + id.text + " Quest Name: " + QuestName.text
            #rewardInfo = row.find_elements(By.TAG_NAME, "td")[8]
            #reward = rewardInfo.find_elements(By.TAG_NAME,"div")[0]
            #if(reward.text == ''):
            #    print("Quest Id: ",id.text, " Quest Name: ",QuestName.text, " Reward: " + rewardInfo.tag_name)
            f.write(string + "\n")
        print("Hi")
        sleep(5)
        driver.find_element(By.XPATH, "//*[@id='QuestsTable_next']/a").click()
    f.close()
def right_click(x, y):
    pyautogui.click(x, y, button='right')
    pyautogui.click(x, y, button='right')

def left_click(x, y):
    pyautogui.click(x, y)
    pyautogui.click(x, y)

def triple_click(x, y):
    pyautogui.click(x, y)
    pyautogui.click(x, y)
    pyautogui.click(x, y)

def checkGame():
    pyautogui.press('j')
    sleep(1)
    x, y = pyautogui.locateCenterOnScreen('./images/Completed.png', confidence=0.55)
    pyautogui.moveTo(x,y,.25)
    left_click(x,y)
    x1, y1 = pyautogui.locateCenterOnScreen('./images/Search.png', confidence=0.55)
    pyautogui.moveTo(x1,y1,.25)
    left_click(x1,y1)

    file = open("VirtueQuest.txt", "r")
    f = open("toComplete.txt", "a")
    for quest in file:
        quest = quest.split("Quest Name: ", 1)[1]
        sleep(.25)
        #print(quest)
        pyautogui.typewrite(quest,0.05)
        #print(quest)g R
        x, y = pyautogui.locateCenterOnScreen('./images/SearchButton.png', confidence=0.8)
        pyautogui.moveTo(x,y,.25)
        pyautogui.click(x, y)
        if(pyautogui.locateCenterOnScreen('./images/Result.png', confidence = 0.8) is None):
            f.write(quest)
            print("Quest Not Found: ", quest)

        #print(quest)
        pyautogui.moveTo(x1,y1,.35)
        sleep(.01)
        left_click(x1, y1)
        pyautogui.keyDown('ctrl')  # hold down the shift key
        pyautogui.press('a')
        pyautogui.keyUp('ctrl')
        sleep(.25)
    f.close()
    file.close()

if __name__ == '__main__':
    checkGame()
    #scrap_data()
