from lxml import etree
import urllib

web = urllib.urlopen("http://www.tennisabstract.com/cgi-bin/player.cgi?p=RafaelNadal")
s = web.read()

html = etree.HTML(s)

tr = html.xpath('//table[@id="overall"]/tbody/tr')

x = [i[0].text for i in tr_nodes[0].xpath("th")]

win = [[td.text for td in tr.xpath('td')] for tr in tr[1:]]
