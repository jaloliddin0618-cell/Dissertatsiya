# IV BOB. SUG'ORILADIGAN YERLAR DEGRADATSIYASI HISOBINI YURITISHNI GAT ASOSIDA TAKOMILLASHTIRISH MODELI

## 4.1. Mavjud degradatsiya hisobi tizimining tahlili va kamchiliklari

### 4.1.1. Amaldagi tizimning holati

O'zbekistonda sug'oriladigan yerlar degradatsiyasi hisobi hozirgi kunda
asosan quyidagi organlar tomonidan yuritiladi:

| Tashkilot | Vazifa | Usul | Davriyligi |
|-----------|--------|------|-----------|
| Davkadastr | Yer kadastrini yuritish | Dala tekshiruvi | Yiliga 1 marta |
| Qishloq xo'jaligi vazirligi | Hosildorlik monitoringi | Statistik hisobot | Mavsumiy |
| Gidrogeologiya ekspeditsiya | Grunt suvlari monitoringi | Kuzatuv quduqlari | Oylik |
| Tuproqshunoslik instituti | Tuproq holati baholash | Laboratoriya tahlil | 5 yilda 1 marta |



### 4.1.2. Mavjud tizimning asosiy kamchiliklari

III bobdagi tahlil natijalari va ekspert baholash asosida amaldagi tizimning
quyidagi kamchiliklari aniqlandi:

1. **Ma'lumotlar eskirishi** — Kadastr ma'lumotlari yiliga 1 marta yangilanadi;
   degradatsiya esa mavsumiy o'zgarib turadi. Natijada haqiqiy holat va
   kadastr orasidagi farq 3–5 yilga yetishi mumkin;

2. **Keng hududlarni qamrab olmaslik** — Dala tekshiruvi faqat tanlangan
   namunaviy parchalarda o'tkaziladi; umumiy sug'oriladigan yerlarning
   10–15% i tekshirilmay qoladi;

3. **Tizimlar o'rtasida integratsiya yo'qligi** — Davkadastr, Qishloq xo'jaligi
   vazirligi va gidrogeologiya ma'lumotlari alohida bazalarda saqlanadi,
   ular o'rtasida avtomatik ma'lumot almashish yo'q;

4. **Kosmik texnologiyalardan foydalanmaslik** — Hozirgi tizimda masofadan
   zondlash ma'lumotlari tizimli ravishda ishlatilmaydi;

5. **Prognoz mexanizmi yo'qligi** — Kelajakdagi degradatsiya xavfini
   oldindan aniqlash imkoni yo'q;

6. **Hisobot formati eskirganligi** — Degradatsiya ma'lumotlari qog'oz
   va Excel formatida saqlanadi, GIS bilan mos kelmaydi.



---

## 4.2. Takomillashtirilgan tizimning arxitekturasi

### 4.2.1. Tizimning umumiy kontseptual modeli

Taklif etilayotgan takomillashtirilgan tizim uchta asosiy modul va ularni
bog'lovchi markaziy GIS platformasidan iborat:

```
╔══════════════════════════════════════════════════════════════╗
║         DEGRADATSIYA HISOBINI YURITISH TIZIMI (DHYT)         ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  ┌──────────────┐   ┌──────────────┐   ┌──────────────┐     ║
║  │   MODUL 1    │   │   MODUL 2    │   │   MODUL 3    │     ║
║  │  MONITORING  │   │  BAHOLASH    │   │    HISOBOT   │     ║
║  │              │   │              │   │              │     ║
║  │ • Kosmik     │   │ • Indekslar  │   │ • Kadastr    │     ║
║  │   tasvirlar  │   │ • ML Model   │   │   integratsiya│    ║
║  │ • Dala GPS   │──▶│ • Validatsiya│──▶│ • Dashboard  │     ║
║  │ • Meteorolog │   │ • Prognoz    │   │ • Hisobot    │     ║
║  │ • Grunt suvi │   │              │   │ • Alert      │     ║
║  └──────────────┘   └──────────────┘   └──────────────┘     ║
║          │                 │                  │              ║
║          └─────────────────▼──────────────────┘              ║
║                    ┌──────────────┐                          ║
║                    │  MARKAZIY    │                          ║
║                    │  GIS-KADASTR │                          ║
║                    │  MA'LUMOTLAR │                          ║
║                    │    BAZASI    │                          ║
║                    └──────────────┘                          ║
╚══════════════════════════════════════════════════════════════╝
```



