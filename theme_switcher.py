import pyautogui

# change vs-code theme to dark

# launch vs-code
import subprocess
subprocess.call(['code'])

# re-focus on vscode
pyautogui.hotkey('alt', 'tab')

# ensure focus is on editor, not terminal or explorer
pyautogui.hotkey('ctrl', '1')

# open theme switcher
pyautogui.hotkey('ctrl', 'k', 't')
pyautogui.typewrite('dark', 0.25)
pyautogui.press('enter')

# this apparently holds onto the shell
subprocess.call(['gitkraken'])

# focus on gitkraken
pyautogui.PAUSE = 5
pyautogui.hotkey('alt', 'tab')
pyautogui.PAUSE = 0.25

# open the ui preferences
pyautogui.hotkey('ctrl', 'p')
pyautogui.typewrite('ui preferences', 0.25)
pyautogui.press('enter')


# for google chrome

# launch google chrome

# navigate to google.com (which is usally white)

# toggle brigteness

# use some image recognition to tell if its white or black