"""
NEED TO DOWNLOAD: https://github.com/mozilla/geckodriver/releases

then move this driver to the same dir that selenium will look for

also need to:
- cd Downloads
- cp geckodriver /Users/hq2nguye/geckodriver
"""

"""
pip install selenium

"""

############ EXTRACT FROM 1ST PAGES #################
# from selenium import webdriver

# # Open up a Firefox browser and navigate to web page.
# driver = webdriver.Firefox()
# driver.get("http://econpy.pythonanywhere.com/ex/001.html")

# # Extract lists of "buyers" and "prices" based on xpath.
# # // perceives xpath and we want this xpath to be in the div tag
# buyers = driver.find_elements_by_xpath('//div[@title="buyer-name"]')
# prices = driver.find_elements_by_xpath('//span[@class="item-price"]')

# # Print out all of the buyers and prices on page:
# num_page_items = len(buyers)
# for i in range(num_page_items):
#     # extract the text from the buyers list
#     print(buyers[i].text + " : " + prices[i].text)

# # Clean up (close browser once completed task).
# driver.close()


########### EXTRACT ALL PAGES AND STORE IN CSV ##############
from selenium import webdriver
# first thing to note is that as we navigate through pages
# the only thing that chages is the url

# tells selenmn where chrome driver is stored
chromedriver = "/home/captainhampton/Downloads/chromedriver"
driver = webdriver.Chrome(chromedriver)
driver.get("http:google.com")

# set max page number: how many times are we gonna click the "load more"
MAX_PAGE_NUM = 5
# set max page digit: this is for editting the url
MAX_PAGE_DIG = 3
driver = webdriver.Firefox()

with open('results.csv', 'w') as f:
    f.write("Buyer, Price \n")

for i in range(1, MAX_PAGE_NUM + 1):
    """
    + len(str(i))): (1, MAX_PAGE_NUM + 1)
    + padding string i with appropirate 0 in front: * "0"
    """
    page_num = (MAX_PAGE_DIG - len(str(i))) * "0" + str(i)
    url = "http://econpy.pythonanywhere.com/ex/" + page_num + ".html"

    driver.get(url)

    buyers = driver.find_elements_by_xpath('//div[@title="buyer-name"]')
    prices = driver.find_elements_by_xpath('//span[@class="item-price"]')

    num_page_items = len(buyers)
    # write to a csv files
    with open('results.csv', 'a') as f:
        for i in range(num_page_items):
            f.write(buyers[i].text + "," + prices[i].text + "\n")

driver.close()
