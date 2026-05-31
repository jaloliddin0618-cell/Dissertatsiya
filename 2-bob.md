# II BOB. TADQIQOT OB'EKTI, MA'LUMOTLAR VA METODOLOGIYA

## 2.1. Tadqiqot hududining tavsifi

### 2.1.1. Umumiy geografik tavsif

Tadqiqot hududi sifatida O'zbekiston Respublikasining **Farg'ona viloyati** tanlangan.
Farg'ona viloyati O'zbekistonning janubi-sharqida joylashgan bo'lib, Farg'ona vodiysining
markaziy qismini egallaydi. Asosiy geografik ko'rsatkichlar:

| Ko'rsatkich | Qiymat |
|-------------|--------|
| Umumiy maydon | 6 760 km² |
| Sug'oriladigan yer maydoni | ~450 000 ga |
| Aholisi (2023) | ~4 015 000 kishi |
| Qishloq aholisi ulushi | 45% |
| Koordinatalar | 40°–41° sh.k., 70°–72° sh.u. |
| Dengiz sathidan balandligi | 380–500 m |

Farg'ona vodiysi O'zbekistonning eng sersuv va eng intensiv sug'oriladigan hududlaridan
biri hisoblanadi. Vodiydagi daryo tizimi asosini Sirdaryoning yuqori oqimlari — Naryn va
Qoradaryo daryolari tashkil etadi. Iqlimi kontinental bo'lib, yozda quruq va issiq (iyul
o'rtacha harorat +27°C), qishda nisbatan sovuq (+1°C) keladi.

### 2.1.2. Qishloq xo'jaligi va sug'orish tizimi

Farg'ona viloyatida dehqonchilik asosan sug'orish orqali amalga oshiriladi. Asosiy
ekin turlari: g'o'za, bug'doy, sholi, sabzavotlar va mevali bog'lar. Viloyatda jami
sug'orish kanallarining uzunligi 8 500 km dan ortiq, shundan 1 200 km — magistral
kanallar.

O'zbekistonda qishloq xo'jaligi YAIMning taxminan 25 foizini tashkil etib, umumiy
suv sarfining 90 foizini iste'mol qiladi (Jahon banki, 2025). 2,4 million gektardan
ortiq qishloq xo'jaligi yerlari nasoslar yordamida sug'oriladi. Sug'orish
infratuzilmasining eskirganligi suv yo'qotishlarini oshirmoqda, bu esa botqoqlashish
va sho'rlanishni kuchaytirmoqda.

### 2.1.3. Degradatsiyaning mavjud holati

Farg'ona vodiysida o'tkazilgan tadqiqotlar shuni ko'rsatadiki (Mirsagatov et al., 2021):
- Sug'oriladigan yerlarning ~35% turli darajada sho'rlangan;
- ~20% botqoqlashish belgilari mavjud;
- Grunt suvlari sathi ko'p hududlarda 1–2 m oralig'ida joylashgan;
- O'simlik qoplami zichligi (NDVI) 1990-yillar bilan solishtirganda sezilarli pasaygan.

---

## 2.2. Tadqiqot uchun foydalanilgan ma'lumotlar

### 2.2.1. Kosmik tasvirlar

Tadqiqotda quyidagi kosmik ma'lumotlar manbalari ishlatiladi:

#### a) Landsat 8/9 (NASA/USGS)
| Parametr | Qiymat |
|----------|--------|
| Fazoviy aniqlik | 30 m (optik), 15 m (pan) |
| Spektral kanallar | 11 ta (OLI + TIRS) |
| Vaqt davri | 16 kun |
| Ma'lumot davriy oralig'i | 2013–2024 |
| Manba | USGS EarthExplorer (earthexplorer.usgs.gov) |

Ishlatilgan Landsat kanallar va degradatsiya tahlilida ularning vazifasi:

| Kanal | Nomi | To'lqin uzunligi (µm) | Maqsad |
|-------|------|----------------------|--------|
| B2 | Ko'k (Blue) | 0.45–0.51 | SI hisoblash |
| B3 | Yashil (Green) | 0.53–0.59 | NDWI, SI |
| B4 | Qizil (Red) | 0.64–0.67 | NDVI, NDSI |
| B5 | Yaqin infraqizil (NIR) | 0.85–0.88 | NDVI, NDWI |
| B6 | SWIR-1 | 1.57–1.65 | Tuproq namligi |
| B7 | SWIR-2 | 2.11–2.29 | Sho'rlanish |
| B10 | Termal (TIRS) | 10.6–11.2 | Yer yuzasi harorati |

