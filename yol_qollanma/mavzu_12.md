# 12-MAVZU: ISHLARNI TASHKIL QILISH LOYIHASI VA ISHCHI HUJJATLAR TARKIBI

## 12.1 Kirish

Yo'l qurilishini samarali tashkil etish loyiha muvaffaqiyatining kalitidir. Ishlarni tashkil qilish loyihasi (ITL) qurilish jarayonini boshqarish, resurslarni taqsimlash va muddatlarni nazorat qilish uchun asosiy hujjat hisoblanadi. Ishchi hujjatlar esa qurilishni bevosita amalga oshirish uchun zarur barcha texnik ma'lumotlarni o'z ichiga oladi.

---

## 12.2 Ishlarni Tashkil Qilish Loyihasi (ITL)

### 12.2.1 ITL nima?

**Ishlarni Tashkil Qilish Loyihasi (ITL)** — qurilish jarayonini bosqichma-bosqich rejalashtiruvchi, resurslar va muddatlarni belgilovchi hujjat.

**ITL ning asosiy vazifalari:**
- Ishlarni ketma-ketligini aniqlash
- Mexanizmlar va ishchi kuchini rejalashtirish
- Material va resurslarni ta'minlash
- Qurilish muddatlarini belgilash
- Xarajatlarni nazorat qilish

### 12.2.2 ITL tarkibi

| Bo'lim | Tavsif |
|--------|--------|
| **Umumiy qism** | Loyiha tavsifi, ish hajmlari |
| **Ish usullari** | Har bir tur uchun texnologiya |
| **Kalendar reja** | Muddatlar va ketma-ketlik |
| **Resurslar rejasi** | Mexanizmlar, ishchilar, materiallar |
| **Xarajatlar rejasi** | Oylik/kvartal xarajatlar |
| **Sifat nazorati** | Nazorat nuqtalari |
| **Xavfsizlik** | Mehnat muhofazasi |

---

## 12.3 Qurilish Jarayonining Bosqichlari

### 12.3.1 Tayyorlov ishlari

**1. Hudud tozalash:**
- Daraxtlar va butalar kesish
- Chirindi tuproqni (gumus) chetga olib ketish
- Toshlar va to'siqlarni olib tashlash

**2. Drenaj tizimi qurish:**
- Xandaqlar qazish
- O'tkazgichlar o'rnatish
- Vaqtinchalik suv oqish yo'llarini tashkil etish

**3. Yo'l o'qini belgilash:**
- Geodezik belgilar o'rnatish
- Pik belgilarini qo'yish
- Yo'l chegaralarini belgilash

### 12.3.2 Yer ishlari

**Mashina mexanizmi texnologiyasi:**

```
Ekskavator → Yuklash → Avtosamosval → Tashish → To'kish → Buldozer (tarqatish) → Vibratsion silindr (zichlashtirish)
```

**Yer ishlari tartib-qoidalari:**
1. Tuproqni qatlamlarda to'ldirish (h_qatlam ≤ 30–50 sm)
2. Har qatlamni zichlashtirish (95–98% standart zichlikka)
3. Zichlik tekshiruvi (shtamp sinovlari)
4. Suv rejimini nazorat qilish

### 12.3.3 Poydevor (subbase) ishlari

**Qum-shag'al aralashma:**
- Qalinligi: 20–30 sm
- Motor grader bilan tekislash
- Vibratsion silindr bilan zichlashtirish

**Toshqoplama poydevor:**
- Yirik tosh (macadam): qalinligi 15–20 sm
- Maydalanib presslanadi

### 12.3.4 Qoplama ishlari

**Asfalt-beton qoplama texnologiyasi:**

```
Asfalt zavodi → Asfaltoukладchik (Paver) → Vibratsion silindr → Tamomlash silindr → Sovitish → Foydalanish
```

| Qoplama qatlami | Qalinligi (sm) | Agregat o'lchami |
|-----------------|----------------|-----------------|
| Yuqori qatlam | 3–5 | 0–10 mm |
| O'rta qatlam | 5–8 | 0–20 mm |
| Quyi qatlam | 8–12 | 0–40 mm |

---

## 12.4 Kalendar Reja (Grafik)

### 12.4.1 Gantt diagrammasi

Eng keng tarqalgan kalendar reja turi:

```
Ish nomi          | 1-oy | 2-oy | 3-oy | 4-oy | 5-oy | 6-oy |
------------------|------|------|------|------|------|------|
Tayyorlov ishlari | ████ |      |      |      |      |      |
Yer ishlari       | ████ | ████ | ████ |      |      |      |
Poydevor          |      |      | ████ | ████ |      |      |
Qoplama           |      |      |      | ████ | ████ |      |
Inshootlar        | ████ | ████ | ████ |      |      |      |
Muhandis tizimlar |      |      |      |      | ████ |      |
Tugallash         |      |      |      |      |      | ████ |
```

