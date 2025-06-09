import requests
import json
import time

def fetch_data_post(url, payload_data, headers, retries=3, backoff_factor=0.5):
    """
    Mengambil data dari URL menggunakan metode POST dengan payload dan headers tertentu.
    Menerapkan mekanisme retry sederhana dengan exponential backoff.
    """
    for attempt in range(retries):
        try:
            response = requests.post(url, data=payload_data, headers=headers, timeout=20)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"Attempt {attempt + 1}/{retries}: HTTP error for {payload_data}: {http_err} - Status: {response.status_code} - Response: {response.text[:200]}")
            if response.status_code == 500 or response.status_code == 502 or response.status_code == 503 or response.status_code == 504 : # Server errors
                 time.sleep(backoff_factor * (2 ** attempt)) # Exponential backoff
            else: # Client errors, no retry needed
                 break
        except requests.exceptions.ConnectionError as conn_err:
            print(f"Attempt {attempt + 1}/{retries}: Connection error for {payload_data}: {conn_err}")
            time.sleep(backoff_factor * (2 ** attempt))
        except requests.exceptions.Timeout as timeout_err:
            print(f"Attempt {attempt + 1}/{retries}: Timeout error for {payload_data}: {timeout_err}")
            time.sleep(backoff_factor * (2 ** attempt))
        except requests.exceptions.RequestException as req_err:
            print(f"Attempt {attempt + 1}/{retries}: Request error for {payload_data}: {req_err}")
            break # Non-retryable for generic request exceptions
        except json.JSONDecodeError as json_err:
            print(f"Attempt {attempt + 1}/{retries}: JSON decode error from {url} for {payload_data}: {json_err} - Response: {response.text[:200]}")
            break 
    return None

# Daftar ID provinsi
province_ids = ["ALL", "11", "12", "13", "14", "15", "16", "17", "18", "19", 
                "21", "31", "32", "33", "34", "35", "36", "51", "52", "53", 
                "61", "62", "63", "64", "65", "71", "72", "73", "74", "75", 
                "76", "81", "82", "91", "92"] 

# URL target
url_chart_data = "https://sipsn.menlhk.go.id/sipsn/public/home/get_chart_data_sampah"
url_ajax_list = "https://sipsn.menlhk.go.id/sipsn/public/home/ajax_list"

# Headers untuk permintaan POST
headers = {
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1 Edg/136.0.0.0",
    "X-Requested-With": "XMLHttpRequest",
    "Referer": "https://sipsn.menlhk.go.id/sipsn/public/data/komposisi",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "en-US,en;q=0.9,id;q=0.8",
    "DNT": "1",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin"
}

tahun_data = ["ALL","2018","2019","2020","2021","2022","2023","2024"]
request_delay = 3  # Detik penundaan antar permintaan

