# V BOB. NATIJALAR, TAVSIYALAR VA XULOSA

## 5.1. Tadqiqotning asosiy natijalari

### 5.1.1. Ilmiy natijalar xulosasi

Dissertatsiya tadqiqoti davomida quyidagi asosiy ilmiy natijalar olindi:

**1-natija — Degradatsiya holati aniqlandi:**
Farg'ona viloyati sug'oriladigan yerlarining 2000–2024 yillar davomidagi
kompleks GAT tahlili natijasida:
- Sug'oriladigan yerlarning **62,7%** (282 200 ga) turli darajada degradatsiyaga uchragan;
- Faol sug'oriladigan yer maydoni 24 yilda **53 400 ga** ga kamaygan (-13,9%);
- Sho'rlangan yerlar **2 barobarga** oshib 58 600 ga ga yetgan;
- Botqoqlashgan yerlar **2,2 barobarga** oshib 31 200 ga ga yetgan;
- O'rtacha NDVI **16,7%** ga pasaygan (0,412 dan 0,343 ga).

**2-natija — Spektral indekslar validatsiyasi:**
NDSI indeksining laboratoriya EC o'lchovlari bilan korrelyatsiyasi
r = **0,84** (R² = 0,71) ni tashkil etdi. Bu ko'rsatkich NDSI indeksining
O'zbekiston sharoitida sho'rlanishni aniqlashda yuqori ishonchlilikda
ekanligini isbotladi.

**3-natija — LDN baholash:**
UNCCD ning uchta LDN ko'rsatkichi (yer qoplami, yer mahsuldorligi, SOC)
bo'yicha ham viloyat sug'oriladigan yerlarida **yomonlashish tendentsiyasi**
qayd etildi. 2030 yilgacha LDN maqsadiga erishish uchun yiliga kamida
2 500 ga erni rekultivatsiya qilish zarur.

**4-natija — Takomillashtirilgan tizim yaratildi:**
GAT asosidagi yangi degradatsiya hisobi tizimi (DHYT) ishlab chiqildi:
- Har 5–16 kunda avtomatik yangilanadigan monitoring;
- 88% aniqlikdagi Random Forest klassifikatsiya modeli;
- Kadastr tizimi bilan REST API integratsiyasi;
- 85% xarajat tejash, 3–7 marta tezroq ishlash.

---

## 5.2. Taklif etilayotgan tizimning samaradorligi

### 5.2.1. Texnik samaradorlik

| Ko'rsatkich | Mavjud tizim | Yangi tizim (DHYT) | Foyda |
|-------------|-------------|-------------------|-------|
| Yangilanish davri | Yiliga 1 marta | Har 5–16 kunda | **25–70 marta tezroq** |
| Qamrov maydoni | ~15% (namunaviy) | 100% | **To'liq qamrov** |
| Klassifikatsiya aniqligi | Ekspert baholash | 88–89% (RF) | **Standartlashtirilgan** |
| Ma'lumot formati | Qog'oz/Excel | GIS-kadastr DB | **Raqamli, integratsiyalashgan** |
| Xarajat (shartli) | 100% | ~15% | **85% tejash** |
| Prognoz imkoni | Yo'q | 5 yilga | **Yangi imkoniyat** |
| Alert tizimi | Yo'q | Bor | **Yangi imkoniyat** |

### 5.2.2. Iqtisodiy samaradorlik

GAT asosidagi monitoring tizimini joriy etishning taxminiy iqtisodiy samarasi:

- **To'g'ridan-to'g'ri foyda:** Yiliga ~1 260 ga degradatsiyaning oldini olish
  imkoni → o'rtacha hosildorlik asosida taxminiy **2,3 mln USD** iqtisodiy zarar
  oldini olish;
- **Xarajat tejash:** An'anaviy dala tekshiruvi xarajatlariga nisbatan yiliga
  taxminiy **450 000 USD** tejash;
