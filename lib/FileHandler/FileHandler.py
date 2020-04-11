import os
import csv


class CSVFileHandler:
    @classmethod
    def read_file_as_list(cls, file_path, first_line=True):
        file_path = os.path.abspath(file_path)
        if os.path.exists(file_path):
            with open(file_path) as csv_file:
                csv_reader = csv.reader(csv_file)
                file_content = []
                for row in csv_reader:
                    if first_line:
                        file_content.append(row)
                    else:
                        first_line = True
                return file_content
        else:
            print("File does not exist @ {}".format(file_path))
            return None
