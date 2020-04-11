import requests


class ResponseManager:
    def __init__(self, url):
        self.STATUS_CODES = {200: "Everything went okay, and the result has been returned (if any).",
                             301: "The server is redirecting you to a different endpoint. " +
                                  "This can happen when a company switches domain names, " +
                                  "or an endpoint name is changed.",
                             400: "The server thinks you made a bad request. " +
                                  "This can happen when you don’t send along the right data, among other things.",
                             401: "The server thinks you’re not authenticated. " +
                                  "Many APIs require login credentials, " +
                                  "so this happens when you don’t send the right credentials to access an API.",
                             403: "The resource you’re trying to access is forbidden: " +
                                  "you don’t have the right permissions to see it.",
                             404: "The resource you tried to access was not found on the server.",
                             503: "The server is not ready to handle the request."}
        self.URL = url

    def get_response(self, parameters: dict):
        response = requests.get(self.URL, params=parameters)

        print("STATUS : {}".format(self.get_status(response.status_code)))
        if response.status_code != 200:
            return None
        else:
            return response.json()

    def check_status_code(self, status_code):
        if status_code in self.STATUS_CODES.keys():
            return True
        else:
            return False

    def get_status(self, status_code):

        if self.check_status_code(status_code):
            return self.STATUS_CODES[status_code]
        else:
            return "Invalid Status Code"
