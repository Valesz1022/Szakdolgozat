# Kvíz Webalkalmazás

## Mi ez az alkalmazás?
- Ez egy egyszerű webalkalmazás, amely segít a tanároknak kvízeket készíteni és diákoknak ezeket a kvízeket kitölteni. 
- A tanárok új kvízeket hozhatnak létre, kérdéseket adhatnak hozzájuk, és csapatokat is kezelhetnek. 
- A diákok megoldhatják a kvízeket és gyakorolhatják a tanultakat.

## Hogyan használhatom?

### Előkészületek
- Szükséged lesz egy számítógépre és internetkapcsolatra.
- Telepítsd a Python és Django szoftvereket a számítógépedre.

### Telepítés lépései

1. **Letöltés és elindítás**
    - Töltsd le az alkalmazást az internetről.
    - Csomagold ki a fájlokat egy mappába a számítógépeden.

2. **Virtuális környezet létrehozása**
    - Nyiss meg egy parancssort vagy terminált.
    - Menj a mappába, ahol az alkalmazás fájljai vannak.
    - Írd be a következő parancsokat:
    ```sh
    python -m venv env
    source env/bin/activate  # Linux vagy macOS esetén
    .\env\Scripts\activate   # Windows esetén
    ```

3. **Szükséges programok telepítése**
    - Írd be a következő parancsot a szükséges programok telepítéséhez:
    ```sh
    pip install -r requirements.txt
    ```

4. **Adatbázis beállítása**
    - Írd be a következő parancsot az adatbázis létrehozásához:
    ```sh
    python manage.py migrate
    ```

5. **Adminisztrátor létrehozása**
    - Írd be a következő parancsot egy adminisztrátor (tanár) felhasználó létrehozásához:
    ```sh
    python manage.py createsuperuser
    ```

6. **Indítsd el az alkalmazást**
    - Írd be a következő parancsot az alkalmazás indításához:
    ```sh
    python manage.py runserver
    ```
    - Nyisd meg a böngésződben a következő címet:
    ```
    http://127.0.0.1:8000/
    ```

### Hogyan jelentkezz be?

#### Tanárok
- Nyisd meg a bejelentkezési oldalt.
- Add meg az adminisztrátorként létrehozott felhasználónevet és jelszót.
- Bejelentkezés után létrehozhatsz új kvízeket és csapatokat, valamint kérdéseket adhatsz hozzá a kvízekhez.

#### Diákok
- Nyisd meg a bejelentkezési oldalt.
- Add meg a diák felhasználónevedet és jelszavadat.
- Bejelentkezés után hozzáférhetsz a tanárok által létrehozott kvízekhez és kitöltheted azokat.