### 12.4.2 Ish muddatlarini hisoblash

**Yig'im sur'ati:**

$$T = \frac{V_{ish}}{P_{sutkalik}}$$

Bu yerda:
- **T** — ish muddati (sut)
- **V_ish** — ish hajmi (m³, m², dona va h.k.)
- **P_sutkalik** — sutkalik unumdorlik

**Mexanizm unumdorligi:**

$$P = P_{soatlik} \cdot T_{sut} \cdot k_{ish}$$

Bu yerda:
- **P_soatlik** — soatlik unumdorlik (texnik xususiyatlardan)
- **T_sut** = 8 soat (8 soatlik smenada)
- **k_ish** = 0,75–0,85 — vaqtdan foydalanish koeffitsienti

---

## 12.5 Resurslar Rejasi

### 12.5.1 Mehnat resurslari

| Kasb | Soni | Vazifa |
|------|------|--------|
| Ekskavatorchi | 2 | Qazish |
| Buldozerchi | 2 | Tekislash |
| Asfalt ukладчik operatori | 1 | Qoplama |
| Silindr operatori | 2 | Zichlashtirish |
| Geodezist | 1 | Nazorat |
| Quruvchilar | 15–20 | Qo'lda ishlar |
| Praba (Brigadir) | 1 | Boshqarish |

### 12.5.2 Mexanizmlar rejasi

| Mexanizm | Soni | Izoh |
|----------|------|------|
| Ekskavator (0,65 m³) | 2 | Qazish |
| Buldozer (D-9) | 2 | Tekislash |
| Autosamosval (10 t) | 6–8 | Tashish |
| Grader | 1 | Profillashtirish |
| Vibro-silindr | 2 | Zichlashtirish |
| Asfalt paver | 1 | Qoplama |

### 12.5.3 Materiallar rejasi

| Material | Hajm | Etkazib berish muddati |
|----------|------|----------------------|
| Asfalt-beton | V = S × h | Ishdan 2 hafta oldin |
| Shag'al | Smeta bo'yicha | Oldindan |
| Bitum | Smeta bo'yicha | Issiq holda |
| O'tkazgich trubalar | Soni bo'yicha | Montajdan oldin |
| Sement | Ko'priklar uchun | — |

---

## 12.6 Ishchi Hujjatlar Tarkibi

### 12.6.1 Ishchi hujjatlar ro'yxati

Ishchi hujjatlar (Working Documents) bevosita qurilish maydonida foydalaniladigan texnik hujjatlardir.

**Asosiy hujjatlar:**

| Hujjat | Belgi | Tavsif |
|--------|-------|--------|
| **Umumiy chizmalar** | ОЧ | Qarorlar va standartlar |
| **Yo'l rejasi** | ДК | Yo'l o'qi koordinatalari |
| **Bo'ylama profil** | ПП | Loyiha va yer profili |
| **Ko'ndalang kesimlar** | ПК | Har 20–100 m da |
| **Ko'prik loyihasi** | МК | Konstruktsiya chizmalari |
| **O'tkazgich loyihasi** | ТУ | Truba o'lchamlari |
| **Drenaj rejasi** | ДР | Xandaqlar va drenaj |
| **Yo'l kesimining konstruktsiyasi** | ДО | Qatlam tarkibi |
| **Geodezik asoslar** | ГА | Koordinatlar va balandliklar |
| **Smeta** | СМ | Xarajatlar hisob-kitoblari |

### 12.6.2 Yo'l kesimining konstruktsiya chizmasi

```
┌─────────────────────────────────────────┐
│ QOPLAMA KONSTRUKTSIYASI (IV-toifa)      │
├─────────────────────────────────────────┤
│ Yupqa asfalt-beton qatlami    h = 4 sm  │
│ Iri asfalt-beton qatlami      h = 6 sm  │
│ Shag'al-qum aralashma         h = 20 sm │
│ Qumli poydevor                h = 20 sm │
│ Zichlashtirilgan yer asosi              │
└─────────────────────────────────────────┘
       Jami qalinlik: 50 sm
```

### 12.6.3 Geodezik hujjatlar

Qurilish paytida yo'l o'qi aniq koordinatalar bo'yicha belgilanadi.

**Asosiy belgilar:**
- **Osovoy** — yo'l o'qidagi belgi
- **Repyer** — absolut balandlik belgisi
- **Triangulatsiya nuqtasi** — koordinata bazasi

---

## 12.7 Sifat Nazorati va Qabul Qilish

### 12.7.1 Qurilish nazorati turlari

