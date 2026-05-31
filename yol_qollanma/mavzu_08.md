# 8-MAVZU: YO'L O'XI YO'NALISHINI TANLASH VA YUK OQIMLARI

## 8.1 Kirish

Yo'l o'qi yo'nalishini tanlash — loyihalashning eng muhim bosqichlaridan biri. To'g'ri yo'nalish tanlash qurilish va ekspluatatsiya xarajatlarini kamaytiradi, transport oqimining samaradorligini oshiradi va atrof-muhitga ta'sirni kamaytiradi.

---

## 8.2 Yo'l O'xi Yo'nalishini Tanlash Asoslari

### 8.2.1 Yo'nalish tanlashga ta'sir etuvchi omillar

| Omil | Tavsif |
|------|--------|
| **Relyef** | Tog', tekislik, vodiylar |
| **Suv oqimlari** | Daryolar, ko'llar, botqoqliklar |
| **Aholi punktlari** | Ulash yoki chetlab o'tish |
| **Yer qoplamlari** | O'rmon, qishloq xo'jaligi erlari |
| **Geologiya** | Ko'chki, tektonik zonalar |
| **Iqtisod** | Yuk oqimlari, aholi zichligi |
| **Ekologiya** | Himoyalangan hududlar |

### 8.2.2 Yo'nalish tanlash ketma-ketligi

**1-bosqich: Stol tadqiqoti**
- Topografik xaritalarni o'rganish (1:50 000, 1:25 000)
- Aerosuratlar va sun'iy yo'ldosh tasvirlarini tahlil qilish
- Mavjud yo'l tarmog'ini o'rganish
- Bir nechta variant ko'rib chiqish

**2-bosqich: Dala tadqiqoti**
- Tanlangan variantlarni joyida tekshirish
- Qiyin joylarni (daryolar, botqoqlar, qiyaliklar) aniqlash
- Mahalliy sharoitlarni hisobga olish

**3-bosqich: Variantlarni solishtirish**
- Har variant uchun xarajatlar hisoblash
- Eng samarali variant tanlash

---

## 8.3 Yuk Oqimlari Hajmini Hisoblash

### 8.3.1 Yuk oqimi (traffic flow) tushunchasi

**Yuk oqimi** — ma'lum vaqt davomida yo'lning bir kesimidan o'tadigan yuklar hajmi.

**Asosiy ko'rsatkichlar:**
- Yillik yuk hajmi (t/yil)
- Yuk oboroti (t·km/yil)
- Harakat intensivligi (avt/sut)

### 8.3.2 Yuk oqimini aniqlash usullari

**1. So'rovnoma usuli:**
Viloyat/tuman statistika ma'lumotlari asosida:

$$Q_{yil} = \sum_{i=1}^{n} Q_i$$

**2. Gravitatsion model:**
Ikkita hudud orasidagi yuk oqimi:

$$T_{AB} = k \cdot \frac{P_A \cdot P_B}{D_{AB}^2}$$

Bu yerda:
- **T_AB** — A va B o'rtasidagi yuk oqimi
- **P_A, P_B** — iqtisodiy potentsial (YaIM yoki aholi)
- **D_AB** — masofa
- **k** — kalibrlash koeffitsienti

**3. O'sish koeffitsienti usuli:**
$$Q_{pers} = Q_0 \cdot (1 + r)^t$$

Bu yerda r — yillik o'sish sur'ati (0,03–0,08).

---

## 8.4 Harakat Miqdorini Hisoblash

### 8.4.1 Sutkasiga harakat intensivligi

$$N_{sut} = \frac{Q_{yil}}{365 \cdot q \cdot \gamma \cdot \beta \cdot K_{nerat}}$$

Bu yerda:
- **q** — o'rtacha yuk ko'tarish (t)
- **γ** — yuklanish koeffitsienti (0,7–0,9)
- **β** — reyslar koeffitsienti (0,45–0,65)
- **K_nerat** — notekislik koeffitsienti (1,1–1,3)

### 8.4.2 Cho'qqi soatlik harakat

