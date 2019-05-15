import math
import re


def calculateCosine(valueA, valueB):
    normA = 0
    normB = 0
    for i in range(len(valueA)):
        normA += valueA[i] * valueA[i]
        normB += valueB[i] * valueB[i]
    normB = math.sqrt(normB)
    normA = math.sqrt(normA)
    innerProduct = 0
    for i in range(len(valueA)):
        innerProduct += valueA[i] * valueB[i]
    return innerProduct / (normB * normA)

class Solution:

    def classification(self, text):
        """
        :type text: str
        :rtype: List[int]
        """
        # 1.处理文本信息
        # 要去除的标点符号、停用词的正则表达式
        punctuation_regex = '[()\\[\\]{},\'\'\\.;"]+'
        stop_word = {"a","about","above","ac","according","accordingly","across","actually","ad","adj","af","after","afterwards","again","against","al","albeit","all","almost","alone","along","already","als","also","although","always","am","among","amongst","amoungst","amount","an","and","another","any","anybody","anyhow","anyone","anything","anyway","anywhere","ap","apart","apparently","are","aren","arise","around","as","aside","at","au","auf","aus","aux","av","avec","away","b","back","be","became","because","become","becomes","becoming","been","before","beforehand","began","begin","beginning","begins","behind","bei","being","below","beside","besides","best","better","between","beyond","bill","billion","both","bottom","briefly","but","by","c","call","came","can","cannot","canst","cant","caption","captions","certain","certainly","cf","choose","chooses","choosing","chose","chosen","clear","clearly","co","come","comes","computer","con","contrariwise","cos","could","couldn","couldnt","cry","cu","d","da","dans","das","day","de","degli","dei","del","della","delle","dem","den","der","deren","des","describe","detail","di","did","didn","die","different","din","do","does","doesn","doing","don","done","dos","dost","double","down","du","dual","due","durch","during","e","each","ed","eg","eight","eighty","either","el","eleven","else","elsewhere","em","empty","en","end","ended","ending","ends","enough","es","especially","et","etc","even","ever","every","everybody","everyone","everything","everywhere","except","excepted","excepting","exception","excepts","exclude","excluded","excludes","excluding","exclusive","f","fact","facts","far","farther","farthest","few","ff","fifteen","fifty","fify","fill","finally","find","fire","first","five","foer","follow","followed","following","follows","for","former","formerly","forth","forty","forward","found","four","fra","frequently","from","front","fuer","full","further","furthermore","furthest","g","gave","general","generally","get","gets","getting","give","given","gives","giving","go","going","gone","good","got","great","greater","h","had","haedly","half","halves","hardly","has","hasn","hasnt","hast","hath","have","haven","having","he","hence","henceforth","her","here","hereabouts","hereafter","hereby","herein","hereto","hereupon","hers","herself","het","high","higher","highest","him","himself","hindmost","his","hither","how","however","howsoever","hundred","hundreds","i","ie","if","ihre","ii","im","immediately","important","in","inasmuch","inc","include","included","includes","including","indeed","indoors","inside","insomuch","instead","interest","into","inward","is","isn","it","its","itself","j","ja","journal","journals","just","k","kai","keep","keeping","kept","kg","kind","kinds","km","l","la","large","largely","larger","largest","las","last","later","latter","latterly","le","least","les","less","lest","let","like","likely","little","ll","long","longer","los","low","lower","lowest","ltd","m","made","mainly","make","makes","making","many","may","maybe","me","meantime","meanwhile","med","might","mill","million","mine","miss","mit","more","moreover","most","mostly","move","mr","mrs","ms","much","mug","must","my","myself","n","na","nach","name","namely","nas","near","nearly","necessarily","necessary","need","needed","needing","needs","neither","nel","nella","never","nevertheless","new","next","nine","ninety","no","nobody","none","nonetheless","noone","nope","nor","nos","not","note","noted","notes","nothing","noting","notwithstanding","now","nowadays","nowhere","o","obtain","obtained","obtaining","obtains","och","of","off","often","og","ohne","ok","old","om","on","once","onceone","one","only","onto","or","ot","other","others","otherwise","ou","ought","our","ours","ourselves","out","outside","over","overall","owing","own","p","par","para","part","particular","particularly","past","per","perhaps","please","plenty","plus","por","possible","possibly","pour","poured","pouring","pours","predominantly","previously","pro","probably","prompt","promptly","provide","provided","provides","providing","put","q","quite","r","rather","re","ready","really","recent","recently","regardless","relatively","respectively","reuters","round","s","said","same","sang","save","saw","say","second","see","seeing","seem","seemed","seeming","seems","seen","sees","seldom","self","selves","send","sending","sends","sent","serious","ses","seven","seventy","several","shall","shalt","she","short","should","shouldn","show","showed","showing","shown","shows","si","side","sideways","significant","similar","similarly","simple","simply","since","sincere","sing","single","six","sixty","sleep","sleeping","sleeps","slept","slew","slightly","small","smote","so","sobre","some","somebody","somehow","someone","something","sometime","sometimes","somewhat","somewhere","soon","spake","spat","speek","speeks","spit","spits","spitting","spoke","spoken","sprang","sprung","staves","still","stop","strongly","substantially","successfully","such","sui","sulla","sung","supposing","sur","system","t","take","taken","takes","taking","te","ten","tes","than","that","the","thee","their","theirs","them","themselves","then","thence","thenceforth","there","thereabout","thereabouts","thereafter","thereby","therefor","therefore","therein","thereof","thereon","thereto","thereupon","these","they","thick","thin","thing","things","third","thirty","this","those","thou","though","thousand","thousands","three","thrice","through","throughout","thru","thus","thy","thyself","til","till","time","times","tis","to","together","too","top","tot","tou","toward","towards","trillion","trillions","twelve","twenty","two","u","ueber","ugh","uit","un","unable","und","under","underneath","unless","unlike","unlikely","until","up","upon","upward","us","use","used","useful","usefully","user","users","uses","using","usually","v","van","various","ve","very","via","vom","von","voor","vs","w","want","was","wasn","way","ways","we","week","weeks","well","went","were","weren","what","whatever","whatsoever","when","whence","whenever","whensoever","where","whereabouts","whereafter","whereas","whereat","whereby","wherefore","wherefrom","wherein","whereinto","whereof","whereon","wheresoever","whereto","whereunto","whereupon","wherever","wherewith","whether","whew","which","whichever","whichsoever","while","whilst","whither","who","whoever","whole","whom","whomever","whomsoever","whose","whosoever","why","wide","widely","will","wilt","with","within","without","won","worse","worst","would","wouldn","wow","x","xauthor","xcal","xnote","xother","xsubj","y","ye","year","yes","yet","yipee","you","your","yours","yourself","yourselves","yu","z","za","ze","zu","zum"}
        text = text.split("\n")
        # 处理到文本
        text_list = []
        for s in text:
            if (len(s) != 0):
                text_list.append(re.sub(punctuation_regex, '', s.lower()))
        # print(text_list)
        # 2. TF-IDF 得到文章模型
        word2Doc = {}
        tf_idf = []
        for s in text_list:#获得文章
            # 分割为词
            # 当前词处理
            curDictWord2Sum = {}
            wordsInText = s.split()
            for word in wordsInText:
                if word in stop_word:
                    continue
                if word in curDictWord2Sum:
                    curDictWord2Sum[word] += 1
                else:
                    curDictWord2Sum[word] = 1
            keys = curDictWord2Sum.keys()
            # 计算TF值
            curDocTF = {}
            sumWord = len(curDictWord2Sum)
            for key in keys:
                curDocTF[key] = curDictWord2Sum[key] / sumWord
            tf_idf.append(curDocTF)
            # 添加至全局 corpus
            for key in keys:
                if key in word2Doc:
                    word2Doc[key] += 1
                else:
                    word2Doc[key] = 1
        # 计算TF-IDF值
        docSum = len(text_list)
        for curDocVal in tf_idf:
            for key in curDocVal:
                curDocVal[key] *= math.log(docSum / word2Doc[key], 2)

        # 生成TF-IDF矩阵
        keys = word2Doc.keys()
        matrix_tfidf = [[0] * len(keys) for i in range(len(text_list))]
        for i in range(len(text_list)):
            for j, key in enumerate(keys):
                curDoc = tf_idf[i]
                if key in curDoc:
                    matrix_tfidf[i][j] = curDoc[key]

        # 3. 生成离散余弦距离矩阵
        size = len(matrix_tfidf)
        cosValMatrix = [[0] * size for i in range(size)]
        for i in range(size - 1):
            for j in range(i + 1, size):
                if i != j:
                    cosValMatrix[i][j] = calculateCosine(matrix_tfidf[i], matrix_tfidf[j])
                    cosValMatrix[j][i] = cosValMatrix[i][j]

        # 4. 层次聚类操作
        ret = []
        for i in range(size):
            ret.append(i)
        flag = True
        while(flag):
            max = 0
            clusterA = 0
            clusterB = 0
            for i in range(len(ret) - 1):
                for j in range(i + 1, len(ret)):
                    if cosValMatrix[i][j] > max:
                        max, clusterA, clusterB = cosValMatrix[i][j], i, j
            if max < 0.028:
                flag = False
            else:
                if (ret[clusterA] > ret[clusterB]):
                    ret[clusterA] = ret[clusterB]
                else:
                    ret[clusterB] = ret[clusterA]
                cosValMatrix[clusterA][clusterB] = 0

        # 5. 聚类结果标准化输出
        start = ret[0]
        for i in range(len(ret)):
            if start < ret[i]:
                substractor = ret[i] - start - 1
                newVal = ret[i] - substractor
                for j in range(i, len(ret)):
                    if ret[j] == ret[i] and i != j:
                        ret[j] = newVal
                ret[i] = newVal
                start = ret[i]

        print("cluster", ret)
        print("words count: ", len(word2Doc))
        return ret

