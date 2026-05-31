# 2-MAVZU: YO'LNING TRANSPORT-FOYDALANISH KO'RSATKICHLARI

## 2.1 Kirish

Yo'lning transport-foydalanish ko'rsatkichlari yo'l infratuzilmasining samaradorligini baholash va loyihalash uchun asosiy mezon hisoblanadi. Bu ko'rsatkichlar yo'lning texnik holati, transport oqimi va iqtisodiy samaradorligini ifodalaydi.

---

## 2.2 Yo'l Rejasini Tuzish

Yo'l rejasi — bu yo'lning gorizontal tekislikdagi tasvirlari bo'lib, quyidagi elementlarni o'z ichiga oladi:

### 2.2.1 Reja elementlari
- **To'g'ri qismlar** — yo'lning to'g'ri yo'nalishli bo'limlari
- **Egri qismlar (gorizontal egrilar)** — yo'nalish o'zgarganda qo'llaniladigan qismlar
- **O'tish egrilari** — to'g'ri va doira shaklli qismlar orasidagi yumshatuvchi elementlar

### 2.2.2 Reja tuzish bosqichlari
1. Topografik asos (xarita yoki yer o'lchov natijalari) tayyorlash
2. Yo'l o'qi yo'nalishini belgilash
3. Burilish nuqtalarini aniqlash
4. Egri radiuslarni hisoblash
5. Reja elementlarini koordinatalar bo'yicha joylashtirish

---

## 2.3 Transport Ko'rsatkichlari

### 2.3.1 Harakat intensivligi (N)
Harakat intensivligi — 1 soat yoki 1 sutkada yo'lning ko'ndalang kesimidan o'tadigan transport vositalari soni.

$$N = N_{yengil} + N_{yuk} \cdot k_{yuk} + N_{avtobus} \cdot k_{avtobus}$$

Bu yerda:
- **k_yuk** — yuk avtomobilini yengil avtomobilga keltirish koeffitsienti (1,5–3,5)
- **k_avtobus** — avtobusni yengil avtomobilga keltirish koeffitsienti (2,0–3,0)

### 2.3.2 Yo'l o'tkazish qobiliyati (P)
Yo'l o'tkazish qobiliyati — yo'lning bir soatda o'tkazishi mumkin bo'lgan maksimal transport oqimi.

$$P = \frac{1000 \cdot v}{l_{min}}$$

Bu yerda:
- **v** — harakat tezligi (km/soat)
- **l_min** — minimal xavfsiz masofa (m)

**Minimal xavfsiz masofa:**
$$l_{min} = \frac{v^2}{2 \cdot g \cdot (\phi \pm i)} + v \cdot t_{reaksia} + l_{avt}$$

Bu yerda:
- **g** = 9,81 m/s² — erkin tushish tezlanishi
- **φ** — tekerlakning yo'l yuzasiga yopishish koeffitsienti (0,3–0,7)
- **i** — yo'l qiyaligi
- **t_reaksia** = 0,8–1,0 s — haydovchi reaktsiya vaqti
- **l_avt** = 5–7 m — avtomobil uzunligi

### 2.3.3 Yo'lning yuklanish darajasi (Z)
$$Z = \frac{N}{P}$$

| Z qiymati | Holat |
|-----------|-------|
| Z < 0,6   | Erkin harakat |
| 0,6–0,8   | Qisman cheklangan |
| 0,8–1,0   | Zich harakat |
| Z > 1,0   | Tiqilinch |

---

## 2.4 Transport Turlarining Yuk Tashish Hajmi

### 2.4.1 Temir yo'l transporti
Temir yo'l transporti — og'ir va katta hajmli yuklarni uzoq masofaga tashishda eng tejamkor tur.

**Xususiyatlari:**
- Tashish quvvati: 1 vagon — 60–70 t; 1 poyezd — 3 000–6 000 t
- Masofa: 500 km dan ortiq samarali
- Tezlik: 40–120 km/soat (yuk)
- Narx: past (uzoq masofa uchun)

**Yuk oboroti formulasi:**
$$Q_{TY} = n_{vagon} \cdot q_{vagon} \cdot \gamma \cdot N_{poyezd} \cdot L$$

### 2.4.2 Avtomobil transporti
Moslashuvchan va qisqa masofaga eng qulay transport turi.

**Xususiyatlari:**
- Yuk ko'tarish: 1–40 t (turli rusumlar)
- Masofa: 1–500 km oralig'ida samarali
- "Eshikdan eshikka" xizmat

**Yillik yuk hajmi:**
$$Q_{AT} = \frac{G \cdot 365}{q \cdot \gamma \cdot \beta \cdot L}$$

Bu yerda **β** — reys koeffitsienti (bo'sh qaytish hisobga olinadi).

### 2.4.3 Havo transporti
Tez va qimmat transport turi; yuqori qiymatli va tez buziluvchi yuklarga mo'ljallangan.

**Xususiyatlari:**
- Yuk ko'tarish: 1–100 t (samolyot turiga qarab)
- Tezlik: 500–900 km/soat
- Narx: eng yuqori

### 2.4.4 Suv transporti (daryo va dengiz)
Og'ir va katta hajmli yuklarni tashishda arzon alternativa.

**Xususiyatlari:**
- Daryo kemasi: 500–5 000 t
- Dengiz kemasi: 10 000–500 000 t (DWT)
- Mavsumiylik (muzlab qolish muammosi)

**Yuk oboroti:**
$$Q_{ST} = q_{kema} \cdot n_{reyslar} \cdot \gamma$$

### 2.4.5 Shahar transporti
Shahardagi yo'lovchi va yuk tashish tizimi.

**Turlari:**
| Tur | Sig'im (yo'lovchi) | Tezlik (km/soat) |
|-----|-------------------|-----------------|
| Metro | 40 000/soat | 40–80 |
| Tram | 7 000/soat | 15–25 |
| Avtobus | 3 000/soat | 20–40 |
| Trolleybus | 4 000/soat | 15–30 |

### 2.4.6 Magistral quvur yo'l transporti
Neft, gaz, suv va boshqa suyuq/gaz holatidagi materiallarni uzluksiz tashish.

**Xususiyatlari:**
- Uzunligi: yuzlab va minglab km
- Quvvati: yiliga millionlab tonna
- Ishlash muddati: 30–50 yil
- Narx: qurilish qimmat, ekspluatatsiya arzon

**Quvur o'tkazuvchanligini hisoblash:**
$$Q_{kv} = \frac{\pi \cdot d^2}{4} \cdot v_{oqim} \cdot \rho \cdot T_{yil}$$

Bu yerda:
- **d** — quvur diametri (m)
- **v_oqim** — oqim tezligi (m/s)
- **ρ** — modda zichligi (kg/m³)
- **T_yil** — yillik ish soati

---

## 2.5 Transport Turlarini Solishtirish

| Ko'rsatkich | Temir yo'l | Avtomobil | Havo | Suv | Quvur |
|-------------|-----------|-----------|------|-----|-------|
| Narx (uzoq) | ★★★★★ | ★★★ | ★ | ★★★★★ | ★★★★ |
| Tezlik | ★★★ | ★★★ | ★★★★★ | ★★ | ★★ |
| Moslashuvchanlik | ★★ | ★★★★★ | ★★★ | ★★ | ★ |
| Sig'im | ★★★★ | ★★ | ★★ | ★★★★★ | ★★★★★ |
| Ishonchlilik | ★★★★ | ★★★ | ★★★★ | ★★★ | ★★★★★ |

---

## 2.6 Yo'lning Foydalanish Ko'rsatkichlari Jadvali

| Ko'rsatkich | Belgi | Birlik | Formula |
|-------------|-------|--------|---------|
| Harakat intensivligi | N | avt/sut | O'lchov |
| O'tkazish qobiliyati | P | avt/soat | P=1000v/l_min |
| Yuklanish darajasi | Z | ulush | Z=N/P |
| Yuk oboroti | G | t·km | G=Q·L |
| Tezlik | v | km/soat | O'lchov |

---

## 2.7 Amaliy Misol

**Masala:** Tuman yo'li uchun o'tkazish qobiliyatini hisoblang.

**Berilgan:**
- Harakat tezligi: v = 60 km/soat
- Yopishish koeffitsienti: φ = 0,5
- Yo'l qiyaligi: i = 0,03
- Reaktsiya vaqti: t = 1,0 s
- Avtomobil uzunligi: l_avt = 6 m

**Yechim:**

To'xtatish masofasi:
$$l_{min} = \frac{(60/3{,}6)^2}{2 \cdot 9{,}81 \cdot (0{,}5 - 0{,}03)} + \frac{60}{3{,}6} \cdot 1{,}0 + 6$$

$$l_{min} = \frac{277{,}78}{9{,}23} + 16{,}67 + 6 = 30{,}1 + 16{,}7 + 6 = 52{,}8 \text{ m}$$

O'tkazish qobiliyati:
$$P = \frac{1000 \cdot 60}{52{,}8} \approx 1136 \text{ avt/soat}$$

---

## 2.8 Nazorat Savollari

1. Yo'lning transport-foydalanish ko'rsatkichlari nima?
2. Harakat intensivligi qanday o'lchanadi?
3. Yo'l o'tkazish qobiliyati qanday formula bilan hisoblanadi?
4. Magistral quvur yo'l transportining afzalliklari nimada?
5. Shahar transportining qanday turlarini bilasiz?
6. Yuklanish darajasi Z > 1 bo'lsa nima degan ma'noni anglatadi?

---

*Keyingi mavzu: Suv to'planish maydonlari chegarasini aniqlash →*
