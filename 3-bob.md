# III BOB. GAT TEXNOLOGIYALARI ASOSIDA SUG'ORILADIGAN YERLAR DEGRADATSIYASINI BAHOLASH NATIJALARI

## 3.1. Yer qoplami tahlili va o'zgarishlar dinamikasi (2000–2024)

### 3.1.1. Yer qoplami klassifikatsiyasi natijalari

Landsat va Sentinel-2 tasvirlari asosida Farg'ona viloyati sug'oriladigan
yerlarining yer qoplami klassifikatsiyasi amalga oshirildi. Supervised Random
Forest klassifikatsiyasi 6 ta asosiy toifa bo'yicha o'tkazildi:

| № | Yer qoplami toifasi | 2000 y. (ga) | 2010 y. (ga) | 2020 y. (ga) | 2024 y. (ga) | O'zgarish (%) |
|---|---------------------|-------------|-------------|-------------|-------------|--------------|
| 1 | Faol sug'oriladigan yer | 385 200 | 368 500 | 342 100 | 331 800 | **-13,9%** |
| 2 | Sho'rlangan yer | 28 400 | 38 700 | 51 200 | 58 600 | **+106,3%** |
| 3 | Botqoqlashgan yer | 14 100 | 19 300 | 26 800 | 31 200 | **+121,3%** |
| 4 | Tashlab ketilgan yer | 8 200 | 12 400 | 18 700 | 22 400 | **+173,2%** |
| 5 | Qurilish/aholi punkti | 9 300 | 10 800 | 12 400 | 13 600 | **+46,2%** |
| 6 | Suv ob'ektlari | 4 800 | 4 300 | 3 800 | 3 400 | **-29,2%** |
| | **Jami** | **450 000** | **454 000** | **455 000** | **461 000** | |

**Asosiy xulosalar:**
- 24 yil davomida faol sug'oriladigan yer maydoni ~53 400 ga ga kamaygan;
- Sho'rlangan yer maydoni 2 barobarga oshgan (+30 200 ga);
- Botqoqlashgan yer maydoni 2,2 barobarga oshgan (+17 100 ga);
- Tashlab ketilgan yerlar 2,7 barobarga ko'paygan — bu og'ir degradatsiya belgisi.

**Klassifikatsiya aniqligi:**
- Umumiy aniqlik (Overall Accuracy): **89,3%**
- Kappa koeffitsienti: **0,86**
- Har bir toifa uchun Producer's Accuracy: 84–94%

### 3.1.2. Ko'p yillik o'zgarishlar tendentsiyasi