text = '''China Merchants Bank (CMB) is a Chinese bank headquartered in Futian District, Shenzhen,Guangdong, China. Founded in 1987, it is the first share-holding commercial bank wholly owned bycorporate legal entities in China.

In November 2007, CMB won federal approval to open a branch in New York City.


Beijing is the capital of the People's Republic of China, the world's third most populous city proper,and most populous capital city.

Combining both modern and traditional architecture, Beijing is one of the oldest cities in the world,with a rich history dating back three millennia. Many of Beijing's 91 universities[23] consistently rankamong the best in China, such as the Peking University and Tsinghua University. Beijing CBD is a centerfor Beijing's economic expansion, with the ongoing or recently completed construction of multipleskyscrapers. Beijing's Zhongguancun area is known as China's Silicon Valley and a center of innovationand technology entrepreneurship.

CMB engages primarily in corporate and retail banking and treasury operations throughout China and operates a branch and an investment advisor subsidiary in Hong Kong. In the United States, CMB operates a representative office in New York. CMB would be a qualifying foreign banking organization under Regulation K.

Financial technology, often shortened to FinTech or fintech, is the new technology and innovation that aims to compete with traditional financial methods in the delivery of financial services. It is an emerging industry that uses technology to improve activities in finance. The use of smartphones for mobile banking, investing services and cryptocurrency are examples of technologies aiming to make financial services more accessible to the general public. Financial technology companies consist of both startups and established financial institutions and technology companies trying to replace or enhance the usage of financial services provided by existing financial companies. Many existing financial institutions are implementing Fintech solutions and technologies in order to improve and develop their services, as well as gaining an improved competitive stance.


After reviewing more than 200 scientific papers citing the term "fintech," a scientific study on the definition of fintech concluded that "fintech is a new financial industry that applies technology to improve financial activities." FinTech is the new applications, processes, products, or business models in the financial services industry, composed of one or more complementary financial services and provided as an end-to-end process via the Internet.


FinTech companies provide both individuals and businesses with more scalable tools. These digital tools are disrupting traditional business models with innovative ideas and software solutions.  Although 2016 was not a good year for FinTech start-ups, several are poised to gain traction this year, and many have already experienced significant growth since their inception.

For traditional financial services companies (including banks, insurers and wealth and asset management companies), the risk of disruption is real, as FinTech companies invade their space. What does this mean for employers? With finance and technology rapidly merging, employers now have access to more scalable tools and online solutions than ever before. These technological solutions can assist them and their employees with offering or enhancing retirement savings plans as well as offering financial wellness programs, an employee benefit that has increasingly grown over the last several years.


Shenzhen (About this soundlisten)) is a major city in Guangdong Province, China; it forms part of the Pearl River Delta megalopolis, bordering Hong Kong to the south, Huizhou to the northeast, and Dongguan to the northwest. It holds sub-provincial administrative status, with powers slightly less than those of a province.


Shenzhen, which roughly follows the administrative boundaries of Bao'an County, officially became a city in 1979, taking its name from the former county town, whose train station was the last stop on the Mainland Chinese section of the railway between Canton and Kowloon. In 1980, Shenzhen was established as China's first special economic zone. Shenzhen's registered population as of 2017 was estimated at 12,905,000. However, the Shenzhen Municipal Party Committee estimates that the population of Shenzhen is about 20 million, due to the large unregistered floating migrant population living in the city. Shenzhen was one of the fastest-growing cities in the world in the 1990s and the 2000s[11] and has been ranked second on the list of ‘top 10 cities to visit in 2019 by Lonely Planet.

Shenzhen was singled out to be the first of the five Special Economic Zones (SEZ) in May 1980. Initially, the SEZ comprised an area of only 327.5 km2 (126.4 sq mi) of southern Shenzhen, covering the current Luohu, Futian, Nanshan and Yantian districts. The SEZ was promoted by Deng Xiaoping[29][30] and created to be an experimental ground for the practice of market capitalism within a community guided by the ideals of "socialism with Chinese characteristics".

Shenzhen became one of the largest cities in the Pearl River Delta region, which itself is an economic hub of China, as well as the largest manufacturing base in the world.

Shenzhen is located within the Pearl River Delta, bordering Hong Kong to the south, Huizhou to the north and northeast, Dongguan to the north and northwest. Lingdingyang and Pearl River to the west and Mirs Bay to the east and roughly 100 kilometres (62 mi) southeast of the provincial capital of Guangzhou. As of the end of 2017, the resident population of Shenzhen was 12,528,300, of which the registered population was 4,472,200, the actual administrative population was over 20 million.[38] It makes up part of Pearl Delta River built-up area with 44,738,513 inhabitants, spread over 9 municipalities (including Macau). The city is elongated measuring 81.4 kilometers from east to west while the shortest section from north to south is 10.8 kilometers.
'''

Solution().classification(text);