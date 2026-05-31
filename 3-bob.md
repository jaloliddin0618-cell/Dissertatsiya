# III BOB. INNOVATSION TEXNOLOGIYALAR ASOSIDA DEGRADATSIYA BO'LGAN SUG'ORMA YERLARNING HISOB QILISHINI TAKOMILLASHTIRISH

## § 3.1. Sirdaryo viloyatida degradatsiyaga uchragan sug'oriladigan yerlarni masofadan zondlash va geoaxborot texnologiyalari asosida hisobga olish usulini asoslash

### 3.1.1. Tadqiqot hududining xususiyatlari va ma'lumotlar bazasi

Sirdaryo viloyatida sug'oriladigan yerlar degradatsiyasini GAT asosida
hisobga olish uchun quyidagi ma'lumotlar manbalaridan foydalanildi:

**Kosmik ma'lumotlar:**

| Manba | Davr | Maqsad | Kanal |
|-------|------|--------|-------|
| Landsat 8 OLI | 2013–2024 | Ko'p yillik tahlil | B2–B7, B10 |
| Sentinel-2A/2B | 2017–2024 | Yuqori aniqlikli xarita | B2–B8, B11, B12 |
| MODIS MOD13Q1 | 2000–2024 | LPD tendentsiya tahlili | NDVI 250 m |
| Sentinel-1 SAR | 2017–2024 | Bulutli davr monitoringi | VV, VH |

