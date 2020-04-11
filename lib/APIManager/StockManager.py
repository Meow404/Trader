from lib.APIManager.ResponseManager import ResponseManager
from lib.FileHandler.FileHandler import CSVFileHandler


class FX:
    def __init__(self, api_key: str):
        self.alpha_vantage_url = "https://www.alphavantage.co/query"
        self.response_manager = ResponseManager(self.alpha_vantage_url)
        self.API_key = api_key
        self.intervals = {0: "1min", 1: "5min", 2: "15min", 3: "30min", 4: "60min"}

    @classmethod
    def get_currency_list(cls, file_list):
        currency_list = []
        for row in file_list:
            currency_list.append(row[0])
        return currency_list

    @classmethod
    def get_valid_currency_list(cls):
        valid_currency_list = []
        physical_currency_list = CSVFileHandler.read_file_as_list("res\\physical_currency_list.csv", first_line=False)
        digital_currency_list = CSVFileHandler.read_file_as_list("res\\physical_currency_list.csv", first_line=False)
        valid_currency_list.extend(physical_currency_list)
        valid_currency_list.extend(digital_currency_list)
        return valid_currency_list

    @classmethod
    def print_valid_currency_list(cls, step: int = 5):
        currency_list = cls.get_valid_currency_list()
        currency_list = cls.get_currency_list(currency_list)
        currency_list_length = len(currency_list)
        print("\n ~~~ Valid Currency List ~~~")
        for index in range(currency_list_length):
            if index % step == step - 1:
                print("{:4}".format(currency_list[index]))
            else:
                print("{:4}".format(currency_list[index]), end="   ")

    @classmethod
    def print_valid_currency(cls, step: int = 5):
        currency_list = cls.get_valid_currency_list()
        currency_list_length = len(currency_list)
        print("\n ~~~ Valid Currency List ~~~")
        for index in range(currency_list_length):
            if index % step == step - 1:
                print("{:4} : {:35}".format(currency_list[index][0], currency_list[index][1]))
            else:
                print("{:4} : {:35}".format(currency_list[index][0], currency_list[index][1]), end="   ")

    def check_interval(self, interval):
        if interval in self.intervals.keys():
            return True
        else:
            return False

    def check_output_size(self, output_size):
        output_sizes = ["compact", "full"]
        if output_size in output_sizes:
            return True
        else:
            return False

    def check_data_type(self, data_type):
        data_types = ["json", "csv"]
        if data_type in data_types:
            return True
        else:
            return False

    def get_currency_exchange_rate(self, from_currency: str = "USD", to_currency: str = "EUR"):
        valid_currency = self.get_currency_list(self.get_valid_currency_list())
        if from_currency in valid_currency:
            if to_currency in valid_currency:
                parameters = {"function": "CURRENCY_EXCHANGE_RATE",
                              "from_currency": from_currency,
                              "to_currency": to_currency,
                              "apikey": self.API_key}
                return self.response_manager.get_response(parameters)
            else:
                print("Invalid To Currency {}".format(to_currency))
        else:
            print("Invalid From Currency {}".format(from_currency))

    def get_fx_intraday(self, from_currency: str = "USD", to_currency: str = "EUR", interval: int = 0,
                        output_size: str = None, data_type: str = None):
        valid_currency = self.get_currency_list(self.get_valid_currency_list())
        if from_currency in valid_currency:
            if to_currency in valid_currency:
                if self.check_interval(interval):
                    parameters = {"function": "FX_INTRADAY",
                                  "from_symbol": from_currency,
                                  "to_symbol": to_currency,
                                  "interval": self.intervals[interval],
                                  "apikey": self.API_key}
                    if self.check_output_size(output_size):
                        parameters["outputsize"] = output_size
                    if self.check_data_type(data_type):
                        parameters["datatype"] = data_type
                    return self.response_manager.get_response(parameters)
            else:
                print("Invalid To Currency {}".format(to_currency))
        else:
            print("Invalid From Currency {}".format(from_currency))

    def get_fx_daily(self, from_currency: str = "USD", to_currency: str = "EUR", output_size: str = None,
                     data_type: str = None):
        valid_currency = self.get_currency_list(self.get_valid_currency_list())
        if from_currency in valid_currency:
            if to_currency in valid_currency:
                parameters = {"function": "FX_DAILY",
                              "from_symbol": from_currency,
                              "to_symbol": to_currency,
                              "apikey": self.API_key}
                if self.check_output_size(output_size):
                    parameters["outputsize"] = output_size
                if self.check_data_type(data_type):
                    parameters["datatype"] = data_type
                return self.response_manager.get_response(parameters)
            else:
                print("Invalid To Currency {}".format(to_currency))
        else:
            print("Invalid From Currency {}".format(from_currency))

    def get_fx_weekly(self, from_currency: str = "USD", to_currency: str = "EUR", output_size: str = None,
                      data_type: str = None):
        valid_currency = self.get_currency_list(self.get_valid_currency_list())
        if from_currency in valid_currency:
            if to_currency in valid_currency:
                parameters = {"function": "FX_WEEKLY",
                              "from_symbol": from_currency,
                              "to_symbol": to_currency,
                              "apikey": self.API_key}
                if self.check_output_size(output_size):
                    parameters["outputsize"] = output_size
                if self.check_data_type(data_type):
                    parameters["datatype"] = data_type
                return self.response_manager.get_response(parameters)
            else:
                print("Invalid To Currency {}".format(to_currency))
        else:
            print("Invalid From Currency {}".format(from_currency))

    def get_fx_monthly(self, from_currency: str = "USD", to_currency: str = "EUR", output_size: str = None,
                       data_type: str = None):
        valid_currency = self.get_currency_list(self.get_valid_currency_list())
        if from_currency in valid_currency:
            if to_currency in valid_currency:
                parameters = {"function": "FX_MONTHLY",
                              "from_symbol": from_currency,
                              "to_symbol": to_currency,
                              "apikey": self.API_key}
                if self.check_output_size(output_size):
                    parameters["outputsize"] = output_size
                if self.check_data_type(data_type):
                    parameters["datatype"] = data_type
                return self.response_manager.get_response(parameters)
            else:
                print("Invalid To Currency {}".format(to_currency))
        else:
            print("Invalid From Currency {}".format(from_currency))
