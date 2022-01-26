import sys, csv, time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

if len(sys.argv)<=1:
    print("\nUsage: python redfinscraper.py <url_from_redfin> ")
    sys.exit()

### do it with firefox
#firefoxProfile = webdriver.FirefoxProfile(r'C:\Users\windows\AppData\Roaming\Mozilla\Firefox\Profiles\2ieb5mqz.default-release')
#browser = webdriver.Firefox(firefox_profile=firefoxProfile)
#browser = webdriver.Firefox()

### to do it with chrome, uncomment these lines and comment the above (firefox) lines
#opts = webdriver.ChromeOptions() 
#opts.add_argument("user-data-dir=C:\\Users\\windows\\AppData\\Local\\Google\\Chrome\\User Data")
#browser=webdriver.Chrome(options=opts)
browser=webdriver.Chrome()

#write text to an output file. if False, print to screen only
writeFile=True
delim=","

wallHeightFt=int(8)
paintSqftPerGal=400
paintCostPerGal=18
paintCostPerSqft=paintCostPerGal/paintSqftPerGal
lvpCostPerSqft=3.6
trimCostPerFt=.78

class CCLI_scraper():
    def __init__(self,argument):
      self.myUrl=argument[0]

      results={}
      if "redfin.com" in self.myUrl:
        results=self.redfin(self.myUrl)
      #elif "zillow.com" in self.myUrl:
      else:
        print("not a redfin url")
      browser.close()

      if writeFile:
        self.writeCostCsv(results)

    def redfin(self,page):
        results={}
        browser.get(page)
        parent=browser.find_element_by_xpath('//*[@id="propertyDetails-collapsible"]/div[2]')
        children=parent.find_elements_by_class_name('amenity-group')
        for child in children:
          print(child)
          section=child.find_element_by_class_name('propertyDetailsHeader').get_attribute('innerHTML').lstrip().strip()
          itemlist=child.find_elements_by_class_name('entryItem')
          length=None
          width=None
          measurements={}
          for pair in itemlist:
            kvpair=pair.find_element_by_class_name('entryItemContent').get_attribute('innerHTML').split(":")
            print(kvpair)
            key=kvpair[0]
            if len(kvpair) > 1:
                value=kvpair[1].lstrip().lstrip("<span>").rstrip("</span>")
                if key == "Sq. Ft.":
                  measurements["floor area"]=value
                  measurements["wall area"]=int(value)*wallHeightFt
                elif key == "Length (Ft.)":
                  length=value
                elif key == "Width (Ft.)":
                  width=value
          if length is not None and width is not None:
            measurements["perimeter"]=(int(length)*2) + (int(width)*2)
          results[section]=measurements
        for i in results:
          print(i,results[i])
        return results

    def writeCostCsv(self,results):
      with open('cost.csv', 'w') as writer:
        writer.write(self.myUrl+"\n")
        for each in results:
          if each:
            myDict=results[each]
            if 'floor area' in myDict.keys():
              flooring=float(myDict['floor area'])*lvpCostPerSqft
              writer.write( each+delim+'floor area'+delim+\
                            str(myDict['floor area'])+delim+\
                            str(lvpCostPerSqft)+delim+\
                            str(flooring)+"\n")
            if 'wall area' in myDict.keys():
              paint=float(myDict['wall area'])*paintCostPerSqft
              writer.write( each+delim+'wall area'+delim+\
                            str(myDict['wall area'])+delim+\
                            str(paintCostPerSqft)+delim+\
                            str(paint)+"\n")
            if 'perimeter' in myDict.keys():
              trim=float(myDict['perimeter'])*trimCostPerFt
              writer.write( each+delim+'trim length'+delim+\
                            str(myDict['perimeter'])+delim+\
                            str(trimCostPerFt)+delim+\
                            str(trim)+"\n")
      writer.close()

pages=sys.argv[1:]
myScraper=CCLI_scraper(pages)
