# PandoKombo
PandoKombo is a utility program that creates combo list 
from Wikipedia Articles specifying depth for related articles.

PandoKombo does not use libs, thus no requirements are needed except **Python 3**

PandoKombo uses the [Wikipedia API](https://fr.wikipedia.org/w/api.php) on the French endpoint

## Usage:
````bash
python3 pandokombo.py

.------..------..------..------..------..------..------..------..------..------.
|P.--. ||A.--. ||N.--. ||D.--. ||O.--. ||K.--. ||O.--. ||M.--. ||B.--. ||O.--. |
| :/\: || (\/) || :(): || :/\: || :/\: || :/\: || :/\: || (\/) || :(): || :/\: |
| (__) || :\/: || ()() || (__) || :\/: || :\/: || :\/: || :\/: || ()() || :\/: |
| '--'P|| '--'A|| '--'N|| '--'D|| '--'O|| '--'K|| '--'O|| '--'M|| '--'B|| '--'O|
`------'`------'`------'`------'`------'`------'`------'`------'`------'`------'
PandoKombo > Search >> Panda
         0 - Panda géant
         1 - Panda
         2 - Ailurus fulgens
         3 - Fiat Panda I
         4 - Kung Fu Panda
         5 - Fiat Panda II
         6 - Fiat Panda III
         7 - Fiat Panda
         8 - Pandas
         9 - Kung Fu Panda : Les Pattes du destin
PandoKombo > Choice >> 0
PandaKombo > Depth (Default 1) >>
[+] Fetching Panda géant...
[!] Can't fetch Références taxinomiques...
[+] Fetching Panda de Qinling...
[+] Fetching Porno-panda...
[+] Fetching Sanctuaires des pandas géants du Sichuan...
[+] Fetching Diplomatie du panda...
[!] Can't fetch (en) Référence Animal Diversity Web : espèce Ailuropoda melanoleuca...
[+] Fetching Chuang Chuang et Lin Hui...
[+] Fetching Panda roux...
[!] Can't fetch (fr+en) Référence ITIS : espèce Ailuropoda melanoleuca (David, 1869) (+ version anglaise)...
[+] Fetching Yuan Zi et Huan Huan...
PandoKombo > Continue (y/n) ? (Default False) >> y
PandoKombo > Search >> Panda
         0 - Panda géant
         1 - Panda
         2 - Ailurus fulgens
         3 - Fiat Panda I
         4 - Kung Fu Panda
         5 - Fiat Panda II
         6 - Fiat Panda III
         7 - Pandas
         8 - Fiat Panda
         9 - Kung Fu Panda 3
PandoKombo > Choice >> 4
PandaKombo > Depth (Default 1) >>
[+] Fetching Kung Fu Panda...
PandoKombo > Continue (y/n) ? (Default False) >> n
PandaKombo > Output Filename >> test.txt
````