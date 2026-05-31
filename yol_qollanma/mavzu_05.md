# 5-MAVZU: YO'LNI REJADA LOYIHALASH VA EGRI RADIUSINI HISOBLASH

## 5.1 Kirish

Yo'lni rejada loyihalash — yo'lning gorizontal tekislikdagi geometrik shakli va elementlarini aniqlash jarayonidir. To'g'ri va egri qismlar almashinuvi yo'lning rejalashuv sxemasini tashkil etadi. Egri radiusini to'g'ri tanlash xavfsiz va qulay harakatni ta'minlaydi.

---

## 5.2 Rejadagi Asosiy Elementlar

Yo'l rejasi uchta asosiy elementdan iborat:

| Element | Belgi | Tavsif |
|---------|-------|--------|
| **To'g'ri qism** | T | Yo'nalish o'zgarmaydi |
| **Doira shaklli egri** | R | Doimiy radiusli burilish |
| **O'tish egrisi** | L | To'g'ri va doira o'rtasidagi yumshatma |

---

## 5.3 Gorizontal Egri (Doira) Elementlari

### 5.3.1 Egri elementlari

```
         T         T
    ----*-----------*----
       /               \
      / R               \
     *         O         *
      \                 /
       \               /
        ---------------
```

| Element | Belgi | Formula |
|---------|-------|---------|
| Radius | R | Loyihalashda tanlanadi |
| Burilish burchagi | α | O'lchanadi (grad) |
| Tangent uzunligi | T | T = R · tg(α/2) |
| Egri uzunligi | K | K = π·R·α/180 |
| Bissektrissa | Б | Б = R · (1/cos(α/2) − 1) |
| Domina (D) | D | D = 2T − K |

### 5.3.2 Tangent uzunligini hisoblash

$$T = R \cdot \tan\left(\frac{\alpha}{2}\right)$$

### 5.3.3 Egri uzunligini hisoblash

$$K = \frac{\pi \cdot R \cdot \alpha}{180}$$

yoki radianlar bilan:

$$K = R \cdot \alpha_{rad}$$

### 5.3.4 Bissektrissa

$$\text{Б} = R \cdot \left(\frac{1}{\cos(\alpha/2)} - 1\right) = R \cdot (\sec(\alpha/2) - 1)$$

---

## 5.4 Minimal Egri Radiusini Aniqlash

### 5.4.1 Markazdan qochma kuch va yon itarilish

Transport burilganda markazdan qochma kuch ta'sir qiladi. Yo'l enining ko'ndalang qiyaligi (superelevatsiya) bu kuchni muvozanatlaydi.

Minimal radius formulasi:

$$R_{min} = \frac{v^2}{127 \cdot (\mu + i_{kp})}$$

Bu yerda:
- **v** — hisoblash tezligi (km/soat)
- **μ** — yon itarilish koeffitsienti (0,06–0,15)
- **i_kp** — ko'ndalang qiyalik (superelevatsiya, 0,02–0,06)

### 5.4.2 Tezlik bo'yicha minimal radiuslar

| Hisoblash tezligi (km/soat) | R_min (m) |
|-----------------------------|-----------|
| 120 | 800 |
| 100 | 600 |
| 80 | 300 |
| 60 | 150 |
| 40 | 60 |
| 30 | 30 |
| 20 | 15 |

### 5.4.3 Yo'l toifasi bo'yicha minimal radius

| Toifa | Hisoblash tezligi (km/soat) | R_min (m) | R_tavsiya (m) |
|-------|---------------------------|-----------|--------------|
| I | 120 | 800 | 3 000 |
| II | 100 | 600 | 2 000 |
| III | 80 | 300 | 1 000 |
| IV | 60 | 150 | 500 |
| V | 40–60 | 60–150 | 200–500 |

---

## 5.5 O'tish Egrisi

### 5.5.1 Maqsad
O'tish egrisi to'g'ri qismdan doira shaklli egriga silliq o'tishni ta'minlaydi. Bu haydovchiga burilishga tayyorlanish imkonini beradi.

### 5.5.2 Klotoida (Euler spirali)
Eng ko'p qo'llaniladigan o'tish egrisi turi:

$$R \cdot l = A^2 = const$$

