from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import re
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



while True:
    time.sleep(10)
    # Create a new instance of the Chrome browser
    driver = webdriver.Chrome()

    # Open the URL in Chrome
    driver.get('https://tempus-termine.com/termine/index.php?anr=3&anwendung=1&sna=T88018e66f4c5fc9953c1f951961069bd&action=open&page=hinweisbestaetigung&tasks=999&kuerzel=Ummeldung&schlangen=67-68-69-70-71-72-73-83-84-85-86')

    # Find the checkbox and select it
    checkbox = driver.find_element(By.ID, 'einzelhinweischeck')
    checkbox.click()

    # Find the button and click it
    button = driver.find_element(By.ID, 'confirm')
    button.click()

    page_content = driver.page_source

    # Find all occurrences of "Kein Termin verfügbar" using regular expressions
    appointment_texts = re.findall(r'Kein Termin verfügbar', page_content)

    # Check the number of occurrences and print the result
    if len(appointment_texts) == 11:
        print("\n---------\nNot Openned Yet\n---------\n")
    else:
        print("\n---------\n---------OPEN\n---------\n")
        while True:
            print('\a')
    driver.quit()
    