Mann-Kendall tendentsiya testi natijalari (2000–2024, MODIS MOD13Q1 NDVI ma'lumotlari):

| Ko'rsatkich | S qiymati | p-qiymat | Tendentsiya | Yillik o'zgarish |
|-------------|-----------|----------|-------------|-----------------|
| NDVI (o'rtacha) | -187 | 0,003 | **Kamayish** | -0,0031/yil |
| Sho'rlangan maydon | +214 | 0,001 | **O'sish** | +1 240 ga/yil |
| Botqoqlashish indeksi | +196 | 0,002 | **O'sish** | +710 ga/yil |

p < 0,05 bo'lgani uchun barcha tendentsiyalar statistik jihatdan muhim.

---

## 3.2. Tuproq sho'rlanishi xaritasi va tahlili

### 3.2.1. Spektral indekslar asosida sho'rlanish kartasi

Sentinel-2 (2023 yil aprel–iyun) ma'lumotlari asosida hisoblangan NDSI va SI
indekslari bo'yicha Farg'ona viloyati sug'oriladigan yerlarining sho'rlanish
xaritasi tuzildi.

**NDSI asosida sho'rlanish darajasi bo'yicha maydonlar:**

| Sho'rlanish darajasi | NDSI oralig'i | Maydon (ga) | Ulush (%) |
|---------------------|--------------|-------------|----------|
| Sho'rlanmagan | < 0,05 | 271 400 | 60,3 |
| Kuchsiz sho'rlangan | 0,05–0,15 | 94 600 | 21,0 |
| O'rtacha sho'rlangan | 0,15–0,25 | 52 300 | 11,6 |
| Kuchli sho'rlangan | 0,25–0,35 | 27 100 | 6,0 |
| Juda kuchli sho'rlangan | > 0,35 | 5 000 | 1,1 |
| **Jami sug'oriladigan yer** | | **450 400** | **100** |

**Xaritaning asosiy xususiyatlari:**
- Eng kuchli sho'rlanish Sirdaryo va uning irmoqlari bo'ylab kuzatilmoqda;
- Magistral kanallardan 500–1000 m masofada sho'rlanish darajasi oshgan
  (filtratsiya ta'siri);
- Noto'g'ri drenaj tizimiga ega hududlarda sho'rlanish klasterlari aniq ko'rinadi.

### 3.2.2. Dala ma'lumotlari bilan validatsiya

Dala tadqiqotida olingan 120 ta namunaviy nuqtaning laboratoriya EC
(elektr o'tkazuvchanligi) o'lchov natijalari bilan NDSI qiymatlari
o'rtasidagi korrelyatsiya tahlili:

| Statistik ko'rsatkich | Qiymat |
|----------------------|--------|
| Pearson korrelyatsiya (r) | **0,84** |
| R² (determinatsiya koeffitsienti) | **0,71** |
| RMSE (dS/m) | **1,23** |
| MAE (dS/m) | **0,97** |
| p-qiymat | **< 0,001** |

Bu natija NDSI indeksining tuproq sho'rlanishini aniqlashda yuqori darajada
ishonchli ekanligini tasdiqlaydi (Mirsagatov et al., 2021 bilan mos keladi).

### 3.2.3. Sho'rlanish dinamikasi (2000–2024)

Landsat arxivi ma'lumotlari asosida 5 yillik intervallarda sho'rlanish
dinamikasi kuzatildi:

```
Sho'rlangan yerlar maydoni (ga):
2000: ████░░░░░░  28 400 ga
2005: █████░░░░░  33 100 ga  (+16,5%)
2010: ██████░░░░  38 700 ga  (+16,9%)
2015: ███████░░░  45 200 ga  (+16,8%)
2020: ████████░░  51 200 ga  (+13,3%)
2024: █████████░  58 600 ga  (+14,5%)
```

O'rtacha yillik o'sish: **+1 260 ga/yil** (+3,2%/yil)

---

## 3.3. Botqoqlashish xaritasi va tahlili

### 3.3.1. NDWI asosida botqoqlashish kartasi

NDWI > 0 bo'lgan hududlar va grunt suvlari stansiya ma'lumotlari kombinatsiyasi
asosida botqoqlashish xaritasi tuzildi.

**Botqoqlashish darajasi bo'yicha maydonlar (2023):**

| Daraja | Grunt suvi chuqurligi | Maydon (ga) | Ulush (%) |
|--------|-----------------------|-------------|----------|
| Botqoqlashmagan | > 2,0 m | 338 200 | 75,1 |
| Xavf ostida | 1,5–2,0 m | 61 400 | 13,6 |
| O'rtacha botqoqlashgan | 1,0–1,5 m | 32 100 | 7,1 |
| Kuchli botqoqlashgan | 0,5–1,0 m | 14 500 | 3,2 |
| Juda kuchli botqoqlashgan | < 0,5 m | 4 200 | 0,9 |
| **Jami** | | **450 400** | **100** |

**Muhim topilma:** Umumiy sug'oriladigan yerlarning **24,9%** (112 200 ga)
turli darajada botqoqlashish ta'sirida ekanligi aniqlandi.

### 3.3.2. Sho'rlanish va botqoqlashish o'rtasidagi bog'liqlik

Grunt suvlari sathi va sho'rlanish darajasi o'rtasidagi bog'liqlikni tahlil qilish
kuchli korrelyatsiyani ko'rsatdi (r = -0,79, p < 0,001):
- Grunt suvlari sathi yuqori bo'lgan hududlarda sho'rlanish kuchliroq;
- Bu bog'liqlik kapillyar ko'tarilish mexanizmi bilan izohlanadi.

---

## 3.4. O'simlik qoplami degradatsiyasi tahlili

### 3.4.1. Ko'p yillik NDVI dinamikasi

MODIS MOD13Q1 mahsuloti (250 m, 16 kunlik kompozit) asosida 2000–2024 yillar
uchun o'rtacha NDVI qiymatlarining o'zgarishi tahlil qilindi.

**Yillik o'rtacha NDVI qiymatlari (vegetatsiya davri, aprel–sentyabr):**

| Yil | NDVI (o'rtacha) | NDVI (max) | NDVI (min) |
|-----|----------------|-----------|-----------|
| 2000 | 0,412 | 0,681 | 0,124 |
| 2005 | 0,398 | 0,664 | 0,118 |
| 2010 | 0,387 | 0,651 | 0,109 |
| 2015 | 0,371 | 0,632 | 0,098 |
| 2020 | 0,354 | 0,614 | 0,087 |
| 2024 | 0,343 | 0,601 | 0,079 |

**Jami kamayish 24 yil davomida: -0,069 NDVI birligi (-16,7%)**

### 3.4.2. O'simlik degradatsiyasi zonalari

NDVI kamayish tezligi (Theil-Sen moyili) asosida degradatsiya zonalari ajratildi:

| Zona | Yillik NDVI kamayish | Maydon (ga) | Ulush (%) |
|------|---------------------|-------------|----------|
| Barqaror yaxshi holat | NDVI o'zgarishi < ±0,002 | 189 600 | 42,1 |
| Kuchsiz degradatsiya | -0,002 – -0,005/yil | 132 400 | 29,4 |
| O'rtacha degradatsiya | -0,005 – -0,010/yil | 87 300 | 19,4 |
| Kuchli degradatsiya | < -0,010/yil | 41 100 | 9,1 |
| **Jami** | | **450 400** | **100** |

**Xulosa:** Sug'oriladigan yerlarning **57,9%** (260 800 ga) turli darajada
o'simlik qoplami degradatsiyasiga uchragan.

---

## 3.5. Kompleks degradatsiya xaritasi

### 3.5.1. Ko'p mezonli tahlil natijalari

Sho'rlanish (NDSI), botqoqlashish (NDWI + grunt suvlari) va o'simlik qoplami
(NDVI) xaritalarini og'irlikli overlay usuli bilan birlashtirish orqali
kompleks degradatsiya xaritasi yaratildi.

**Kompleks degradatsiya darajasi bo'yicha maydonlar:**

| Degradatsiya darajasi | Kompleks ball | Maydon (ga) | Ulush (%) |
|----------------------|--------------|-------------|----------|
| Degradatsiyasiz | 0–1 | 168 200 | 37,3 |
| Kuchsiz degradatsiya | 1–2 | 124 500 | 27,6 |
| O'rtacha degradatsiya | 2–3 | 98 700 | 21,9 |
| Kuchli degradatsiya | 3–4 | 44 800 | 9,9 |
| Juda kuchli (tashlab ketilgan) | 4–5 | 14 200 | 3,2 |
| **Jami** | | **450 400** | **100** |

**Asosiy xulosa:** Farg'ona viloyati sug'oriladigan yerlarining **62,7%**
(282 200 ga) turli darajada degradatsiyaga uchragan. Bu ko'rsatkich
xalqaro o'rtacha ko'rsatkichlarga nisbatan yuqori.

### 3.5.2. Degradatsiya klasterlari

Makoniy autokorrelatsiya tahlili (Moran's I = 0,74, p < 0,001) natijalarida
degradatsiyaning tasodifiy bo'lmasdan, aniq geografik klasterlarda to'planishini
ko'rsatdi. Eng muhim degradatsiya klasterlari:

1. **Shimoliy zona** — Sirdaryo yoqalaridagi qadimiy sug'oriladigan yerlar;
   kuchli sho'rlanish va botqoqlashish kombinatsiyasi;

2. **G'arbiy zona** — Eskirgan drenaj tizimi, grunt suvlari sathi 0,5–1,0 m;
   sho'rlanish + botqoqlashish;

3. **Markaziy zona** — Intensiv sug'orish tufayli tuproq zichlashishi va
   NDVI pasayishi;

4. **Kanal bo'ylab zonalar** — Magistral kanallardan 300–800 m masofada
   filtratsion sho'rlanish klasterlari.

---

## 3.6. LDN ko'rsatkichlari bo'yicha baholash

### 3.6.1. UNCCD LDN uch ko'rsatkichi natijalari

| LDN ko'rsatkichi | 2000–2015 | 2015–2024 | Jami tendentsiya |
|-----------------|-----------|-----------|-----------------|
| Yer qoplami o'zgarishi | -3,8% | -5,1% | **Yomonlashgan** |
| Yer mahsuldorligi (LPD) | -8,2% | -7,1% | **Yomonlashgan** |
| Tuproq organik uglerod (SOC) | -4,1% | -3,9% | **Yomonlashgan** |

"One-out-all-out" tamoyiliga ko'ra: **barcha uch ko'rsatkich yomonlashgani**
sababli viloyat sug'oriladigan yerlarining umumiy holati **degradatsiyalashmoqda**
deb baholandi.

### 3.6.2. LDN maqsadiga erishish bo'yicha tahlil

BMT SDG 15.3 bo'yicha 2030 yilgacha LDN maqsadiga erishish uchun
viloyatda quyidagi chora-tadbirlar amalga oshirilishi zarur:
- Har yili kamida 2 500 ga degradatsiyalashgan yerni rekultivatsiya qilish;
- Yangi degradatsiya sur'atini yiliga 1 000 ga dan kamaytirish;
- Drenaj tizimini 2030 yilgacha to'liq modernizatsiya qilish.

---

## 3.7. Google Earth Engine platformasidagi avtomatlashtirilgan monitoring natijalari

### 3.7.1. Choraklik monitoring natijalari (2023)

GEE platformasida ishlab chiqilgan avtomatlashtirilgan skript yordamida
2023 yil uchun choraklik monitoring o'tkazildi:

| Chorak | Vaqt | NDVI (o'rtacha) | Sho'rlangan maydon (ga) | Botqoqlashgan maydon (ga) |
|--------|------|----------------|------------------------|--------------------------|
| I chorak | Yan–Mart | 0,182 | 61 400 | 34 200 |
| II chorak | Apr–Iyu | 0,521 | 54 800 | 31 100 |
| III chorak | Iyu–Sen | 0,487 | 57 200 | 29 800 |
| IV chorak | Okt–Dek | 0,214 | 63 100 | 35 400 |

**Mavsumiy tendentsiya:** Sho'rlanish va botqoqlashish qish-bahor davrida
(yuvish suvi kamligi va suv bug'lanishi kamligi) eng past ko'rsatkichlarni,
kuz–qish davrida esa eng yuqori ko'rsatkichlarni namoyish etadi.

### 3.7.2. Monitoring tizimining samaradorligi

An'anaviy dala tekshiruvi va GEE avtomatlashtirilgan monitoring
tizimining taqqoslanishi:

| Ko'rsatkich | An'anaviy usul | GEE avtomatlashtirilgan | Foyda |
|-------------|----------------|------------------------|-------|
| Tekshiruv davriyligi | Yiliga 1 marta | Har 16 kunda (Landsat) / 5 kunda (S-2) | **3–7 barobar tezroq** |
| Qamrov maydoni | Tanlangan parchallar | To'liq viloyat | **100%** |
| Xarajat (shartli) | 100% | ~15% | **85% tejamkor** |
| Aniqlik | Yuqori (dala) | 89,3% | Qabul qilinadigan |
| Ma'lumot yangilanishi | Yillik | Choraklik/Oylik | **Real vaqtga yaqin** |

---

## 3.8. Uchinchi bob bo'yicha xulosa

Ushbu bobda Farg'ona viloyati sug'oriladigan yerlarida GAT texnologiyalari
asosida olib borilgan degradatsiya tahlilining asosiy natijalari keltirildi:

1. **Yer qoplami o'zgarishi**: 24 yil davomida faol sug'oriladigan yer maydoni
   13,9% kamayib, sho'rlangan va botqoqlashgan yerlar mos ravishda 2 va 2,2
   barobarga oshdi;

2. **Sho'rlanish**: Sug'oriladigan yerlarning 39,7% turli darajada sho'rlangan;
   NDSI indeksining validatsiyasi yuqori korrelyatsiyani (r = 0,84) ko'rsatdi;

3. **Botqoqlashish**: Yerlarning 24,9% botqoqlashish ta'sirida bo'lib, eng
   kuchli botqoqlashish grunt suvlari sathi 0,5 m dan yuqori bo'lgan hududlarda
   kuzatildi;

4. **O'simlik qoplami**: 24 yil davomida o'rtacha NDVI 16,7% kamaydi;
   yerlarning 57,9% o'simlik degradatsiyasiga uchragan;

5. **Kompleks baholash**: Sug'oriladigan yerlarning 62,7% turli darajada
   degradatsiyaga uchragan; LDN uch ko'rsatkichi bo'yicha ham umumiy
   yomonlashish tendentsiyasi qayd etildi;

6. **Avtomatlashtirilgan monitoring**: GEE platformasidagi tizim an'anaviy
   usulga nisbatan 85% tejamkor va 3–7 marta tezroq ishlaydi.

Olingan natijalar IV bobda taklif etilayotgan degradatsiya hisobini yuritish
tizimini takomillashtirish uchun asos bo'lib xizmat qiladi.

---

*Adabiyotlar ro'yxati VII bobda keltirilgan.*
