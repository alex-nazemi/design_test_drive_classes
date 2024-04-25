from lib.music_tracker import MusicTracker
import pytest

# when I add a track it is added to the list
def test_track_added():
    music_tracker = MusicTracker()
    music_tracker.add("Happy")
    assert music_tracker.getTracks() == ["Happy"] 

def test_adding_multiple_tracks():
    music_tracker = MusicTracker()
    music_tracker.add("Happy")
    music_tracker.add("Wrecking Ball")
    music_tracker.add("Lose Yourself")
    assert music_tracker.getTracks() == ["Happy", "Wrecking Ball", "Lose Yourself"]

def test_list_is_created():
    music_tracker = MusicTracker()
    assert music_tracker.getTracks() == []

def test_title_is_empty_string():
    music_tracker = MusicTracker()
    with pytest.raises(Exception, match=r"No title was entered."):
        music_tracker.add("")