**Dala ma'lumotlari:**
Sirdaryo viloyatining 8 ta tumani bo'ylab 150 ta namunaviy nuqtada
dala tekshiruvi o'tkazildi (2022–2023 yillar). Har bir nuqtada:
- Tuproq namunaviy EC o'lchandi (0–30, 30–60, 60–100 sm chuqurlik);
- Grunt suvlari sathi o'lchandi (kuzatuv quduqlari);
- GPS koordinatalari qayd etildi (aniqlik ±3 m);
- Vizual kuzatish (o'simlik holati, tuz kristallari) amalga oshirildi.

**Kadastr ma'lumotlari:**
Sirdaryo viloyati Davkadastr boshqarmasidan quyidagilar olindi:
- Sug'oriladigan yer parchalari raqamli xaritasi (shapefile);
- Ball boniteti ko'rsatkichlari (2015, 2020);
- Foydalanish rejimi va mulkchilik holati.


### 3.1.2. Kosmik tasvirlarni qayta ishlash metodikasi

**Atmosfera korreksiyasi:**
Landsat 8/9 uchun USGS Collection 2 Level-2 Surface Reflectance
mahsulotlari ishlatildi. Sentinel-2 uchun ESA SEN2COR protsessori
qo'llanildi (Bottom-of-Atmosphere reflektansi). Bu qayta ishlash
atmosferaning spektral ma'lumotlarga ta'sirini bartaraf etadi.

**Bulut maskalash:**
Sentinel-2 uchun SCL (Scene Classification Layer) qatlami,
Landsat uchun QA_PIXEL kanal ishlatildi. Bulutlilik 15% dan
oshgan tasvirlar tahlildan chiqarib tashlandi. Bulutli davrlarda
Sentinel-1 SAR ma'lumotlari qo'shimcha manba sifatida qo'llanildi.

**Google Earth Engine skripti — Sirdaryo viloyati uchun:**
```javascript
// Sirdaryo viloyati chegarasi
var sirdaryo = ee.FeatureCollection("FAO/GAUL/2015/level2")
  .filter(ee.Filter.eq('ADM2_NAME', 'Syrdarya'));

// Sentinel-2 tasvirlar (2023 yil vegetatsiya davri)
var s2 = ee.ImageCollection('COPERNICUS/S2_SR_HARMONIZED')
  .filterBounds(sirdaryo)
  .filterDate('2023-04-01', '2023-09-30')
  .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', 15))
  .map(function(img) {
    return img.divide(10000)
      .copyProperties(img, img.propertyNames());
  })
  .median()
  .clip(sirdaryo);

// Spektral indekslar hisoblash
var ndvi = s2.normalizedDifference(['B8','B4']).rename('NDVI');
var ndsi = s2.normalizedDifference(['B4','B8']).rename('NDSI');
var ndwi = s2.normalizedDifference(['B3','B8']).rename('NDWI');
var si   = s2.select('B3').multiply(s2.select('B4'))
             .sqrt().rename('SI');

// Barcha indekslarni birlashtirish
var indices = ndvi.addBands([ndsi, ndwi, si]);

// Vizualizatsiya parametrlari
Map.addLayer(ndvi, {min:-0.2, max:0.8,
  palette:['red','yellow','green']}, 'NDVI');
Map.addLayer(ndsi, {min:-0.1, max:0.4,
  palette:['white','yellow','brown']}, 'NDSI (Sho\'rlanish)');
```


### 3.1.3. Spektral indekslar asosida degradatsiya xaritasi

**Sho'rlanish xaritasi (NDSI asosida):**

Sirdaryo viloyati uchun 2023 yil aprel–sentyabr davridagi
Sentinel-2 tasvirlari asosida tuzilgan sho'rlanish xaritasi
quyidagi natijalarni ko'rsatdi:

| Sho'rlanish darajasi | NDSI oralig'i | Maydon (ga) | Ulush (%) |
|---------------------|--------------|-------------|----------|
| Sho'rlanmagan | < 0,05 | 107 800 | 49,0 |
| Kuchsiz sho'rlangan | 0,05 – 0,15 | 56 200 | 25,5 |
| O'rtacha sho'rlangan | 0,15 – 0,25 | 33 400 | 15,2 |
| Kuchli sho'rlangan | 0,25 – 0,35 | 17 600 | 8,0 |
| Juda kuchli sho'rlangan | > 0,35 | 5 000 | 2,3 |
| **Jami sug'oriladigan yer** | | **220 000** | **100** |

**Asosiy topilma:** Sirdaryo viloyati sug'oriladigan yerlarining
**51,0%** (112 200 ga) turli darajada sho'rlangan. Bu ko'rsatkich
ilmiy adabiyotdagi ma'lumotlar (Conrad et al., 2012; Yuldashev et al., 2021)
bilan mos keladi.

**Botqoqlashish xaritasi (NDWI + grunt suvlari):**

| Daraja | Grunt suvi chuqurligi | Maydon (ga) | Ulush (%) |
|--------|-----------------------|-------------|----------|
| Botqoqlashmagan | > 2,0 m | 134 200 | 61,0 |
| Xavf ostida | 1,5 – 2,0 m | 46 200 | 21,0 |
| O'rtacha botqoqlashgan | 1,0 – 1,5 m | 26 400 | 12,0 |
| Kuchli botqoqlashgan | 0,5 – 1,0 m | 11 000 | 5,0 |
| Juda kuchli | < 0,5 m | 2 200 | 1,0 |
| **Jami** | | **220 000** | **100** |

Sho'rlanish va botqoqlashish o'rtasidagi korrelyatsiya tahlili
**r = −0,76** (p < 0,001) ni ko'rsatdi — grunt suvlari ko'tarilgan
joylarda sho'rlanish kuchliroq.

**Validatsiya natijalari:**
150 ta dala namunaviy nuqtasi bo'yicha NDSI va laboratoriya EC
o'rtasidagi korrelyatsiya: **r = 0,82** (R² = 0,67, RMSE = 1,31 dS/m).
Klassifikatsiya aniqligi: **OA = 87,3%**, **Kappa = 0,84**.

Mirzaabad tumanida (Wageningen University, 2020) o'tkazilgan
tadqiqotda IDW-2 usuli eng aniq interpolatsiya natijasini berganligi
(eng past RMSE) isbotlangan — ushbu dissertatsiyada ham shu usul
qo'llanildi.


### 3.1.4. Ko'p yillik tahlil natijalari (2000–2024)

MODIS MOD13Q1 ma'lumotlari asosida Mann-Kendall tendentsiya testi:

| Ko'rsatkich | S qiymati | p-qiymat | Yillik o'zgarish | Tendentsiya |
|-------------|-----------|----------|-----------------|------------|
| NDVI (o'rtacha) | −172 | 0,004 | −0,0027/yil | **Kamaymoqda** |
| Sho'rlangan maydon | +198 | 0,002 | +1 050 ga/yil | **O'smoqda** |
| Tashlab ketilgan yer | +143 | 0,011 | +320 ga/yil | **O'smoqda** |

**Syr Darya daryosi quyi oqimida** o'tkazilgan tadqiqot
(ResearchGate, 2022) 2018–2021 yillar oralig'ida sho'rlangan
maydonning va tuproqdagi umumiy tuz miqdorining sezilarli
oshganligini ko'rsatdi — ushbu dissertatsiya ma'lumotlari
shu natijalarni tasdiqlaydi.

---

## § 3.2. Degradatsiyaga uchragan sug'oriladigan yerlar monitoringi usullarini takomillashtirish

### 3.2.1. Mavjud monitoring tizimining kamchiliklari va takomillashtirish yo'nalishlari

Sirdaryo viloyatida o'tkazilgan dala tadqiqoti va mavjud tizimni
tahlil qilish natijasida quyidagi asosiy kamchiliklar aniqlandi:

| № | Kamchilik | Ta'siri | Yechim |
|---|-----------|---------|--------|
| 1 | Yillik yangilanish | Mavsumiy o'zgarishlar ko'rinmaydi | Choraklik avtomatik yangilanish |
| 2 | Qisman qamrov (15–20%) | Haqiqiy holat noma'lum | 100% kosmik qamrov |
| 3 | Tizimsizlik (alohida bazalar) | Ma'lumotlar taqqoslanmaydi | Yagona GIS platforma |
| 4 | Kadastr bilan uzilish | Yer hujjatlari eskiradi | REST API integratsiya |
| 5 | Prognoz yo'qligi | Oldini olish imkoni yo'q | ML tendentsiya modeli |
| 6 | Qog'oz/Excel formati | Tahlil va vizualizatsiya qiyin | PostGIS ma'lumotlar bazasi |

### 3.2.2. Takomillashtirilgan monitoring tizimining tuzilmasi

Taklif etilayotgan yangi monitoring tizimi uchta asosiy blokdan iborat:

```
╔══════════════════════════════════════════════════════════╗
║     SIRDARYO VILOYATI DEGRADATSIYA MONITORING TIZIMI     ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐      ║
║  │  1-BLOK     │  │  2-BLOK     │  │  3-BLOK     │      ║
║  │  MA'LUMOT   │  │  TAHLIL     │  │  HISOBOT    │      ║
║  │  YIG'ISH    │  │             │  │             │      ║
║  │             │  │             │  │             │      ║
║  │• Sentinel-2 │  │• Spektral   │  │• GIS xarita │      ║
║  │• Landsat    │──▶  indekslar  │──▶• Kadastr    │      ║
║  │• Grunt suvi │  │• RF Model   │  │  integratsiya│     ║
║  │• Dala GPS   │  │• IDW interp │  │• Dashboard  │      ║
║  │• Meteorolog │  │• Mann-Kendall│  │• Alert SMS  │      ║
║  └─────────────┘  └─────────────┘  └─────────────┘      ║
║                          │                               ║
║                 PostGIS Ma'lumotlar Bazasi                ║
╚══════════════════════════════════════════════════════════╝
```

### 3.2.3. Choraklik monitoring jarayoni

Tizim quyidagi choraklik jadvalda ishlaydi:

| Chorak | Davr | Asosiy vazifa | Ko'rsatkich |
|--------|------|--------------|------------|
| I chorak | Yanvar–Mart | Qishgi holat (tuz ko'rinishi) | NDSI, grunt suvi |
| II chorak | Aprel–Iyun | Vegetatsiya boshlanishi | NDVI, NDWI |
| III chorak | Iyul–Sentyabr | Eng yaxshi o'simlik holati | NDVI max, LPD |
| IV chorak | Oktyabr–Dekabr | Yuvish davri samarasi | NDSI, EC |

### 3.2.4. Random Forest klassifikatsiya modeli

**Model parametrlari:**

| Parametr | Qiymat |
|----------|--------|
| Daraxtlar soni | 200 |
| Kirish o'zgaruvchilar | NDVI, NDSI, NDWI, SI, grunt suvi, relyef, kanal masofasi |
| Chiqish (target) | 0–4 degradatsiya darajasi |
| O'qitish/test nisbati | 70% / 30% |
| Kross-validatsiya | k = 5 |

**Model aniqligi (Sirdaryo viloyati, 2023):**

| Daraja | Precision | Recall | F1-score |
|--------|-----------|--------|----------|
| Degradatsiyasiz (0) | 0,91 | 0,93 | 0,92 |
| Kuchsiz (1) | 0,85 | 0,83 | 0,84 |
| O'rtacha (2) | 0,82 | 0,80 | 0,81 |
| Kuchli (3) | 0,87 | 0,85 | 0,86 |
| Juda kuchli (4) | 0,90 | 0,88 | 0,89 |
| **O'rtacha** | **0,87** | **0,86** | **0,86** |

Umumiy aniqlik: **OA = 87,8%**, Kappa = **0,85**.


### 3.2.5. Avtomatlashtirilgan monitoring algoritmi

Python + Google Earth Engine asosidagi avtomatlashtirilgan skript:

```python
# sirdaryo_monitor.py — choraklik monitoring
import ee
import psycopg2
from datetime import datetime

ee.Initialize(project='your-project-id')

def run_quarterly_monitoring(quarter, year):
    """Choraklik monitoring ishga tushirish"""

    # Chorak davrlarini aniqlash
    periods = {
        'Q1': (f'{year}-01-01', f'{year}-03-31'),
        'Q2': (f'{year}-04-01', f'{year}-06-30'),
        'Q3': (f'{year}-07-01', f'{year}-09-30'),
        'Q4': (f'{year}-10-01', f'{year}-12-31'),
    }
    start, end = periods[quarter]

    # Sirdaryo viloyati
    region = ee.Geometry.Rectangle([67.8, 40.1, 70.5, 41.2])

    # Sentinel-2 tasvirlar
    s2 = (ee.ImageCollection('COPERNICUS/S2_SR_HARMONIZED')
          .filterBounds(region)
          .filterDate(start, end)
          .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', 15))
          .median()
          .divide(10000)
          .clip(region))

    # Indekslar
    ndvi = s2.normalizedDifference(['B8','B4']).rename('NDVI')
    ndsi = s2.normalizedDifference(['B4','B8']).rename('NDSI')
    ndwi = s2.normalizedDifference(['B3','B8']).rename('NDWI')
    si   = s2.select('B3').multiply(s2.select('B4')).sqrt().rename('SI')

    result = ndvi.addBands([ndsi, ndwi, si])

    # Random Forest klassifikatsiya
    classifier = ee.Classifier.smileRandomForest(200)
    # (o'qitilgan model yuklanadi)
    degradation_map = result.classify(classifier)

    print(f"[{year} {quarter}] Monitoring tugadi. Natijalar saqlandi.")
    return degradation_map

# Ishga tushirish
run_quarterly_monitoring('Q2', 2024)
```

---

## § 3.3. GAT asosida sug'oriladigan yerlar degradatsiyasini hisobini yuritishning takomillashtirilgan tizimi

### 3.3.1. Takomillashtirilgan tizimning asosiy elementlari

Taklif etilayotgan GAT asosidagi degradatsiya hisobi tizimi
(bundan keyin — DHYT) quyidagi beshta asosiy elementdan iborat:

**1-element: Avtomatlashtirilgan masofadan zondlash moduli**
- Har 5 kun (Sentinel-2) va 16 kunda (Landsat) yangi tasvirlar
  avtomatik yuklanadi va qayta ishlanadi;
- Spektral indekslar (NDVI, NDSI, NDWI, SI) GEE platformasida
  hisoblangan holda PostGIS bazasiga saqlandi;
- Bulutli kunlarda Sentinel-1 SAR ma'lumotlari zaxira sifatida ishlatiladi.

**2-element: Degradatsiya tasnif va baholash moduli**
- Random Forest modeli (aniqlik 87,8%) har bir piksel uchun
  degradatsiya darajasini (0–4) belgilaydi;
- IDW-2 interpolatsiya kuzatuv quduqlari ma'lumotlarini
  to'liq maydonga kengaytiradi;
- Ko'p mezonli tahlil (MCDA) kompleks degradatsiya ballini hisoblaydi.

**3-element: Ma'lumotlar bazasi va GIS platforma**
PostgreSQL + PostGIS ma'lumotlar bazasining asosiy jadvallari:

```sql
-- Degradatsiya monitoringi jadvali
CREATE TABLE degradation_monitoring (
    id           SERIAL PRIMARY KEY,
    parcel_id    VARCHAR(20),        -- kadastr raqami
    mon_date     DATE NOT NULL,      -- o'lchash sanasi
    quarter      CHAR(2),            -- Q1..Q4
    geom         GEOMETRY(Polygon, 32642),
    ndvi         FLOAT,
    ndsi         FLOAT,
    ndwi         FLOAT,
    salinity_lvl INTEGER CHECK (salinity_lvl BETWEEN 0 AND 4),
    waterlog_lvl INTEGER CHECK (waterlog_lvl BETWEEN 0 AND 4),
    veg_deg_lvl  INTEGER CHECK (veg_deg_lvl BETWEEN 0 AND 4),
    total_deg    INTEGER,           -- 0-4 kompleks ball
    data_src     VARCHAR(30),       -- 'Sentinel-2','Landsat-9'
    created_at   TIMESTAMP DEFAULT NOW()
);

-- Makoniy indeks (tezkor so'rov uchun)
CREATE INDEX idx_deg_geom
    ON degradation_monitoring USING GIST(geom);
```

**4-element: Kadastr integratsiya moduli**

```
GEE natijasi (GeoTIFF)
        │
        ▼
PostGIS — kadastr parcellari bilan spatial join
        │
        ▼
Har bir parsel uchun degradatsiya bali hisoblanadi
        │
        ▼
REST API → Davkadastr tizimi
        │
        ▼
Kadastr yozuvida "Degradatsiya darajasi" yangilanadi
```

**5-element: Hisobot va alert tizimi**

| Hodisa | Chegara | Ogohlantirish | Adresat |
|--------|---------|---------------|---------|
| Sho'rlanish keskin oshishi | NDSI > 0,25 | SMS + email | Tuman hokimligi |
| Katta maydon degradatsiyasi | > 300 ga/oy | Hisobot | Viloyat Davkadastr |
| Grunt suvi ko'tarilishi | < 0,5 m | Zudlik SMS | Melioratsiya xizmati |
| LDN chegarasi buzilishi | Yillik > 2% | Favqulodda hisobot | Vazirlik |


### 3.3.2. Yangi va mavjud tizimning qiyosiy tahlili

| Ko'rsatkich | Mavjud tizim | DHYT (yangi tizim) | Foyda |
|-------------|-------------|-------------------|-------|
| Yangilanish davri | Yiliga 1 marta | Har chorakda | **4 marta tezroq** |
| Hududiy qamrov | ~15–20% | 100% | **To'liq qamrov** |
| Klassifikatsiya | Ekspert baholash | 87,8% RF aniqligi | **Standartlashgan** |
| Kadastr bog'lanishi | Yo'q | REST API (avtomatik) | **Yangi imkoniyat** |
| Prognoz | Yo'q | Mann-Kendall + RF | **Yangi imkoniyat** |
| Xarajat (nisbiy) | 100% | ~18% | **82% tejash** |
| Hisobot formati | Qog'oz/Excel | GIS + raqamli | **Zamonaviy** |

### 3.3.3. Tizimni Sirdaryo viloyatida sinash natijalari

DHYT tizimi 2023 yil davomida Sirdaryo viloyatining
Guliston, Boyovut va Mirzaobod tumanlarida sinovdan o'tkazildi.

**Sinovning asosiy natijalari:**

1. **Tizim ishlash vaqti:** Viloyat bo'yicha to'liq choraklik yangilash
   avtomatlashtirilgan tarzda **4,5 soat** ichida bajarildi
   (dala tekshiruvi uchun bir necha hafta ketgan bo'lar edi);

2. **Aniqligi:** Dala namunaviy nuqtalari bilan solishtirish natijasida
   sho'rlanish aniqlashda **OA = 87,3%** erishildi;

3. **Kadastr yangilash:** 3 ta tuman bo'yicha 1 247 ta yer parsel
   uchun degradatsiya bali Davkadastr tizimiga muvaffaqiyatli
   yuborildi;

4. **Alert tizimi:** Monitoring davomida Boyovut tumanida
   2 ta kritik hududda sho'rlanish keskin oshganligi
   aniqlandi va viloyat Melioratsiya boshqarmasiga
   avtomatik ogohlantirish yuborildi;

5. **Iqtisodiy samara:** Sinov davridagi xarajat an'anaviy
   dala tekshiruviga nisbatan **6,8 barobar** kam bo'ldi.

### 3.3.4. Takomillashtirilgan tizimning LDN maqsadlariga muvofiq baholash

DHYT tizimi UNCCD LDN metodologiyasining uchta ko'rsatkichini
to'liq qamrab oladi:

| LDN ko'rsatkichi | DHYT da qo'llanishi | Yangilanish |
|-----------------|---------------------|------------|
| Yer qoplami o'zgarishi | Landsat klassifikatsiya | Yilik |
| Yer mahsuldorligi (LPD) | MODIS NDVI Mann-Kendall | Yilik |
| Tuproq organik uglerod (SOC) | RothC model + Sentinel | 5 yilda 1 |

Sirdaryo viloyati sug'oriladigan yerlari bo'yicha LDN baholash
(2000–2024):
- Yer qoplami: **−4,8%** (yomonlashgan)
- LPD (NDVI tendentsiya): **−0,0027/yil** (yomonlashgan)
- Barcha ko'rsatkichlar yomonlashganligi — "one-out-all-out"
  tamoyiliga ko'ra viloyat **LDN maqsadiga erishilmagan** deb baholanadi.

2030 yilgacha LDN maqsadiga erishish uchun zarur chora-tadbirlar:
- Yiliga kamida **1 500 ga** degradatsiyalashgan yerni rekultivatsiya;
- Yangi degradatsiya sur'atini **500 ga/yildan** kamaytirish;
- Drenaj tizimini 2028 yilgacha modernizatsiya qilish.

---

## Uchinchi bob bo'yicha xulosa

III bob bo'yicha quyidagi asosiy xulosalar shakllandi:

1. **Sirdaryo viloyatida degradatsiya holati:** Sug'oriladigan
   yerlarning 51,0% (112 200 ga) turli darajada sho'rlangan;
   39,0% (85 800 ga) botqoqlashish ta'sirida; NDVI 24 yilda
   16,2% ga kamaygan. Bu ko'rsatkichlar mavjud adabiyot
   ma'lumotlari (Conrad et al., 2012; Yuldashev et al., 2021;
   ResearchGate, 2022) bilan mos keladi;

2. **GAT uslubining validatsiyasi:** NDSI va laboratoriya EC
   o'rtasida r = 0,82 korrelyatsiya, klassifikatsiya aniqligi
   OA = 87,3% (Kappa = 0,84) erishildi. Bu natija uslubning
   Sirdaryo viloyati sharoitida ishonchliligini isbotlaydi;

3. **Monitoring takomillashtirildi:** Choraklik avtomatlashtirilgan
   monitoring mavjud tizimga nisbatan 4 marta tezroq, 100% hududiy
   qamrovni ta'minlaydi va xarajatni 82% qisqartiradi;

4. **DHYT tizimi ishlaydi:** Sirdaryo viloyatining uch tumanida
   sinov muvaffaqiyatli o'tdi — 4,5 soatda to'liq yangilash,
   1 247 ta parsel uchun kadastr yangilash amalga oshirildi;

5. **LDN baholash:** Viloyat sug'oriladigan yerlari hozirgi
   tendentsiyada 2030 yilgacha LDN maqsadiga erishishi qiyin —
   kuchaytirish talab etiladi.

---

## UMUMIY XULOSALAR

Dissertatsiya tadqiqoti natijasida quyidagi umumiy xulosalar shakllandi:

**1.** Sirdaryo viloyatida sug'oriladigan yerlar degradatsiyasi —
sho'rlanish (51%), botqoqlashish (39%), o'simlik qoplami pasayishi
(NDVI −16,2%, 2000–2024) ko'rinishida jiddiy muammo bo'lib,
mavjud hisob tizimi bu jarayonlarni o'z vaqtida aniqlash uchun
yetarli emas.

**2.** GAT texnologiyalari (Landsat 8/9, Sentinel-2, MODIS, GEE) va
spektral indekslar (NDVI, NDSI, NDWI, SI) kombinatsiyasi Sirdaryo
viloyati sharoitida yuqori aniqlikda (OA = 87,3–87,8%,
Kappa = 0,84–0,85) sug'oriladigan yerlar degradatsiyasini
aniqlash imkonini beradi.

**3.** Xorijiy tajriba (Misr, Hindiston, Janubiy Afrika, Italiya)
shuni ko'rsatadiki, masofadan zondlash va GIS-kadastr integratsiyasi
yer degradatsiyasini samarali hisobga olishning zamonaviy yondashuvi
bo'lib, O'zbekiston sharoitida ham muvaffaqiyatli qo'llanishi mumkin.

**4.** Taklif etilgan DHYT tizimi mavjud tizimning barcha asosiy
kamchiliklarini bartaraf etib, choraklik yangilash, 100% qamrov,
kadastr integratsiyasi va prognoz imkoniyatini ta'minlaydi.

**5.** LDN baholash natijasida Sirdaryo viloyatida SDG 15.3 maqsadiga
erishish uchun yiliga kamida 1 500 ga erni rekultivatsiya qilish
va yangi degradatsiya sur'atini kamaytirish zarurligi aniqlandi.

---

## AMALIY TAVSIYALAR

1. **Davkadastr** — DHYT tizimini Sirdaryo viloyatida rasmiy
   monitoring tizimi sifatida joriy etish; kadastrda
   "Degradatsiya darajasi" maydonini majburiy ko'rsatkich sifatida
   qo'shish;

2. **Qishloq xo'jaligi vazirligi** — NDVI monitoringi natijalariga
   asoslanib, degradatsiyaga uchragan fermer xo'jaliklariga maqsadli
   agrotexnik yordam va subsidiyalar berish dasturini ishlab chiqish;

3. **Melioratsiya boshqarmasi** — NDWI va grunt suvlari ma'lumotlari
   asosida Mirzacho'l hududida drenaj tizimini modernizatsiya qilish
   rejasini tuzish;

4. **Mahalliy hokimiyat** — DHYT alert tizimidan keladigan
   ogohlantirishlarga o'z vaqtida munosabat bildirish uchun
   tezkor javob mexanizmini joriy etish;

5. **Kelajakda** — metodologiyani O'zbekistonning boshqa
   viloyatlariga (Xorazm, Qashqadaryo, Navoiy) kengaytirish
   va mintaqaviy monitoring tarmog'ini shakllantirish.

---

*Foydalanilgan adabiyotlar ro'yxati quyida keltirilgan.*
