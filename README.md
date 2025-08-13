# myfirsthelloworld

Ez a repó egy oktatási célú programot tartalmaz, amely az Airbus A320 család abnormal és vészhelyzeti eljárásainak gyakorlását segíti.
Az eljárások a `procedures.json` állományból töltődnek be, és egy interaktív Tkinter felületen lépésről lépésre jelennek meg.

A mellékelt mintaadatbázis néhány tipikus QRH-procedúrát tartalmaz (pl. ENGINE 1 FIRE, EMERGENCY DESCENT, LOSS OF BRAKING).
A JSON fájl bővíthető további eljárásokkal, így saját tananyag állítható össze.

## Futatás
```bash
python app.py
```

Grafikus megjelenítéshez X11 felület szükséges. Ha nincs kijelző, a program figyelmeztetést ad és kilép.

## Figyelmeztetés / Disclaimer
Ez a program kizárólag szemléltető jellegű. Nem helyettesíti az Airbus hivatalos dokumentációját,
nem minősül repülőképzésnek. Valódi műveletekhez mindig a QRH-t és megfelelően képzett oktató utasításait kövesse.
