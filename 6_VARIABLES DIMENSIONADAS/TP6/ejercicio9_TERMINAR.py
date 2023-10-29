import time
from TP6_functions import fill_cards, show_cards, turn_cards_around, validate_equal_cards

print("🧠 MEMOTEST JUEGO 🧠\n")
arranged_cards = fill_cards()
#show_cards(arranged_cards)

hidden_cards = [["⬜","⬜","⬜"], ["⬜","⬜","⬜"]]
show_cards(arranged_cards)
time.sleep(1)
show_cards(hidden_cards)
time.sleep(1)

print("\n¿Qué cartas dar vuelta?")
show_cards([[1,2,3],[4,5,6]])

both_hearts_index = turn_cards_around(arranged_cards)
print(both_hearts_index)

validate_equal_cards(both_hearts_index, arranged_cards)


