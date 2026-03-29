import os

API_ID = int(os.getenv("API_ID", "24638343"))
API_HASH = os.getenv("API_HASH", "c16b13b73c2f2473b8e3cbcf2ab1d200")
BOT_TOKEN = os.getenv("BOT_TOKEN", "8630166667:AAHae0Tj0wOo13JVQmKsNmZf7BOgt9FfeiU")

MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://aflahtbm:da9yNWm8Vhjqv1vl@cluster0.7mrpr1d.mongodb.net/?appName=Cluster0")
DB_NAME = "ProAutoFilterBot"

ADMINS = [int(x) for x in os.getenv("ADMINS", "6272165202").split()]
