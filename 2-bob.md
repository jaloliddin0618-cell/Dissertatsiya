# II BOB. SUG'ORILADIGAN YERLAR DEGRADATSIYASINI ANIQLASH VA HISOB OLISHNING USLUBIY ASOSLARI

## § 2.1. Sug'oriladigan yerlar degradatsiyasini aniqlashning ilmiy-uslubiy asoslari

### 2.1.1. Degradatsiyani aniqlashning an'anaviy uslublari

Sug'oriladigan yerlar degradatsiyasini aniqlashda an'anaviy va zamonaviy
uslublar bir-birini to'ldiradi. An'anaviy uslublar asosan quyidagilardan iborat:

**Dala tekshiruvi (field survey):**
Mutaxassislar bevosita dala sharoitida tuproq namunalarini oladi va
ko'zga ko'rinadigan degradatsiya belgilarini qayd etadi. Bu uslub
eng aniq natija beradi, ammo katta vaqt va moliyaviy xarajat talab qiladi,
keng hududlarni qamrab olish imkoni esa cheklangan.

Dala tekshiruvi ko'rsatkichlari:
- Tuproq yuzasida tuz kristallarining ko'rinishi;
- O'simlik qoplamining seyraklanishi yoki yo'qligi;
- Tuproq rangining o'zgarishi (oqarib ketish — sho'rlanish belgisi);
- Grunt suvlari sathini kuzatuv quduqlari orqali o'lchash.

**Laboratoriya tahlili:**
Dala tekshiruvi jarayonida olingan tuproq namunalari
laboratoriyada quyidagi ko'rsatkichlar bo'yicha tahlil qilinadi:

