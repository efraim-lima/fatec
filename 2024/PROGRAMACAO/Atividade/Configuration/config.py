from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.common.exceptions import WebDriverException
import random, os, inspect, sys, subprocess;

def webDriver():
    # if not os.path.exists(os.path.abspath("geckodriver")):
    #     install_geckodriver()

    #d = DesiredCapabilities.FIREFOX
    #d['loggingPrefs'] = {'browser': 'ALL'}
    agentes = [ 
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36" ,
		"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36",
		"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36 OPR/68.0.3618.63",
		"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:63.0) Gecko/20100101 Firefox/63.0",
		"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36",
		"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
		];
    agente = agentes[random.randint(0, len(agentes) - 1)]
    try:
        from selenium.webdriver.firefox.options import Options as FireOptions
        from selenium.webdriver.firefox.service import Service
        
        options = FireOptions()
        options.set_preference("log_level","trace")
        options.headless = True
        options.add_argument("user-agent=" + agente)
        #options.add_argument("--headless")
        #options.add_argument("--disable-gpu")
        #options.add_argument("--no-sandbox")
        #options.add_argument("--mute-audio")
        #os.environ['MOZ_NO_REMOTE'] = '1'
        geckodriver_autoinstaller.install()
        global driver
        driver = webdriver.Firefox(options=options, service=Service(GeckoDriverManager().install()))
    except Exception as e:
        print("Excception: \n\n", e)

        try:
            from webdriver_manager.chrome import ChromeDriverManager
            from selenium.webdriver.chrome.service import Service
            from selenium.webdriver.chrome.options import Options
            
            options = Options()
            options.set_preference("log_level","trace")
            options.headless = True
            options.add_argument("user-agent=" + agente)
            #options.add_argument("--headless")
            #options.add_argument("--disable-gpu")
            #options.add_argument("--no-sandbox")
            #options.add_argument("--mute-audio")
            #os.environ['MOZ_NO_REMOTE'] = '1'

            driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
        except Exception as e:
            print("Exception: \n\n", e)
    
    # capabilities = {
    #     "goog:loginPrefs": {"performance":"ALL"},
    #     "moz:firefoxOptions":{
    #         "llog":{"level":"trace"}
    #     }
    # }

    # profile = webdriver.FirefoxProfile()

    
    #driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    # driver.getInstance().useTaobaoMirror().setup()
    
    return driver

def quit():
    quit = driver.quit()
    return quit

def close():
    close = driver.close()
    return close
