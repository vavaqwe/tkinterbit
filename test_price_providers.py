#!/usr/bin/env python3
"""
Тест пріоритету провайдерів цін: DexScreener -> CoinGecko -> Blockchain
"""
import time
from config import *
from dex_client import dex_client

# Тестові токени
test_symbols = ['BTC', 'ETH', 'SOL', 'XRP', 'ADA', 'DOGE', 'MATIC', 'LINK', 'AVAX', 'UNI']

print("\n🧪 ТЕСТ ПРІОРИТЕТУ ПРОВАЙДЕРІВ ЦІН\n")
print("Пріоритет: 1. DexScreener -> 2. CoinGecko -> 3. Blockchain\n")
print("=" * 80)

for symbol in test_symbols:
    print(f"\n🔍 Тестуємо: {symbol}")
    print("-" * 80)
    
    start_time = time.time()
    result = dex_client.resolve_best_pair(f"{symbol}/USDT:USDT", for_convergence=False)
    elapsed = time.time() - start_time
    
    if result:
        price = result.get('price_usd', 0)
        provider = result.get('provider', 'unknown')
        liquidity = result.get('liquidity_usd', 0)
        volume = result.get('volume_24h', 0)
        
        print(f"✅ SUCCESS!")
        print(f"   Провайдер: {provider}")
        print(f"   Ціна: ${price:.6f}")
        print(f"   Ліквідність: ${liquidity:,.0f}")
        print(f"   Об'єм 24г: ${volume:,.0f}")
        print(f"   Час: {elapsed:.2f}s")
        
        # Перевірка валідації
        if price > 0.000001 and price < 100000:
            print(f"   ✅ Ціна валідна")
        else:
            print(f"   ⚠️  Ціна може бути невалідна")
    else:
        print(f"❌ FAILED - ціна не знайдена")
        print(f"   Час: {elapsed:.2f}s")
    
    # Невелика пауза між запитами
    time.sleep(0.5)

print("\n" + "=" * 80)
print("\n✅ Тест завершено!\n")

# Статистика провайдерів
stats = dex_client.provider_stats
print("📊 Статистика CoinGecko:")
print(f"   Успішно: {stats['coingecko_success']}")
print(f"   Помилки: {stats['coingecko_failed']}")
print(f"   Rate limit: {stats['coingecko_429']}")
