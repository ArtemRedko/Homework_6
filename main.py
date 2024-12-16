import HW.chess as ch

positions = [(0, 2), (1, 5), (2, 3), (3, 0), (4, 7), (5, 4), (6, 6), (7, 1)]

if ch.check_queen_8x8(positions):
    print("Ферзи не бьют друг друга")
else:
    print("Есть ферзи под угрозой!")

total_case_generate = 0  # всего расстановок 
case_ok = 0  # удачных расстановок 
list_ok_positions = []  # список удачных расстановок

while case_ok < 4:
    generated_position = ch.gen_positions()
    total_case_generate += 1
    if ch.check_queen_8x8(generated_position):
        case_ok += 1
        list_ok_positions.append(generated_position)

print(f"Сгенерировано {total_case_generate}, удачные:")
for pos in list_ok_positions:
    print(pos)