# 6-MAVZU: YO'LNING KO'RINISHI, BO'YLAMA KESIM VA LOYIHA CHIZIG'I

## 6.1 Kirish

Yo'lning ko'rinishi — haydovchi oldida yo'l yuzasining ko'rinadigan qismidir. Bu xavfsiz harakatni ta'minlashning asosiy shartidir. Bo'ylama kesim esa yo'lning vertikal geometriyasini belgilab, loyiha chizig'ining qiyaliklari va vertikal egrilarni o'z ichiga oladi.

---

## 6.2 Yo'lning Ko'rinishi

### 6.2.1 Ko'rinish masofasi ta'rifi

**Ko'rinish masofasi (S)** — haydovchi yo'l oldida xavfni ko'rishi va zarur harakatni amalga oshirishi uchun kerakli minimal masofa.

Ko'rinish masofasining uch turi:

| Tur | Tavsif | Belgi |
|-----|--------|-------|
| **To'xtash uchun** | Xavfni ko'rib to'xtash masofasi | S₁ |
| **Oldinga o'tish uchun** | Qarama-qarshi yo'nalishda kelayotgan mashina ko'rinishi | S₂ |
| **Manevrli** | Teskari harakat maneuvrasi uchun | S₃ |

### 6.2.2 To'xtash masofasi (S₁)

$$S_1 = \frac{v^2}{2g(\phi \pm i)} + v \cdot t_r + l_a$$

Bu yerda:
- **v** — harakat tezligi (m/s)
- **g** = 9,81 m/s²
- **φ** — yopishish koeffitsienti (0,3–0,6)
- **i** — yo'l qiyaligi (+ pastga, − tepalikka)
- **t_r** = 0,8–1,0 s — reaktsiya vaqti
- **l_a** = 5–6 m — avtomobil uzunligi

**km/soatda:**
$$S_1 = \frac{v^2}{254(\phi \pm i)} + \frac{v \cdot t_r}{3{,}6} + l_a$$

### 6.2.3 Oldinga o'tish masofasi (S₂)

$$S_2 = 6 \cdot v - \frac{v^2}{6(\phi \pm i)}$$

Bu yerda **v** — km/soatda.

### 6.2.4 Ko'rinish masofasi me'yorlari

| Toifa | v (km/soat) | S₁ (m) | S₂ (m) |
|-------|------------|--------|--------|
| I | 120 | 250–300 | 700–1000 |
| II | 100 | 200 | 600 |
| III | 80 | 150 | 450 |
| IV | 60 | 100 | 350 |
| V | 40–60 | 75 | 200 |

---

## 6.3 Ko'rinishni Cheklash Holatlari

### 6.3.1 Qarama-qarshi qirg'oqlar (o'yilmalarda)
O'yilmalarda yo'lning yon tomonlaridagi qirg'oqlar ko'rinishni cheklaydi.

Maksimal o'yilma balandligi:
$$h_{max} = R_v \cdot \frac{1 - \cos(\alpha/2)}{1}$$

Bu yerda **R_v** — vertikal egri radiusi.

### 6.3.2 Vertikal egrilar
Tepalikdagi (konveks) vertikal egrilar ham ko'rinishni cheklaydi.

Ko'rinish uchun minimal konveks radius:

$$R_{konv,min} = \frac{S_1^2}{2 \cdot (h_1 + h_2)^2} \cdot 8$$

Soddalashtirilgan formula:
$$R_{konv,min} = \frac{S_1^2}{8 \cdot h}$$

Bu yerda:
- **h** = 0,12 m — haydovchi ko'zi balandligi (standart)
- yoki **h** = 0,10 m — to'siqni ko'rish uchun

---

## 6.4 Bo'ylama Kesim va Loyiha Chizig'i

### 6.4.1 Bo'ylama kesim tuzish

Bo'ylama kesim quyidagi ma'lumotlarni o'z ichiga oladi:

**Yuqori qism (grafik):**
- Qora chiziq — tabiiy yer yuzasi profili
- Qizil chiziq — loyiha chizig'i
- Ko'prik, o'tkazgich belgilari
- Km belgilari

**Pastki qism (jadval):**
| Satr | Ma'lumot |
|------|----------|
| Tuproq | Yer osti tuproq qatlami |
| Gidrologiya | Suv sathi, qor qoplami |
| Yershov | Har pikdagi nasip/o'yilma |
| Loyiha balandligi | Loyiha chizig'i absolut balandligi |
| Yer balandligi | Tabiiy yer balandligi |
| Masofalar | Piklar orasidagi masofa |
| Piklar | Pik raqamlari |

### 6.4.2 Loyiha Chizig'ini O'tkazish Tamoyillari

