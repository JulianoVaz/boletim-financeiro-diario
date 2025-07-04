import smtplib
import requests
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime, timedelta
import pytz
import json

# Configurações
EMAIL_FROM = os.getenv("EMAIL_FROM")
EMAIL_TO = os.getenv("EMAIL_TO")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
SMTP_SERVER = "smtp.office365.com"
SMTP_PORT = 587

WORDPRESS_SITE = os.getenv("WORDPRESS_SITE")
WORDPRESS_TOKEN = os.getenv("WORDPRESS_TOKEN")

def gerar_boletim_html():
    now = datetime.now(pytz.timezone("America/Sao_Paulo"))
    data_hora = now.strftime("%d de %B de %Y – %H:%M (UTC -3:00)")
    html = f"""
    <html><body>
    <h1>📊 Boletim Financeiro Diário</h1>
    <p><strong>Data:</strong> {data_hora}</p>
    <h2>📰 Resumo das Principais Notícias do Dia</h2>
    <p><strong>Bitcoin pode atingir US$ 135 mil até o 3º trimestre de 2025, segundo o Standard Chartered.</strong><br>
    O banco britânico revisou sua previsão para o preço do Bitcoin, elevando a meta para US$ 135.000. O BTC opera hoje em torno de US$ 109.250.<br>
    <strong>Fonte:</strong> <a href='https://www.kucoin.com/pt/news/category/news-flash'>KuCoin</a></p>
    <p><strong>USDC da Circle cresce 29 vezes em um ano e domina 75% do volume OTC.</strong><br>
    A stablecoin USDC teve um crescimento explosivo em 2025, consolidando-se como a principal moeda para transações institucionais.<br>
    <strong>Fonte:</strong> <a href='https://www.kucoin.com/pt/news/category/news-flash'>KuCoin</a></p>
    <h2>📈 Top 5 Ações em Alta – Brasil (B3)</h2>
    <ul>
    <li>Armac ON (ARML3): +27,12%</li>
    <li>Cemepe PN: +14,86%</li>
    <li>FII SC 401: +12,18%</li>
    <li>Dtcom ON: +12,14%</li>
    <li>GDS Holdings BDR: +10,08%</li>
    </ul>
    <h2>📉 Top 5 Ações em Baixa – Brasil (B3)</h2>
    <ul>
    <li>Usiminas (USIM5): -21,37%</li>
    <li>Cogna (COGN3): -14,12%</li>
    <li>São Martinho (SMTO3): -9,88%</li>
    <li>Totvs (TOTS3): -8,81%</li>
    <li>Marfrig (MRFG3): -8,50%</li>
    </ul>
    <h2>🌍 Top 5 Ações em Alta – Mercado Mundial</h2>
    <ul>
    <li>Tripadvisor: +20,10%</li>
    <li>Datadog BDR: +15,31%</li>
    <li>Citizens Financial Group BDR: +13,81%</li>
    <li>First Solar BDR: +6,82%</li>
    <li>GeoPark BDR: +6,32%</li>
    </ul>
    <h2>🌍 Top 5 Ações em Baixa – Mercado Mundial</h2>
    <ul>
    <li>Finor: -6,98%</li>
    <li>Eucatex (ON): -3,95%</li>
    <li>Cisco (BDR): -3,34%</li>
    <li>Costco (BDR): -3,18%</li>
    <li>Beyond Meat (BDR): -3,06%</li>
    </ul>
    <h2>💡 Análise e Dicas de Investimento</h2>
    <p><strong>Criptomoedas em ascensão com apoio institucional.</strong><br>
    O mercado cripto está entrando em uma nova fase de maturidade. Investidores podem considerar alocações estratégicas em BTC e stablecoins.</p>
    <p><strong>Fintechs e inovação financeira ganham tração.</strong><br>
    A integração entre finanças tradicionais e cripto está se acelerando.</p>
    <p><strong>Mercado de ações brasileiro atrai capital estrangeiro.</strong><br>
    Setores como commodities, energia e bancos continuam sendo boas apostas.</p>
    <p><strong>Economia americana resiliente favorece ativos de risco.</strong><br>
    A criação de empregos nos EUA reforça a tese de que o ciclo de aperto monetário pode estar perto do fim.</p>
    <h2>🧠 Conclusão Estratégica</h2>
    <p>O mercado financeiro global está em transição. A diversificação entre ações brasileiras, criptoativos e empresas globais inovadoras pode ser uma estratégia vencedora para o segundo semestre de 2025.</p>
    </body></html>
    """
    return html

def enviar_email(html):
    msg = MIMEMultipart("alternative")
    msg["Subject"] = "Boletim Financeiro Diário"
    msg["From"] = EMAIL_FROM
    msg["To"] = EMAIL_TO
    part = MIMEText(html, "html")
    msg.attach(part)

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(EMAIL_FROM, EMAIL_PASSWORD)
        server.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())

def publicar_no_wordpress(html):
    headers = {
        "Authorization": f"Bearer {WORDPRESS_TOKEN}",
        "Content-Type": "application/json"
    }
    data = {
        "title": "Boletim Financeiro Diário",
        "content": html,
        "status": "publish"
    }
    response = requests.post(f"https://public-api.wordpress.com/rest/v1.1/sites/{WORDPRESS_SITE}/posts/new", headers=headers, data=json.dumps(data))
    print("Publicação no WordPress:", response.status_code, response.text)

if __name__ == "__main__":
    html = gerar_boletim_html()
    enviar_email(html)
    publicar_no_wordpress(html)
