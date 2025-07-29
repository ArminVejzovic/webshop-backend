# webshop-backend
Backend for webshop app

Backend aplikacija za webshop sistem, razvijena u sklopu tehničkog dijela selekcijskog procesa za firmu **Neptis Space**.

## 🚀 Tehnologije

- Python
- FastAPI
- JWT za autentifikaciju
- Retool API, sva logika vezana za podatke s Retool API-ja implementirana je na frontend strani

## Instalacija i pokretanje

1. Kloniraj repozitorij:
   ```bash
   git clone https://github.com/ArminVejzovic/webshop-backend.git
   cd webshop-backend

2. pip install -r requirements.txt

3. dodaj .env fajl sadrzaja
  FRONTEND_URL=<your_frontend_url>
  ADMIN_USERNAME=<your_admin_username>
  ADMIN_PASSWORD=<your_admin_password>
  SECRET_KEY=<your_secret_key>
  ALGORITHM=<your_algoritam>
  ACCESS_TOKEN_EXPIRE_MINUTES=<your_access_token_expire_minutes>

5. uvicorn main:app --reload

6. <your_backend_url>/docs


## Tipovi korisnika
  Admin
  Kupac (Guest)

## Autentifikacija
  JWT token se generise prilikom logina
  Token je potreban za pristup zasticenim rutama

## Kontakt
  Autor: Armin Vejzović
  Email: 29armin.vejzovic@gmail.com



