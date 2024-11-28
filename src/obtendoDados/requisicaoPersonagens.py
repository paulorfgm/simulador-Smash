from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configurações do navegador Brave e ChromeDriver
brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"  # Caminho do Brave
chromedriver_path = r"C:\Users\Paulo\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"  # Caminho do ChromeDriver

options = Options()
options.binary_location = brave_path
options.add_argument("--disable-gpu")
options.add_argument("--headless")
options.add_argument("--window-size=1920,1080")

service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service, options=options)

# Lista de personagens para buscar
characters = [
    ("mario"),
    ("donkey-kong"),
    ("link"),
    ("samus"),
    ("dark-samus"),
    ("yoshi"),
    ("kirby"),
    ("fox"),
    ("pikachu"),
    ("luigi"),
    ("ness"),
    ("captain-falcon"),
    ("jigglypuff"),
    ("peach"),
    ("daisy"),
    ("bowser"),
    ("ice-climbers"),
    ("sheik"),
    ("zelda"),
    ("dr-mario"),
    ("pichu"),
    ("falco"),
    ("marth"),
    ("lucina"),
    ("young-link"),
    ("ganondorf"),
    ("mewtwo"),
    ("roy"),
    ("chrom"),
    ("mr-game-and-watch"),
    ("meta-knight"),
    ("pit"),
    ("dark-pit"),
    ("zero-suit-samus"),
    ("wario"),
    ("snake"),
    ("ike"),
    ("pokemon-trainer"),
    ("diddy-kong"),
    ("lucas"),
    ("sonic"),
    ("king-dedede"),
    ("olimar"),
    ("lucario"),
    ("rob"),
    ("toon-link"),
    ("wolf"),
    ("villager"),
    ("mega-man"),
    ("wii-fit-trainer"),
    ("rosalina"),
    ("little-mac"),
    ("greninja"),
    ("palutena"),
    ("pac-man"),
    ("robin"),
    ("shulk"),
    ("bowser-jr"),
    ("duck-hunt"),
    ("ryu"),
    ("ken"),
    ("cloud"),
    ("corrin"),
    ("bayonetta"),
    ("inkling"),
    ("ridley"),
    ("simon"),
    ("richter"),
    ("king-k-rool"),
    ("isabelle"),
    ("incineroar"),
    ("piranha-plant"),
    ("joker"),
    ("hero"),
    ("banjo-and-kazooie"),
    ("terry"),
    ("byleth"),
    ("min-min"),
    ("steve"),
    ("sephiroth"),
    ("pyra-and-mythra"),
    ("kazuya"),
    ("sora")
]

resultados = []

try:
    # Iteramos sobre os personagens
    for character in characters:

        # Construimos a URL
        url = f"https://ultimatestagedata.com/character/{character}"
        driver.get(url)

        # Aguardamos a página carregar completamente
        wait = WebDriverWait(driver, 10)

        # Pegamos as porcentagens
        percentage_element = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "div.font-fjalla.font-bold.text-3xl")
        ))
        percentages = percentage_element.text.strip()

        # Adicionamos as porcentagens ao vetors
        resultados.append({"character": f"{character}", "percentages": percentages})

# Exceção caso a url não seja carregada, ou os dados não sejam encontrados
except Exception as e:
    print(f"Erro ao acessar os dados: {e}")

finally:
    driver.quit()
