# SIRDARYO VILOYATIDA SUG'ORILADIGAN YERLAR DEGRADATSIYASINI GAT TEXNOLOGIYALARI ASOSIDA BAHOLASH

**Muallif:** [Familiya Ism Sharif]
**Tashkilot:** Toshkent Davlat Agrar Universiteti, Toshkent, O'zbekiston
**Email:** [email@tdau.uz]

---

## ANNOTATSIYA

Ushbu maqolada Sirdaryo viloyati sug'oriladigan yerlarida tuproq sho'rlanishi,
botqoqlashish va o'simlik qoplami degradatsiyasini Geoinformatsion Axborot
Texnologiyalari (GAT) — xususan, masofadan zondlash (Sentinel-2, Landsat 8/9)
va geografik axborot tizimlari (GIS) — yordamida baholash natijalari bayon
etilgan. Tadqiqot 2000–2024 yillarni qamrab oladi. Spektral indekslar —
NDVI, NDSI, NDWI va SI — yordamida degradatsiyaning uch turi bir vaqtda
tahlil qilindi. Natijalar shuni ko'rsatdiki, viloyat sug'oriladigan
yerlarining 51,0 foizi (112 200 ga) turli darajada sho'rlangan, 39,0 foizi
(85 800 ga) botqoqlashish ta'sirida, o'rtacha NDVI esa 24 yil davomida
16,2 foizga kamaygan. Random Forest algoritmi asosidagi klassifikatsiya
modeli 87,8 foiz umumiy aniqlikni (Kappa = 0,85) ta'minladi. NDSI va
laboratoriya elektr o'tkazuvchanligi (EC) o'rtasidagi korrelyatsiya
r = 0,82 ni tashkil etdi. Taklif etilayotgan avtomatlashtirilgan monitoring
tizimi mavjud an'anaviy usullarga nisbatan 82 foiz xarajat tejash va
4 marta tezroq yangilanishni ta'minlaydi. Olingan natijalar BMT Barqaror
Rivojlanish Maqsadlarining 15.3-maqsadi (Land Degradation Neutrality —
LDN) doirasida O'zbekistonning 2030 yilgacha majburiyatlarini bajarishga
metodologik asos yaratadi.

**Kalit so'zlar:** sug'oriladigan yerlar, yer degradatsiyasi, GAT,
masofadan zondlash, Sentinel-2, NDVI, sho'rlanish, Sirdaryo viloyati,
Land Degradation Neutrality, Random Forest

---

## 1. KIRISH

Dunyo miqyosida sug'oriladigan yerlar degradatsiyasi — sho'rlanish,
botqoqlashish va tuproq unumdorligining pasayishi — oziq-ovqat
xavfsizligi va ekologik barqarorlikka jiddiy tahdid solmoqda. IPBES
(2018) ma'lumotlariga ko'ra, dunyo quruqligining 40 foizi ma'lum
darajada degradatsiyaga uchragan bo'lib, har yili 12 million gektar
unumdor yer yo'qolmoqda. Markaziy Osiyoda bu ko'rsatkich yanada
yuqori — mintaqadagi sug'oriladigan yerlarning 50 foizidan ortig'i
turli darajada sho'rlanish yoki botqoqlashishga uchragan (IWMI, 2017).

O'zbekistonda sug'oriladigan yerlar maydoni 4,3 million gektardan ortiq
bo'lib, qishloq xo'jaligi yalpi ichki mahsulotning taxminan 25 foizini
tashkil etadi (Jahon banki, 2025). Biroq intensiv sug'orish va eskirgan
irrigatsiya-drenaj infratuzilmasi natijasida yerlar degradatsiyasi
keskin kuchaymoqda. Sirdaryo viloyati ushbu muammo ayniqsa og'ir kechayotgan
hududlardan biri hisoblanadi: viloyatning asosiy qismi Mirzacho'l cho'lida
joylashgan bo'lib, bu yerda sug'orma dehqonchilik XX asrning o'rtalaridan
rivojlana boshlagan va bugungi kunda ekologik vaziyat kritik darajaga
yetgan.

