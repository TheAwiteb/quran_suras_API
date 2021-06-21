<br>
<h1 align="center">
  quran_suras_API
</h1>


<p align="center">
The API is based on the <a href=https://pypi.org/project/quran-suras>quran_suras</a> library
</p>


<p align="center">
  <a href="#requirements">requirements</a>
  •
  <a href="#installation">Installation</a>
  •
  <a href="#features">Features</a>
  •
  <a href="#usage">Usage</a>
  •
  <a href="#license">License</a>
</p>

## requirements
  **>= python3.7**

## Installation


```bash
# Installation
git clone https://codeberg.org/Awiteb/quran_suras_API
# Run
cd quran_suras_API
pip3 install -r requirements.txt
python3 app.py
```

## Features
* Access to all [quran_suras](https://pypi.org/project/quran-suras) library functions

## Usage

**get surah by number:**
```python
import requests

url = "http://127.0.0.1:8000/get_sura_by_number/?sura_number={}&amount={}"
sura_number = 2
amount = 1
suras = requests.get(url.format(sura_number, amount)).json()
print(suras)

```
<details>
<summary> Example Result</summary>

```json
{'ok': True,
 'result': [{'reader': 'أحمد الحذيفي',
             'url': 'https://server8.mp3quran.net/ahmad_huth/002.mp3'}],
 'sura_name': 'البقرة'}

```
</details>
<br><br>

**get surah by name:**
```python
import requests

url = "http://127.0.0.1:8000/get_sura_by_name/?sura_name={}&amount={}"
sura_name = 'الفرقان'
amount = 1
suras = requests.get(url.format(sura_name, amount)).json()
print(suras)
```
<details>
<summary> Example Result</summary>

```json
{'ok': True,
 'result': [{'reader': 'أحمد الحواشي',
             'url': 'https://server11.mp3quran.net/hawashi/025.mp3'}],
 'sura_name': 'الفرقان'}
```

</details>
<br><br>

**get surah name by number:**
```python
import requests

url = "http://127.0.0.1:8000/get_sura_name/?sura_number={}"
sura_number = 33
sura_name = requests.get(url.format(sura_number)).json()
print(sura_name)
```

<details>
<summary> Example Result</summary>

```json
{'name': 'الأحزاب', 'ok': True}
```

</details>
<br><br>

**get surah number by name:**
```python
import requests

url = "http://127.0.0.1:8000/get_sura_number/?sura_name={}"
sura_name = 'الناس'
sura_number = requests.get(url.format(sura_name)).json()
print(sura_number)

```

<details>
<summary> Example Result</summary>

```json
{'number': 114, 'ok': True}
```

</details>
<br><br>

**get page from quran by page number:**
```python
import requests

url = "http://127.0.0.1:8000/get_page/?page_number={}"
page_number = 7
page = requests.get(url.format(page_number)).json()
print(page)
```

<details>
<summary> Example Result</summary>

```json
https://www.mp3quran.net/api/quran_pages_arabic/601.png{'page_url': 'https://www.mp3quran.net/api/quran_pages_arabic/007.png', 'ok': True}
```

</details>
<br><br>

**get radios by language:**
```python
import requests

url = "http://127.0.0.1:8000/get_radios/?language={}&amount={}"
language = 'ar'
amount = 1
radios = requests.get(url.format(language, amount)).json()
print(radios)
```

<details>
<summary> Example Result</summary>

```json
{'language': 'ar', 'result': [{'name': '---تراتيل قصيرة متميزة---', 'url': 'http://live.mp3quran.net:9702/'}], 'ok': True}

```

</details>
<br><br>

## LICENSE
[GPLv3](https://www.gnu.org/licenses/gpl-3.0.html)