**1. Balanslash tamoyili:**
Nasip va o'yilma hajmlari imkon qadar teng bo'lishi kerak (yer o'z yerida ishlatilsin).

**2. Minimal yer ishlari:**
Loyiha chizig'i tabiiy yer sathiga yaqin bo'lishi kerak.

**3. Drenaj ta'minlash:**
i_min = 5‰ dan kichik bo'lmasin (suv oqib ketishi uchun).

**4. Ko'rinish ta'minlash:**
Konveks egrilarda R ≥ R_min bo'lishi kerak.

---

## 6.5 Bo'ylama Qiyalikning Eng Katta Qiymatini Asoslash

### 6.5.1 Texnik me'yorlar

Maksimal qiyalik yo'l toifasiga qarab belgilanadi:

| Toifa | i_max (‰) | Izoh |
|-------|----------|------|
| I | 30 | Tezkor yo'llar |
| II | 40 | |
| III | 50 | |
| IV | 60 | Tuman yo'llari |
| V | 70 | Mahalliy yo'llar |

### 6.5.2 i_max ni asoslash omillari

**1. Transport dinamikasi:**
Qiylik ortganda avtomobil tezligi pasayadi. IV-toifali yo'lda i = 60‰ da tezlik 20–30% ga kamayishi mumkin.

**2. Tormoz samaradorligi:**
$$i_{max,torm} = \phi - \frac{v^2}{2gL_{tok}}$$

**3. Qish sharoiti:**
Muzlagan yo'lda φ = 0,1–0,2 ga tushadi. Shuning uchun i_max = 40–50‰ dan oshmasligi tavsiya etiladi.

**4. Yuk avtomobillari harakati:**
Yuk avtomobili uchun chiquvchi qiyalik:
$$i_{max,yuk} = \frac{T_{dvigatel}}{G_{avt}} - f$$

Bu yerda:
- **T_dvigatel** — dvigatel tortish kuchi (N)
- **G_avt** — avtomobil og'irligi (N)
- **f** — dumalanish qarshilik koeffitsienti (0,012–0,025)

### 6.5.3 Uzun qiyaliklar (Ramp)

Uzun tepalikda tezlik pasayib ketmasligi uchun qo'shimcha "sekin yuruvchi" bo'laklar yoki o'tish joylari mo'ljallanadi.

---

## 6.6 Vertikal Egrilar

### 6.6.1 Vertikal egrilarning maqsadi
Ikkita qiyalik qo'shilgan joyda to'satdan siltanish va ko'rinish muammosini hal qilish.

**Konveks egri** — tepalikda (qiyaliklar + va − qo'shilganda)
**Konkav egri** — vodiyda (qiyaliklar − va + qo'shilganda)

### 6.6.2 Vertikal egri parametrlari

Qiyaliklar farqi:
$$\omega = |i_2 - i_1|$$

Egri uzunligi:
$$L_v = R_v \cdot \omega$$

Bu yerda **R_v** — vertikal egri radiusi.

### 6.6.3 Minimal vertikal radius

**Konveks egri (ko'rinish ta'minlash uchun):**
$$R_{konv,min} = \frac{S_1^2}{2h_0}$$

h₀ = 0,12 m (ko'z balandligi)

**Konkav egri (qulay sezgi uchun):**
$$R_{konk,min} = \frac{v^2}{13}$$

(v — km/soatda)

### 6.6.4 Yo'l toifasi bo'yicha minimal vertikal radiuslar

| Toifa | R_konv,min (m) | R_konk,min (m) |
|-------|---------------|---------------|
| I | 15 000 | 5 000 |
| II | 10 000 | 3 000 |
| III | 5 000 | 2 000 |
| IV | 2 500 | 1 500 |
| V | 1 500 | 1 000 |

---

## 6.7 Amaliy Misol

**Masala:** IV-toifali yo'l uchun loyiha qiyaligi va vertikal egri parametrlarini hisoblang.

**Berilgan:**
- Tezlik: v = 60 km/soat
- 1-qiyalik: i₁ = +30‰ = +0,030
- 2-qiyalik: i₂ = −20‰ = −0,020
- To'xtash masofasi: S₁ = 100 m

**Yechim:**

**1. Qiyaliklar farqi:**
$$\omega = |{-0{,}020} - (+0{,}030)| = 0{,}050$$

**2. Minimal konveks radius:**
$$R_{konv} = \frac{S_1^2}{2 \cdot h_0} = \frac{100^2}{2 \cdot 0{,}12} = \frac{10000}{0{,}24} = 41\,667 \text{ m}$$

Standart bo'yicha: R_min = 2 500 m < 41 667 m → R = 5 000 m qabul qilamiz.

**3. Egri uzunligi:**
$$L_v = R_v \cdot \omega = 5000 \cdot 0{,}050 = 250 \text{ m}$$

---

## 6.8 Nazorat Savollari

1. Ko'rinish masofasining qanday turlari bor?
2. To'xtash masofasi qanday formula bilan hisoblanadi?
3. Loyiha chizig'ini o'tkazishda qanday tamoyillarga amal qilinadi?
4. Bo'ylama maksimal qiyalikni asoslashda qanday omillar hisobga olinadi?
5. Konveks va konkav egrilar qanday farqlanadi?
6. Vertikal egri uzunligi qanday hisoblanadi?

---

*Keyingi mavzu: Ko'ndalang kesim va texnik me'yorlar →*