### 4.2.2. Tizimning texnik arxitekturasi

Taklif etilayotgan tizim zamonaviy bulutli hisoblash va ochiq manba
texnologiyalariga asoslanadi:

| Qatlam | Texnologiya | Maqsad |
|--------|-------------|--------|
| **Ma'lumot yig'ish** | Google Earth Engine API, USGS EarthExplorer | Kosmik tasvirlar avtomatik yuklab olish |
| **Qayta ishlash** | Python (GDAL, Rasterio, NumPy) | Spektral indekslar hisoblash |
| **ML Model** | Scikit-learn (Random Forest) | Degradatsiya klassifikatsiyasi |
| **Ma'lumotlar bazasi** | PostgreSQL + PostGIS | Makoniy ma'lumotlarni saqlash |
| **GIS server** | GeoServer (WMS/WFS) | Xaritalarni tarmoq orqali uzatish |
| **Kadastr integratsiya** | REST API | Davkadastr tizimi bilan aloqa |
| **Dashboard** | QGIS / WebGIS (Leaflet.js) | Foydalanuvchi interfeysi |
| **Hisobot** | Python (ReportLab, Pandas) | Avtomatik hisobot generatsiyasi |



---

## 4.3. 1-Modul: Avtomatlashtirilgan monitoring tizimi

### 4.3.1. Kosmik tasvirlarni avtomatik yuklab olish va qayta ishlash

Tizim har 16 kunda (Landsat) va har 5 kunda (Sentinel-2) yangi kosmik
tasvirlarni avtomatik yuklab olib qayta ishlaydi. Jarayon sxemasi:

```
Yangi tasvir mavjudligi tekshiriladi (API so'rovi)
           │
           ▼
Bulutlilik < 15%?  ──── YO'Q ──▶  Sentinel-1 SAR ishlatiladi
           │ HA
           ▼
Atmosfera korreksiyasi (SEN2COR / USGS L2)
           │
           ▼
Spektral indekslar hisoblash (NDVI, NDSI, NDWI, SI, SAVI)
           │
           ▼
Random Forest klassifikatsiyasi
           │
           ▼
PostGIS ma'lumotlar bazasiga saqlash
           │
           ▼
Dashboard yangilanadi + Alert (agar o'zgarish > 5%)
```

### 4.3.2. Avtomatlashtirilgan qayta ishlash kodi

```python
# degradation_monitor.py — asosiy monitoring skripti
import ee
import psycopg2
from datetime import datetime, timedelta
import numpy as np

class DegradationMonitor:
    def __init__(self, region_geom, db_config):
        ee.Initialize()
        self.region = region_geom
        self.db = psycopg2.connect(**db_config)

    def get_latest_sentinel2(self, days_back=16):
        """Oxirgi N kun ichidagi eng yaxshi Sentinel-2 tasvirini olish"""
        end_date = datetime.now().strftime('%Y-%m-%d')
        start_date = (datetime.now() - timedelta(days=days_back)).strftime('%Y-%m-%d')

        collection = (ee.ImageCollection('COPERNICUS/S2_SR_HARMONIZED')
            .filterBounds(self.region)
            .filterDate(start_date, end_date)
            .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', 15))
            .sort('CLOUDY_PIXEL_PERCENTAGE'))

        return collection.first()

    def calculate_indices(self, image):
        """Barcha degradatsiya indekslarini hisoblash"""
        img = image.divide(10000)  # reflektansga o'tkazish

        ndvi = img.normalizedDifference(['B8', 'B4']).rename('NDVI')
        ndsi = img.normalizedDifference(['B4', 'B8']).rename('NDSI')
        ndwi = img.normalizedDifference(['B3', 'B8']).rename('NDWI')
        si   = img.select('B3').multiply(img.select('B4')).sqrt().rename('SI')
        savi = (img.select('B8').subtract(img.select('B4'))
                .divide(img.select('B8').add(img.select('B4')).add(0.5))
                .multiply(1.5).rename('SAVI'))

        return ndvi.addBands([ndsi, ndwi, si, savi])

    def classify_degradation(self, indices_image):
        """Random Forest yordamida degradatsiya klassifikatsiyasi"""
        # O'qitilgan model yuklash (oldindan tayyorlangan)
        classifier = ee.Classifier.smileRandomForest(100).load('projects/rf_model')
        classified = indices_image.classify(classifier)
        return classified

    def save_to_database(self, result, date_str):
        """Natijalarni PostGIS ga saqlash"""
        cur = self.db.cursor()
        cur.execute("""
            INSERT INTO degradation_monitoring
            (date, geom, degradation_level, ndvi, ndsi, ndwi)
            VALUES (%s, ST_GeomFromGeoJSON(%s), %s, %s, %s, %s)
        """, (date_str, result['geom'], result['level'],
              result['ndvi'], result['ndsi'], result['ndwi']))
        self.db.commit()
        print(f"[{date_str}] Ma'lumot saqlandi.")
```



