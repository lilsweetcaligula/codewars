def fuelPrice(litres, pricePerLiter):
    discount = min(litres // 2 * 0.05, 0.25) * litres
    return litres * pricePerLiter - discount