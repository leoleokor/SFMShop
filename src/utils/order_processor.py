def load_orders_from_file(filename):
    orders = []
    try:
        with open (filename,"r",encoding="utf-8") as file:
            for lines in file:
                orders.append(lines.strip())
    except FileNotFoundError:
        print("Ошибка: Файл не найден!")

    return orders


def calculate_order_total(price, discount_rate):
    total = round(price * (1 - discount_rate),2)
    return total


def get_discount_by_total(total):
    if total > 10000:
        return 0.15
    elif total > 5000:
        return 0.10
    elif total <= 0:
        return 0
    else:
        return 0.05


def process_orders(orders_data):
    orders_info = []
    for line in orders_data:
        try:
            info = line.split(':')
            if len(info) != 4:
                raise ValueError("Ошибка: Строка неверного формата!")
            order_id = info[0]
            price = int(info[1])
            status = info[2]
            user = info[3]
            discount = get_discount_by_total(price)
            order_total = calculate_order_total(price, discount)

            order_info_dict = {
                "order_id": order_id,
                "total": order_total,
                "status": status,
                "user": user
            }

            orders_info.append(order_info_dict)
        except ValueError as e:
            print(f"Ошибка обработки строки '{line}': {e}. Строка пропущена.")
    return orders_info


def analyze_orders(processed_orders):
    stats = {
        "total_orders": 0,
        "total_sum": 0,
        "by_status": {},
        "unique_users": set()
    }

    stats['total_orders'] = len(processed_orders)

    for order in processed_orders:
        stats['total_sum'] += order['total']
        status = order['status']
        if status not in stats['by_status']:
            stats['by_status'][status] = 1
        else:
            stats['by_status'][status] += 1
        stats['unique_users'].add(order['user'])
    stats['unique_users'] = list(stats['unique_users'])
    return stats


def process_order_file(input_file, output_file):
    orders_data = load_orders_from_file(input_file)
    processing = process_orders(orders_data)
    analyze = analyze_orders(processing)
    status_parts = []
    for status in analyze['by_status']:
        status_parts.append(f"{status}: {analyze['by_status'][status]}")
    statuses_text = ", ".join(status_parts)

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(f"Обработано заказов: {analyze['total_orders']}\n")
        file.write(f"Общая сумма: {analyze['total_sum']} руб.\n")
        file.write(f"По статусам: {statuses_text}\n")
        file.write(f"Уникальных пользователей: {len(analyze['unique_users'])}")