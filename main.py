from prepare_weather import prepare_weather
from prepare_events import prepare_events
from merge_data import merge_data
from prepare_isw import prepare_isw


def prepare_dataset():
    prepare_weather()
    prepare_events()
    prepare_isw()
    merge_data()
    


if __name__ == "__main__":
    prepare_dataset()
