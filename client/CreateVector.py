from nltk import word_tokenize, sent_tokenize, FreqDist as fd


def createVector(filename, last):
    #Lexical
    doc = open('text/'+filename,'r')
    DocString = doc.read()
    data = []
    charactercount = len(DocString)
    alphebetcount = 0
    uppercasecount = 0
    digitcount = 0
    whitespacecount = 0
    tab_and_spacecount = 0
    # Freq Special char

    # WordBased
    totalwordcount = 0
    totalshortwords = 0
    totalcharinwordsC = 0
    avgwordlen = 0
    avg_sent_len_chars = 0
    avg_sent_len_word = 0
    total_dif_words = 0
    freq_once_ocur_words = 0  # Hapax legomena
    freq_twice_ocur_words = 0  # Hapax dislegomena
    Yule_K_measure = 0  # vocab richness def by yule
    Simpson_D_measure = 0  # vocab rich def by simpson
    Sichel_S_measure = 0 # vocab rich by sichele
    Brunet_W_measure  = 0# vocab rich by Brune
    Honore_R_measure  = 0# vocab rich by Honre
    Freq_dist_Wordlen = 0  # need 20 of these
    punclist = [0,0,0,0,0,0,0,0] #, . ? ! : ; ' "
    for x in DocString:
        if x.isalpha():
            alphebetcount+=1
        if x.isdigit():
            digitcount+=1
        if x.isupper():
            uppercasecount+=1
        if x==',':
            punclist[0]+=1
        if x=='.':
            punclist[1]+=1
        if x=='?':
            punclist[2]+=1
        if x=='!':
            punclist[3]+=1
        if x==':':
            punclist[4]+=1
        if x==';':
            punclist[5]+=1
        if x=='\'':
            punclist[6]+=1
        if x=='"':
            punclist[7]+=1

    # A-Z count
    letcur = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for line in enumerate(DocString):
        tab_and_spacecount+=line.count('\t')
        tab_and_spacecount+=line.count(' ')

        for i in range(0, 25):
            letcur[i] = letcur[i] + line.count(chr(i+65))+line.count(chr(i+97))

    words = word_tokenize(DocString, language='english')
    totalwordcount = len(words)
    temp = [x for x in words if len(x)<4]
    totalshortwords = len(temp)
    for x in words:
        totalcharinwordsC+=len(x)
    avgwordlen=totalcharinwordsC/len(words)
    sents = sent_tokenize(DocString,language='english')
    senttemp = 0
    for x in sents:
        senttemp+=len(x)
    avg_sent_len_chars=senttemp/len(sents)
    wordtemp = 0
    for x in sents:
        wordtemp+=len(word_tokenize(x,language='english'))
    avg_sent_len_word = wordtemp/len(sents)
    freqdist = fd(words)

    total_dif_words=len(freqdist)
    freq_once_ocur_words=len(freqdist.hapaxes())
    freqwords = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for x in freqdist:
        if freqdist[x]<=20:
            if freqdist[x]>=3:
                freqwords[freqdist[x]-3]+=1
    #richness measures

    #syntatic feat: freq punctuation, and function words will be loaded from the research doc asd


    #structural freatures
    data+=[charactercount,alphebetcount,uppercasecount,digitcount,whitespacecount,tab_and_spacecount]+letcur+\
          [totalwordcount,total_dif_words,totalshortwords,totalcharinwordsC,freq_twice_ocur_words,freq_once_ocur_words]\
          + freqwords+punclist
    read = open('profiles/'+last+'.txt', 'a')
    read.write('\n')
    for a in data:
        read.write(str(a)+',')

    read.write(" ")

def createVectorNoFile(filename):
    #Lexical
    doc = open('text/'+filename,'r')
    DocString = doc.read()
    data = []
    charactercount = len(DocString)
    alphebetcount = 0
    uppercasecount = 0
    digitcount = 0
    whitespacecount = 0
    tab_and_spacecount = 0
    # Freq Special char

    # WordBased
    totalwordcount = 0
    totalshortwords = 0
    totalcharinwordsC = 0
    avgwordlen = 0
    avg_sent_len_chars = 0
    avg_sent_len_word = 0
    total_dif_words = 0
    freq_once_ocur_words = 0  # Hapax legomena
    freq_twice_ocur_words = 0  # Hapax dislegomena
    Yule_K_measure = 0  # vocab richness def by yule
    Simpson_D_measure = 0  # vocab rich def by simpson
    Sichel_S_measure = 0 # vocab rich by sichele
    Brunet_W_measure  = 0# vocab rich by Brune
    Honore_R_measure  = 0# vocab rich by Honre
    Freq_dist_Wordlen = 0  # need 20 of these
    punclist = [0,0,0,0,0,0,0,0] #, . ? ! : ; ' "
    for x in DocString:
        if x.isalpha():
            alphebetcount+=1
        if x.isdigit():
            digitcount+=1
        if x.isupper():
            uppercasecount+=1
        if x==',':
            punclist[0]+=1
        if x=='.':
            punclist[1]+=1
        if x=='?':
            punclist[2]+=1
        if x=='!':
            punclist[3]+=1
        if x==':':
            punclist[4]+=1
        if x==';':
            punclist[5]+=1
        if x=='\'':
            punclist[6]+=1
        if x=='"':
            punclist[7]+=1

    # A-Z count
    letcur = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for line in enumerate(DocString):
        tab_and_spacecount+=line.count('\t')
        tab_and_spacecount+=line.count(' ')

        for i in range(0, 25):
            letcur[i] = letcur[i] + line.count(chr(i+65))+line.count(chr(i+97))

    words = word_tokenize(DocString, language='english')
    totalwordcount = len(words)
    temp = [x for x in words if len(x)<4]
    totalshortwords = len(temp)
    for x in words:
        totalcharinwordsC+=len(x)
    avgwordlen=totalcharinwordsC/len(words)
    sents = sent_tokenize(DocString,language='english')
    senttemp = 0
    for x in sents:
        senttemp+=len(x)
    avg_sent_len_chars=senttemp/len(sents)
    wordtemp = 0
    for x in sents:
        wordtemp+=len(word_tokenize(x,language='english'))
    avg_sent_len_word = wordtemp/len(sents)
    freqdist = fd(words)

    total_dif_words=len(freqdist)
    freq_once_ocur_words=len(freqdist.hapaxes())
    freqwords = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for x in freqdist:
        if freqdist[x]<=20:
            if freqdist[x]>=3:
                freqwords[freqdist[x]-3]+=1
    #richness measures

    #syntatic feat: freq punctuation, and function words will be loaded from the research doc asd


    #structural freatures
    data+=[charactercount,alphebetcount,uppercasecount,digitcount,whitespacecount,tab_and_spacecount]+letcur+\
          [totalwordcount,total_dif_words,totalshortwords,totalcharinwordsC,freq_twice_ocur_words,freq_once_ocur_words]\
          + freqwords+punclist
    return data

createVector('AlbertCamusThePlague.txt', 'Camus')
createVector('CAMUS, Albert - The Fall.txt', 'Camus')
createVector('existentialismIsAHumanismSartre.txt', 'Sartre')
createVector('The_Metamorphosis_T.txt', 'Kafka')
