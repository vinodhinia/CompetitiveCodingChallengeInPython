class Solution:
    def flatten_dictionary(self, dictionary):

        return self.flatten_dictionary_helper(dictionary, '', {})

    def flatten_dictionary_helper(self, dictionary, key_str, result):
        for key, value in dictionary.items():
            if isinstance(value, type(dict)):
                if key_str is '':
                    self.flatten_dictionary_helper(value, key, result)
                else:
                    self.flatten_dictionary_helper(value, key_str+'.'+key, result)
            else:
                if key_str is '':
                    result[key] = value
                else:
                    result[key_str+'.'+key] = value
        return result

s = Solution()
dict = {
    "key1" : "1",
    "key2" : {
        "a" : "2",
        "b" : "3",
        "c": {
            "d" : "1"
        }
    }
}
print(s.flatten_dictionary({"Key1":"1","Key2":{"a":"2","b":"3","c":{"d":"3","e":"1"}}}))