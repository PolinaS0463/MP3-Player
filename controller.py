from model import YourMusic
import view, text, database

def start():
    yrm = YourMusic()
    database.create_table()
    yrm.restore_songs()
    while True:
        user_choice = view.print_menu(text.main_menu)
        match user_choice:
            case 1:
                if yrm.my_songs:
                    view.show_songs(yrm, yrm.my_songs)
                    song_id = view.get_id(text.song_option(text.options[0]), yrm)
                    song = yrm.my_songs[song_id]
                    yrm.play_song(song_id)
                    view.print_message(text.song_action(song.name, text.actions[0]))
                else: view.print_warning(text.empty_song_sequence_error)
            case 2:
                if yrm.my_songs:
                    view.show_songs(yrm, yrm.my_songs)
                else: 
                    view.print_warning(text.empty_song_sequence_error)
            case 3:
                song_info = view.get_song_info_to_download()
                a_link = yrm.find_link(song_info)
                if a_link:
                    yrm.download_song(song_info, a_link)
                    view.print_message(text.song_action(song_info[1], text.actions[1]))
                else: view.print_warning(text.unknown_song_error(song_info[1]))
            case 4:
                if yrm.my_songs:
                    view.show_songs(yrm, yrm.my_songs)
                    song_id = view.get_id(text.song_option(text.options[1]), yrm)
                    song = yrm.my_songs[song_id]
                    yrm.delete_song(song_id)
                    view.print_message(text.song_action(song.name, text.actions[2]))
                else: view.print_warning(text.empty_song_sequence_error)
            case 5:
                if yrm.my_songs:
                    sample = view.input_request(text.input_sample_to_search)
                    findings = yrm.search_song(sample)
                    if findings: 
                        view.print_message(text.findings(True, sample, len(findings)))
                        view.show_songs(yrm, findings)
                    else: view.print_warning(text.findings(False, sample))
                else: view.print_warning(text.empty_song_sequence_error)
            case 6:
                yrm.exit()