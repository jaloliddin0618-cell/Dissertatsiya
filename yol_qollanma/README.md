# 🛣️ YO'L QURILISHI VA LOYIHALASH
## O'quv Qo'llanma — Universitet Talabalari Uchun

> **Muallif:** Jaloliddin  
> **Fan:** Yo'l qurilishi va loyihalash  
> **Daraja:** Bakalavr / Magistr  
> **Yil:** 2026  

---

## 📖 Qo'llanma Haqida

Ushbu o'quv qo'llanma yo'l qurilishi va loyihalash fanining asosiy mavzularini qamrab oladi. Har bir mavzuda:
- 📚 Nazariy asoslar
- 📐 Formulalar va hisoblash usullari
- 💡 Amaliy misollar
- ✅ Nazorat savollari

mavjud bo'lib, talabalar mustaqil o'rganishi uchun qulay shaklda tuzilgan.

---

## 📚 Mavzular Ro'yxati

| № | Mavzu | Fayl |
|---|-------|------|
| 1 | Mahalliy yo'llar va ularning turlari. Tumandagi yo'l aloqasi va yuk hajmlarini hisoblash | [mavzu_01.md](mavzu_01.md) |
| 2 | Yo'lning transport-foydalanish ko'rsatkichlari. Yo'l rejasini tuzish. Transport turlarining yuk tashish hajmi | [mavzu_02.md](mavzu_02.md) |
| 3 | Suv oqimining berilgan nuqtasi uchun suv to'planish maydonlari chegarasini aniqlash | [mavzu_03.md](mavzu_03.md) |
| 4 | Berilgan chiziq bo'yicha bo'ylama profilini tuzish. Berilgan nishablik bo'yicha kartada chiziq o'tkazish | [mavzu_04.md](mavzu_04.md) |
| 5 | Yo'lni rejada loyihalashni o'rganish. Rejadagi egri radiusini hisoblash | [mavzu_05.md](mavzu_05.md) |
| 6 | Yo'lning ko'rinishini aniqlash. Bo'ylama kesimni chizish va loyiha chizig'ini o'tkazish | [mavzu_06.md](mavzu_06.md) |
| 7 | Ko'ndalang kesimni tasvirlash. Texnik me'yorlar. Loyihaning texnik-iqtisodiy asoslash | [mavzu_07.md](mavzu_07.md) |
| 8 | Yo'l o'xi yo'nalishini tanlashda yuk oqimlari va harakat miqdorini hisobga olish | [mavzu_08.md](mavzu_08.md) |
| 9 | Elektron dasturlardan foydalanish. Yer ishlari hajmini aniqlash. Tuproqni tashish uzoqligini aniqlash | [mavzu_09.md](mavzu_09.md) |
| 10 | Relyef shakllarini o'rganish. Gorizontallar. Nishablik yo'nalishini aniqlash | [mavzu_10.md](mavzu_10.md) |
| 11 | Qidiruv turlari. Yo'l rejasi, bo'ylama va ko'ndalang kesimini loyihalash. Ish hajmlarini aniqlash | [mavzu_11.md](mavzu_11.md) |
| 12 | Ishlarni tashkil qilish loyihasini ishlab chiqish. Ishchi hujjatlar tarkibini aniqlash | [mavzu_12.md](mavzu_12.md) |

---

## 🔑 Asosiy Formulalar (Tezkor Manba)

### Yo'l Toifasi
```
N_pers = N₀ · (1 + p)^t        — Perspektiv intensivlik
```

### Suv Sarfi
```
Q_max = α · h · F / (3.6 · T)  — Ratsional formula
```

### Egri Elementlari
```
T = R · tan(α/2)               — Tangent
K = π · R · α / 180            — Egri uzunligi
Б = R · (1/cos(α/2) − 1)       — Bissektrissa
```

### Minimal Radius
```
R_min = v² / [127 · (μ + i_kp)] — Gorizontal egri
```

