# FACEBOOK-PokeBackBot

This bot pokes back people from https://www.facebook.com/pokes

## Requirements

Google Chrome `https://www.google.com/intl/pl_pl/chrome/`  
Chromedrivers `https://chromedriver.chromium.org`  
Selenium `python -m pip install selenium`

## User Manuala

Fill in these lines of code according to your Facebook login details:

```
userName = "Jan@gmail.com"
passWord = "12345678pass"
```

Select the location of the drivers and complete it in this line:

```
driver = webdriver.Chrome(options=options, executable_path =
r"C:/chromedriver_win32/chromedriver.exe", chrome_options = option)
```

Start the program with `python main.py`
