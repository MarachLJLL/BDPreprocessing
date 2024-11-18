
class CSV():

    def CSV(self, filepath):
        pass
    
    def add_column(self, column):
        pass
    
    @staticmethod
    def col_to_index(column):
        if (type(column) != str or not column.isalpha()):
            raise TypeError("method CSV.col_to_index only takes strings that contain just letters.")
        column = column.upper()  # Convert to uppercase to handle case insensitivity
        column_index = 0
        for i, char in enumerate(reversed(column)):
            column_index += (ord(char) - ord('A') + 1) * (26 ** i)
        return column_index - 1
            
            

        