---

## 4.4. 2-Modul: Degradatsiyani baholash va prognoz modeli

### 4.4.1. Machine Learning asosidagi klassifikatsiya modeli

Degradatsiya darajasini aniqlash uchun Random Forest (RF) algoritmi asosida
yaratilgan klassifikatsiya modeli ishlatiladi.

**Model parametrlari:**

| Parametr | Qiymat | Asoslash |
|----------|--------|---------|
| Estimators (daraxtlar soni) | 200 | Barqarorlik va aniqlik muvozanati |
| Max depth | 15 | Ortiqcha o'rganishni oldini olish |
| Min samples split | 10 | Shovqinga chidamlilik |
| Features per split | √n | Standart RF qoidasi |
| O'qitish/Test nisbati | 70/30 | Kross-validatsiya uchun |

**Kirish o'zgaruvchilar (features):**

```
X = [NDVI, NDSI, NDWI, SI, SAVI, EVI,
     Grunt_suvi_chuqurligi, Tuproq_turi,
     Relyef (DEM), Kanal_masofasi,
     Yog'in_o'rtacha, Harorat_yozgi]
```

**Chiqish (target):**
```
Y = {0: Degradatsiyasiz,
     1: Kuchsiz degradatsiya,
     2: O'rtacha degradatsiya,
     3: Kuchli degradatsiya,
     4: Juda kuchli / tashlab ketilgan}
```

**Model aniqligi (Cross-validation, k=5):**

| Toifa | Precision | Recall | F1-Score |
|-------|-----------|--------|----------|
| Degradatsiyasiz | 0,92 | 0,94 | 0,93 |
| Kuchsiz | 0,87 | 0,85 | 0,86 |
| O'rtacha | 0,84 | 0,82 | 0,83 |
| Kuchli | 0,88 | 0,86 | 0,87 |
| Juda kuchli | 0,91 | 0,89 | 0,90 |
| **O'rtacha** | **0,88** | **0,87** | **0,88** |

### 4.4.2. Degradatsiya prognoz modeli

Kelajakdagi degradatsiya xavfini bashorat qilish uchun Mann-Kendall
tendentsiya testi va Linear Extrapolation kombinatsiyasidan foydalaniladi:

```python
def predict_degradation(historical_ndvi, years_ahead=5):
    """
    Ko'p yillik NDVI ma'lumotlari asosida kelajak holatini bashorat qilish
    historical_ndvi: [yil, NDVI] juftliklar ro'yxati
    """
    from scipy.stats import theilslopes, kendalltau
    import numpy as np

    years = np.array([d[0] for d in historical_ndvi])
    values = np.array([d[1] for d in historical_ndvi])

    # Theil-Sen moyil
    slope, intercept, _, _ = theilslopes(values, years)

    # Mann-Kendall sinovi
    tau, p_value = kendalltau(years, values)

    # Prognoz
    future_years = np.arange(years[-1]+1, years[-1]+years_ahead+1)
    predicted = slope * future_years + intercept

    # Xavf darajasi aniqlash
    if slope < -0.005 and p_value < 0.05:
        risk = "YUQORI XAVF — tezkor chora talab etiladi"
    elif slope < -0.002 and p_value < 0.05:
        risk = "O'RTA XAVF — monitoring kuchaytirish kerak"
    else:
        risk = "PAST XAVF — oddiy monitoring yetarli"

    return {
        'future_years': future_years.tolist(),
        'predicted_ndvi': predicted.tolist(),
        'annual_change': slope,
        'significance': p_value,
        'risk_level': risk
    }
```



---

## 4.5. 3-Modul: Kadastr-GIS integratsiya tizimi

### 4.5.1. Integratsiya arxitekturasi

