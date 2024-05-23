# Funkcionális specifikáció

## 1. A jelenlegi helyzet leírása
Jelenleg nincs olyan rendszer, amely egyszerűen lehetővé tenné a tanárok számára, hogy kvízeket készítsenek és kezeljék a diákok kvízekre adott válaszait. 
A tanárok manuálisan készítik el a kvízeket papíron vagy különféle szoftverek segítségével, amelyek nem nyújtanak megfelelő támogatást a kérdések generálására és a csapatok kezelésére.

## 2. A kívánt rendszer leírása
A kvíz webalkalmazás célja, hogy egyszerű és hatékony eszközt biztosítson a tanárok számára kvízek készítéséhez és csapatok kezeléséhez, valamint lehetőséget adjon a diákoknak a kvízek kitöltésére. 
Az alkalmazás támogatja az AI által generált kérdéseket, amelyeket a tanárok felülvizsgálhatnak és módosíthatnak.

## 3. A jelenlegi üzleti folyamatok modellje
1. A tanár kézzel készít kvízt papíron vagy szoftverben.
2. A diákok papíron vagy szoftveren keresztül válaszolnak a kérdésekre.
3. A tanár kézzel értékeli a válaszokat és rögzíti az eredményeket.

## 4. A kívánt üzleti folyamatok modellje
1. A tanár bejelentkezik az alkalmazásba.
2. A tanár létrehoz egy új kvízt és hozzáad kérdéseket, manuálisan vagy AI segítségével.
3. A tanár létrehozza és kezeli a csapatokat.
4. A diákok bejelentkeznek az alkalmazásba és kitöltik a kvízeket.
5. Az alkalmazás automatikusan értékeli a válaszokat és rögzíti az eredményeket.

## 5. Követelmények listája

| Id | Modul | Név | Leírás |
| :---: | --- | --- | --- |
| K1 | Felhasználói hitelesítés | Bejelentkezés | A tanárok és diákok külön bejelentkezhetnek. |
| K2 | Kvízkezelés | Kvíz létrehozása | A tanárok új kvízeket hozhatnak létre. |
| K3 | Kvízkezelés | Kérdések hozzáadása | A tanárok kézzel vagy AI segítségével kérdéseket adhatnak hozzá a kvízekhez. |
| K4 | Csapatkezelés | Csapatok létrehozása | A tanárok csapatokat hozhatnak létre és kezelhetnek. |
| K5 | Kvízrészvétel | Kvízek kitöltése | A diákok kitölthetik a hozzájuk rendelt kvízeket. |
| K6 | Adminisztráció | Szuperuser létrehozása | A szuperuser (adminisztrátor) jogosultsággal rendelkező felhasználókat kezelheti. |

## 6. Használati esetek

### 6.1 Tanár bejelentkezése
- **Szereplők**: Tanár
- **Leírás**: A tanár bejelentkezik az alkalmazásba.
- **Előfeltétel**: A tanár rendelkezik felhasználónévvel és jelszóval.
- **Lépések**:
  1. A tanár megnyitja a bejelentkezési oldalt.
  2. A tanár megadja a felhasználónevét és jelszavát.
  3. A tanár rákattint a "Bejelentkezés" gombra.
- **Utófeltétel**: A tanár sikeresen bejelentkezik és eléri a főoldalt.

### 6.2 Diák bejelentkezése
- **Szereplők**: Diák
- **Leírás**: A diák bejelentkezik az alkalmazásba.
- **Előfeltétel**: A diák rendelkezik felhasználónévvel és jelszóval.
- **Lépések**:
  1. A diák megnyitja a bejelentkezési oldalt.
  2. A diák megadja a felhasználónevét és jelszavát.
  3. A diák rákattint a "Bejelentkezés" gombra.
- **Utófeltétel**: A diák sikeresen bejelentkezik és eléri a főoldalt.

### 6.3 Kvíz létrehozása
- **Szereplők**: Tanár
- **Leírás**: A tanár új kvízt hoz létre.
- **Előfeltétel**: A tanár bejelentkezett az alkalmazásba.
- **Lépések**:
  1. A tanár a főoldalon kiválasztja a "Kvíz létrehozása" opciót.
  2. A tanár megadja a kvíz címét és leírását.
  3. A tanár rákattint a "Mentés" gombra.
- **Utófeltétel**: A kvíz sikeresen létrejött és megjelenik a kvízlistában.

### 6.4 Kérdések hozzáadása kvízhez
- **Szereplők**: Tanár
- **Leírás**: A tanár kérdéseket ad hozzá a kvízhez.
- **Előfeltétel**: A tanár létrehozott egy kvízt.
- **Lépések**:
  1. A tanár megnyitja a kvízt.
  2. A tanár kiválasztja a "Kérdés hozzáadása" opciót.
  3. A tanár megadja a kérdést és a válaszlehetőségeket.
  4. A tanár rákattint a "Mentés" gombra.
- **Utófeltétel**: A kérdés sikeresen hozzáadódik a kvízhez.

### 6.5 Kvíz kitöltése
- **Szereplők**: Diák
- **Leírás**: A diák kitölti a kvízt.
- **Előfeltétel**: A diák bejelentkezett és van számára elérhető kvíz.
- **Lépések**:
  1. A diák megnyitja az elérhető kvízek listáját.
  2. A diák kiválasztja a kvízt.
  3. A diák válaszol a kérdésekre.
  4. A diák rákattint a "Beküldés" gombra.
- **Utófeltétel**: A kvíz válaszai elmentődnek és a diák látja az eredményeket.

## 7. Leképezés: Hogyan igazodnak a használati esetek a követelményekhez

| Használati eset | Követelmény |
| --- | --- |
| Tanár bejelentkezése | K1 |
| Diák bejelentkezése | K1 |
| Kvíz létrehozása | K2 |
| Kérdések hozzáadása kvízhez | K3 |
| Kvíz kitöltése | K5 |

## 8. Forgatókönyvek

### 8.1 Tanár kvíz létrehozása és kérdések hozzáadása
- **Szereplők**: Tanár
- **Forgatókönyv**:
  1. A tanár bejelentkezik.
  2. A tanár létrehoz egy új kvízt.
  3. A tanár kérdéseket ad hozzá a kvízhez.
  4. A tanár elmenti a kvízt.
- **Várható eredmény**: A kvíz létrejön és tartalmazza a hozzáadott kérdéseket.

### 8.2 Diák kvíz kitöltése
- **Szereplők**: Diák
- **Forgatókönyv**:
  1. A diák bejelentkezik.
  2. A diák kiválaszt egy elérhető kvízt.
  3. A diák kitölti a kvízt és beküldi.
- **Várható eredmény**: A diák válaszai elmentődnek és az eredmények megjelennek.