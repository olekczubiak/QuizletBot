#nauka/quizletbot
**Informacje**
Jako iż prowadzący/nauczyciele zadają prace domowe na quizlecie i patrzą czy je rozwiązujemy. To jest skrypt który służy do pobrania bazy danych słówek a następnie wypełniania zadań.

**Instalacja**
1. Sciągnięcie i instalacja _pythona_ w wersji  >  3.6
2. Instalacja modułu pip, na Windowsie ściąga sie on automatyczne podczas ściągania pythona
3. Instalacja _selenium_ `pip Install selenium`  lub `python3.7 -m Install selenium` 
4. instalacja _chromedrivera_ [link](https://sites.google.com/a/chromium.org/chromedriver/)
5. Pobranie skryptu z githuba [GitHub](https://github.com/olekczubiak/QuizletBot)
6. Całość odpalamy przez terminal pamiętając o fladze -i która pozwala nam na integrację podczas pracy kodu
7. Tworzymy plik `secret.py` w którym piszemy 2 linijki kodu 

```
email = 'Tu wpisz swoj login/email’
password = 'Tu wpisz swoje haslo’
```

Instalacja może zająć trochę czasu najłatwiej jest ją wykonać na systemach unix’owych  

**Instrukcja**
1. Otwieramy terminal i wpisujemy `python3 -i quizlebot.py` co uruchamia nasz skrypt.
2. Otwiera sie przeglądarka i wybieramy dział który nas interesuje. 
3. Pamiętamy żeby w słówkach zaznaczyć **Oryginalną kolejność**
4. w konsoli wpisujemu `bot.words(50)` (50 to przykładowa liczba ktora symbolizuje ilosc słówek w danym ‚temacie’)
5. następnie przechodzimy do zakładki **pisanie** i w terminalu wpisujemy `bot.writting(50)` (tak samo jak wyżej z tą 50)
