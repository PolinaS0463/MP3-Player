main_menu = ["     - Меню -     ",
        "Прослушать песню;",
        "Посмотреть песни;",
        "Скачать песню;",
        "Удалить песню;",
        "Найти песню;",
        "| Выход |"
        ]

song_play_menu = ["Поставить на паузу",
                  "",]

input_song_path = "Введите название файла, под которым будет скачана песня: "
input_song_name = "Введите ТОЧНОЕ название песни БЕЗ кавычек и прочих символов (например, Sonne): "
input_song_singer = "Введите ТОЧНОГО исполнителя песни БЕЗ кавычек и прочих символов (например, Rammstein): "
input_sample_to_search = "Поиск: "

select_menu_item = "Выберите пункт меню: "
select_sorting_option = "Выберите путь сортировки песен: "

actions = ["воспроизведена", "скачана", "удалена"]
options = ["воспроизведения", "удаления"]

invalid_menu_item_error = f"Введите корректный пункт меню! Пункт меню представляет собой ЧИСЛО от 1 до {len(main_menu) - 1}!"
empty_song_sequence_error = "У вас еще нет песен! Добавьте первую!"

def song_action(name: str, action: str) -> str:
    return f"Песня '{name}' успешно {action}!"

def song_option(option: str) -> str:
    return f"Выберите песню для {option}: "

def findings(are: bool, sample: str, length: int = None) -> str:
    if are: return f"По вашему запросу '{sample}' было найдено {length} результатов"
    else: return f"К сожалению, по вашему запросу '{sample}' ничего не найдено!"

def invalid_song_id_error(my_songs_list_length: int) -> str:
    return f"Заметки с таким ID не существует! ID заметки представляет собой ЧИСЛО от 1 до {my_songs_list_length}"

def unknown_song_error(song_name: str) -> str:
    return f"К сожалению, песня '{song_name}' не была найдена!"