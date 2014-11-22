from bs4 import BeautifulSoup
import urllib2

wiki = "https://www.besmith.com/candidates/search"
header = {'User-Agent': 'Mozilla/5.0'}
req = urllib2.Request(wiki,headers=header)
page = urllib2.urlopen(req)
soup = BeautifulSoup(page)
print ""
print "Title | " + "Job Link"
print ""
data = []
for table in soup.find_all('table', attrs={'id': 'job-opportunity'}):
   
    links = table.findAll('a')
    for link in links:
        print link.string + " | "+link['href']
print ""
print "Oraganization Name | " + "Position | " + "Location"
for table in soup.find_all('table', attrs={'id': 'job-opportunity'}):
    data.append(table.select('tr:nth-of-type(2) > td:nth-of-type(2)')[0].string or '') 
    data.append(table.select('tr:nth-of-type(2) > td:nth-of-type(3)')[0].string or '')
    data.append(table.select('tr:nth-of-type(2) > td:nth-of-type(4)')[0].string or '')
    data.append("\n")
    data.append(table.select('tr:nth-of-type(3) > td:nth-of-type(2)')[0].string or '') 
    data.append(table.select('tr:nth-of-type(3) > td:nth-of-type(3)')[0].string or '')
    data.append(table.select('tr:nth-of-type(3) > td:nth-of-type(4)')[0].string or '')
    data.append("\n")
    data.append(table.select('tr:nth-of-type(4) > td:nth-of-type(2)')[0].string or '') 
    data.append(table.select('tr:nth-of-type(4) > td:nth-of-type(3)')[0].string or '')
    data.append(table.select('tr:nth-of-type(4) > td:nth-of-type(4)')[0].string or '')
    data.append("\n")
    data.append(table.select('tr:nth-of-type(5) > td:nth-of-type(2)')[0].string or '') 
    data.append(table.select('tr:nth-of-type(5) > td:nth-of-type(3)')[0].string or '')
    data.append(table.select('tr:nth-of-type(5) > td:nth-of-type(4)')[0].string or '')
    data.append("\n")
    data.append(table.select('tr:nth-of-type(6) > td:nth-of-type(2)')[0].string or '') 
    data.append(table.select('tr:nth-of-type(6) > td:nth-of-type(3)')[0].string or '')
    data.append(table.select('tr:nth-of-type(6) > td:nth-of-type(4)')[0].string or '')
    data.append("\n")
    data.append(table.select('tr:nth-of-type(7) > td:nth-of-type(2)')[0].string or '') 
    data.append(table.select('tr:nth-of-type(7) > td:nth-of-type(3)')[0].string or '')
    data.append(table.select('tr:nth-of-type(7) > td:nth-of-type(4)')[0].string or '')
    data.append("\n")
    data.append(table.select('tr:nth-of-type(8) > td:nth-of-type(2)')[0].string or '') 
    data.append(table.select('tr:nth-of-type(8) > td:nth-of-type(3)')[0].string or '')
    data.append(table.select('tr:nth-of-type(8) > td:nth-of-type(4)')[0].string or '')
    data.append("\n")
    data.append(table.select('tr:nth-of-type(9) > td:nth-of-type(2)')[0].string or '') 
    data.append(table.select('tr:nth-of-type(9) > td:nth-of-type(3)')[0].string or '')
    data.append(table.select('tr:nth-of-type(9) > td:nth-of-type(4)')[0].string or '')
    data.append("\n")
    data.append(table.select('tr:nth-of-type(10) > td:nth-of-type(2)')[0].string or '') 
    data.append(table.select('tr:nth-of-type(10) > td:nth-of-type(3)')[0].string or '')
    data.append(table.select('tr:nth-of-type(10) > td:nth-of-type(4)')[0].string or '')
    data.append("\n")
    data.append(table.select('tr:nth-of-type(11) > td:nth-of-type(2)')[0].string or '') 
    data.append(table.select('tr:nth-of-type(11) > td:nth-of-type(3)')[0].string or '')
    data.append(table.select('tr:nth-of-type(11) > td:nth-of-type(4)')[0].string or '')
    data.append("\n")
    data.append(table.select('tr:nth-of-type(12) > td:nth-of-type(2)')[0].string or '') 
    data.append(table.select('tr:nth-of-type(12) > td:nth-of-type(3)')[0].string or '')
    data.append(table.select('tr:nth-of-type(12) > td:nth-of-type(4)')[0].string or '')
    data.append("\n")
    data.append(table.select('tr:nth-of-type(13) > td:nth-of-type(2)')[0].string or '') 
    data.append(table.select('tr:nth-of-type(13) > td:nth-of-type(3)')[0].string or '')
    data.append(table.select('tr:nth-of-type(13) > td:nth-of-type(4)')[0].string or '')
    data.append("\n")
    data.append(table.select('tr:nth-of-type(14) > td:nth-of-type(2)')[0].string or '') 
    data.append(table.select('tr:nth-of-type(14) > td:nth-of-type(3)')[0].string or '')
    data.append(table.select('tr:nth-of-type(14) > td:nth-of-type(4)')[0].string or '')
    data.append("\n")

    print(' | '.join(data))

    # for i in range(2,4) :
    #     for j in range(2,5) :
    #         data.append(table.select('tr:nth-of-type(i) > td:nth-of-type(j)')[0].string or '') 

