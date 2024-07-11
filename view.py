from model import YourMusic, Song
import text

def print_menu(menu) -> int:
    for i, item in enumerate(menu):
        if i == 0: print("\n" + item)
        else: print(f'{i}. {item}')
    while True:
        user_choice = input(text.select_menu_item)
        if user_choice.isdigit() and 0 < int(user_choice) < len(menu): return int(user_choice)
        else: print(text.invalid_menu_item_error)

def get_id(input_msg: str, music: YourMusic):
    while True:
        note_id = input_request(input_msg)
        if note_id.isdigit() and int(note_id) >= 1 and int(note_id) <= len(music.my_songs): return int(note_id) - 1
        else: print(text.invalid_song_id_error(len(music.my_songs)))

def show_songs(music: YourMusic, songs: list[Song]) -> None:
    lens = [len(song.full(music)) for song in songs]
    max_len = max(lens)
    print('\n' + '>' * max_len)
    for id in range(len(songs)):
        print(songs[id].full(music))
    print('>' * max_len + "\n")

def get_song_info_to_download() -> list[str]:
    song_name = input_request(text.input_song_name)
    song_singer = input_request(text.input_song_singer)
    song_path = input_request(text.input_song_path) + ".mp3"
    return [f"{song_name.replace(' ', '+')}+{song_singer.replace(' ', '+')}", song_name, song_singer, song_path]

def print_warning(msg: str) -> None:
    print('\n' + '=' * len(msg))
    print(msg)
    print('=' * len(msg) + '\n')
    
def print_message(msg: str) -> None:
    print('\n' + '*' * len(msg))
    print(msg)
    print('*' * len(msg) + '\n')

def input_request(input_text: str) -> str:
    return input(input_text) 