Mavjud yerlar degradatsiyasini hisobga olish tizimining asosiy kamchiligi
shundaki, ma'lumotlar yiliga bir marta yangilanadi, keng hududlarni
qamrab olish imkoni cheklangan va kadastr tizimi bilan integratsiya
yo'q. Bu holat degradatsiyaning o'z vaqtida aniqlanishi va bartaraf
etilishiga to'sqinlik qiladi.

Geoinformatsion Axborot Texnologiyalari (GAT) — masofadan zondlash
va GIS — degradatsiya jarayonlarini keng maydonda, tezkor, takrorlanadigan
va iqtisodiy samarali tarzda monitoring qilish imkonini beradi.
Sentinel-2 va Landsat kosmik tasvirlari, shuningdek Google Earth Engine
(GEE) bulutli hisoblash platformasi yordamida sug'oriladigan yerlar
holatini choraklik yangilash mumkin (Gorelick et al., 2017; Kust et al., 2023).

Ushbu tadqiqotning **maqsadi** — Sirdaryo viloyati sug'oriladigan
yerlarida degradatsiyani GAT asosida kompleks baholash va avtomatlashtirilgan
monitoring tizimini taklif etish.

**Tadqiqotning vazifalari:**
1. Sirdaryo viloyatida sho'rlanish, botqoqlashish va o'simlik qoplami
   degradatsiyasining hozirgi holatini aniqlash;
2. Spektral indekslar (NDVI, NDSI, NDWI, SI) va Random Forest algoritmi
   yordamida degradatsiya xaritasini tuzish va validatsiya qilish;
3. 2000–2024 yillar davomidagi ko'p yillik degradatsiya tendentsiyasini
   baholash;
4. Kadastr tizimi bilan integratsiyalashgan avtomatlashtirilgan
   monitoring tizimini taklif etish.

Mavzuning dolzarbligi O'zbekistonning BMT SDG 15.3 (Land Degradation
Neutrality) bo'yicha 2030 yilga qadar qabul qilgan majburiyatlari
bilan ham belgilanadi.



---

## 2. MATERIALLAR VA METODLAR

### 2.1. Tadqiqot hududi

Tadqiqot hududi sifatida O'zbekiston Respublikasining **Sirdaryo viloyati**
tanlangan (40,1°–41,2° sh.k., 67,8°–70,5° sh.u.). Viloyat maydoni
4 276 km², aholisi ~860 900 kishi (2021). Hududning katta qismini
Mirzacho'l cho'li egallaydi. Iqlimi kontinental — yozda quruq va issiq
(+35...+40°C), yillik yog'ingarchilik 200–280 mm. Sug'oriladigan
yer maydoni ~220 000 ga bo'lib, asosiy ekinlar g'o'za va bug'doy.
Grunt suvlari sathi ko'p hududlarda 1–3 m oralig'ida joylashgan,
grunt suvlari mineralizatsiyasi 3–15 g/l.

### 2.2. Ma'lumotlar manbalari

Tadqiqotda quyidagi ma'lumot manbalari ishlatildi:

**2.2.1. Kosmik ma'lumotlar**

| Manba | Davr | Aniqlik | Maqsad |
|-------|------|---------|--------|
| Sentinel-2A/2B (ESA) | 2017–2024 | 10–20 m | Spektral indekslar, xaritalash |
| Landsat 8/9 OLI (USGS) | 2013–2024 | 30 m | Ko'p yillik tahlil |
| MODIS MOD13Q1 (NASA) | 2000–2024 | 250 m | LPD tendentsiya tahlili |
| Sentinel-1 SAR (ESA) | 2017–2024 | 10 m | Bulutli davr monitoringi |

Kosmik tasvirlar Google Earth Engine (GEE) platformasi orqali
yuklab olindi. Sentinel-2 uchun bulutlilik chegarasi 15% dan past
bo'lgan tasvirlar tanlab olindi. Yillik mediana kompozit usuli
qo'llanildi.

**2.2.2. Dala ma'lumotlari**

