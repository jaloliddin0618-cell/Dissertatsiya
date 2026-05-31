# 3-MAVZU: SUV TO'PLANISH MAYDONLARI CHEGARASINI ANIQLASH

## 3.1 Kirish

Yo'l qurilishida suv oqimlarini to'g'ri hisoblash juda muhim. Ko'priklar, o'tkazgichlar (truba) va boshqa gidrotexnik inshootlarni loyihalash uchun birinchi navbatda **suv to'planish maydoni (watershed area)** aniqlanadi. Bu maydon — yomg'ir va qor suvlari oqib kelib ma'lum bir nuqtaga to'planadigan hududdir.

---

## 3.2 Asosiy Tushunchalar

### 3.2.1 Suv to'planish maydoni (F)
Suv to'planish maydoni — ma'lum bir daryo kesimi yoki suv oqimi nuqtasiga barcha suvlar oqib keladigan yer yuzasi maydoni.

**Belgilash:** F (km² yoki ga)

### 3.2.2 Suv ayirg'ich (waterhed divide)
Suv ayirg'ich — ikki qo'shni suv havzasini ajratib turuvchi cho'qqi va tizmalar chizig'i. Yomg'ir suvi bu chiziqdan bir tomonga yoki ikkinchi tomonga oqadi.

### 3.2.3 Gidrologik hisoblashning ahamiyati
- Ko'prik va o'tkazgich o'lchamlarini aniqlash
- Sel va toshqin xavfini baholash
- Drenaj tizimlarini loyihalash
- Yo'lni suv ta'siridan himoya qilish

---

## 3.3 Suv To'planish Maydonini Aniqlash Usullari

### 3.3.1 Topografik xarita usuli

Bu eng keng tarqalgan usul bo'lib, quyidagi ketma-ketlikda bajariladi:

**1-qadam: Berilgan nuqtani aniqlash**
Hisoblash nuqtasi — odatda ko'prik, o'tkazgich yoki daryoning kesilayotgan joyi.

**2-qadam: Gorizontallarni o'rganish**
Gorizontallar — bir xil balandlikdagi nuqtalarni birlashtiruvchi chiziqlar. Suvlar pastga — gorizontallarni kesib o'tib oqadi.

**3-qadam: Suv ayirg'ich chizig'ini chizish**
- Berilgan nuqtadan yuqoriga qarab suv ayirg'ich yo'nalishini kuzatish
- Suv ayirg'ich — har doim gorizontallarni to'g'ri burchak ostida kesadi
- Eng yuqori nuqtalarni (cho'qqilarni) birlashtiruvchi chiziq chiziladi

**4-qadam: Maydonni o'lchash**
- Suv ayirg'ich chizig'i bilan o'ralgan maydon planimetr yoki katak usuli bilan o'lchanadi
- Xarita masshtabiga ko'ra haqiqiy maydonga o'tkaziladi

$$F_{haqiqiy} = F_{xarita} \cdot M^2$$

Bu yerda:
- **F_xarita** — xaritadagi maydon (sm²)
- **M** — xarita masshtabi bo'luvchisi (masalan, 1:10 000 uchun M = 10 000)

### 3.3.2 GIS (Geografik Axborot Tizimlari) usuli

Zamonaviy usul bo'lib, raqamli relyef modeli (DEM) asosida bajariladi:

1. DEM ma'lumotlari yuklash (SRTM, ASTER yoki mahalliy so'rovlar)
2. ArcGIS, QGIS, SAGA GIS dasturlarida suv yo'nalishi (flow direction) hisoblash
3. Suv to'planish maydoni avtomatik ajratiladi
4. Maydon, perimetr, o'rtacha qiyalik va boshqa parametrlar hisoblanadi

---

## 3.4 Suv To'planish Chizig'ini Chizish Qoidalari

### 3.4.1 Asosiy qoidalar

| Qoida | Tavsif |
|-------|--------|
| **Chiziq gorizontalni kesadi** | Suv ayirg'ich gorizontallarni to'g'ri burchak ostida kesadi |
| **Chiziq cho'qqidan o'tadi** | Har bir cho'qqi suv ayirg'ich chizig'ida yotadi |
| **Chiziq yopiq** | Suv to'planish maydoni yopiq kontur hosil qiladi |
| **Chiziq past joylardan o'tmaydi** | Vodiylar va jarliklarda suv ayirg'ich bo'lmaydi |

### 3.4.2 Xato manbalar va ularning oldini olish

- **Gorizontallarni noto'g'ri o'qish** → Xaritani diqqat bilan o'rganish
- **Cho'qqilarni o'tkazib yuborish** → Barcha cho'qqilarni belgilash
- **Past joylardan o'tkazish** → Suv doim pastga oqishini esda tutish

---

## 3.5 Gidrologik Hisoblashlar

### 3.5.1 Maksimal suv sarfi (Q_max)
Yo'l inshootlarini loyihalash uchun eng muhim ko'rsatkich — maksimal (toshqin) suv sarfi.