#### b) Sentinel-2A/2B (ESA Copernicus)
| Parametr | Qiymat |
|----------|--------|
| Fazoviy aniqlik | 10 m (B2,B3,B4,B8), 20 m (B5–B7,B11,B12), 60 m |
| Spektral kanallar | 13 ta |
| Vaqt davri | 5 kun (ikkita sun'iy yo'ldosh) |
| Ma'lumot davriy oralig'i | 2017–2024 |
| Manba | Copernicus Open Access Hub / GEE |

#### c) MODIS Terra/Aqua
| Parametr | Qiymat |
|----------|--------|
| Fazoviy aniqlik | 250–500 m (NDVI), 1 km (LST) |
| Vaqt davri | Kunlik |
| Mahsulotlar | MOD13Q1 (NDVI, 16 kunlik kompozit) |
| Ma'lumot davriy oralig'i | 2000–2024 |
| Maqsad | Uzoq muddatli LPD tahlili |

### 2.2.2. Dala tadqiqoti ma'lumotlari (Ground Truth)

Masofadan zondlash natijalarini tasdiqlash uchun dala tadqiqoti o'tkazildi.
Namunaviy nuqtalar tanlash metodikasi:

- **Stratifikatsiya usuli**: degradatsiya darajasiga ko'ra zonalarga bo'lib, har zonadan
  proporsional namunaviy nuqtalar olindi;