$$N_{cho'qqi} = N_{sut} \cdot K_{soatlik}$$

K_soatlik = 0,10–0,15 (cho'qqi soat ulushi).

### 8.4.3 Transport turiga keltirish koeffitsienti

Aralash oqimni yengil avtomobil ekvivalentiga keltirish:

| Transport turi | Koeffitsient |
|----------------|--------------|
| Yengil avtomobil | 1,0 |
| Yuk avto (yengil) | 1,5 |
| Yuk avto (o'rta) | 2,5 |
| Yuk avto (og'ir) | 3,5 |
| Avtobus (kichik) | 2,0 |
| Avtobus (katta) | 3,0 |
| Tirkama bilan | 4,0 |

---

## 8.5 Yuk Oqimlari Sxemasi (Epyura)

### 8.5.1 Yuk oqimi sxemasi nima?

Yuk oqimi sxemasi — xaritada turli qismlardagi yuk oqimlari hajmini ko'rsatuvchi grafik tasvir.

**Qurilish tartibi:**
1. Manba va iste'molchi nuqtalarini belgilash
2. Har yo'nalish bo'yicha yuk hajmini hisoblash
3. Strelkalar bilan yo'nalish va hajmni ko'rsatish
4. Yo'l segmentlaridagi umumiy oqimni yig'ish

### 8.5.2 Yuk oqimi sxemasini o'qish

```
    Ferma A → 500 t
    Ferma B → 300 t    →  [Ombor]  → 800 t → [Bozor]
    Ferma C → 200 t             ↓
                            200 t → [Zavod]
```

### 8.5.3 Eng yuklangan yo'l kesimini aniqlash

$$Q_{kesim} = \sum_{i} Q_i \cdot x_i$$

Bu yerda **x_i** — i-yukni shu kesimdan o'tish ulushi.

---

## 8.6 Yo'l Tarmog'ini Rivojlantirish Rejalari

### 8.6.1 Qisqa muddatli reja (5 yil)
- Mavjud yo'llarni ta'mirlash va rekonstruktsiya
- Eng og'ir nuqtalarni bartaraf etish

### 8.6.2 O'rta muddatli reja (10 yil)
- Yangi yo'l qurilishi
- Ko'prik va inshootlar

### 8.6.3 Uzoq muddatli reja (20 yil)
- Tarmog'ni kengaytirish
- Yangi yo'nalishlar
- Yo'l toifasini oshirish

---

## 8.7 Yo'nalish Yo'qotishlarini Baholash

### 8.7.1 Tortish (kilometraj) koeffitsienti

$$K_{tort} = \frac{L_{haqiqiy}}{L_{to'g'ri}}$$

**Maqbul qiymatlar:**
- Tekis: 1,1–1,2
- O'rtacha: 1,2–1,4
- Tog'li: 1,4–1,8

### 8.7.2 Qiyalik xarajatlari (qo'shimcha masofa)

Qiyalik qo'shimcha qarshilik yaratadi. Ekvivalent tekis masofa:

$$L_{ekv} = L \cdot (1 + \alpha \cdot i)$$

Bu yerda **α** = 30 (qiyalik qarshilik koeffitsienti).

---

## 8.8 Amaliy Misol

**Masala:** Tuman markazidan qishloqlarga yuk oqimini hisoblang va yo'l o'qi yo'nalishini tanlang.

**Berilgan ma'lumotlar:**

| Qishloq | Aholi | Masofasi A (km) | Masofasi B (km) | Yillik yuk (t) |
|---------|-------|-----------------|-----------------|----------------|
| Q-1 | 1 500 | 8 | 12 | 2 400 |
| Q-2 | 2 000 | 5 | 7 | 3 200 |
| Q-3 | 800 | 10 | 8 | 1 200 |
| Q-4 | 1 200 | 7 | 9 | 1 900 |

**Variant A — to'g'ri chiziq:**

$$G_A = 2400 \cdot 8 + 3200 \cdot 5 + 1200 \cdot 10 + 1900 \cdot 7 = 19200 + 16000 + 12000 + 13300 = 60\,500 \text{ t·km}$$

**Variant B — aylanma yo'l:**

$$G_B = 2400 \cdot 12 + 3200 \cdot 7 + 1200 \cdot 8 + 1900 \cdot 9 = 28800 + 22400 + 9600 + 17100 = 77\,900 \text{ t·km}$$

**Xulosa:** Variant A — yuk oboroti 22% ga kam → **Variant A tanlandi** ✓

---

## 8.9 Nazorat Savollari

1. Yo'l o'qi yo'nalishini tanlashda qanday omillar hisobga olinadi?
2. Gravitatsion model nima va qanday ishlatiladi?
3. Yuk oqimi sxemasi (epyura) qanday quriladi?
4. Tortish koeffitsienti nima?
5. Ekvivalent tekis masofa qanday hisoblanadi?
6. Perspektiv yuk oqimi qanday aniqlanadi?

---

*Keyingi mavzu: Elektron dasturlar va yer ishlari hajmi →*