**Ratsional formula (kichik havzalar uchun, F < 100 km²):**

$$Q_{max} = \frac{\alpha \cdot h \cdot F}{3{,}6 \cdot T}$$

Bu yerda:
- **α** — oqim koeffitsienti (tuproq va o'simlikka qarab, 0,2–0,9)
- **h** — hisoblash yog'ingarchiligi (mm)
- **F** — suv to'planish maydoni (km²)
- **T** — suv to'planish vaqti (soat)

**Muravyev formulasi (o'rta havzalar uchun):**

$$Q_{max} = q_p \cdot F^n$$

Bu yerda:
- **q_p** — solishtirma sarfning hisoblash qiymati (m³/s·km²)
- **F** — havza maydoni (km²)
- **n** — ko'rsatkich (0,6–0,8)

### 3.5.2 Oqim koeffitsienti (α)

| Yer yuzasi turi | α qiymati |
|-----------------|-----------|
| Toshloq tog'lar | 0,8–0,9 |
| O'rmonli tog'lar | 0,6–0,7 |
| Qiyalik dalalar | 0,4–0,6 |
| Tekis dalalar | 0,2–0,4 |
| Botqoqliklar | 0,1–0,3 |

### 3.5.3 O'rtacha qiyalik (J)
Havza qiyaligi oqim tezligiga ta'sir qiladi.

$$J = \frac{\Delta h}{L}$$

Bu yerda:
- **Δh** — havzadagi maksimal va minimal balandliklar farqi (m)
- **L** — asosiy daryoning uzunligi (km)

---

## 3.6 Ko'prik va O'tkazgich O'lchamlarini Aniqlash

### 3.6.1 O'tkazgich diametrini tanlash

Hisoblangan Q_max bo'yicha standart jadvaldan diametr tanlanadi:

| Q_max (m³/s) | Tavsiya etiladigan diametr |
|-------------|--------------------------|
| 0,1–0,5 | d = 0,5 m |
| 0,5–1,5 | d = 0,75 m |
| 1,5–3,0 | d = 1,0 m |
| 3,0–6,0 | d = 1,25 m |
| 6,0–10,0 | d = 1,5 m |
| > 10,0 | Ko'prik quriladi |

### 3.6.2 Ko'prik kengligi
$$B_{koprik} = Q_{max} / (v \cdot h)$$

Bu yerda:
- **v** — suv oqish tezligi (m/s)
- **h** — suv chuqurligi (m)

---

## 3.7 Amaliy Misol

**Masala:** 1:25 000 masshtabli xaritada berilgan nuqta uchun suv to'planish maydonini aniqlang va maksimal suv sarfini hisoblang.

**Berilgan:**
- Xaritadagi maydon: F_xarita = 12,5 sm²
- Masshtab: 1:25 000
- Oqim koeffitsienti: α = 0,5
- Hisoblash yog'ingarchiligi: h = 80 mm
- Suv to'planish vaqti: T = 2 soat

**Yechim:**

**1. Haqiqiy maydon:**
$$F = 12{,}5 \cdot (25\,000)^2 = 12{,}5 \cdot 625 \cdot 10^6 \text{ sm}^2 = 7{,}8125 \text{ km}^2$$

(1 km² = 10¹⁰ sm²)

$$F = \frac{12{,}5 \cdot 625 \cdot 10^6}{10^{10}} = 0{,}78 \text{ km}^2 = 78 \text{ ga}$$

**2. Maksimal suv sarfi:**
$$Q_{max} = \frac{0{,}5 \cdot 80 \cdot 0{,}78}{3{,}6 \cdot 2} = \frac{31{,}2}{7{,}2} = 4{,}33 \text{ m}^3/\text{s}$$

**Xulosa:** Q_max = 4,33 m³/s → diametri **d = 1,25 m** bo'lgan o'tkazgich o'rnatiladi.

---

## 3.8 GIS Dasturida Bajarish Tartibi (QGIS misoli)

```
1. QGIS → Raster → Analysis → Fill Sinks (cho'kma nuqtalarni to'ldirish)
2. Raster → Analysis → Flow Direction (oqim yo'nalishi)
3. Raster → Analysis → Flow Accumulation (oqim to'planishi)
4. Nuqtani belgilash → Vectorize
5. Watershed → suv to'planish chegarasini ajratish
6. Maydon hisoblash: Field Calculator → $area
```

---

## 3.9 Nazorat Savollari

1. Suv to'planish maydoni nima va u nima uchun aniqlanadi?
2. Suv ayirg'ich chizig'ini chizishda qanday qoidalarga amal qilinadi?
3. Ratsional formula qanday holatlarda qo'llaniladi?
4. Oqim koeffitsienti nimaga bog'liq?
5. Hisoblangan Q_max asosida o'tkazgich diametri qanday tanlanadi?

---

*Keyingi mavzu: Bo'ylama profil tuzish va nishablik bo'yicha chiziq →*
