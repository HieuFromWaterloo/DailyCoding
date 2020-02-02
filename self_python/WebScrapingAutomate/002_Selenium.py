"""
NEED TO DOWNLOAD: https://github.com/mozilla/geckodriver/releases

then move this driver to the same dir that selenium will look for

also need to:
- cd Downloads
- cp geckodriver /Users/hq2nguye/geckodriver

OR ON MAC:

brew install geckodriver

which geckodiver : to get the path

driver = webdriver.Firefox(executable_path = '/usr/local/bin/geckodriver')
"""

"""
pip install selenium

"""

########### EXTRACT ALL PAGES AND STORE IN CSV ##############
from selenium import webdriver
import csv
# first thing to note is that as we navigate through pages
# the only thing that chages is the url

# tells selenmn where chrome driver is stored
# chromedriver = "/Users/hq2nguye/Downloads/chromedriver"
# driver = webdriver.Chrome(chromedriver)
# driver.get("http:google.com")

# set max page number: how many times are we gonna click the "load more"
MAX_PAGE_NUM = 43  # 43
# set max page digit: this is for editting the url
MAX_PAGE_DIG = 3
# Note we nolong need to specify a specific webpage here
driver = webdriver.Firefox()
page_num = 43
url = "https://insolvencyinsider.ca/filing/?fwp_load_more=5"

driver.get(url)
"""
Filing Type: Receivership
Company Counsel: Advocates
Trustee: BDO
Trustee Counsel: Aird & Berlis
Applicant: RBC
Applicant Counsel: Harrison Pensa
Industry: Automotive
Province: Ontario
"""
# create a dict of title:
"""
# {1: None, 2: None, 3: None}
"""
d = dict.fromkeys(["Company", "Ticker", "Filing Date", "Filing Type",
                   "Company Counsel", "Trustee", "Trustee Counsel", "Applicant",
                   "Applicant Counsel", "Industry", "Province", "Summary"])

key_set = set(d.keys())
key_set -= {"Company", "Filing Date", "Summary"}

for key, _ in d.items():
    d[key] = []

filing_entry = driver.find_elements_by_xpath('//div[@class="filing-entry"]')
links = driver.find_elements_by_partial_link_text('View Case')

# get all the url
# for link in links:
#     d["Link"].append(str(link.get_attribute("href")))
# print(str(link.get_attribute("href")))


for e in filing_entry:
    list_of_content = [str(i).strip() for i in e.text.split("\n")]
    print(list_of_content)
    print("\n")
    # remove empty str
    list_of_content = list(filter(None, list_of_content))

    com_name = list_of_content[0]
    if "(" in com_name:
        ticker = str(com_name[com_name.index("("):])
    else:
        ticker = "NA"

    # print(f">>>> WORKING ON {com_name} <<<<<<\n")

    d["Company"].append(com_name)
    d["Ticker"].append(ticker)
    d["Filing Date"].append(list_of_content[1])
    d["Summary"].append(list_of_content[-2])
    # take care of the rest of the labels
    list_of_labels = [i for i in list_of_content[2:-2] if len(i.split(":")) == 2]
    # ['Filing Type: Bankruptcy', 'Trustee: KSV Advisory', 'Industry: Transportation']
    set_of_labels = set([i.split(":")[0] for i in list_of_labels])
    # {'Industry', 'Filing Type', 'Trustee'}
    for label in list_of_labels:
        tmp = label.split(":")
        d[tmp[0].strip()].append(tmp[1].strip())

    # non overlap:
    sym_diff_list = list(key_set.symmetric_difference(set_of_labels))
    for diff in sym_diff_list:
        d[diff].append("NA")

# print(d)

with open("test_d.csv", "w") as outfile:
    writer = csv.writer(outfile)
    writer.writerow(d.keys())
    writer.writerows(zip(*d.values()))

print(f">>>>>>>>>>>>>> SCRAPING COMPLETED >>>>>>>>>>>>>>>\n")
print(len(filing_entry))
print(len(links))

# num_page_items = len(test_label)
# write to a csv files
# with open('results.csv', 'a') as f:
#     for i in range(num_page_items):
#         f.write(test_label[i].text + "," + class_content[i].text + "\n")

# filing_type = driver.find_elements_by_xpath('//div[@title="buyer-name"]')
# prices = driver.find_elements_by_xpath('//span[@class="item-price"]')

# num_page_items = len(buyers)
# write to a csv files
# with open('results.csv', 'a') as f:
#     for i in range(num_page_items):
#         f.write(buyers[i].text + "," + prices[i].text + "\n")

driver.close()