def fetch_propinsi_name_from_ajax(prov_id, tahun, headers):
    """
    Mengambil nama provinsi menggunakan endpoint ajax_list
    """
    # Payload sesuai dengan format yang Anda berikan
    payload = (
        "draw=59&columns%5B0%5D%5Bdata%5D=tahun&columns%5B0%5D%5Bname%5D=&columns%5B0%5D%5Bsearchable%5D=true&columns%5B0%5D%5Borderable%5D=true&columns%5B0%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B0%5D%5Bsearch%5D%5Bregex%5D=false"
        "&columns%5B1%5D%5Bdata%5D=nama_propinsi&columns%5B1%5D%5Bname%5D=&columns%5B1%5D%5Bsearchable%5D=true&columns%5B1%5D%5Borderable%5D=true&columns%5B1%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B1%5D%5Bsearch%5D%5Bregex%5D=false"
        "&columns%5B2%5D%5Bdata%5D=nama_dati2&columns%5B2%5D%5Bname%5D=&columns%5B2%5D%5Bsearchable%5D=true&columns%5B2%5D%5Borderable%5D=true&columns%5B2%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B2%5D%5Bsearch%5D%5Bregex%5D=false"
        "&columns%5B3%5D%5Bdata%5D=sisa_makanan&columns%5B3%5D%5Bname%5D=&columns%5B3%5D%5Bsearchable%5D=true&columns%5B3%5D%5Borderable%5D=false&columns%5B3%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B3%5D%5Bsearch%5D%5Bregex%5D=false"
        "&columns%5B4%5D%5Bdata%5D=kayu_ranting&columns%5B4%5D%5Bname%5D=&columns%5B4%5D%5Bsearchable%5D=true&columns%5B4%5D%5Borderable%5D=false&columns%5B4%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B4%5D%5Bsearch%5D%5Bregex%5D=false"
        "&columns%5B5%5D%5Bdata%5D=kertas_karton&columns%5B5%5D%5Bname%5D=&columns%5B5%5D%5Bsearchable%5D=true&columns%5B5%5D%5Borderable%5D=false&columns%5B5%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B5%5D%5Bsearch%5D%5Bregex%5D=false"
        "&columns%5B6%5D%5Bdata%5D=plastik&columns%5B6%5D%5Bname%5D=&columns%5B6%5D%5Bsearchable%5D=true&columns%5B6%5D%5Borderable%5D=false&columns%5B6%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B6%5D%5Bsearch%5D%5Bregex%5D=false"
        "&columns%5B7%5D%5Bdata%5D=logam&columns%5B7%5D%5Bname%5D=&columns%5B7%5D%5Bsearchable%5D=true&columns%5B7%5D%5Borderable%5D=false&columns%5B7%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B7%5D%5Bsearch%5D%5Bregex%5D=false"
        "&columns%5B8%5D%5Bdata%5D=kain&columns%5B8%5D%5Bname%5D=&columns%5B8%5D%5Bsearchable%5D=true&columns%5B8%5D%5Borderable%5D=false&columns%5B8%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B8%5D%5Bsearch%5D%5Bregex%5D=false"
        "&columns%5B9%5D%5Bdata%5D=karet_kulit&columns%5B9%5D%5Bname%5D=&columns%5B9%5D%5Bsearchable%5D=true&columns%5B9%5D%5Borderable%5D=false&columns%5B9%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B9%5D%5Bsearch%5D%5Bregex%5D=false"
        "&columns%5B10%5D%5Bdata%5D=kaca&columns%5B10%5D%5Bname%5D=&columns%5B10%5D%5Bsearchable%5D=true&columns%5B10%5D%5Borderable%5D=false&columns%5B10%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B10%5D%5Bsearch%5D%5Bregex%5D=false"
        "&columns%5B11%5D%5Bdata%5D=lainnya&columns%5B11%5D%5Bname%5D=&columns%5B11%5D%5Bsearchable%5D=true&columns%5B11%5D%5Borderable%5D=false&columns%5B11%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B11%5D%5Bsearch%5D%5Bregex%5D=false"
        f"&start=0&length=10&search%5Bvalue%5D=&search%5Bregex%5D=false&jenis=komposisi&tahun={tahun}&id_propinsi={prov_id}&id_district=&id_das=0"
    )
    
    resp = fetch_data_post(url_ajax_list, payload, headers)
    if resp and isinstance(resp, dict) and resp.get("data") and len(resp["data"]) > 0:
        first_item = resp["data"][0]
        return first_item.get("nama_propinsi")
    return None

def fetch_districts_by_province(prov_id, tahun, headers):
    """
    Mengambil daftar kabupaten/kota berdasarkan provinsi dan tahun
    """
    payload = (
        "draw=1&columns%5B0%5D%5Bdata%5D=tahun&columns%5B0%5D%5Bname%5D=&columns%5B0%5D%5Bsearchable%5D=true&columns%5B0%5D%5Borderable%5D=true&columns%5B0%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B0%5D%5Bsearch%5D%5Bregex%5D=false"
        "&columns%5B1%5D%5Bdata%5D=nama_propinsi&columns%5B1%5D%5Bname%5D=&columns%5B1%5D%5Bsearchable%5D=true&columns%5B1%5D%5Borderable%5D=true&columns%5B1%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B1%5D%5Bsearch%5D%5Bregex%5D=false"
        "&columns%5B2%5D%5Bdata%5D=nama_dati2&columns%5B2%5D%5Bname%5D=&columns%5B2%5D%5Bsearchable%5D=true&columns%5B2%5D%5Borderable%5D=true&columns%5B2%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B2%5D%5Bsearch%5D%5Bregex%5D=false"
        f"&start=0&length=1000&search%5Bvalue%5D=&search%5Bregex%5D=false&jenis=komposisi&tahun={tahun}&id_propinsi={prov_id}&id_district=&id_das=0"
    )
    
    resp = fetch_data_post(url_ajax_list, payload, headers)
    if not resp or "data" not in resp:
        return []
    
    # Ekstrak daftar kabupaten/kota unik
    districts = {}
    for row in resp["data"]:
        district_name = row.get("nama_dati2")
        if district_name and district_name not in districts:
            districts[district_name] = {
                "nama": district_name,
                # Jika ada ID district di response, bisa ditambahkan di sini
                # "id": row.get("id_district") 
            }
    
    return list(districts.values())

def fetch_composition_data(prov_id, district_id, tahun, headers):
    """
    Mengambil data komposisi sampah untuk provinsi/kabupaten tertentu
    """
    # Jika district_id None atau kosong, ambil data level provinsi
    district_param = f"&id_district={district_id}" if district_id else "&id_district="
    
    payload = f"jenis=komposisi&tahun={tahun}&id_propinsi={prov_id}{district_param}"
    
    chart_data_raw = fetch_data_post(url_chart_data, payload, headers)
    
    # Handle respons dict
    if isinstance(chart_data_raw, dict) and 'data_series' in chart_data_raw:
        chart_data_raw = chart_data_raw['data_series']
    
    if chart_data_raw and isinstance(chart_data_raw, list):
        parsed_composition_data = []
        for item in chart_data_raw:
            jenis_sampah = item.get("name") 
            persentase_raw = item.get("value")

            if jenis_sampah is None or persentase_raw is None:
                continue

            try:
                persentase = float(persentase_raw)
            except (ValueError, TypeError):
                persentase = 0.0
            
            parsed_composition_data.append({
                "jenis_sampah": jenis_sampah,
                "persentase": persentase
            })
        
        return parsed_composition_data
    
    return None