| Ko'rsatkich | O'lchov birligi | Ahamiyati |
|-------------|----------------|-----------|
| EC (elektr o'tkazuvchanligi) | dS/m | Sho'rlanish darajasi |
| pH | — | Tuproq muхiti |
| Natriy, Xlorid, Sulfat | mg/kg | Tuz tarkibi |
| Organik modda | % | Tuproq unumdorligi |
| Mexanik tarkib | % | Tuproq teksturasi |
| Grunt suvlari mineralizatsiyasi | g/l | Sho'rlanish manbai |

**Kartografik uslub:**
An'anaviy uslubda dala ma'lumotlari asosida qog'oz yoki raqamli
xaritalar tuziladi. Biroq bu xaritalar tezda eskirib qoladi va
muntazam yangilanishni talab qiladi.

### 2.1.2. Zamonaviy GAT asosidagi uslublar

GAT texnologiyalari an'anaviy uslublarning kamchiliklarini bartaraf etib,
degradatsiyani yanada samarali aniqlash imkonini beradi.

**Masofadan zondlash asosidagi uslub:**
Kosmik tasvirlardan hisoblangan spektral indekslar tuproq va o'simlik
holatini bevosita aks ettiradi. Bu uslubning asosiy bosqichlari:

```
1-bosqich: Kosmik tasvir yuklash (Landsat/Sentinel)
           │
           ▼
2-bosqich: Geometrik va atmosfera korreksiyasi
           │
           ▼
3-bosqich: Spektral indekslar hisoblash (NDVI, NDSI, NDWI)
           │
           ▼
4-bosqich: Klassifikatsiya (supervised/unsupervised)
           │
           ▼
5-bosqich: Xarita tuzish va vizualizatsiya
           │
           ▼
6-bosqich: Dala ma'lumotlari bilan tekshirish (validatsiya)
```

**IDW interpolatsiya uslubi:**
Sirdaryo viloyatida o'tkazilgan tadqiqotlar (Yuldashev et al., 2021)
shuni ko'rsatdiki, kuzatuv quduqlari ma'lumotlari asosida IDW
(Inverse Distance Weighting) interpolatsiya uslubi yordamida
tuproq sho'rlanishi xaritasini tuzish yuqori aniqlikni ta'minlaydi
(RMSE = 1,18 dS/m). IDW formulasi:

```
Z(x) = Σ[Z(xᵢ) / d(x,xᵢ)ᵖ] / Σ[1 / d(x,xᵢ)ᵖ]

bu yerda:
  Z(x)    — interpolatsiya qilinayotgan nuqta qiymati
  Z(xᵢ)   — ma'lum nuqta qiymati
  d(x,xᵢ) — masofа
  p        — og'irlik daraja (odatda p = 2)
```

**Ko'p mezonli tahlil (MCDA):**
Degradatsiya xavfini baholashda bir necha omillarni og'irlikli
birlashtirish uslubi (Weighted Linear Combination):

```
D = W₁×Sho'rlanish + W₂×Botqoqlashish + W₃×NDVI_kamayish + ...
```

### 2.1.3. Degradatsiya indikatorlari tizimi

Sug'oriladigan yerlar degradatsiyasini kompleks baholash uchun
quyidagi indikatorlar tizimi qo'llanilishi tavsiya etiladi:

**Bevosita indikatorlar (to'g'ridan-to'g'ri o'lchanadigan):**

| Indikator | O'lchov usuli | Maqbul chegara |
|-----------|--------------|----------------|
| Tuproq sho'rlanishi (ECe) | Lab. tahlil / NDSI | < 4 dS/m |
| Grunt suvlari sathi | Kuzatuv quduqlari | > 1,5 m |
| NDVI qiymati | Kosmik tasvir | > 0,3 |
| Botqoqlashish maydoni | NDWI / GIS | 0% |
| Tashlab ketilgan yer | Yer qoplami tasnifi | 0% |

**Bilvosita indikatorlar (hisob-kitob yo'li bilan):**

| Indikator | Hisoblash formulasi | Maqsad |
|-----------|---------------------|--------|
| LPD (Yer mahsuldorligi dinamikasi) | NDVI vaqt qatori moyili | Uzoq muddatli trend |
| Sho'rlanish o'sish tezligi | ΔS/Δt | Dinamika |
| Degradatsiya indeksi | f(ECe, GWT, NDVI) | Kompleks ball |

### 2.1.4. Degradatsiya darajasini tasniflash tizimi

Dissertatsiyada quyidagi besh darajali tasniflash tizimi qo'llaniladi:

| Daraja | Ball | Tavsif | Chora-tadbir |
|--------|------|--------|-------------|
| Degradatsiyasiz | 0 | Barcha ko'rsatkichlar normada | Oddiy monitoring |
| Kuchsiz | 1 | 1–2 ko'rsatkich chegarada | Kuzatish kuchaytirish |
| O'rtacha | 2 | 2–3 ko'rsatkich yomon | Agrotexnik tadbirlar |
| Kuchli | 3 | 3–4 ko'rsatkich yomon | Melioratsiya ishlari |
| Juda kuchli | 4 | Barcha ko'rsatkichlar yomon | Rekultivatsiya |

---

## § 2.2. Degradatsiyaga uchragan sug'oriladigan yerlarni tahlil qilish bo'yicha xorijiy tajribalar va ularni O'zbekistonda qo'llash imkoniyatlari

### 2.2.1. Misr tajribasi — Nil deltasida GIS asosidagi monitoring

Misr — dunyodagi eng katta sug'oriladigan hudud bo'lmish Nil deltasida
yer degradatsiyasi muammosi O'zbekistonga juda o'xshash. Misr tajribasida
quyidagi asosiy yondashuvlar ishlab chiqilgan:

**Gidro-sho'rlanish baholash tizimi (Amer, 2021; Remote Sensing MDPI):**
Nil deltasida Sentinel-2 va Landsat ma'lumotlari yordamida sug'orish
suvi sho'rlanganligi, botqoqlashish va ekin yerlari degradatsiyasining
makoniy bog'liqligi o'rganildi. Tadqiqot natijalari:
- Sentinel-2 tasvirlari sho'rlanishni aniqlashda 85% aniqlik berdi;
- Sug'orish suvi sifati va tuproq sho'rlanganligi o'rtasida kuchli
  korrelyatsiya (r = 0,81) aniqlandi;
- Botqoqlashish va sho'rlanish klasterlari kanallar bo'yida to'planadi.

**O'zbekistonga qo'llash imkoniyati:** Sirdaryo bo'yi hududlari va
magistral kanallar atrofida xuddi shunday klaster tahlili o'tkazish
mumkin. Sirdaryo daryosi bo'yidagi yerlar tarkibi Nil deltasiga
o'xshash xususiyatlarga ega.

### 2.2.2. Hindiston tajribasi — Haryona shtatida GIS asosidagi hisob

Hindistonning Haryona shtati (shimoli-g'arb) O'zbekistonga o'xshash
yarim qurg'oq iqlim va sug'oriladigan dehqonchilik bilan xarakterlanadi.

**GIS va melioratsiya boshqaruvi:**
Hindistonda Uttar Pradesh Bhumi Sudhar Nigam (Yer isloh qilish
tashkiloti) GIS texnologiyalarini dehqonchilik yerlarini boshqarishda
muvaffaqiyatli qo'llaydi:
- Tuproq sho'rlanganligi, grunt suvlari va ekin holati haqidagi
  ma'lumotlar yagona GIS platformasida birlashtirilgan;
- Fermer parchalari darajasida degradatsiya xaritasi tuzilgan;
- Natijalar kadastr ma'lumotlari bilan bog'langan.

**O'zbekistonga qo'llash imkoniyati:** Yer parchalari darajasida
degradatsiya ballini kadastr tizimiga kiritish — Hindiston modelini
bevosita qo'llash mumkin bo'lgan yo'nalish.

### 2.2.3. Janubiy Afrika tajribasi — sug'orish sxemalarida monitoring

Janubiy Afrikada botqoqlashish va tuz to'planishini kuzatish uchun
ishlab chiqilgan metodologiya (ResearchGate, 2016) quyidagi
elementlarni o'z ichiga oladi:
- **Yer qoplami xaritalash** — Landsat yordamida;
- **Yalang'och tuproq tahlili** (bare soil analysis) — vegetatsiya
  davridan tashqarida ko'proq aniqlik beradi;
- **Ko'p vaqtli ekin holati monitoringi** — NDVI vaqt qatori;
- **Relyef tahlili** — botqoqlashish xavfi past joylarda yuqori;
- **Qaror daraxti tahlili** (decision tree) — degradatsiya
  sabablarini aniqlash uchun.

**O'zbekistonga qo'llash imkoniyati:** Mirzacho'lning tekis relyefida
botqoqlashish relyef bilan kam bog'liq — lekin kanal joylashuvi
va drenaj tizimi tahlili bu yondashuvdan foydalanishga imkon beradi.

### 2.2.4. Italiya (Basilicata) tajribasi — GIS va masofadan zondlash kombinatsiyasi

Basilicata mintaqasida (Springer, 2022) iqlim o'zgarishi bilan
bog'liq yer degradatsiyasini kuzatish uchun GIS va masofadan zondlash
kombinatsiyalashtirilgan tizim ishlab chiqildi. Asosiy xususiyatlari:
- Tuproq eroziyasi, sho'rlanish va organik uglerod yo'qolishi
  bir vaqtda baholanadi;
- 20 yillik Landsat arxivi tendentsiya tahlili uchun ishlatilgan;
- Natijalar mahalliy hokimiyat va muhofaza qilish rejalashtirish
  uchun amaliy vosita sifatida qo'llanilmoqda.

**O'zbekistonga qo'llash imkoniyati:** Ko'p yillik arxiv tahlili
va mahalliy hokimiyat bilan integratsiya — bevosita qo'llanishi
mumkin bo'lgan tajriba.

### 2.2.5. Xorijiy tajribalarning qiyosiy tahlili

| Mamlakat | Qo'llangan texnologiya | Asosiy yutuq | O'zbekistonga mosligi |
|----------|----------------------|-------------|----------------------|
| Misr | Sentinel-2 + GIS klaster tahlil | Kanal bo'yida sho'rlanish aniqlash | Yuqori |
| Hindiston | GIS + kadastr integratsiya | Fermer parsel darajasida hisob | Juda yuqori |
| Janubiy Afrika | Ko'p vaqtli NDVI + qaror daraxti | Avtomatlashtirilgan tasnif | O'rtacha |
| Italiya | Landsat arxivi + tendentsiya | Ko'p yillik tahlil | Yuqori |
| O'zbekiston (Conrad et al., 2012) | Landsat + logistik regressiya | Degradatsiya xaritalash | To'g'ridan-to'g'ri |

**Xulosa:** Xorijiy tajribalar shuni ko'rsatadiki, eng samarali yondashuv —
masofadan zondlash, GIS va kadastr tizimining integratsiyasi bo'lib,
Sirdaryo viloyatida ham aynan shu yondashuvni qo'llash maqsadga muvofiqdir.

---

## § 2.3. Degradatsiyaga uchragan sug'oriladigan yerlarni hisobga olishning uslubiy asoslari

### 2.3.1. Hisob yuritishning davlat standartlari va normativ hujjatlari

O'zbekistonda sug'oriladigan yerlar degradatsiyasini hisobga olish
quyidagi normativ-huquqiy hujjatlar asosida tartibga solinadi:

- O'zR "Yer to'g'risida"gi Qonuni (1998, o'zgartishlar bilan);
- O'zR "Davlat yer kadastri to'g'risida"gi Qonuni;
- O'zR Vazirlar Mahkamasi qarorlari: yer kadastrini yuritish tartibi;
- O'zR Davkadastr tomonidan tasdiqlangan "Yerlar sifatini baholash
  metodikasi" (ball boniteti tizimi);
- GOST 17.4.3.02-85 — Tuproqni muhofaza qilish davlat standarti.

**Ball boniteti tizimi:**
Hozirgi kunda O'zbekistonda yerlar sifati asosan "ball boniteti"
ko'rsatkichi bilan baholanadi. Bu ko'rsatkich tuproqning tabiiy
xususiyatlarini (granulometrik tarkib, gumus miqdori, sho'rlanish
darajasi va h.k.) hisobga olgan holda 0 dan 100 gacha ball bilan
ifodalanadi. Biroq ball boniteti:
- 3–5 yilda bir marta yangilanadi (real vaqt emas);
- GAT texnologiyalari bilan bog'lanmagan;
- Dinamika va tendentsiyalarni ko'rsatmaydi.

### 2.3.2. LDN asosidagi hisob yuritish metodologiyasi

Xalqaro miqyosda UNCCD tomonidan ishlab chiqilgan LDN (Land
Degradation Neutrality) metodologiyasi — hozirgi kunda eng ilg'or
va keng qabul qilingan yondashuv hisoblanadi. LDN uslubiyati
uchta asosiy ko'rsatkichni talab qiladi:

**1. Yer qoplami o'zgarishi (Land Cover Change — LCC):**
- Manba: MODIS MCD12Q1 yoki Landsat ma'lumotlari;
- Hisoblash: ikki davr orasidagi o'zgarish matritsasi;
- O'lchov: degradatsiyalashgan yer maydoni (ga yoki %);
- Davriylik: har 1–5 yilda yangilash.

**2. Yer mahsuldorligi dinamikasi (Land Productivity Dynamics — LPD):**
- Manba: MODIS MOD13Q1 — 16 kunlik NDVI kompoziti;
- Hisoblash: Mann-Kendall tendentsiya testi NDVI vaqt qatori bo'yicha;
- Tasnif: yaxshilanmoqda / barqaror / yomonlashmoqda;
- Davriylik: yillik yangilash.

**3. Tuproq organik uglerod (Soil Organic Carbon — SOC):**
- Manba: RothC modeli yoki WoSIS ma'lumotlar bazasi;
- Hisoblash: t C/ha;
- Davriylik: 5–10 yilda bir marta.

### 2.3.3. Taklif etilayotgan hisob yuritish tizimining uslubiy asoslari

Ushbu dissertatsiyada Sirdaryo viloyati uchun taklif etilayotgan
degradatsiya hisobi tizimining uslubiy asosi quyidagi tamoyillarga
asoslanadi:

**1. Komplekslilik tamoyili:**
Faqat bitta degradatsiya turi emas, balki sho'rlanish, botqoqlashish
va o'simlik degradatsiyasi bir vaqtda baholanadi.

**2. Davriylik tamoyili:**
Yiliga 1 marta emas, balki har chorakda (yiliga 4 marta) yangilash
ta'minlanadi.

**3. Integratsiyalik tamoyili:**
Degradatsiya ma'lumotlari kadastr tizimiga avtomatik uzatiladi
va har bir yer parsel uchun degradatsiya bali hisoblanadi.

**4. Validatsiya tamoyili:**
Har bir yangilash dala tekshiruvi ma'lumotlari bilan taqqoslanadi
va aniqlik baholanadi.

**5. Shaffoflik tamoyili:**
Barcha hisob-kitob metodlari va natijalar ochiq bo'lib, tegishli
organlarga hisobot sifatida taqdim etiladi.

### 2.3.4. Ma'lumotlarni yig'ish va birlashtirish uslubiyati

Dissertatsiya tadqiqotida quyidagi ma'lumotlar manbalari
integratsiyalashtiriladi:

```
┌──────────────────────────────────────────────────────┐
│              MA'LUMOTLAR MANBALARI                    │
├─────────────┬─────────────────────┬──────────────────┤
│  KOSMIK     │     DALA            │    KADASTR       │
│  MA'LUMOT   │     MA'LUMOT        │    MA'LUMOT      │
├─────────────┼─────────────────────┼──────────────────┤
│ Landsat 8/9 │ Tuproq namunalari   │ Yer parchalari   │
│ Sentinel-2  │ EC o'lchash         │ Ball boniteti    │
│ MODIS NDVI  │ Grunt suvi chuqurl. │ Ekin rejimi      │
│ Sentinel-1  │ GPS koordinatalari  │ Mulkchilik holati│
│ DEM relyef  │ Lab. tahlil         │ Foydalanish turi │
└─────────────┴─────────────────────┴──────────────────┘
                        │
                        ▼
              MARKAZIY GIS PLATFORMA
                (PostGIS / QGIS)
                        │
                        ▼
              DEGRADATSIYA XARITASI
                        │
                        ▼
              KADASTR YANGILASH
```

### 2.3.5. Validatsiya uslubiyati

Olingan natijalarning ishonchliligini baholash uchun quyidagi
statistik ko'rsatkichlar hisoblanadi:

**Xatolar matritsasi (Confusion Matrix)** — klassifikatsiya
aniqligi baholash uchun asosiy vosita.

**Umumiy aniqlik (Overall Accuracy):**
```
OA = (To'g'ri tasniflangan piksellar soni) / (Jami piksellar) × 100%
```
Maqbul chegara: OA ≥ 85%

**Kappa koeffitsienti (Cohen's Kappa):**
```
K = (Po − Pe) / (1 − Pe)
```
Maqbul chegara: K ≥ 0,80

**RMSE — kvadrat o'rtacha xato:**
```
RMSE = √(Σ(yᵢ − ŷᵢ)² / n)
```
Sho'rlanish uchun maqbul chegara: RMSE ≤ 1,5 dS/m

**Pearson korrelyatsiyasi (r):**
Spektral indeks (NDSI) va laboratoriya EC qiymatlari
o'rtasidagi bog'liqlikni aniqlash uchun.
Maqbul chegara: r ≥ 0,75

---

## Ikkinchi bob bo'yicha xulosa

II bob bo'yicha quyidagi asosiy xulosalar shakllandi:

1. Sug'oriladigan yerlar degradatsiyasini aniqlashning ilmiy-uslubiy
   asosi dala tekshiruvi, laboratoriya tahlili va GAT texnologiyalari
   kombinatsiyasidan iborat bo'lib, har bir uslubning o'z afzalliklari
   va cheklovlari mavjud;

2. IDW interpolatsiya, ko'p mezonli tahlil va spektral indekslar
   kombinatsiyasi Sirdaryo viloyati sharoitida degradatsiyani
   aniqlashning eng samarali uslubiy yondashuvi hisoblanadi;

3. Misr, Hindiston, Janubiy Afrika va Italiya tajribasi shuni
   ko'rsatadiki, masofadan zondlash va GIS-kadastr integratsiyasi
   — yer degradatsiyasini hisobga olishning zamonaviy va samarali
   yondashuvi bo'lib, O'zbekiston sharoitida ham muvaffaqiyatli
   qo'llanishi mumkin;

4. LDN metodologiyasi (yer qoplami, LPD, SOC) yer degradatsiyasini
   tizimli baholash uchun xalqaro miqyosda tan olingan asos bo'lib,
   bu dissertatsiyada qo'llaniladigan takomillashtirilgan tizim
   shu metodologiyaga asoslanadi;

5. Taklif etilayotgan tizimning uslubiy asosi beshta tamoyilga
   (komplekslilik, davriylik, integratsiyalik, validatsiya,
   shaffoflik) asoslanib, mavjud tizimning barcha asosiy
   kamchiliklarini bartaraf etishga yo'naltirilgan.

---

*Foydalanilgan adabiyotlar ro'yxati dissertatsiya oxirida keltirilgan.*
