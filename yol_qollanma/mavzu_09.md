# 9-MAVZU: ELEKTRON DASTURLARDAN FOYDALANISH VA YER ISHLARI HAJMI

## 9.1 Kirish

Zamonaviy yo'l loyihalash elektron dasturlarsiz tasavvur qilib bo'lmaydi. Kompyuter dasturlari qo'lda hisoblash vaqtini sezilarli kamaytiradi, xatolar sonini kamaytiradi va loyiha sifatini oshiradi. Yer ishlari hajmini aniq hisoblash esa loyihaning moliyaviy asosi hisoblanadi.

---

## 9.2 Yo'l Loyihalashda Ishlatiladigan Dasturlar

### 9.2.1 AutoCAD Civil 3D (Autodesk)

Eng keng tarqalgan professional dastur.

**Asosiy imkoniyatlar:**
- Raqamli yer modeli (DEM) yaratish
- Bo'ylama va ko'ndalang profillar
- Yer ishlari hajmini avtomatik hisoblash
- Yo'l o'qi koordinatalarini hisoblash
- 3D vizualizatsiya

**Asosiy buyruqlar:**
```
CREATEALIGNMENT   → yo'l o'xi yaratish
CREATEPROFILE     → profil yaratish
CREATESURFACE     → yer yuzasini modellashtirish
EARTHWORKVOLUME   → yer ishlari hajmini hisoblash
```

### 9.2.2 ROBUR (Rossiyadan)

O'rta Osiyo va MDH mamlakatlarida keng qo'llaniladigan dastur.

**Afzalliklari:**
- O'zbek/Rus normativlariga moslashtirilgan
- Bo'ylama loyiha chizig'i avtomatik hisoblash
- Smetalar tuzish moduli

### 9.2.3 IndorCAD / IndorRoad

Rusiyada ishlab chiqilgan, O'rta Osiyoda ham qo'llaniladi.

**Imkoniyatlar:**
- Yo'l loyihalashning barcha bosqichlari
- Yer ishlari va transport hisoblari
- Tuproqni tashish uzoqligini hisoblash

### 9.2.4 QGIS + OpenRoads

Ochiq kodli GIS bilan kombinatsiya:
- Topografik tahlil
- Suv havzalari modeli
- Yo'l varianti tanlash

### 9.2.5 Excel va dasturlash

Oddiy hisoblashlar uchun:
- Yer ishlari hajmi hisob-kitoblari
- Massa diagrammasi (Masse diagramm)
- Moliyaviy hisob-kitoblar

---

## 9.3 Yer Ishlari Hajmini Aniqlash

### 9.3.1 Yer ishlari turlari

| Tur | Tavsif |
|-----|--------|
| **O'yish (excavation)** | Tuproqni kesilgan joydan olib tashlash |
| **To'ldirish (fill)** | Nasip uchun tuproq qo'yish |
| **Tashish (haulage)** | Tuproqni bir joydan ikkinchisiga ko'chirish |
| **Zichlashtirish** | Nasipni mexanik zichlashtirish |

### 9.3.2 Ko'ndalang kesim maydoni hisoblash

**Nasip kesimi (trapetsiya):**

$$F_{nasip} = \frac{(B + B + 2mH)}{2} \cdot H = (B + mH) \cdot H$$

**O'yilma kesimi (trapetsiya):**

$$F_{oyilma} = (B + mH) \cdot H + F_{xandak}$$

Bu yerda:
- **B** — yo'l asosi eni (m)
- **m** — yon nishablik koeffitsienti
- **H** — nasip balandligi yoki o'yilma chuqurligi (m)

### 9.3.3 Hajmni hisoblash (Prismatoid metodi)

Ikkita kesim orasidagi hajm:

