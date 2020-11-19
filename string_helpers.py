#string_helpers

class String_helper:

    def integer_array_to_string(self, array):
        result = str()
        for num in array:
            result += str(num)
        return result
         
    def string_to_array(self, string):
        result = list()
        for letter in string:
            result.append(letter)
        print(result)
        return result
