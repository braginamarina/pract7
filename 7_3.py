week_days = ("ПН", "ВТ", "СР", "ЧТ", "ПТ", "СБ", "ВС")
weekend_count = int(input("Сколько выходных дней на неделе вы хотите? "))

weekend_days = list(week_days[-weekend_count:])
work_days = list(week_days[:-weekend_count])

print(f"\nВаши выходные дни: {weekend_days}")
print(f"Ваши рабочие дни: {work_days}")