$$V = \frac{L}{6} \cdot (F_1 + 4 \cdot F_{o'rta} + F_2)$$

Bu yerda:
- **L** — kesimlar orasidagi masofa (m)
- **F₁, F₂** — uchdagi kesim maydonlari (m²)
- **F_o'rta** — o'rta kesimdagi maydon (m²)

**Sodda formula (trapetsiya usuli):**

$$V = \frac{(F_1 + F_2)}{2} \cdot L$$

### 9.3.4 Nol nuqtalarda hajm hisoblash

Nasipdan o'yilmaga o'tish joyida (nol nuqta):

$$V_{uchburchak} = \frac{F \cdot x}{2}$$

Bu yerda **x** — nol nuqtagacha masofa.

---

## 9.4 Massa Diagrammasi (Maslov Diagrammasi)

### 9.4.1 Maqsad

Massa diagrammasi — yo'l bo'ylab to'plangan yer hajmini ko'rsatuvchi grafik. U tuproqni qaerdan qazib, qayerga tashishni aniqlashga yordam beradi.

### 9.4.2 Diagramma qurish

**1-qadam:** Har pikdagi hajmni hisoblash (+nasip, −o'yilma)

**2-qadam:** Kumulyativ (yig'ma) hajm hisoblash:

$$V_{yig'ma,i} = V_{yig'ma,i-1} + V_i$$

**3-qadam:** Grafikda piklar vs yig'ma hajmni chizish

### 9.4.3 Diagrammani o'qish

```
V (m³)
  |          *
  |        *   *
  |      *       *
--+----*-----------*----→ L (m)
  |                  *
  |                    *
```

- **Yuqoriga ketish** → O'yilma (qazish ortib bormoqda)
- **Pastga ketish** → Nasip (to'ldirish)
- **Gorizontal chiziq kesishi** → Nol nuqta (nasip↔o'yilma o'tish)
- **Maksimum nuqta** → O'yilma tugaydi, nasip boshlanadi

### 9.4.4 Maqbul tashish masofasi

Massa diagrammasida gorizontal "kompensatsiya chizig'i" chiziladi. Bu chiziq ostidagi va ustidagi maydonlar tashish hajmini ifodalaydi.

**Iqtisodiy tashish masofasi (L_iqt):**

$$L_{iqt} = \frac{C_{qazish} + C_{to'ldirish}}{c_{tashish}}$$

Bu yerda:
- **C_qazish** — 1 m³ tuproq qazish narxi
- **C_to'ldirish** — 1 m³ to'ldirish narxi
- **c_tashish** — 1 m³·km tashish narxi

---

## 9.5 Tuproqni Tashish Uzoqligini Aniqlash

### 9.5.1 O'rtacha tashish masofasi

$$L_{tashish} = \frac{\sum V_i \cdot L_i}{\sum V_i}$$

Bu yerda:
- **V_i** — i-qismdan tashiladigan hajm (m³)
- **L_i** — i-qismning tashish masofasi (m)

### 9.5.2 Tashish variantlari

**Holat 1: Ichki tashish**
Qazilgan tuproq bir piketdan ikkinchisiga tashiladi (iqtisodiy).

**Holat 2: Yon manbadan tashish (borrow pit)**
Yo'l yon tomonida maxsus karerdan tuproq tashiladi.

**Holat 3: Tashlab ketish (waste dump)**
Ortiqcha tuproq maxsus joyga tashiladi.

### 9.5.3 Tashish uzoqligi kategoriyalari

| Masofa | Mexanizm | Narx darajasi |
|--------|----------|---------------|
| 0–50 m | Buldozer | Past |
| 50–500 m | Skraper | O'rta |
| 500–5 000 m | Avtosamosvol | Yuqori |
| > 5 000 m | Konveyer/poyezd | Juda yuqori |

---

## 9.6 Mexanizatsiya Vositalari

### 9.6.1 Asosiy mexanizmlar

| Mexanizm | Qo'llanish | Unumdorlik |
|----------|------------|------------|
| **Ekskavator** | Qazish, tuproq yuklash | 100–500 m³/soat |
| **Buldozer** | Qazish, siljitish (< 50 m) | 50–200 m³/soat |
| **Skraper** | Qazish + tashish (50–500 m) | 80–300 m³/soat |
| **Autosamosval** | Tashish (> 500 m) | Hajmga bog'liq |
| **Grayfer** | Qattiq tuproq, tosh | 30–100 m³/soat |
| **Vibratsion zichlash** | Nasip zichlashtirish | — |

### 9.6.2 Mexanizm tanlash mezonlari
- Tuproq turi (qum, gil, qoya)
- Tashish masofasi
- Ish hajmi
- Ish sharoitlari (qishloq/shahar)

---

## 9.7 Yer Ishlari Hajmini Hisoblash Jadvali (Namuna)

| Pik | Masofa (m) | F_nasip (m²) | F_oyilma (m²) | V_nasip (m³) | V_oyilma (m³) |
|-----|-----------|-------------|--------------|-------------|--------------|
| 0   | —         | 12,5        | 0            | —           | —            |
| 1   | 100       | 8,0         | 0            | 1 025       | 0            |
| 2   | 100       | 0           | 5,0          | 400         | 250          |
| 3   | 100       | 0           | 18,5         | 0           | 1 175        |
| 4   | 100       | 4,5         | 0            | 225         | 925          |
| **Jami** | — | — | — | **1 650** | **2 350** |

**Nol nuqta:** Pik 1 va 2 orasida.

---

## 9.8 Amaliy Misol

**Masala:** Quyidagi ma'lumotlar bo'yicha yer ishlari hajmini hisoblang.

**Berilgan:**
- Yo'l asosi eni: B = 9 m
- Yon nishablik: m = 1,5
- Pik 0: H = +2,0 m (nasip)
- Pik 1: H = +0,8 m (nasip)
- Pik 2: H = −1,5 m (o'yilma)
- Piklar oralig'i: L = 100 m

**Yechim:**

**Pik 0 kesim maydoni (nasip):**
$$F_0 = (9 + 1{,}5 \cdot 2{,}0) \cdot 2{,}0 = (9 + 3) \cdot 2 = 24{,}0 \text{ m}^2$$

**Pik 1 kesim maydoni (nasip):**
$$F_1 = (9 + 1{,}5 \cdot 0{,}8) \cdot 0{,}8 = (9 + 1{,}2) \cdot 0{,}8 = 8{,}16 \text{ m}^2$$

**Pik 0–1 orasidagi nasip hajmi:**
$$V_{01} = \frac{(24{,}0 + 8{,}16)}{2} \cdot 100 = 16{,}08 \cdot 100 = 1\,608 \text{ m}^3$$

**Nol nuqta (Pik 1 dan Pik 2 gacha):**
$$x_0 = \frac{0{,}8}{0{,}8 + 1{,}5} \cdot 100 = \frac{0{,}8}{2{,}3} \cdot 100 = 34{,}8 \text{ m}$$

**Nol nuqtadan Pik 2 gacha: o'yilma**
$$F_2 = (9 + 1{,}5 \cdot 1{,}5) \cdot 1{,}5 = 11{,}25 \cdot 1{,}5 = 16{,}88 \text{ m}^2$$
$$V_{12,oyilma} \approx \frac{16{,}88}{2} \cdot (100 - 34{,}8) = 8{,}44 \cdot 65{,}2 = 550 \text{ m}^3$$

---

## 9.9 Nazorat Savollari

1. AutoCAD Civil 3D dasturining asosiy imkoniyatlari qaysilar?
2. Ko'ndalang kesim maydoni qanday hisoblanadi?
3. Massa diagrammasi nima va u qanday quriladi?
4. Tuproqni tashish uzoqligini aniqlashda qanday omillar hisobga olinadi?
5. Prismatoid va trapetsiya usullari qanday farqlanadi?
6. Nol nuqta masofasi qanday hisoblanadi?

---

*Keyingi mavzu: Relyef shakllari va nishablik yo'nalishi →*
