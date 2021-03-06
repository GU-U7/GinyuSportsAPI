from bs4 import BeautifulSoup
import requests

month_number = {'Jan': "01", "Feb": "02", "Mar": "03", "Apr": "04", "May":"05", "Jun": "06","Jul": "07", "Aug": "08", "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"}
anho = "2022"

def date_format(datestr):
    datestr = datestr.split(' ')
    mes = month_number[datestr[2]]
    dia = datestr[1].zfill(2)
    return anho+"-"+mes+'-'+dia


def scrapear(params):
    enlace = "https://www.soccerstats.com/results.asp?league="
    mes = "&pmtype=month3"

    # RETRIEVAL OF HTML USING REQUESTS
    html_text = requests.get(enlace+params+mes).text

    # SCRAP OBJECT CREATION
    tabla = BeautifulSoup(html_text, 'lxml')

    # OBTAINS LIST OF HTML STRUCTURE OF MATCHES
    partidos = tabla.find('table', {'id': "btable"}).find_all('tr', class_="odd")

    # STRINGIFY RESULTS
    result = ""
    for partido in partidos:
        attr = partido.find_all("td")[:4]

        result += date_format(attr[0].text) + ','
        result += attr[1].text[:-1] +','
        result += attr[3].text[1:]+','
        result += attr[2].text+','
        result += params
        result += '\n'
    return result