### Bo'ylama Profil
```
d = h / (i · M)                — Nishablik bo'yicha masofa
Δh = i · L                     — Balandlik farqi
```

### Yer Ishlari
```
V = (F₁ + F₂) / 2 · L         — Trapetsiya usuli
F = (B + m·H) · H              — Kesim maydoni
```

### Ko'rinish Masofasi
```
S₁ = v² / [254·(φ ± i)] + v·t_r/3.6 + l_a
```

---

## 📐 Yo'l Toifalari Jadvali

| Toifa | Tezlik (km/soat) | Yo'l eni (m) | R_min (m) | i_max (‰) |
|-------|-----------------|-------------|-----------|----------|
| I | 120 | 27,5 | 800 | 30 |
| II | 100 | 15 | 600 | 40 |
| III | 80 | 12 | 300 | 50 |
| IV | 60 | 10 | 150 | 60 |
| V | 40–60 | 8 | 60 | 70 |

---

## 🛠️ Foydalaniladigan Dasturlar

| Dastur | Maqsad |
|--------|--------|
| **AutoCAD Civil 3D** | Professional yo'l loyihalash |
| **QGIS** | Topografik tahlil, suv havzalari |
| **ROBUR / IndorCAD** | MDH me'yorlari asosida loyihalash |
| **MS Excel** | Hisob-kitoblar, massa diagrammasi |

---

## 📋 Atamalar Lug'ati

| Atama | Inglizcha | Izoh |
|-------|-----------|------|
| Gorizontal | Contour line | Bir xil balandlikdagi nuqtalar chizig'i |
| Nishablik | Slope / Grade | Balandlik farqining masofa nisbati |
| Nasip | Embankment / Fill | Ko'tarilib qurilgan yo'l asosi |
| O'yilma | Cut / Excavation | Qazib yo'l o'rnatilgan joy |
| Egri | Curve | Yo'lning burilish qismi |
| Tangent | Tangent | Egri boshlanadigan to'g'ri chiziq |
| Superelevatsiya | Superelevation | Egridagi ko'ndalang qiyalik |
| Yuk oboroti | Freight turnover | Yuk × masofa (t·km) |
| Intensivlik | Traffic intensity | Vaqt birligida transport soni |
| DEM | Digital Elevation Model | Raqamli balandlik modeli |
| ITL | Construction Organization Plan | Ishlarni tashkil qilish loyihasi |
| TEA | Feasibility Study | Texnik-iqtisodiy asoslash |

---

## 📁 Fayl Tarkibi

```
yol_qollanma/
├── README.md          ← Bosh sahifa (shu fayl)
├── mavzu_01.md        ← Mahalliy yo'llar va turlari
├── mavzu_02.md        ← Transport ko'rsatkichlari
├── mavzu_03.md        ← Suv to'planish maydoni
├── mavzu_04.md        ← Bo'ylama profil
├── mavzu_05.md        ← Rejada loyihalash, egri radius
├── mavzu_06.md        ← Ko'rinish va bo'ylama kesim
├── mavzu_07.md        ← Ko'ndalang kesim, texnik me'yorlar
├── mavzu_08.md        ← Yo'l o'xi va yuk oqimlari
├── mavzu_09.md        ← Elektron dasturlar, yer ishlari
├── mavzu_10.md        ← Relyef shakllari, nishablik
├── mavzu_11.md        ← Qidiruv turlari, loyihalash
└── mavzu_12.md        ← ITL va ishchi hujjatlar
```

---

## ✍️ Foydalanish Tavsiyalari

1. **Ketma-ket o'qing** — mavzular bir-biriga bog'liq
2. **Formulalarni yod oling** — amaliy ishlarda kerak bo'ladi
3. **Misollarni o'zingiz yoching** — o'zlashtirishni tekshirish uchun
4. **Nazorat savollariga javob bering** — har mavzu oxirida
5. **Dasturlar bilan mashq qiling** — QGIS va Excel bepul

---

*© 2026 — O'zbekiston Respublikasi Yo'l Qurilishi mutaxassislari uchun*
