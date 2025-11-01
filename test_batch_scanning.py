#!/usr/bin/env python3
"""
Тест батч-сканування всіх 733 пар
"""
import time
import threading
from config import *
from xt_client import create_xt, load_xt_futures_markets

# Ініціалізація XT
xt = create_xt(api_key=XT_API_KEY, api_secret=XT_API_SECRET, account_name="Test")
markets = load_xt_futures_markets(xt)

print(f"\n🚀 Знайдено {len(markets)} торгових пар на XT біржі\n")

# Тест батч-обробки
symbols = list(markets.keys())
batch_size = MAX_CONCURRENT_SYMBOLS
total_symbols = len(symbols)

print(f"📦 Розбиваємо {total_symbols} символів на батчі по {batch_size}")
print(f"Всього батчів: {(total_symbols + batch_size - 1) // batch_size}\n")

batch_count = 0
for batch_start in range(0, total_symbols, batch_size):
    batch_end = min(batch_start + batch_size, total_symbols)
    batch_symbols = symbols[batch_start:batch_end]
    batch_count += 1
    
    print(f"📦 Батч {batch_count}: символи {batch_start+1}-{batch_end} ({len(batch_symbols)} символів)")
    print(f"   Перші 5: {batch_symbols[:5]}")
    print(f"   Останні 5: {batch_symbols[-5:]}")
    
    if batch_end < total_symbols:
        print(f"   ⏸️  Пауза між батчами...")
        print()

print(f"\n✅ Всього оброблено батчів: {batch_count}")
print(f"✅ Всього символів буде оброблено: {total_symbols}")
