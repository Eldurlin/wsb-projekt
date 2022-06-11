# Kalkulator Xero

Zakodował: Adam 11326

Aplikacja jest dostępna na serwerze, wykorzystując Microsoft Azure pod następującym adresem: http://xero-calc-wsb-11326.azurewebsites.net/

Do napisania został użyty:
- język Python,
- framework Flask do backendu,
- Bootstrap do frontendu,
- SQLite3 do bazy danych.

Aplikacja składa się:
- ze strony głównej, na której wyszczególnione są produkty, których cenę można obliczyć,
- ze strony logowania (admin - admin),
- ze strony, gdzie po zalogowaniu się można zmienić cenę pojedynczych rzeczy potrzebnych do wytworzenia zamówienia.

W ramach uporządkowania tworzenia aplikacji, wykorzystany został wzorzec projektowy:
- Builder do tworzenia kolejnych obiektów potrzebnych do obliczenia końcowej ceny,
- Singleton do logowania się.

Na ten moment możliwość rejestracji nie istnieje, jednakże będzie to dodane w przyszłości, gdyż na podstawie tej aplikacji będzie tworzona praca inżynierska.
