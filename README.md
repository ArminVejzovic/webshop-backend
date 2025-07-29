# webshop-backend
Backend for webshop app

Backend aplikacija za webshop sistem, razvijena u sklopu tehničkog dijela selekcijskog procesa za firmu **Neptis Space**.

## 🚀 Tehnologije

- Python
  
- FastAPI
  
- JWT za autentifikaciju

- Retool API, sva logika vezana za podatke s Retool API-ja implementirana je na frontend strani

## Tipovi korisnika
  
  Admin
  
  Kupac (Guest)

## API

Aplikacija koristi dva REST API-ja za upravljanje podacima

  /articles API

  Ovaj API služi za dohvat i upravljanje artiklima koji su dostupni u web shopu. Svaki artikal ima jedinstveni ID, naziv, cijenu, količinu, sliku, opis i datum kreiranja.

  [
    {
      "id": 23,
      "name": "Set Tanjira",
      "price": 19.99,
      "quantity": 20,
      "image_url": "https://cdn.pixabay.com/photo/2016/05/08/15/39/icon-1379313_1280.png",
      "created_at": "2025-07-26T19:32:23.853Z",
      "description": "Set Tanjira 6 komada"
    }
  ]

Polja:

  id: Jedinstveni identifikator artikla

  name: Naziv artikla

  price: Cijena artikla (decimalni broj)

  quantity: Dostupna količina na stanju

  image_url: Link ka slici artikla

  created_at: Datum i vrijeme kada je artikal kreiran

  description: Kratki opis artikla


  /orders API

  Ovaj API omogućava kreiranje i pregled narudžbi korisnika. Svaka narudžba sadrži listu artikala, status, informacije o kupcu i vremena obrade.

[
  {
    "id": 33,
    "items": "23, 23, 24",
    "status": "Rejected",
    "created_at": "7/29/2025, 3:45:00 PM",
    "processed_at": "2025-07-29T13:47:05.179Z",
    "customer_email": "armin.vejzovic@gmail.com",
    "customer_phone": "+3234432432",
    "customer_address": "Adresa Armin 123",
    "customer_lastname": "Vejzovic",
    "customer_firstname": "Armin"
  },
]

Polja:

  id: Jedinstveni identifikator narudžbe

  items: String s ID-jevima artikala iz narudžbe, odvojenim zarezima

  status: Trenutni status narudžbe (Processing, Accepted, Rejected, Finished)

  created_at: Vrijeme kada je narudžba kreirana (format može varirati)

  processed_at: Vrijeme kada je narudžba obrađena (može biti null ako nije još obrađena)

  customer_email: Email kupca

  customer_phone: Broj telefona kupca

  customer_address: Adresa kupca

  customer_lastname: Prezime kupca

  customer_firstname: Ime kupca

Za pravilno funkcionisanje aplikacije potrebno je da oba API-ja budu implementirana i dostupna, jer:

  /articles omogućava prikaz proizvoda i dodavanje u korpu,

  /orders omogućava slanje narudžbi i praćenje njihovog statusa.

## Instalacija i pokretanje

1. Kloniraj repozitorij:

   ```bash

   git clone https://github.com/ArminVejzovic/webshop-backend.git

   cd webshop-backend

3. Instaliraj zavisnosti:

   pip install -r requirements.txt

6. Kreiraj .env fajl u root direktoriju sa sljedećim sadržajem

   FRONTEND_URL=<your_frontend_url>

   ADMIN_USERNAME=<your_admin_username>

   ADMIN_PASSWORD=<your_admin_password>

   SECRET_KEY=<your_secret_key>

   ALGORITHM=<your_algoritam>

   ACCESS_TOKEN_EXPIRE_MINUTES=<your_access_token_expire_minutes>

7. Pokreni aplikaciju sa:

   uvicorn main:app --reload

9. API dokumentacija dostupna je na:

    http://localhost:8000/docs

## Autentifikacija
  
  JWT token se generise prilikom logina
  
  Token je potreban za pristup zasticenim rutama

## Kontakt
  
  Autor: Armin Vejzović
  
  Email: 29armin.vejzovic@gmail.com