- **Tizimni joriy etish xarajati:** Birinchi yil ~120 000 USD (server, litsenziya,
  o'qitish), keyingi yillarda ~30 000 USD/yil.

---

## 5.3. Amaliy tavsiyalar

### 5.3.1. Davlat organlari uchun tavsiyalar

**O'zbekiston Yer resurslari va davlat kadastr agentligiga:**
1. Sug'oriladigan yerlar kadastrida "Degradatsiya darajasi" (0–4 ball) maydonini
   majburiy ko'rsatkich sifatida joriy etish;
2. GEE platformasi asosidagi avtomatlashtirilgan monitoring tizimini Farg'ona
   viloyatida pilot loyiha sifatida ishga tushirish va keyinchalik barcha
   viloyatlarga kengaytirish;
3. Kadastr tizimining GIS integratsiyasini ta'minlovchi ochiq standartlar
   (OGC WFS/WMS) asosida ma'lumot almashinuv mexanizmini joriy etish.

**Qishloq xo'jaligi va oziq-ovqat xavfsizligi vazirligiga:**
4. Degradatsiyaga uchragan yerlar egalariga maqsadli subsidiyalar va
   agronomik yordam ko'rsatish dasturini ishlab chiqish;
5. Sug'orish normalari va drenaj standartlarini GAT monitoring natijalari
   asosida viloyat bo'yicha differentsiyalash.

**Ekologiya, tabiatni muhofaza qilish va iqlim o'zgarishi vazirligiga:**
6. LDN maqsadlari bo'yicha milliy hisobotni GAT ma'lumotlari asosida
   tayyorlash metodologiyasini standartlashtirish;
7. UNCCD va FAO bilan hamkorlikda degradatsiya monitoringi bo'yicha
   xalqaro ma'lumotlar almashinuvini yo'lga qo'yish.

### 5.3.2. Irrigatsiya tashkilotlari uchun tavsiyalar

8. Grunt suvlari sathi 1,5 m dan ko'tarilgan hududlarda zudlik bilan
   drenaj tizimini kuchaytirish;
9. Kanallar bo'ylab 500 m zonada sho'rlanishga qarshi maxsus agrotexnik
   tadbirlar (yuvish, gips qo'llash) rejasini ishlab chiqish;
10. Sug'orish jadvallarini NDWI ko'rsatkichlari asosida optimallash.

### 5.3.3. Fermerlar uchun tavsiyalar

11. Sho'rlangan (NDSI > 0,15) hududlarda tuzga chidamli ekin navlarini
    (arpa, sorgo, qand lavlagi) joriy etish;
12. Degradatsiyaga uchragan yer parchalari uchun alohida agrotexnik reja
    tuzish va monitoring jurnalini yuritish;
13. Qo'shni fermerlar bilan hamkorlikda kollektiv drenaj tizimini yaratish.

---

## 5.4. Tadqiqotning cheklovlari va kelajak yo'nalishlari

### 5.4.1. Tadqiqotning cheklovlari

1. Tadqiqot bitta viloyat (Farg'ona) bilan cheklangan; boshqa viloyatlarda
   natijalar farqlanishi mumkin;
2. Dala validatsiyasi 120 ta nuqta bilan o'tkazilgan; kattaroq namunaviy
   hajm aniqlikni oshirishi mumkin;
3. Iqtisodiy samaradorlik hisob-kitoblari taxminiy xarakterdadir.

### 5.4.2. Kelajak tadqiqot yo'nalishlari

1. **Kengaytirish** — metodologiyani O'zbekistonning barcha sug'oriladigan
   viloyatlariga (Xorazm, Qashqadaryo, Surxondaryo) qo'llash;
2. **Chuqurlashtirish** — Hyperspectral tasvirlar (PRISMA, DESIS) va
   UAV (dron) ma'lumotlarini qo'shish orqali aniqlikni oshirish;
3. **AI integratsiyasi** — Deep Learning (CNN, U-Net) asosidagi
   segmentatsiya modellarini joriy etish;
4. **Mobil ilova** — Dala inspektorlari uchun Android/iOS ilovasi yaratish;
5. **Markaziy Osiyo miqyosi** — Qozog'iston, Tojikiston, Turkmaniston bilan
   mintaqaviy monitoring tarmog'ini shakllantirish.

---

## 5.5. Umumiy xulosa

Mazkur dissertatsiya tadqiqoti "Sug'oriladigan yerlar degradatsiyasini hisobini
yuritishni GAT texnologiyalari asosida takomillashtirish" mavzusida olib borildi
va quyidagi asosiy xulosalar shakllandi:

**1.** O'zbekiston sug'oriladigan yerlarida, xususan Farg'ona viloyatida, yer
degradatsiyasi — sho'rlanish, botqoqlashish va o'simlik qoplami pasayishi —
jiddiy muammo bo'lib, 24 yil davomida doimiy yomonlashish tendentsiyasi kuzatildi.
Sug'oriladigan yerlarning 62,7 foizi turli darajada degradatsiyaga uchragan.

**2.** Masofadan zondlash ma'lumotlari (Landsat 8/9, Sentinel-2) va spektral
indekslar (NDVI, NDSI, NDWI, SI) kombinatsiyasi sug'oriladigan yerlar degradatsiyasini
yuqori aniqlikda (89,3%, Kappa = 0,86) aniqlash imkonini beradi va an'anaviy
dala usullariga samarali muqobil hisoblanadi.

**3.** LDN kontseptsiyasining uchta ko'rsatkichi bo'yicha baholash sug'oriladigan
yerlar holatini tizimli tahlil qilish uchun ishonchli metodologik asos yaratadi
va O'zbekistonning SDG 15.3 bo'yicha xalqaro majburiyatlarini bajarishga xizmat qiladi.

**4.** Taklif etilgan GAT asosidagi degradatsiya hisobi tizimi (DHYT) mavjud
tizimning asosiy kamchiliklarini bartaraf etib, monitoring davriyligini keskin
oshiradi (yiliga 1 martadan har 5–16 kunga), to'liq hududiy qamrovni ta'minlaydi
va kadastr tizimi bilan avtomatik integratsiyani amalga oshiradi.

**5.** Tadqiqot natijalari O'zbekiston yer resurslarini boshqarish amaliyotiga
bevosita tatbiq etilishi mumkin bo'lib, sug'oriladigan yerlar degradatsiyasini
kamaytirish, qishloq xo'jaligi mahsuldorligini oshirish va LDN maqsadlariga
erishishga muhim hissa qo'shadi.

Dissertatsiyada ilgari surilgan ilmiy yangiliklar, amaliy tavsiyalar va ishlab
chiqilgan tizim modeli sug'oriladigan yerlar degradatsiyasini hisobini yuritish
sohasida keyingi ilmiy tadqiqotlar uchun poydevor bo'lib xizmat qiladi.

---

*Adabiyotlar ro'yxati VII bobda keltirilgan.*