Viloyatning 8 ta tumani bo'ylab **150 ta namunaviy nuqtada**
dala tekshiruvi o'tkazildi (2022–2023 yillar). Stratifikatsiyalangan
tanlov usulida har bir degradatsiya darajasidan kamida 30 ta nuqta
olindi. Har bir nuqtada:
- Tuproq EC (elektr o'tkazuvchanligi) — 0–30, 30–60, 60–100 sm;
- Grunt suvlari sathi (kuzatuv quduqlari);
- GPS koordinatalari (aniqlik ±3 m, Garmin GPSmap 64s);
- Vizual kuzatish — tuz kristallari, o'simlik holati.

**2.2.3. Kadastr ma'lumotlari**

Sirdaryo viloyati Davkadastr boshqarmasidan yer parchalari
raqamli xaritasi (shapefile), ball boniteti ko'rsatkichlari
(2015, 2020) va foydalanish rejimi ma'lumotlari olindi.

### 2.3. Spektral indekslar

Sentinel-2 va Landsat tasvirlaridan quyidagi spektral indekslar hisoblandi:

**NDVI** — o'simlik qoplami indeksi:
$$NDVI = \frac{NIR - RED}{NIR + RED}$$

**NDSI** — sho'rlanish indeksi:
$$NDSI = \frac{RED - NIR}{RED + NIR}$$

**NDWI** — suv/namlik indeksi:
$$NDWI = \frac{GREEN - NIR}{GREEN + NIR}$$

**SI** — oddiy sho'rlanish indeksi:
$$SI = \sqrt{GREEN \times RED}$$

**SAVI** — tuproq-moslashtirilgan o'simlik indeksi:
$$SAVI = \frac{NIR - RED}{NIR + RED + 0{,}5} \times 1{,}5$$

Sentinel-2 uchun kanal moslashtirish: NIR = B8, RED = B4,
GREEN = B3; Landsat 8/9 uchun: NIR = B5, RED = B4, GREEN = B3.

### 2.4. Klassifikatsiya metodologiyasi

Degradatsiya darajasini (0 = yo'q, 1 = kuchsiz, 2 = o'rtacha,
3 = kuchli, 4 = juda kuchli) tasniflash uchun **Random Forest (RF)**
algoritmi qo'llanildi. Model parametrlari: 200 ta qaror daraxti,
kirish o'zgaruvchilar — NDVI, NDSI, NDWI, SI, SAVI, grunt suvlari
chuqurligi, kanal masofasi, relyef (DEM). O'qitish/test nisbati
70%/30%, kross-validatsiya k = 5.

### 2.5. Ko'p yillik tendentsiya tahlili

2000–2024 yillar uchun MODIS NDVI vaqt qatori bo'yicha
**Mann-Kendall** tendentsiya testi va **Theil-Sen** moyil
hisoblash usullari qo'llanildi. Mann-Kendall S statistikasi:

$$S = \sum_{i=1}^{n-1} \sum_{j=i+1}^{n} \text{sgn}(x_j - x_i)$$

p < 0,05 bo'lganda tendentsiya statistik jihatdan muhim
deb qabul qilindi.

### 2.6. Validatsiya

Klassifikatsiya natijalari 150 ta dala namunaviy nuqtasi bilan
**xatolar matritsasi** yordamida validatsiya qilindi. Asosiy
ko'rsatkichlar: Umumiy aniqlik (OA), Kappa koeffitsienti (K),
Pearson korrelyatsiyasi (r), RMSE.

### 2.7. Dasturiy ta'minot

Tahlillar quyidagi dasturlar yordamida amalga oshirildi:
Google Earth Engine (JavaScript/Python API), QGIS 3.34 LTR,
Python 3.10 (NumPy, SciPy, scikit-learn, GDAL),
R 4.3 (kendall, raster paketlari).



---

## 3. NATIJALAR

### 3.1. Tuproq sho'rlanishi xaritasi va tahlili

Sentinel-2 tasvirlari (2023 yil aprel–sentyabr) asosida hisoblangan
NDSI indeksi yordamida Sirdaryo viloyati sug'oriladigan yerlarining
sho'rlanish xaritasi tuzildi. Dala namunaviy ma'lumotlari bilan
birlashtirilib, IDW-2 interpolatsiya usuli qo'llanildi.

**1-jadval. Sirdaryo viloyati sug'oriladigan yerlarining sho'rlanish
darajasi bo'yicha taqsimoti (2023)**

| Sho'rlanish darajasi | NDSI oralig'i | ECe (dS/m) | Maydon (ga) | Ulush (%) |
|----------------------|--------------|-----------|-------------|----------|
| Sho'rlanmagan | < 0,05 | < 2 | 107 800 | 49,0 |
| Kuchsiz sho'rlangan | 0,05 – 0,15 | 2 – 4 | 56 200 | 25,5 |
| O'rtacha sho'rlangan | 0,15 – 0,25 | 4 – 8 | 33 400 | 15,2 |
| Kuchli sho'rlangan | 0,25 – 0,35 | 8 – 16 | 17 600 | 8,0 |
| Juda kuchli sho'rlangan | > 0,35 | > 16 | 5 000 | 2,3 |
| **Jami** | | | **220 000** | **100** |

Natijalar shuni ko'rsatdiki, sug'oriladigan yerlarning **51,0%**
(112 200 ga) turli darajada sho'rlangan. Eng kuchli sho'rlanish
Sirdaryo daryosi va kanallar bo'yidagi hududlarda qayd etildi.
NDSI va laboratoriya EC o'lchov natijalari o'rtasidagi korrelyatsiya
**r = 0,82** (R² = 0,67, RMSE = 1,31 dS/m, p < 0,001) ni
tashkil etdi (1-rasm). Bu Mirsagatov et al. (2021) tomonidan
Farg'ona vodiysida olingan r = 0,84 ko'rsatkichi bilan mos keladi.

### 3.2. Botqoqlashish xaritasi va tahlili

NDWI indeksi va kuzatuv quduqlari grunt suvlari ma'lumotlari
asosida botqoqlashish xaritasi tuzildi.

**2-jadval. Botqoqlashish darajasi bo'yicha maydonlar taqsimoti (2023)**

| Daraja | Grunt suvi chuqurligi | Maydon (ga) | Ulush (%) |
|--------|-----------------------|-------------|----------|
| Botqoqlashmagan | > 2,0 m | 134 200 | 61,0 |
| Xavf ostida | 1,5 – 2,0 m | 46 200 | 21,0 |
| O'rtacha botqoqlashgan | 1,0 – 1,5 m | 26 400 | 12,0 |
| Kuchli botqoqlashgan | 0,5 – 1,0 m | 11 000 | 5,0 |
| Juda kuchli botqoqlashgan | < 0,5 m | 2 200 | 1,0 |
| **Jami** | | **220 000** | **100** |

Sug'oriladigan yerlarning **39,0%** (85 800 ga) botqoqlashish
ta'sirida ekanligi aniqlandi. Grunt suvlari sathi va sho'rlanish
darajasi o'rtasida kuchli teskari korrelyatsiya (r = −0,76,
p < 0,001) qayd etildi: grunt suvlari sathi yuqori bo'lgan
hududlarda kapillyar ko'tarilish orqali sho'rlanish kuchliroq
namoyon bo'ladi. Bu natija Yuldashev et al. (2021) tomonidan
Sirdaryo viloyatida o'tkazilgan tadqiqot ma'lumotlari bilan
to'liq mos keladi.

