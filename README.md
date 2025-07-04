# Boletim Financeiro Diário

Este projeto gera automaticamente um boletim financeiro diário em HTML, envia por e-mail e publica no seu blog WordPress usando GitHub Actions.

## ✅ O que você precisa configurar

### 1. Criar um repositório no GitHub

- Nome sugerido: `boletim-financeiro-diario`

### 2. Adicionar os seguintes segredos no GitHub (Settings > Secrets > Actions)

- `EMAIL_FROM`: seu e-mail Outlook (ex: vaz.juliano@hotmail.com)
- `EMAIL_TO`: destinatário (pode ser o mesmo)
- `EMAIL_PASSWORD`: senha de app do Outlook
- `WORDPRESS_SITE`: ID ou domínio do seu blog (ex: boletimfinancas.wordpress.com)
- `WORDPRESS_TOKEN`: token de acesso da API do WordPress

### 3. Agendamento

O boletim será gerado todos os dias às **12h (UTC -3)** automaticamente.

## 📦 Arquivos

- `generate_boletim.py`: script principal
- `.github/workflows/boletim.yml`: agendamento automático
- `README.md`: instruções

## 📬 Resultado

- Você receberá o boletim por e-mail
- Ele será publicado automaticamente no seu blog WordPress

