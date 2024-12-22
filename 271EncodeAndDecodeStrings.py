class Codec:

    def encode(self, strs):
        encoded = ""

        messageLength = len(strs)

        encoded += str(messageLength) + ":"

        for word in strs:
            wordLength = len(word)
            encoded += str(wordLength) + ":" + word

        return encoded

    def decode(self, s):
        decoded = []

        messageLength = int(s.split(":")[0])

        currentMessage = ":".join(s.split(":")[1:])

        for i in range(messageLength):
            dividerIndex = currentMessage.find(":")
            wordLength = int(currentMessage[:dividerIndex])
            word = currentMessage[dividerIndex + 1 : dividerIndex + wordLength + 1]
            currentMessage = currentMessage[dividerIndex + wordLength + 1 :]
            decoded.append(word)

        return decoded
