# ONE/USDT Futures Backtester

Этот проект — простой бэктестер для пары ONEUSDT (фьючерсы, Binance).

## Структура
- `data/` — CSV файлы с историческими данными
- `backtester.py` — основной файл для запуска
- `utils.py` — вспомогательные функции
- `requirements.txt` — зависимости

## Установка
```bash
git clone https://github.com/yourusername/oneusdt-backtester.git
cd oneusdt-backtester
pip install -r requirements.txt
```

## Запуск
```bash
python backtester.py --csv data/oneusdt.csv --strategy sma
```

