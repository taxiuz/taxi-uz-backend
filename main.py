import sqlite3
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="Taxi UZ API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DB_NAME = "taxi_orders.db"


def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            order_id TEXT UNIQUE,
            name TEXT,
            phone TEXT,
            from_loc TEXT,
            to_loc TEXT,
            tariff TEXT,
            status TEXT
        )
    """)
    conn.commit()
    conn.close()


init_db()


class Order(BaseModel):
    name: str
    phone: str
    from_loc: str
    to_loc: str
    tariff: str = "standard"


@app.get("/")
def home():
    return {
        "service": "Taxi UZ",
        "status": "online"
    }


@app.get("/calculate")
def calculate_fare(from_loc: str, to_loc: str, tariff: str = "standard"):
    base_fares = {
        "standard": 10000,
        "comfort": 15000,
        "biznes": 25000
    }

    price = base_fares.get(tariff.lower(), 10000)

    return {
        "from": from_loc,
        "to": to_loc,
        "tariff": tariff,
        "price_som": price,
        "currency": "UZS"
    }


@app.post("/orders")
def create_order(order: Order):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM orders")
    count = cursor.fetchone()[0]
    order_id = f"TXU-{(count + 1):04d}"

    cursor.execute("""
        INSERT INTO orders (order_id, name, phone, from_loc, to_loc, tariff, status)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (order_id, order.name, order.phone, order.from_loc, order.to_loc, order.tariff, "created"))

    conn.commit()
    conn.close()

    return {
        "order_id": order_id,
        "status": "created",
        "name": order.name,
        "phone": order.phone,
        "from": order.from_loc,
        "to": order.to_loc,
        "tariff": order.tariff
    }


@app.get("/orders")
def get_orders():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT order_id, name, phone, from_loc, to_loc, tariff, status FROM orders")
    rows = cursor.fetchall()
    conn.close()

    orders_list = []
    for row in rows:
        orders_list.append({
            "order_id": row[0],
            "name": row[1],
            "phone": row[2],
            "from": row[3],
            "to": row[4],
            "tariff": row[5],
            "status": row[6]
        })

    return {
        "total": len(orders_list),
        "orders": orders_list
    }