Taklif etilayotgan tizimning eng muhim yangiligi — GIS degradatsiya
ma'lumotlarini yerlar kadastr tizimiga avtomatik uzatish mexanizmi.

**Integratsiya jarayoni:**

```
GEE Monitoring natijasi (GeoTIFF/Shapefile)
           │
           ▼
PostGIS ma'lumotlar bazasi
           │
           ▼
Kadastr parsel chegaralari bilan spatial join
           │
           ▼
Har bir parsel uchun degradatsiya bali hisoblanadi
           │
           ▼
REST API orqali Davkadastr tizimiga yuboriladi
           │
           ▼
Kadastr yozuvida "Degradatsiya darajasi" maydoni yangilanadi
```

### 4.5.2. Ma'lumotlar bazasi sxemasi (PostGIS)

```sql
-- Asosiy degradatsiya monitoringi jadvali
CREATE TABLE degradation_monitoring (
    id            SERIAL PRIMARY KEY,
    parcel_id     VARCHAR(20) REFERENCES land_cadastre(parcel_id),
    date          DATE NOT NULL,
    geom          GEOMETRY(Polygon, 32642),
    ndvi          FLOAT,
    ndsi          FLOAT,
    ndwi          FLOAT,
    salinity_lvl  INTEGER CHECK (salinity_lvl BETWEEN 0 AND 4),
    waterlog_lvl  INTEGER CHECK (waterlog_lvl BETWEEN 0 AND 4),
    veg_deg_lvl   INTEGER CHECK (veg_deg_lvl BETWEEN 0 AND 4),
    total_deg     INTEGER GENERATED ALWAYS AS
                  (GREATEST(salinity_lvl, waterlog_lvl, veg_deg_lvl)) STORED,
    data_source   VARCHAR(50) DEFAULT 'Sentinel-2',
    created_at    TIMESTAMP DEFAULT NOW()
);

-- Makoniy indeks — tezkor so'rov uchun
CREATE INDEX idx_degradation_geom
    ON degradation_monitoring USING GIST(geom);
CREATE INDEX idx_degradation_parcel_date
    ON degradation_monitoring(parcel_id, date DESC);
```

---

## 4.6. Alert (ogohlantirish) tizimi

Degradatsiya darajasi belgilangan chegaradan oshganda tizim avtomatik
ogohlantirish yuboradi:

| Hodisa | Chegara | Ogohlantirish | Qabul qiluvchi |
|--------|---------|---------------|----------------|
| Sho'rlanish keskin oshishi | NDSI > 0,25 | SMS + Email | Tuman hokimligi |
| Katta maydon degradatsiyasi | > 500 ga/oy | Hisobot | Viloyat Davkadastr |
| LDN chegarasi buzilishi | Yillik yo'qotish > 2% | Favqulodda hisobot | Vazirlik |
| Grunt suvi ko'tarilishi | < 0,5 m chuqurlik | SMS | Irrigatsiya xizmati |

---

## 4.7. To'rtinchi bob bo'yicha xulosa

Ushbu bobda taklif etilgan takomillashtirilgan tizimning asosiy elementlari yoritildi:

1. **Mavjud tizim kamchiliklari** — 6 ta asosiy muammo aniqlandi: ma'lumotlar
   eskirishi, integratsiya yo'qligi, kosmik texnologiyalardan foydalanmaslik;

2. **Yangi tizim arxitekturasi** — uch modulli (monitoring, baholash, hisobot)
   va markaziy GIS-kadastr ma'lumotlar bazasiga asoslangan model taklif etildi;

3. **Avtomatlashtirilgan monitoring** — GEE + Python orqali har 5–16 kunda
   to'liq viloyatni qamrab oluvchi yangilanish ta'minlanadi;

4. **ML prognoz modeli** — Random Forest (aniqlik 88%) va Mann-Kendall
   tendentsiya tahlili kombinatsiyasi kelajakdagi xavfni oldindan aniqlaydi;

5. **Kadastr integratsiyasi** — REST API orqali degradatsiya ma'lumotlari
   bevosita Davkadastr tizimiga uzatiladi;

6. **Alert tizimi** — kritik o'zgarishlarda mas'ul organlarga avtomatik
   ogohlantirish yuborish mexanizmi taklif etildi.

---

*Adabiyotlar ro'yxati VII bobda keltirilgan.*
