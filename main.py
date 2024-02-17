import requests

def ip_secret_address(api_key, ip_address):
    url = f"https://ipinfo.io/{ip_address}?token={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None
def main():
    api_key = "0a8f57aeb9c041"
    ip_address = input("Konum bilgisi için istenilen ip adresini giriniz: ")
    konum_bilgisi = ip_secret_address(api_key, ip_address)

    if konum_bilgisi:
        print(f"\n{ip_address} IP Adresinin Konum Bilgisi:")
        print(f"Şehir: {konum_bilgisi.get('city', 'Bilinmiyor')}")
        print(f"Ülke: {konum_bilgisi.get('country', 'Bilinmiyor')}")
        print(f"Konum: {konum_bilgisi.get('loc', 'Bilinmiyor')}")
    else:
        print("Konum bilgisi alınamadı. Lütfen IP adresinizi kontrol edin.")

if __name__ == "__main__":
    main()
