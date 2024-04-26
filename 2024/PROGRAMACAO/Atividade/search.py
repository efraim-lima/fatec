import pandas as pd
# from selenium.websession.common.by import By
from requests_html import HTMLSession, AsyncHTMLSession
import datetime

# config = Configuration.config
def searcher(theme, *args, **kwargs):
    session = HTMLSession()

    # session = config.websession()
    url = session.get(f'https://www.google.com/search?q={theme}',
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'},
        proxies={"http": "http://111.233.225.166:1234"})
     
    url.raise_for_status()  # raises exception when not a 2xx response
    # url = url.content
    url.html.render()
    
    quantity = url.html.find(
        "#result-stats"
    )[0].text

    
    quantity = float(quantity.split('Aproximadamente ')[1]
                        .split(' resultados')[0]
                        .replace('.',''))
    pages = quantity/10
        
    actually_page = 0
    start = 10
    
    Quant = []
    Pages = []
    Theme = []
    Textos = []
    Links =[]
    Descript = []
    
    textos = url.html.xpath('//span/a')

    for texto in textos:
        try:
            link = texto.attrs.get('href')
            Links.append(link)
            print(link)
            texto1 = texto.find('h3')
            if texto1:
                texto = texto1[0].text
                print(texto)
        except:
            texto = "None"
        Textos.append(texto)
        
    linkads = url.html.xpath(
        "//body/div[@id='main']/div[@id='cnt']/div[@id='rcnt']/div[1]/div[1]/div[2]/div[1]/div/div[1]/div[1]/div[1]/div[1]/a[1]"
    )
    for links in linkads:
        links = links.attrs['href']
        Links.append(links)
                    
    descriptions = url.html.xpath(
        "//body/div[@id='main']/div[@id='cnt']/div[@id='rcnt']/div[1]/div[1]/div[2]/div[1]/div/div[1]/div[1]/div[1]/div[2]/div[1]"
    )
    for description in descriptions:
        Descript.append(description.text)        
    
    ### organic
    try:
        links = url.html.xpath(
            "//body/div[@id='main']/div[@id='cnt']/div[@id='rcnt']/div[@id='center_col']/div[@id='res']/div[@id='search']/div[1]/div[1]/div/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]"
        )
        for link in links:
            link = link.attrs['href']
            Links.append(link)
            
        textos = url.html.xpath(
            "//body/div[@id='main']/div[@id='cnt']/div[@id='rcnt']/div[@id='center_col']/div[@id='res']/div[@id='search']/div[1]/div[1]/div/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]/h3"
        )
        for texto in textos:
            Textos.append(texto.text)
            
        descriptions = url.html.xpath(
            "//body/div[@id='main']/div[@id='cnt']/div[@id='rcnt']/div[@id='center_col']/div[@id='res']/div[@id='search']/div[1]/div[1]/div/div[1]/div[1]/div[1]/div[3]"
        )
        for description in descriptions:
            Descript.append(description.text)
            
        links = url.html.xpath(
            "//body/div[@id='main']/div[@id='cnt']/div[@id='rcnt']/div[@id='center_col']/div[@id='res']/div[@id='search']/div[1]/div[1]/div/div[1]/div[1]/div[1]/div[1]/a[1]"
        )
        for link in links:
            link = link.attrs['href']
            Links.append(link)
            
        textos = url.html.xpath(
            "//body/div[@id='main']/div[@id='cnt']/div[@id='rcnt']/div[@id='center_col']/div[@id='res']/div[@id='search']/div[1]/div[1]/div/div[1]/div[1]/div[1]/div[1]/a[1]/h3"
        )
        for texto in textos:
            Textos.append(texto.text)
            
        descriptions = url.html.xpath(
            "//body/div[@id='main']/div[@id='cnt']/div[@id='rcnt']/div[@id='center_col']/div[@id='res']/div[@id='search']/div[1]/div[1]/div/div[1]/div[1]/div[2]"
        )
        for description in descriptions:
            Descript.append(description.text)
            
        for texto in Textos:
            Theme.append(theme)
            Quant.append(quantity)
            Pages.append(pages)

                            
        url.close()
    except:
        pass

    session.close()
    url.close()
    
    dfList = []

    for theme, texto, link, quantity, rank, description in zip(
        Theme, Textos, Links, Quant, Pages, Descript): 
        
        from app.Configuration.processing import clearing
        
        mach1 = clearing(texto, theme)
        mach2 = clearing(description, theme)

        if mach1 or mach2 == True:
            if quantity > 50000:
                calendar = day.pop()
            else:
                calendar = datetime.date.today()
                
            try:
                print("No try")  
                print("usar db_module")
            except:
                print("Except")
            dfList.append({
                'Category': theme,
                'News': texto,
                'URL': link,
                f'Quantity': quantity,
                f'Pontuation': rank/1000,
                'Description':description,
            })
                            
    df = pd.DataFrame(dfList)
    df = df.to_json()

    return df

async def get_page(url_page):
    asession = AsyncHTMLSession()
    url = await asession.get(url_page)

    url.run(get_page)

searcher('como fazer pastel')