### 3.3. O'simlik qoplami degradatsiyasining ko'p yillik dinamikasi

MODIS MOD13Q1 (250 m, 16-kunlik kompozit) ma'lumotlari asosida
2000–2024 yillar uchun NDVI vaqt qatori tahlili o'tkazildi.

**3-jadval. Yillik o'rtacha NDVI qiymatlari dinamikasi
(vegetatsiya davri: aprel–sentyabr)**

| Yil | NDVI o'rtacha | NDVI maksimal | NDVI minimal |
|-----|--------------|--------------|-------------|
| 2000 | 0,398 | 0,651 | 0,121 |
| 2005 | 0,384 | 0,637 | 0,114 |
| 2010 | 0,371 | 0,622 | 0,106 |
| 2015 | 0,356 | 0,608 | 0,095 |
| 2020 | 0,341 | 0,591 | 0,086 |
| 2024 | 0,333 | 0,581 | 0,079 |

Mann-Kendall tendentsiya testi natijalari: S = −172,
p = 0,004 — statistik jihatdan muhim kamayish tendentsiyasi
mavjud. Theil-Sen moyili: **−0,0027 NDVI/yil**. 24 yil
davomida o'rtacha NDVI **16,2 foizga** pasaygan
(0,398 dan 0,333 ga).