Bu yerda:
- **R** — egri radius (o'zgaruvchan)
- **l** — klotoida boshidan o'lchanadigan uzunlik
- **A** — klotoida parametri

### 5.5.3 O'tish egrisi uzunligi

$$L_{ot} = \frac{v^3}{C \cdot R}$$

Bu yerda:
- **C** = 0,5–0,6 m/s³ — ko'ndalang tezlanish o'zgarish tezligi

**Yoki superelevatsiya bo'yicha:**

$$L_{ot} = \frac{\Delta i \cdot B}{m}$$

Bu yerda:
- **Δi** — superelevatsiya o'zgarishi
- **B** — yo'l eni (m)
- **m** — o'zgarish qiyaligi (1/100 dan 1/400 gacha)

---

## 5.6 Superelevatsiya (Ko'ndalang Qiyalik)

### 5.6.1 Superelevatsiya nima?
Egri qismlarda yo'lning tashqi qirrasini ko'tarish — **superelevatsiya** deyiladi. Bu markazdan qochma kuchni muvozanatlaydi.

### 5.6.2 Superelevatsiya qiymatlari

| Radius (m) | i_sup (%) |
|-----------|-----------|
| > 3 000 | 2 (oddiy ko'ndalang qiyalik) |
| 2 000–3 000 | 3 |
| 1 000–2 000 | 4 |
| 600–1 000 | 5 |
| 400–600 | 6 |
| < 400 | 7–8 |

---

## 5.7 Ko'rinish Masofasi Rejada

### 5.7.1 Ko'rinish masofasi ta'rifi
Haydovchi yo'l oldida xavfni ko'rishi va to'xtashi uchun kerakli minimal masofa.

### 5.7.2 To'xtash masofasi

$$S_{tok} = \frac{v^2}{2 \cdot g \cdot (\phi \pm i)} + v \cdot t_r + l_{avt}$$

### 5.7.3 Ko'rinishni cheklash radiusi

Egri qismlarda ichki tomonda ko'rinishni cheklovchi to'siq (bino, o'rmon, qirg'oq) bo'lmasligi kerak.

Maksimal ichki to'siq masofasi:

$$m = R - \sqrt{R^2 - \left(\frac{S_{tok}}{2}\right)^2}$$

---

## 5.8 Reja Elementlarini Hisoblash Jadvali

| Element | Formula | Misol (R=300, α=40°) |
|---------|---------|---------------------|
| T (tangent) | R·tg(α/2) | 300·tg(20°) = 109,2 m |
| K (egri) | π·R·α/180 | π·300·40/180 = 209,4 m |
| Б (bissektrissa) | R·(1/cos(α/2)−1) | 300·(1/cos20°−1) = 19,5 m |
| D (domina) | 2T−K | 2·109,2−209,4 = 9,0 m |

---

## 5.9 Amaliy Misol

**Masala:** IV-toifali yo'l uchun egri elementlarini hisoblang.

**Berilgan:**
- Burilish burchagi: α = 30°
- Hisoblash tezligi: v = 60 km/soat
- Tanlab olingan radius: R = 300 m

**Yechim:**

**1. Tangent:**
$$T = 300 \cdot \tan(15°) = 300 \cdot 0{,}2679 = 80{,}4 \text{ m}$$

**2. Egri uzunligi:**
$$K = \frac{\pi \cdot 300 \cdot 30}{180} = \frac{28274}{180} = 157{,}1 \text{ m}$$

**3. Bissektrissa:**
$$\text{Б} = 300 \cdot \left(\frac{1}{\cos 15°} - 1\right) = 300 \cdot (1{,}0353 - 1) = 10{,}6 \text{ m}$$

**4. Domina:**
$$D = 2 \cdot 80{,}4 - 157{,}1 = 160{,}8 - 157{,}1 = 3{,}7 \text{ m}$$

**5. Minimal radius tekshiruvi:**
$$R_{min} = \frac{60^2}{127 \cdot (0{,}08 + 0{,}06)} = \frac{3600}{17{,}78} = 202 \text{ m}$$

R = 300 m > R_min = 202 m → **shartni qanoatlantiradi** ✓

---

## 5.10 Nazorat Savollari

1. Yo'l rejasining asosiy elementlari qaysilar?
2. Egri tangent uzunligi qanday hisoblanadi?
3. Minimal egri radiusi nimaga bog'liq?
4. Superelevatsiya nima va u qachon qo'llaniladi?
5. O'tish egrisi nima maqsadda o'rnatiladi?
6. Ko'rinish masofasi va egri radius o'rtasidagi bog'liqlik qanday?

---

*Keyingi mavzu: Yo'lning ko'rinishi va bo'ylama kesim →*
