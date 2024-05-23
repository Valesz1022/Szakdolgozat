# Követelményspecifikáció

## 1. Áttekintés
Ez a dokumentum a kvíz webalkalmazás követelményeit tartalmazza. 
Az alkalmazás célja, hogy a tanárok kvízeket készíthessenek és a diákok ezeket kitölthessék. 
Az alkalmazás két felhasználói szerepkört támogat: tanár és diák.

## 2. A jelenlegi helyzet leírása
Jelenleg nincs olyan rendszer, amely egyszerűen lehetővé tenné a tanárok számára, hogy kvízeket készítsenek és kezeljék a diákok kvízekre adott válaszait. 
A tanárok manuálisan készítik el a kvízeket papíron vagy különféle szoftverek segítségével, amelyek nem nyújtanak megfelelő támogatást a kérdések generálására és a csapatok kezelésére.

## 3. A jövőbeli rendszer víziója
A kvíz webalkalmazás célja, hogy egyszerű és hatékony eszközt biztosítson a tanárok számára kvízek készítéséhez és csapatok kezeléséhez, valamint lehetőséget adjon a diákoknak a kvízek kitöltésére. 
Az alkalmazás támogatja az AI által generált kérdéseket, amelyeket a tanárok felülvizsgálhatnak és módosíthatnak.

## 4. A jelenlegi üzleti folyamatok modellje
1. A tanár kézzel készít kvízt papíron vagy szoftverben.
2. A diákok papíron vagy szoftveren keresztül válaszolnak a kérdésekre.
3. A tanár kézzel értékeli a válaszokat és rögzíti az eredményeket.

## 5. A kívánt üzleti folyamatok modellje
1. A tanár bejelentkezik az alkalmazásba.
2. A tanár létrehoz egy új kvízt és hozzáad kérdéseket, manuálisan vagy AI segítségével.
3. A tanár létrehozza és kezeli a csapatokat.
4. A diákok bejelentkeznek az alkalmazásba és kitöltik a kvízeket.
5. Az alkalmazás automatikusan értékeli a válaszokat és rögzíti az eredményeket.

## 6. Követelmények listája

| Id | Modul | Név | Leírás |
| :---: | --- | --- | --- |
| K1 | Felhasználói hitelesítés | Bejelentkezés | A tanárok és diákok külön bejelentkezhetnek. |
| K2 | Kvízkezelés | Kvíz létrehozása | A tanárok új kvízeket hozhatnak létre. |
| K3 | Kvízkezelés | Kérdések hozzáadása | A tanárok kézzel vagy AI segítségével kérdéseket adhatnak hozzá a kvízekhez. |
| K4 | Csapatkezelés | Csapatok létrehozása | A tanárok csapatokat hozhatnak létre és kezelhetnek. |
| K5 | Kvízrészvétel | Kvízek kitöltése | A diákok kitölthetik a hozzájuk rendelt kvízeket. |
| K6 | Adminisztráció | Szuperuser létrehozása | A szuperuser (adminisztrátor) jogosultsággal rendelkező felhasználókat kezelheti. |

## 7. Szójegyzék
- **AI**: Mesterséges intelligencia, amely segíthet a kérdések generálásában.
- **Tanár**: Az alkalmazás azon felhasználója, aki kvízeket hoz létre és csapatokat kezel.
- **Diák**: Az alkalmazás azon felhasználója, aki kvízeket tölt ki.
- **Kvíz**: Egy teszt, amely kérdésekből áll, és amelyet a diákok kitölthetnek.
- **Csapat**: Több diák csoportja, amelyeket a tanár hozhat létre.
- **Szuperuser**: Olyan felhasználó, aki adminisztrátori jogosultságokkal rendelkezik.