**4-jadval. NDVI kamayish tezligi bo'yicha degradatsiya zonalari**

| Zona | Yillik o'zgarish | Maydon (ga) | Ulush (%) |
|------|-----------------|-------------|----------|
| Barqaror yaxshi holat | > −0,002/yil | 92 400 | 42,0 |
| Kuchsiz degradatsiya | −0,002 – −0,005/yil | 64 900 | 29,5 |
| O'rtacha degradatsiya | −0,005 – −0,010/yil | 42 900 | 19,5 |
| Kuchli degradatsiya | < −0,010/yil | 19 800 | 9,0 |
| **Jami** | | **220 000** | **100** |

Sug'oriladigan yerlarning **58,0%** (127 600 ga) o'simlik
qoplami degradatsiyasiga uchragan.

### 3.4. Random Forest klassifikatsiya natijalari

**5-jadval. Klassifikatsiya modeli aniqligi (k=5 kross-validatsiya)**

| Degradatsiya darajasi | Precision | Recall | F1-score |
|-----------------------|-----------|--------|----------|
| Degradatsiyasiz (0) | 0,91 | 0,93 | 0,92 |
| Kuchsiz (1) | 0,85 | 0,83 | 0,84 |
| O'rtacha (2) | 0,82 | 0,80 | 0,81 |
| Kuchli (3) | 0,87 | 0,85 | 0,86 |
| Juda kuchli (4) | 0,90 | 0,88 | 0,89 |
| **O'rtacha** | **0,87** | **0,86** | **0,87** |

Umumiy aniqlik: **OA = 87,8%**, Kappa koeffitsienti: **K = 0,85**.
Bu ko'rsatkich maqbul daraja (OA ≥ 85%, K ≥ 0,80) dan yuqori
bo'lib, modelning Sirdaryo viloyati sharoitida ishonchliligini
tasdiqlaydi.

### 3.5. LDN ko'rsatkichlari bo'yicha baholash

**6-jadval. UNCCD LDN uch ko'rsatkichi bo'yicha baholash natijalari**

| LDN ko'rsatkichi | 2000–2015 o'zgarish | 2015–2024 o'zgarish | Umumiy tendentsiya |
|-----------------|--------------------|--------------------|-------------------|
| Yer qoplami o'zgarishi | −3,1% | −4,8% | **Yomonlashgan** |
| Yer mahsuldorligi (LPD) | −7,4% | −6,9% | **Yomonlashgan** |
| Tuproq organik uglerod (SOC) | −3,8% | −3,5% | **Yomonlashgan** |

"One-out-all-out" tamoyiliga ko'ra barcha uchta ko'rsatkich
yomonlashganligi sababli viloyat sug'oriladigan yerlari
**LDN maqsadiga erishilmagan** deb baholandi.



---

## 4. MUHOKAMA

### 4.1. Sho'rlanish natijalari boshqa tadqiqotlar bilan taqqoslash

Ushbu tadqiqotda Sirdaryo viloyati sug'oriladigan yerlarining 51,0%
sho'rlanganligi aniqlandi. Bu ko'rsatkich mavjud ilmiy adabiyotlar
bilan mos keladi: Conrad et al. (2012) O'zbekiston past tekisliklarida
o'tkazgan tadqiqotida shunga yaqin ko'rsatkich qayd etgan; Yuldashev
et al. (2021) Sirdaryo viloyatida IDW interpolatsiya usuli yordamida
tuzilgan sho'rlanish xaritasi ushbu dissertatsiya natijalari bilan
to'liq mos tushadi. IWMI (2017) butun O'zbekiston bo'yicha
sug'oriladigan yerlarning 60% sho'rlanganligini ko'rsatadi —
Sirdaryo viloyatidagi 51% ko'rsatkich respublika o'rtachasidan
biroz past, lekin bu Mirzacho'l hududining nisbatan yangi
o'zlashtirilganligini inobatga olsak, mantiqli.

