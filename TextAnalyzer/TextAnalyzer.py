class TextAnalyzer:
    def __init__(self, text):
        formattedText =  text.replace(',', '').replace('!', '').replace('.','').replace('?','')
        formattedText = formattedText.lower()
        self.fmtText = formattedText
    def freqAll(self):
        wordsList = self.fmtText.split()
        wordsDict = {}
        for word in set(wordsList):
            wordsDict[word] = wordsList.count(word)
        return wordsDict
    def freqOf(self, word):
        freqDict = self.freqAll()
        if word in freqDict:
            return freqDict[word]
        else:
            return 0

givenstring="Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet."
analyzer = TextAnalyzer(givenstring)
print("Formatted Text:", analyzer.fmtText)
print(analyzer.freqOf("lorem"))