| Tur | Kim bajaradi | Vaqti |
|-----|-------------|-------|
| **Kiruvchi nazorat** | Loyihachi + Buyurtmachi | Material kelganda |
| **Operatsion nazorat** | Brigadir | Har ish bosqichida |
| **Qabul nazorati** | Buyurtmachi + mustaqil lab. | Bosqich tugagach |
| **Davlat nazorati** | Davlat inspektsiyasi | Yakuniy qabul |

### 12.7.2 Asosiy sinov parametrlari

| Parametr | Usul | Me'yor |
|----------|------|--------|
| Nasip zichligi | Shtamp sinovi | ≥ 0,95–0,98 |
| Qoplama tekisligi | 3 m reyka | ≤ 5–6 mm |
| Qoplama qalinligi | Teshib ko'rish | ±15% ruxsat |
| Qoplama mustahkamligi | Yuk sinovlari | Loyiha bo'yicha |
| Geometrik o'lchamlar | Roulетka, total stansiya | ±5–10 cm |

### 12.7.3 Ijro hujjatlari

Qurilish jarayonida **ijro hujjatlari** to'ldiriladi:

- **Ijro rejasi** — haqiqiy o'lchamlar bilan loyiha
- **Yashirin ishlar daftari** — ko'mib ketilgan inshootlar
- **Laboratoriya natijalari** — materiallar sifati
- **Ish jurnali** — kunlik bajarilgan ishlar

---

## 12.8 Atrof-Muhitni Muhofaza Qilish

### 12.8.1 Qurilish davridagi chora-tadbirlar

1. **Tuproq muhofazasi:** Qazilgan tuproqni maxsus joyga to'kish
2. **Suv muhofazasi:** Zovurlarni qurilish materiallaridan himoya
3. **Havo muhofazasi:** Changni kamaytirish (suv sepish)
4. **Shovqin:** Aholi punktlarida tungi ishlarni cheklash
5. **O'simlik muhofazasi:** Yo'l bo'yidagi daraxtlarni saqlash

### 12.8.2 Rekultivatsiya

Qurilish tugagach buzilgan hududlarni qayta tiklash:
- Qazilma joylarni to'ldirish
- O't ekish
- Daraxt ko'chat ekish

---

## 12.9 Xavfsizlik Talablari

### 12.9.1 Mehnat muhofazasi

| Holat | Talab |
|-------|-------|
| Chuqur o'yilmalar (> 1,5 m) | To'siq o'rnatish |
| Tungi ishlar | Yoritish ta'minlash |
| Portlash ishlari | Maxsus ruxsat, ogohlantirish |
| Og'ir mexanizmlar | Xavfsizlik zonasi (r > 5 m) |
| Elektroli ishlar | Izolyatsiyali qo'lqoplar |

### 12.9.2 Traffic Management (Yo'l harakatini boshqarish)

Qurilish paytida yo'l berk bo'lsa:
- Yo'nalish belgilari o'rnatish
- Vaqtinchalik yo'l qurish
- Harakatni tartibga soluvchi qo'yish

---

## 12.10 Amaliy Misol: ITL Tuzish

**Masala:** 5 km IV-toifali yo'l qurilishi uchun soddalashtirilgan ITL tuzilsin.

**Berilgan:**
- Yo'l uzunligi: L = 5 km = 5 000 m
- Yer ishlari: V = 45 000 m³
- Asfalt-beton: S = 5 000 × 6 = 30 000 m²

**Muddatlar hisoblash:**

**1. Yer ishlari (ekskavator + autosamosval):**
- Ekskavator unumdorligi: 500 m³/sut × 2 ta = 1 000 m³/sut
$$T_{yer} = \frac{45\,000}{1\,000} = 45 \text{ sutka}$$

**2. Poydevor (grader + silindr):**
- Grader unumdorligi: 800 m²/sut
$$T_{poydevor} = \frac{30\,000}{800} = 37{,}5 \approx 38 \text{ sutka}$$

**3. Asfalt qoplama (paver):**
- Paver unumdorligi: 1 500 m²/sut
$$T_{asfalt} = \frac{30\,000}{1\,500} = 20 \text{ sutka}$$

**Jami muddat (ketma-ket):** 45 + 38 + 20 = 103 sutka ≈ **3,5 oy**

Parallel ishlash bilan: ≈ **2,5–3 oy** (yer va poydevor bir vaqtda)

---

## 12.11 Nazorat Savollari

1. Ishlarni Tashkil Qilish Loyihasi (ITL) nima va nima uchun zarur?
2. Qurilish bosqichlarini ketma-ketlikda sanab bering.
3. Gantt diagrammasi nima?
4. Ishchi hujjatlar tarkibiga nimalar kiradi?
5. Qurilishda qanday nazorat turlari mavjud?
6. Rekultivatsiya nima va nima uchun amalga oshiriladi?

---

*Barcha mavzular muvaffaqiyatli yakunlandi. Qo'llanma to'liq.*