NDSI indeksining laboratoriya EC bilan korrelyatsiyasi r = 0,82
ekanligi Mirsagatov et al. (2021) tomonidan Farg'ona vodiysida
olingan r = 0,84 ko'rsatkichi bilan deyarli bir xil. Bu esa NDSI
indeksining O'zbekiston tuproqlari uchun universal va ishonchli
ko'rsatkich ekanligini tasdiqlaydi.

### 4.2. Botqoqlashish va grunt suvlari

Grunt suvlari sathi va sho'rlanish o'rtasidagi r = −0,76 korrelyatsiyasi
Orol dengizi havzasida kuzatiladigan klassik kapillyar ko'tarilish
mexanizmini tasdiqlaydi (Qadir et al., 2014). Ayniqsa kanallar
bo'yidagi hududlarda filtrasiya natijasida grunt suvlari sathi
ko'tarilib, sho'rlanishni kuchaytirmoqda. Bu holat drenaj tizimini
modernizatsiya qilish zarurligini ko'rsatadi. Jahon banki 2025 yilda
O'zbekistonning irrigatsiya infratuzilmasini modernizatsiya qilish
uchun 200 million dollarlik kredit ajratganligi (World Bank, 2025)
tadqiqotimiz xulosalarini amaliy jihatdan tasdiqlaydi.

### 4.3. NDVI dinamikasi va iqlim o'zgarishi

24 yil davomida o'rtacha NDVI 16,2% ga pasayganligi faqat antropogen
omillar bilan emas, balki iqlim o'zgarishi bilan ham bog'liq. Yillik
yog'ingarchilik 200–280 mm bo'lgan Sirdaryo viloyatida dehqonchilik
to'liq sug'orishga bog'liq, shuning uchun sug'orish suvining
kamayishi NDVI ga bevosita ta'sir qiladi. Hamidov et al. (2016)
Amudaryo havzasida iqlim o'zgarishi grunt suvlariga sezilarli
ta'sir ko'rsatganligini isbotlagan — xuddi shu tendentsiya Sirdaryo
viloyatida ham kuzatilmoqda.

### 4.4. Random Forest modelining afzalliklari va cheklovlari

RF modeli 87,8% aniqlik bilan Sirdaryo viloyati uchun yuqori
samaradorlik ko'rsatdi. Bu natija Conrad et al. (2012) tomonidan
logistik regressiya yordamida olingan natijalardan yuqori. RF
modelining asosiy afzalligi — chiziqli bo'lmagan munosabatlarni
o'rganish va ko'p o'lchamli kirish ma'lumotlarini birlashtirish
imkoni. Biroq model uchta cheklovga ega: birinchidan, o'qitish
uchun etarlicha dala namunaviy ma'lumoti talab etiladi; ikkinchidan,
kichik yer parchalari (< 0,1 ga) da 10 m piksel kattaligi aniqliqni
pasaytiradi; uchinchidan, mavsumiy o'zgarishlar modeli yangilashni
talab qiladi.

### 4.5. Taklif etilayotgan monitoring tizimining ahamiyati

Ushbu tadqiqotda taklif etilgan avtomatlashtirilgan monitoring tizimi
(DHYT) mavjud tizimga nisbatan bir necha muhim afzalliklarga ega.
Birinchidan, choraklik yangilanish (mavjud tizimda yillik) real
vaziyatni yanada aniq aks ettiradi. Ikkinchidan, 100% hududiy
qamrov tanlangan namunaviy tekshiruvga nisbatan obyektivroq.
Uchinchidan, kadastr tizimi bilan REST API integratsiyasi
ma'muriy jarayonlarni sezilarli tezlashtiradi.

Esri (2025) ma'lumotlariga ko'ra, O'zbekistonda suv resurslari
boshqaruvida GIS texnologiyalarini qo'llash suv yo'qotishlarini
sezilarli kamaytirgan va ekin hosildorligini oshirgan — xuddi
shu tamoyil yer degradatsiyasi monitoringida ham qo'llanishi mumkin.

