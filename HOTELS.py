import pandas as pd
import requests
from bs4 import BeautifulSoup

URL = 'https://www.trustpilot.com/categories/hotels'
HTML_DATA = requests.get(URL).text
BASE_URL = 'https://www.trustpilot.com/categories/hotels?page='
URL_LIST = []
i = 1
SERVICES = []
NAME = []
TRUST_SCORE = []
REVIEWSS = []
URLs = []
LOCATION = []
for num in range(1, 26):
    URL_LIST.append(BASE_URL + str(num))
for url in URL_LIST:
    HTML_DATA = requests.get(url).text
    soup = BeautifulSoup(HTML_DATA, 'lxml')
    INFO = soup.find_all('div',
                         class_='paper_paper_29o4A card_card2F_07 card_noPadding1tkWv styles_wrapper2QC-c styles_businessUnitCard_1-z5m')
    li = []
    for DATA in INFO:
        try:
            NAME = DATA.find('p',
                             class_='typography_typography_23IQz typography_h4IhMYK typography_weight-heavy36UHe typography_fontstyle-normal1_HQI styles_displayName_1LIcI').text.strip()
            if NAME == 'Newchip':
                continue

            SCORE = DATA.find('span',
                              class_='typography_typography_23IQz typography_bodysmall24hZa typography_weight-regulariZYoT typography_fontstyle-normal1_HQI styles_trustScore_nLHX2')

            if SCORE is not None:
                SCORE = SCORE.text
                var = SCORE.split(' ')
                TRUST_SCORE = var[1]

            REVIEW = DATA.find('p',
                               class_='typography_typography_23IQz typography_bodysmall24hZa typography_color-gray-72eGCj typography_weight-regulariZYoT typography_fontstyle-normal1_HQI styles_ratingText_nheL7')
            if REVIEW is not None:
                REVIEW = REVIEW.text
                VARIABLE = REVIEW.split('|')
                REVIEWS = VARIABLE[1]
                A = (REVIEWS.split('r'))
                E = A[0]

            LINK = DATA.find('a')['href']
            L = LINK.split('/')
            C = L[2]
            URLs = 'https://www.trustpilot.com/review/' + C

            F = requests.get(URLs).text
            SOP = BeautifulSoup(F, 'lxml')
            G = SOP.find_all('li', class_='styles_contactInfoElement__SxlS3')
            LOCATION = SOP.find('ul',
                                class_='typography_typography_QgicV typography_bodysmallirytL typography_weight-regularTWEnf typography_fontstyle-normalkHyN3 styles_contactInfoAddressList_RxiJI').text.strip()

        except AttributeError:
            pass
        MY_DICT = {
            'Sr.No': i,
            'NAME': NAME,
            'TRUST SCORE': TRUST_SCORE,
            'TOTAL REVIEWS': E,
            'URL': URLs,
            'LOCATION': LOCATION

        }
        i += 1
        SERVICES.append(MY_DICT)
df = pd.DataFrame(SERVICES)
print(df)
df.to_excel('HOTELS.xlsx')
