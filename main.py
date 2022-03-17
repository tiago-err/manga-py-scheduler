import os
from supabase import create_client, Client
import schedule
import time


def download_mangas(supabase_client):
    print("DOWNLOADING MANGAS")

    try:
        mangas = supabase.table("mangas").select("*").execute()
    except:
        return

    for manga in mangas.data:
        os.system(
            f"manga-py {manga['url']} --cbz -d /mangas --name '{manga['name']}'")


url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")

supabase: Client = create_client(url, key)
download_mangas(supabase)

schedule.every(int(os.environ.get("SCHEDULE"))
               ).minutes.do(download_mangas, supabase)
while True:
    schedule.run_pending()
    time.sleep(1)