# Main scraping process
all_results = []

print(f"Memulai proses scraping data komposisi sampah SIPSN...")

for tahun in tahun_data:
    print(f"\n=== MEMPROSES TAHUN {tahun} ===")
    
    tahun_results = {
        "tahun": tahun,
        "provinsi": []
    }
    
    for prov_id in province_ids:
        print(f"\nMemproses Provinsi ID: {prov_id} untuk tahun {tahun}")
        
        # Ambil nama provinsi
        nama_prop = fetch_propinsi_name_from_ajax(prov_id, tahun, headers)
        
        if not nama_prop:
            print(f"Gagal mendapatkan nama provinsi untuk ID: {prov_id}")
            continue
            
        print(f"Nama Provinsi: {nama_prop}")
        
        # Struktur data provinsi
        provinsi_data = {
            "provinsi_id": prov_id,
            "nama_provinsi": nama_prop,
            "komposisi_provinsi": [],
            "kabupaten_kota": [],
            "catatan_error": None
        }
        
        # 1. Ambil data komposisi level provinsi
        print(f"Mengambil data komposisi level provinsi...")
        comp_data = fetch_composition_data(prov_id, None, tahun, headers)
        if comp_data:
            provinsi_data["komposisi_provinsi"] = comp_data
            print(f"Data komposisi provinsi berhasil ({len(comp_data)} item)")
        else:
            print(f"Gagal mengambil data komposisi provinsi")
        
        time.sleep(request_delay)
        
        # 2. Ambil daftar kabupaten/kota
        print(f"Mengambil daftar kabupaten/kota...")
        districts = fetch_districts_by_province(prov_id, tahun, headers)
        print(f"Ditemukan {len(districts)} kabupaten/kota")
        
        time.sleep(request_delay)
        
        # 3. Untuk setiap kabupaten/kota, ambil data komposisinya
        for district in districts:
            district_name = district["nama"]
            print(f"  Memproses kabupaten/kota: {district_name}")
            
            # Struktur data kabupaten/kota
            district_data = {
                "nama_kabupaten_kota": district_name,
                "komposisi_sampah": [],
                "catatan_error": None
            }
            
            # Ambil data komposisi untuk kabupaten/kota ini
            # Catatan: Mungkin perlu ID district yang spesifik, 
            # tapi berdasarkan payload yang ada, sepertinya district kosong untuk agregat
            comp_data_district = fetch_composition_data(prov_id, "", tahun, headers)
            
            if comp_data_district:
                district_data["komposisi_sampah"] = comp_data_district
                print(f"    Data komposisi berhasil ({len(comp_data_district)} item)")
            else:
                district_data["catatan_error"] = "Gagal mengambil data komposisi"
                print(f"    Gagal mengambil data komposisi")
            
            provinsi_data["kabupaten_kota"].append(district_data)
            time.sleep(request_delay)
        
        tahun_results["provinsi"].append(provinsi_data)
        print(f"Selesai memproses Provinsi: {nama_prop}")
    
    all_results.append(tahun_results)
    print(f"\n=== SELESAI TAHUN {tahun} ===")

print(f"\nProses scraping selesai. Total {len(all_results)} tahun diproses.")

# Menyimpan hasil ke file JSON
output_filename = "sipsn_komposisi_sampah_lengkap.json"
try:
    with open(output_filename, "w", encoding="utf-8") as f:
        json.dump(all_results, f, ensure_ascii=False, indent=2)
    print(f"Data berhasil disimpan ke {output_filename}")
except IOError as e:
    print(f"Gagal menyimpan data ke file: {e}")

# Menyimpan ringkasan struktur data
summary = {
    "total_tahun": len(all_results),
    "struktur_data": {
        "tahun": "string",
        "provinsi": [
            {
                "provinsi_id": "string",
                "nama_provinsi": "string", 
                "komposisi_provinsi": [{"jenis_sampah": "string", "persentase": "float"}],
                "kabupaten_kota": [
                    {
                        "nama_kabupaten_kota": "string",
                        "komposisi_sampah": [{"jenis_sampah": "string", "persentase": "float"}],
                        "catatan_error": "string/null"
                    }
                ],
                "catatan_error": "string/null"
            }
        ]
    }
}

try:
    with open("struktur_data_summary.json", "w", encoding="utf-8") as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)
    print("Ringkasan struktur data disimpan ke struktur_data_summary.json")
except IOError as e:
    print(f"Gagal menyimpan ringkasan: {e}")