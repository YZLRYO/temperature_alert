import sys
from enum import Enum


class Status(Enum):
    NORMAL = 0
    FREEZING = 1
    BOILING = 2


def isNumber(line):
    try:
        num = float(line)
    except ValueError:
        print(line + " is not a valid number. Please input valid numbers.")
        return False
    return True


class TemperatureAlerting:
    def __init__(
        self,
        freezing_threshold,
        boiling_threshold,
        fluctuation_value,
        status=Status.NORMAL,
    ):
        self.freezing_threshold = freezing_threshold
        self.boiling_threshold = boiling_threshold
        self.fluctuation_value = fluctuation_value
        self.status = status

    def checkTemperature(self, temperature):
        result = str(temperature)
        if self.status == Status.NORMAL:
            if temperature <= self.freezing_threshold:
                self.status = Status.FREEZING
                result += " freezing"
            elif temperature >= self.boiling_threshold:
                self.status = Status.BOILING
                result += " boiling"
        elif self.status == Status.FREEZING:
            if temperature > self.freezing_threshold + self.fluctuation_value:
                self.status = Status.NORMAL
                result += " unfreezing"
            if temperature >= self.boiling_threshold:
                self.status = Status.BOILING
                result += " boiling"
        elif self.status == Status.BOILING:
            if temperature < self.boiling_threshold - self.fluctuation_value:
                self.status = Status.NORMAL
                result += " unboiling"
            if temperature <= self.freezing_threshold:
                self.status = Status.FREEZING
                result += " freezing"
        print(result)


def main():
    # Set up freezing threshold, boiling threshold and fluctuation value
    configs = []
    prompts_format = "Please input number for {}:"
    prompts_variable = ["freezing threshold", "boiling threshold", "fluctuation value"]
    while len(configs) != 3:
        i = len(configs)
        print(prompts_format.format(prompts_variable[i]))
        line = sys.stdin.readline().strip()
        if isNumber(line):
            if len(configs) == 1 and float(line) <= configs[0]:
                print("Boiling threshold should be higher than freezing threshold.")
            else:
                configs.append(float(line))
    freezing_threshold, boiling_threshold, fluctuation_value = (
        configs[0],
        configs[1],
        configs[2],
    )

    temperatureAlerting = TemperatureAlerting(
        freezing_threshold=configs[0],
        boiling_threshold=configs[1],
        fluctuation_value=configs[2],
    )

    # Check input value and alert
    while True:
        try:
            print("Please input number(s) for alerting, input `exit` to exit app.")
            line = sys.stdin.readline().strip()
            if line == "exit":
                print("Exiting the alerting application")
                break
            for temperature in line.split(" "):
                if isNumber(temperature):
                    temperatureAlerting.checkTemperature(float(temperature))
        except KeyboardInterrupt:
            break


if __name__ == "__main__":
    main()