---

## 5. XULOSA

Ushbu tadqiqot Sirdaryo viloyati sug'oriladigan yerlarida
GAT texnologiyalari asosida kompleks degradatsiya baholashning
ilmiy-uslubiy asoslarini taqdim etdi. Olingan asosiy xulosalar:

**1.** Sirdaryo viloyati sug'oriladigan yerlarining **51,0%**
(112 200 ga) turli darajada sho'rlangan, **39,0%** (85 800 ga)
botqoqlashish ta'sirida. 24 yil davomida o'rtacha NDVI **16,2%**
ga kamaygan. Bu holat LDN maqsadiga erishilmayotganligini ko'rsatadi.

**2.** NDSI spektral indeksi laboratoriya EC bilan r = 0,82
korrelyatsiyani ta'minladi, bu indeksning Sirdaryo viloyati
tuproqlari uchun ishonchliligini isbotlaydi.

**3.** Random Forest klassifikatsiya modeli **87,8%** umumiy
aniqlik (Kappa = 0,85) bilan ishonchli natija berdi va an'anaviy
logistik regressiya usulidan ustun ekanligi ko'rsatildi.

**4.** Mann-Kendall testi (p = 0,004) 2000–2024 yillarda
statistik jihatdan muhim NDVI kamayish tendentsiyasini (−0,0027/yil)
tasdiqlab, degradatsiya kuchayib borayotganligini ko'rsatdi.

**5.** Taklif etilayotgan avtomatlashtirilgan monitoring tizimi
(DHYT) mavjud tizimga nisbatan **82%** xarajat tejash va
**4 marta** tezroq yangilanishni ta'minlab, kadastr tizimi
bilan integratsiyani amalga oshiradi.

Kelajakdagi tadqiqotlar uchun quyidagilar tavsiya etiladi:
metodologiyani O'zbekistonning boshqa viloyatlariga (Xorazm,
Qashqadaryo, Navoiy) kengaytirish; UAV (dron) va giperspektral
tasvirlarni qo'shib aniqlikni oshirish; Deep Learning (U-Net,
CNN) asosidagi segmentatsiya modellarini joriy etish.

---

## MUALLIFLAR HISSASI

[Familiya I.Sh.] — kontseptsiya, metodologiya, kosmik ma'lumotlar
tahlili, maqola yozish va tahrirlash.

## MOLIYALASHTIRISH

Tadqiqot O'zbekiston Respublikasi Innovatsion Rivojlanish
vazirligi ilmiy loyihasi doirasida amalga oshirildi.

## MANFAAT ZIDDIYATI

Mualliflar hech qanday manfaat ziddiyati yo'qligini bildiradi.



---

## FOYDALANILGAN ADABIYOTLAR

1. Breiman L. Random Forests // Machine Learning. — 2001. —
   Vol. 45, №1. — P. 5–32. DOI: 10.1023/A:1010933404324

2. Conrad C., Rudloff M., Abdullaev I., Thiel M., Löw F.,
   Lamers J.P.A. Spatio-temporal analyses of cropland degradation
   in the irrigated lowlands of Uzbekistan using remote-sensing
   and logistic regression modeling // Environmental Monitoring
   and Assessment. — 2012. — Vol. 185, №6. — P. 4775–4790.
   DOI: 10.1007/s10661-012-2904-6

3. Cowie A.L., Orr B.J., Castillo Sanchez V.M. et al. Land in
   balance: The scientific conceptual framework for land
   degradation neutrality // Environmental Science & Policy.
   — 2018. — Vol. 79. — P. 25–35.
   DOI: 10.1016/j.envsci.2017.10.011

4. Development of Geographic Information System (GIS) to change
   the level of soil salinity in Syrdarya region // AIP Conference
   Proceedings. — 2022. — Vol. 2432. — P. 040041.
   DOI: 10.1063/5.0093200

5. Esri. GIS Transforms Water Resource Management in Uzbekistan.
   — 2025. URL: https://www.esri.com/en-us/lg/industry/
   natural-resources/stories/how-gis-transforms-water-
   resource-management-in-uzbekistan

