# ЗАДАЧА:
# 🦄 “Превращение единорогов в радугу”
#
# Вам дан список единорогов, каждый представлен в виде словаря с полем color.
# Напишите функцию unicorns_to_rainbows(unicorns: list[dict]) -> list[str],
# которая превращает каждого единорога в строку:
# "🌈 Rainbow unicorn of color COLOR", где COLOR — цвет единорога.
#
# Пример:
unicorns = [{"color": "pink"}, {"color": "blue"}, {"color": "sparkly"}]

# результат:
# [
#   "🌈 Rainbow unicorn of color pink",
#   "🌈 Rainbow unicorn of color blue",
#   "🌈 Rainbow unicorn of color sparkly"
# ]
unicorns_list = []
def unicorns_to_rainbows(unicorns: list[dict]) -> list[str]:
    for i in unicorns:
        unicorns_list.append(f"🌈 Rainbow unicorn of color {i["color"]}")
    return unicorns_list

    print(unicorns_to_rainbows(unicorns))
