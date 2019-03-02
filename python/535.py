"""
1. Use hash() function to quickly get a hash string of the object.
2. Use a dictionary to store the mappings for retrieving process.
"""
class Codec:
    def __init__(self):
        self.database = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        shortUrl = "http://tinyurl.com/" + str(abs(hash(longUrl)))
        self.database[shortUrl] = longUrl
        return shortUrl

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.database[shortUrl]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))