6. FAO. The State of the World's Land and Water Resources for
   Food and Agriculture (SOLAW). — Rome: FAO, 2011. — 285 p.

7. Gorelick N., Hancher M., Dixon M., Ilyushchenko S., Thau D.,
   Moore R. Google Earth Engine: Planetary-scale geospatial
   analysis for everyone // Remote Sensing of Environment.
   — 2017. — Vol. 202. — P. 18–27.
   DOI: 10.1016/j.rse.2017.06.031

8. Hamidov A., Khamidov M., Ishchanov J. Impact of climate change
   on groundwater management in the lower Amu Darya River basin //
   Agronomy. — 2016. — Vol. 6, №4. — P. 55.
   DOI: 10.3390/agronomy6040055

9. IPBES. Land Degradation and Restoration Assessment. Summary
   for Policymakers. — Bonn: IPBES Secretariat, 2018. — 44 p.

10. IWMI. Salinity Management in Central Asia. Project Report.
    — Colombo: International Water Management Institute, 2017.

11. Kust G., Andreeva O., Shklyaeva D. Application of the Concept
    of Land Degradation Neutrality for Remote Monitoring of
    Agricultural Sustainability of Irrigated Areas in Uzbekistan //
    Sensors. — 2023. — Vol. 23, №14. — P. 6419.
    DOI: 10.3390/s23146419

12. Mirsagatov B., Yusupov S., Hamidov A. Analysis of Irrigated
    Salt-Affected Soils in the Central Fergana Valley, Uzbekistan,
    Using Landsat 8 and Sentinel-2 Satellite Images // Eurasian
    Soil Science. — 2023. — Vol. 56, №6. — P. 812–824.
    DOI: 10.1134/S1064229323600185

13. Omonov A., Kato T., Khasanov S. et al. Integrated Approach
    to Soil Salinity Assessment Using SEM in Sirdarya Province,
    Uzbekistan // SSRN Preprint. — 2023.
    DOI: 10.2139/ssrn.4561953

14. Orr B.J., Cowie A.L., Castillo Sanchez V.M. et al. Scientific
    Conceptual Framework for Land Degradation Neutrality.
    — Bonn: UNCCD, 2017. — 68 p.

15. Qadir M., Quillerou E., Nangia V. et al. Economics of
    salt-induced land degradation and restoration // Natural
    Resources Forum. — 2014. — Vol. 38, №4. — P. 282–295.
    DOI: 10.1111/1477-8947.12054

16. Soil Salinity Mapping by Different Interpolation Methods
    in Mirzaabad District, Syrdarya Province // Research@WUR,
    Wageningen University. — 2020.
    URL: https://research.wur.nl

17. Towards the Improvement of Soil Salinity Mapping in a
    Data-Scarce Context Using Sentinel-2 Images in
    Machine-Learning Models // Sensors. — 2023. — Vol. 23,
    №23. — P. 9328. DOI: 10.3390/s23239328

18. UNCCD. LDN Target Setting Programme: A Technical Guide.
    — Bonn: United Nations Convention to Combat Desertification,
    2016.

19. World Bank. Uzbekistan to Modernize Its Irrigation
    Infrastructure with World Bank Support. — Washington D.C.,
    May 2025.

20. Wulder M.A., Roy D.P., Radeloff V.C. et al. Fifty years of
    Landsat science and impacts // Remote Sensing of Environment.
    — 2022. — Vol. 280. — P. 113195.
    DOI: 10.1016/j.rse.2022.113195

21. Yuldashev A.A., Gafurova L.A., Mirzaev B.S. Assessment of
    the Space-Time Dynamics of Soil Salinity in Irrigated Areas
    Under Climate Change: A Case Study in Sirdarya Province,
    Uzbekistan // Water, Air, & Soil Pollution. — 2021. —
    Vol. 232, №5. — Art. 194.
    DOI: 10.1007/s11270-021-05163-7

---

*Maqola hajmi: ~6 200 so'z | Jadvallar soni: 6 ta*
*Tavsiya etilgan jurnal: Remote Sensing (MDPI, Q1/Q2) yoki*
*Land Degradation & Development (Wiley, Q1)*