- **Namunaviy nuqtalar soni**: 120 ta (har bir degradatsiya toifasi uchun kamida 30 ta);
- **Laboratoriya tahlillari**: tuproq namunaviy EC (elektr o'tkazuvchanligi), pH,
  grunt suvlari chuqurligi o'lchandi;
- **GPS koordinatalari**: Garmin GPSmap 64s qurilmasi yordamida aniqlik ±3 m;
- **Tasvirlarni olish davri**: vegetatsiya davri (aprel–iyun) va undan tashqari (noyabr–dekabr).

### 2.2.3. Yerlar kadastr ma'lumotlari

- O'zR Davkadastr ma'lumotlar bazasidan viloyat sug'oriladigan yerlari raqamli xaritasi;
- Yer parchalari chegaralari (shapefile format);
- Ball boniteti ko'rsatkichlari (2015 va 2020 yillar);
- Ekin turlari va foydalanish rejimi ma'lumotlari.

### 2.2.4. Gidrometeorologik ma'lumotlar

- Farg'ona viloyati meteorologiya stansiyalari ma'lumotlari (yog'ingarchilik, harorat);
- Grunt suvlari monitoringi stansiyalarining ko'p yillik ma'lumotlari;
- Sug'orish suvi sifati (mineral tarkibi) tahlillari.

---

## 2.3. Tadqiqot metodologiyasi

### 2.3.1. Umumiy metodologik sxema

Tadqiqot quyidagi bosqichlardan iborat bo'ladi:

```
┌─────────────────────────────────────────────────────────────┐
│                  TADQIQOT METODOLOGIYASI                     │
└─────────────────┬───────────────────────────────────────────┘
                  │
        ┌─────────▼──────────┐
        │  1. MA'LUMOTLARNI   │
        │     YIG'ISH         │
        │ • Kosmik tasvirlar  │
        │ • Dala namunaviy    │
        │ • Kadastr ma'lumot  │
        └─────────┬──────────┘
                  │
        ┌─────────▼──────────┐
        │  2. QAYTA ISHLASH  │
        │ • Geometrik to'g'r │
        │ • Radiometrik to'g'r│
        │ • Atmosfera to'g'r  │
        │ • Bulut maskasi     │
        └─────────┬──────────┘
                  │
        ┌─────────▼──────────┐
        │  3. SPEKTRAL        │
        │     TAHLIL          │
        │ • NDVI              │
        │ • NDSI              │
        │ • NDWI              │
        │ • SI, SAVI          │
        └─────────┬──────────┘
                  │
        ┌─────────▼──────────┐
        │  4. KLASSIFIKATSIYA │
        │ • Supervised        │
        │ • Unsupervised      │
        │ • Random Forest     │
        └─────────┬──────────┘
                  │
        ┌─────────▼──────────┐
        │  5. VALIDATSIYA     │
        │ • Dala ma'lumotlari │
        │ • Aniqlik matrisi   │
        │ • Kappa koeffitsient│
        └─────────┬──────────┘
                  │
        ┌─────────▼──────────┐
        │  6. XARITALASH VA  │
        │     MONITORING      │
        │ • GIS xarita        │
        │ • Kadastr integratsiya│
        │ • Hisobot           │
        └─────────────────────┘
```

### 2.3.2. Masofadan zondlash ma'lumotlarini qayta ishlash

#### a) Geometrik korreksiya
Kosmik tasvirlar USGS tomonidan Level-2 mahsulot sifatida taqdim etiladi va WGS84 /
UTM (Zone 42N) koordinata tizimida registrlangan bo'ladi. Zarur hollarda 2-nchi darajali
polinom transformatsiyasi va eng yaqin qo'shni interpolatsiya (nearest neighbor) usuli
qo'llaniladi. Geometrik xato 0,5 pikseldan oshmasligi ta'minlanadi.

#### b) Radiometrik va atmosfera korreksiyasi
Landsat tasvirlari uchun USGS Collection 2 Level-2 mahsulotlaridan foydalaniladi.
Bu mahsulotlar o'z ichiga to'lqin uzunligi o'ziga xos reflektanslikni (Surface Reflectance)
oladi. Sentinel-2 uchun ESA tomonidan taqdim etilgan SEN2COR protsessori ishlatiladi
(Bottom-of-Atmosphere reflektansi).

Google Earth Engine platformasida:
```javascript
// Sentinel-2 bulut maskalash va indeks hisoblash misoli
var s2 = ee.ImageCollection('COPERNICUS/S2_SR')
  .filterBounds(studyArea)
  .filterDate('2023-04-01', '2023-06-30')
  .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', 10))
  .map(maskS2clouds);

function maskS2clouds(image) {
  var qa = image.select('QA60');
  var cloudBitMask = 1 << 10;
  var cirrusBitMask = 1 << 11;
  var mask = qa.bitwiseAnd(cloudBitMask).eq(0)
               .and(qa.bitwiseAnd(cirrusBitMask).eq(0));
  return image.updateMask(mask).divide(10000);
}
```

#### c) Ko'p vaqtli kompozitlash
Mavsumiy tahlil uchun piksel asosidagi mediana kompozitlash (median composite) usuli
qo'llaniladi. Bu bulut va soya ta'sirini minimallashtirishga imkon beradi.

### 2.3.3. Spektral indekslarni hisoblash metodikasi

**1. NDVI (O'simlik qoplami indeksi):**
```
NDVI = (NIR - RED) / (NIR + RED)
```
Landsat 8/9 uchun: NIR = B5, RED = B4
Sentinel-2 uchun: NIR = B8, RED = B4

NDVI klassifikatsiyasi (sug'oriladigan yerlar uchun):
| NDVI oralig'i | Tavsif |
|---------------|--------|
| < 0.1 | Yalang'och tuproq / juda kuchli degradatsiya |
| 0.1–0.2 | Juda siyrak o'simlik / kuchli degradatsiya |
| 0.2–0.4 | Siyrak o'simlik / o'rtacha degradatsiya |
| 0.4–0.6 | O'rtacha zich o'simlik / normal |
| > 0.6 | Zich o'simlik / yaxshi holat |

**2. NDSI (Sho'rlanish indeksi):**
```
NDSI = (RED - NIR) / (RED + NIR)
```
Farg'ona vodiysida o'tkazilgan tadqiqot (Mirsagatov et al., 2021) shuni ko'rsatdiki,
NDSI sho'rlanishni aniqlashda boshqa indekslarga nisbatan yuqori aniqlik beradi.

**3. SI (Oddiy sho'rlanish indeksi):**
```
SI = √(GREEN × RED)
```
Yuqori SI qiymatlar sho'rlangan hududlarni bildiradi. Ikkilamchi sho'rlanish va tuproq yuzasida
tuz kristallari to'planganligini aniqlashda samarali.

**4. NDWI (Suv indeksi / botqoqlashish):**
```
NDWI = (GREEN - NIR) / (GREEN + NIR)
```
NDWI > 0 bo'lgan hududlar suv sathida, ya'ni botqoqlashish xavfi bor deb belgilanadi.

**5. EVI (Kuchaytirilgan o'simlik indeksi):**
```
EVI = 2.5 × (NIR - RED) / (NIR + 6×RED - 7.5×BLUE + 1)
```
NDVI to'yingan bo'lgan zich o'simlikli hududlarda qo'llaniladi.

**6. SAVI (Tuproq moslashtirilgan o'simlik indeksi):**
```
SAVI = ((NIR - RED) / (NIR + RED + 0.5)) × 1.5
```
Qurg'oq hududlarda tuproq foni ta'sirini kamaytiradi.

### 2.3.4. Klassifikatsiya metodlari

#### a) Nazorat ostida klassifikatsiya (Supervised Classification)
- **Maximum Likelihood (ML)** — an'anaviy statistik yondashuv;
- **Random Forest (RF)** — ensemble machine learning usuli, 100–500 ta qaror daraxti;
- **Support Vector Machine (SVM)** — ko'p o'lchamli makon klassifikatsiyasi.

Random Forest klassifikatsiyasi uchun o'qitish ma'lumotlari:
```
Degradatsiya toifalari:
  1 — Sho'rlangan (kuchsiz, o'rtacha, kuchli, juda kuchli)
  2 — Botqoqlashgan
  3 — O'simlik degradatsiyasi
  4 — Normal sug'oriladigan yer
  5 — Kombinatsiyalashgan degradatsiya
```

#### b) Nazorat ostida bo'lmagan klassifikatsiya (Unsupervised)
Dastlabki xaritalash va sinf sonini aniqlash uchun K-Means algoritmi ishlatiladi.

### 2.3.5. Ko'p yillik vaqt qatori tahlili

Uzoq muddatli tendentsiyalarni aniqlash uchun quyidagi statistik usullar qo'llaniladi:

**Mann-Kendall tendentsiya testi:**
Vaqt qatori ma'lumotlarida statistik jihatdan muhim tendentsiyani aniqlash uchun
parametrik bo'lmagan usul. Formula:
```
S = Σᵢ₌₁ⁿ⁻¹ Σⱼ₌ᵢ₊₁ⁿ sgn(xⱼ - xᵢ)
```
S > 0: o'sish tendentsiyasi, S < 0: kamayish tendentsiyasi.

**Theil-Sen moyil (slope):**
Mediana asosidagi regresion moyil hisoblash — anomal qiymatlarga chidamli.
```
β = median((xⱼ - xᵢ)/(j - i)) barcha j > i uchun
```

**Linear regression va R² koeffitsient:**
Degradatsiya indekslarining yillik o'zgarish tezligini hisoblash uchun.

### 2.3.6. Validatsiya metodikasi

Klassifikatsiya natijalari va spektral indekslar bo'yicha yaratilgan xaritalar
quyidagi metodlar bilan tekshiriladi:

**Xatolar matrisi (Confusion Matrix):**
```
           Tashhis qilingan holat
              Yer-1  Yer-2  Yer-3  Yer-4
Haqiqiy  Yer-1 | TP  |  FP  |  FP  |  FP  |
holat    Yer-2 | FN  |  TP  |  FP  |  FP  |
         Yer-3 | FN  |  FN  |  TP  |  FP  |
         Yer-4 | FN  |  FN  |  FN  |  TP  |
```

**Umumiy aniqlik (Overall Accuracy):**
```
OA = (Σ TPᵢ) / N × 100%
```

**Kappa koeffitsienti:**
```
K = (Po - Pe) / (1 - Pe)
```
K > 0.8 — juda yaxshi aniqlik, K 0.6–0.8 — yaxshi aniqlik qabul qilinadi.

**RMSE (Root Mean Square Error)** — spektral indeks va laboratoriya o'lchash natijalari
o'rtasidagi farqni baholash uchun:
```
RMSE = √(Σ(yᵢ - ŷᵢ)² / n)
```

---

## 2.4. GIS tahlil metodikasi

### 2.4.1. Makoniy interpolatsiya

Dala namunaviy nuqtalaridan butun maydon xaritasini yaratish uchun:

- **IDW (Inverse Distance Weighting)** — Sirdaryo viloyatida samarali ekanligi
  isbotlangan (Yuldashev et al., 2021);
- **Kriging** — variogramma modeliga asoslangan geostatistik interpolatsiya;
- **Spline** — silliq yuzani modellashtirish uchun.

### 2.4.2. Ko'p mezonli tahlil (MCDA)

Degradatsiya xavf xaritasini yaratish uchun bir necha omillarni birlashtirish:

| Omil | Og'irlik (%) | Asoslash |
|------|-------------|---------|
| Grunt suvlari chuqurligi | 25 | Botqoqlashish va sho'rlanishning asosiy omili |
| Sho'rlanish indeksi (NDSI) | 25 | Bevosita sho'rlanish o'lchovi |
| NDVI pasayishi | 20 | O'simlik va hosildorlik degradatsiyasi |
| Tuproq turiga bog'liqlik | 15 | Sho'rlanishga moyillik |
| Sug'orish intensivligi | 15 | Anthropogen ta'sir |
| **Jami** | **100** | |

### 2.4.3. Overlay (Qatlam ustma-ust qo'yish) tahlili

Sho'rlanish, botqoqlashish va o'simlik degradatsiyasi xaritalarini birlashtirib
kompleks degradatsiya xaritasini yaratish uchun:

```
Kompleks_degradatsiya = f(Sho'rlanish × W₁ + Botqoqlashish × W₂ + NDVI_kamayish × W₃)
```

---

## 2.5. Dasturiy ta'minot va texnik vositalar

### 2.5.1. GIS va masofadan zondlash dasturlari

| Dastur | Versiya | Maqsad |
|--------|---------|--------|
| QGIS | 3.34 LTR | Asosiy GIS tahlil, xaritalash |
| Google Earth Engine | Bulutli | Ko'p vaqtli tahlil, Python/JS API |
| Python (Rasterio, GDAL) | 3.10+ | Rastr qayta ishlash, avtomatlash |
| R (raster, sp, rgdal) | 4.3+ | Statistik tahlil, Mann-Kendall |
| ENVI | 5.6 | Giperspektral tahlil |

### 2.5.2. Python skripti — NDVI hisoblash misoli (Google Earth Engine)

```python
import ee
ee.Initialize()

# Tadqiqot hududini aniqlash
study_area = ee.Geometry.Rectangle([70.0, 40.0, 72.0, 41.0])

# Sentinel-2 tasvirlar kolleksiyasi
s2 = (ee.ImageCollection('COPERNICUS/S2_SR_HARMONIZED')
      .filterBounds(study_area)
      .filterDate('2023-05-01', '2023-06-30')
      .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', 10))
      .median())

# NDVI hisoblash
ndvi = s2.normalizedDifference(['B8', 'B4']).rename('NDVI')

# NDSI hisoblash (sho'rlanish)
ndsi = s2.normalizedDifference(['B4', 'B8']).rename('NDSI')

# NDWI hisoblash (botqoqlashish)
ndwi = s2.normalizedDifference(['B3', 'B8']).rename('NDWI')

# Natijalarni birlashtirish
result = ndvi.addBands(ndsi).addBands(ndwi)

# Export
task = ee.batch.Export.image.toDrive(
    image=result,
    description='Fergana_Degradation_2023',
    region=study_area,
    scale=10,
    crs='EPSG:32642'
)
task.start()
print("Export boshlandi...")
```

---

## 2.6. Tadqiqotning chegara va cheklovlari

Tadqiqot natijalarini talqin qilishda quyidagi cheklovlarni inobatga olish lozim:

1. **Bulutli ob-havo** — Farg'ona vodiysi qishining ayrim davrlarida bulutlilik yuqori
   bo'ladi; bu muammo Sentinel-1 SAR ma'lumotlari bilan qisman bartaraf etiladi;

2. **Dala namunaviy ma'lumotlarning soni** — barcha maydoni qamrab olish uchun 120 ta
   namunaviy nuqta etarli bo'lishi mumkin emas; biroq, stratifitsiyalangan tanlov bu
   kamchilikni kamaytiradi;

3. **Kadastr ma'lumotlarining eski bo'lishi** — ayrim er parchalari chegaralari va
   sifat ko'rsatkichlari oxirgi 5–10 yil ichida yangilanmagan bo'lishi mumkin;

4. **Masshtab muammosi** — 10–30 m piksel kattaligi bilan kichik yer parchalari (< 0,1 ga)
   da aniqlik pasayishi mumkin.

---

## 2.7. Ikkinchi bob bo'yicha xulosa

Ushbu bobda tadqiqot hududi (Farg'ona viloyati), ishlatilgan ma'lumotlar manbalari
(Landsat 8/9, Sentinel-2, MODIS, dala namunaviy, kadastr) va metodologiya (spektral
indekslar, klassifikatsiya, vaqt qatori tahlili, GIS overlay, validatsiya) batafsil
yoritildi. Taklif etilayotgan metodologiya:

- Bir vaqtda uchta degradatsiya turini (sho'rlanish, botqoqlashish, o'simlik degradatsiyasi)
  baholash imkonini beradi;
- Avtomatlashtirilgan qayta ishlash Google Earth Engine platformasida amalga oshiriladi;
- Natijalar validatsiya orqali tekshiriladi va kadastr tizimi bilan integratsiya uchun
  tayyor format (GeoPackage, Shapefile) ga aylantiriladi.

---

*Adabiyotlar ro'yxati VII bobda keltirilgan.*
