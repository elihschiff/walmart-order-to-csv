import sys
from lxml import html
import csv


with open(sys.argv[1], "r") as f:
    html_page = f.read()

dom = html.fromstring(html_page)

# Generates a list of itmes ordered
# Also makes sure the items in the list were not canceled
output = []
items = dom.xpath(
    '//*[@data-automation-id="details-table-header" and not(text() = "Unavailable")]/ancestor::*[contains(@class, "OrderItemDetails__groupTableContainer")]//*[not(contains(@class, "OrderItemDetails__fadedItemRow"))]/*[@data-automation-id="itemContainer"]'
)
for item in items:
    name = item.xpath('child::*//*[@data-automation-id="productName"]/text()')[0]
    cost = item.xpath('child::*//*[@data-automation-id="totalValue"]/text()')[0]
    output.append([name, cost])

with open(
    f"{sys.argv[2].replace('.csv', '') if len(sys.argv) >= 3 else 'output'}.csv", "w+"
) as my_csv:
    csvWriter = csv.writer(my_csv, delimiter=",")
    csvWriter.writerows(output)
