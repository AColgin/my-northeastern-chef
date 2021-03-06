from chef.Query import *


class MessageParser(object):

    @staticmethod
    def food_location_time_parse(split_message : str) -> (str, str, str):
        food = ""
        location = ""
        time = ""
        last_keyword = ""
        for word in split_message:
            if word == "at" or word == "for":
                last_keyword = word
            elif last_keyword == "at":
                location += word + " "
            elif last_keyword == "for":
                time += word + " "
            else:
                food += word + " "
        food = food.strip()
        location = location.strip()
        time = time.strip()

        return food, location, time

    @staticmethod
    def parse_message(message : str) -> Query:
        message = message.lower()
        if message.startswith("!next "):
            split_message = message.split()[1:]
            food, location, time = MessageParser.food_location_time_parse(split_message)

            if not food:
                return InvalidQuery("Invalid food")

            return NextOccurrenceQuery(food, location, time)
        if message.startswith("!now "):
            split_message = message.split()[1:]
            food, location, _ = MessageParser.food_location_time_parse(split_message)

            if not food:
                return InvalidQuery("Invalid food")

            return CurrentStatusQuery(food, location)
        if message.startswith("!test"):
            return TestQuery()

        else:
            return InvalidQuery("")