page2 = "https://www.besmith.com/candidates/search?field_state_value=All&field_job_category_tid=&field_job_type_tid=&field_code_value=&body_value=&field_term_tags_value=&page=1"
header = {'User-Agent': 'Mozilla/5.0'}
req = urllib2.Request(page2,headers=header)
page = urllib2.urlopen(req)
soup = BeautifulSoup(page)
print ""
print "2nd page Job Listings"
print "Title | " + "Job Link"
print ""
data2 = []
for table in soup.find_all('table', attrs={'id': 'job-opportunity'}):
   
    links = table.findAll('a')
    for link in links:
        print link.string + " | "+link['href']
print ""
print "Oraganization Name | " + "Position | " + "Location"
for table in soup.find_all('table', attrs={'id': 'job-opportunity'}):
    data2.append(table.select('tr:nth-of-type(2) > td:nth-of-type(2)')[0].string or '') 
    data2.append(table.select('tr:nth-of-type(2) > td:nth-of-type(3)')[0].string or '')
    data2.append(table.select('tr:nth-of-type(2) > td:nth-of-type(4)')[0].string or '')
    data2.append("\n")
    data2.append(table.select('tr:nth-of-type(3) > td:nth-of-type(2)')[0].string or '') 
    data2.append(table.select('tr:nth-of-type(3) > td:nth-of-type(3)')[0].string or '')
    data2.append(table.select('tr:nth-of-type(3) > td:nth-of-type(4)')[0].string or '')
    data2.append("\n")
    data2.append(table.select('tr:nth-of-type(4) > td:nth-of-type(2)')[0].string or '') 
    data2.append(table.select('tr:nth-of-type(4) > td:nth-of-type(3)')[0].string or '')
    data2.append(table.select('tr:nth-of-type(4) > td:nth-of-type(4)')[0].string or '')
    data2.append("\n")
    data2.append(table.select('tr:nth-of-type(5) > td:nth-of-type(2)')[0].string or '') 
    data2.append(table.select('tr:nth-of-type(5) > td:nth-of-type(3)')[0].string or '')
    data2.append(table.select('tr:nth-of-type(5) > td:nth-of-type(4)')[0].string or '')
    data2.append("\n")
    data2.append(table.select('tr:nth-of-type(6) > td:nth-of-type(2)')[0].string or '') 
    data2.append(table.select('tr:nth-of-type(6) > td:nth-of-type(3)')[0].string or '')
    data2.append(table.select('tr:nth-of-type(6) > td:nth-of-type(4)')[0].string or '')
    data2.append("\n")
    data2.append(table.select('tr:nth-of-type(7) > td:nth-of-type(2)')[0].string or '') 
    data2.append(table.select('tr:nth-of-type(7) > td:nth-of-type(3)')[0].string or '')
    data2.append(table.select('tr:nth-of-type(7) > td:nth-of-type(4)')[0].string or '')
    data2.append("\n")
    data2.append(table.select('tr:nth-of-type(8) > td:nth-of-type(2)')[0].string or '') 
    data2.append(table.select('tr:nth-of-type(8) > td:nth-of-type(3)')[0].string or '')
    data2.append(table.select('tr:nth-of-type(8) > td:nth-of-type(4)')[0].string or '')
    data2.append("\n")
    data2.append(table.select('tr:nth-of-type(9) > td:nth-of-type(2)')[0].string or '') 
    data2.append(table.select('tr:nth-of-type(9) > td:nth-of-type(3)')[0].string or '')
    data2.append(table.select('tr:nth-of-type(9) > td:nth-of-type(4)')[0].string or '')
    data2.append("\n")
    data2.append(table.select('tr:nth-of-type(10) > td:nth-of-type(2)')[0].string or '') 
    data2.append(table.select('tr:nth-of-type(10) > td:nth-of-type(3)')[0].string or '')
    data2.append(table.select('tr:nth-of-type(10) > td:nth-of-type(4)')[0].string or '')
    data2.append("\n")
    data2.append(table.select('tr:nth-of-type(11) > td:nth-of-type(2)')[0].string or '') 
    data2.append(table.select('tr:nth-of-type(11) > td:nth-of-type(3)')[0].string or '')
    data2.append(table.select('tr:nth-of-type(11) > td:nth-of-type(4)')[0].string or '')
    data2.append("\n")
    data2.append(table.select('tr:nth-of-type(12) > td:nth-of-type(2)')[0].string or '') 
    data2.append(table.select('tr:nth-of-type(12) > td:nth-of-type(3)')[0].string or '')
    data2.append(table.select('tr:nth-of-type(12) > td:nth-of-type(4)')[0].string or '')
    data2.append("\n")
    data2.append(table.select('tr:nth-of-type(13) > td:nth-of-type(2)')[0].string or '') 
    data2.append(table.select('tr:nth-of-type(13) > td:nth-of-type(3)')[0].string or '')
    data2.append(table.select('tr:nth-of-type(13) > td:nth-of-type(4)')[0].string or '')
    data2.append("\n")
    data2.append(table.select('tr:nth-of-type(14) > td:nth-of-type(2)')[0].string or '') 
    data2.append(table.select('tr:nth-of-type(14) > td:nth-of-type(3)')[0].string or '')
    data2.append(table.select('tr:nth-of-type(14) > td:nth-of-type(4)')[0].string or '')
    data2.append("\n")
    print(' | '.join(data2))


