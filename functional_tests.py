from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:8000')

if 'Django' in browser.title:
    print "Test Passed: Django server running"
    print browser.title
else:
    print "Test failed: Check if django server is running"
