from random import choice

varianat = {
    1: 'камень',
    2: "ножницы",
    3: "бумага"
}

def varianat_game(user_choice: int) -> str:
    coumputer_choice = choice(list(varianat))
    if user_choice == coumputer_choice:
        return f"Ничья, Бот выбрал {varianat[coumputer_choice]}"
    elif user_choice == 1 and coumputer_choice == 2 \
        or user_choice == 2 and coumputer_choice == 3 \
            or user_choice == 3 and coumputer_choice == 1:
        return f"Вы выиграли, Бот выбрал {varianat[coumputer_choice]}"
    
    elif user_choice == 1 and coumputer_choice == 3 \
        or user_choice == 2 and coumputer_choice == 1 \
            or user_choice == 3 and coumputer_choice == 2:
        return f"Вы проиграли, Бот выбрал {varianat[coumputer_choice]}"

    else:
        return 'Выберите корректный ответ'