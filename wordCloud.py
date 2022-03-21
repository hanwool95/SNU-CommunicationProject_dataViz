from wordcloud import WordCloud
# import matplotlib.pyplot as plt

from data import Weight

w = Weight()

sharowjabda = {'mz세대': 25.3*w.sharojabda[0],
               '샤로잡다': 5.9*w.sharojabda[0]+19.9*w.sharojabda[2]+27.8*w.sharojabda[3]+15.6*w.sharojabda[5]+2*w.sharojabda[5]+5.5*w.sharojabda[7],
               'mz': 5.7*w.sharojabda[0],
               '서울대학교': 5.7*w.sharojabda[0]+4.7*w.sharojabda[1]+4.1*w.sharojabda[2]+3.2*w.sharojabda[2]+5.4*w.sharojabda[3]+3.6*w.sharojabda[3]+4.9*w.sharojabda[5],
               '사로잡다': 4.6*w.sharojabda[0]+6.3*w.sharojabda[3]+5.9*w.sharojabda[7],
               '저출산': 13.8*w.sharojabda[1], '출산율': 10.7*w.sharojabda[1], '인구절벽': 6.6*w.sharojabda[1],
               '조영태 교수': 3.7*w.sharojabda[1], '누리호': 21.4*w.sharojabda[2], '누리호 발사 장면': 1.8*w.sharojabda[2],
               '플랫폼': 3.1*w.sharojabda[3], '난민': 30.8*w.sharojabda[4], '아프가니스탄': 6.5*w.sharojabda[4],
               '아프가니스탄 난민': 5.1*w.sharojabda[4], '아프간 난민 한국': 4.7*w.sharojabda[4], '메타버스': 5.8*w.sharojabda[5], '맥스트': 2.6*w.sharojabda[5], 'bts': 32.8*w.sharojabda[7],
               '방탕소년단': 12.5*w.sharojabda[7], 'how bts melt the world': 1.4*w.sharojabda[7], '코로나 언제 끝날까': 15.3*w.sharojabda[8], '오명돈 교수 코로나': 12.1*w.sharojabda[8],
               '이왕재교수 코로나19백신': 4.6*w.sharojabda[8]}

peoples = {'서울대학교': 29.7*w.peoples[0]+7.6*w.peoples[0]+6*w.peoples[1]+5.5*w.peoples[2]+4.1*w.peoples[2]+13.2*w.peoples[3]+8.7*w.peoples[3],
           '샤로잡다': 4.7*w.peoples[0],
           'seoul national university': 2.8*w.peoples[0], '기부': 2.5*w.peoples[0],
           '서울대 언론정보학과': 16.4*w.peoples[1], '언론정보학과': 9*w.peoples[1], '이오플로우': 1.5*w.peoples[1],
           '김인권': 6.8*w.peoples[2], '김수인원장': 1.4*w.peoples[2], '서울대 철학과': 6.6*w.peoples[3], '장대익': 5.7*w.peoples[3],
           '서울대 자유전공학부': 4.5*w.peoples[3], '유성호': 19.4*w.peoples[4]+11.4*w.peoples[4],
           '유성호 법의학자': 7.2*w.peoples[4]+6.3*w.peoples[4], '법의학자': 4.6*w.peoples[4],
           '김경민교수': 20*w.peoples[5]+12.6*w.peoples[5]+5.9*w.peoples[5], '부동산': 11.3*w.peoples[5],
           '김경민부동산': 5.9*w.peoples[5],
           '에릭오': 20.9*w.peoples[6],
           '서울대 서양학과': 7.7*w.peoples[6],
           '박훈': 1.4*w.peoples[7], '홍성욱': 1.4*w.peoples[7],
           '이날치': 51*w.peoples[8], '범내려온다': 12.9*w.peoples[8], '이날치 범내려온다': 5.1*w.peoples[8],
           '이날치 신유진': 2.1*w.peoples[8], '이날치밴드': 1.6*w.peoples[8],
           '권오철': 32.2*w.peoples[9]+2.9*w.peoples[9], '권오철 천체사진': 8*w.peoples[9], '유퀴즈 천체사진': 4*w.peoples[9],
           '천체사진가': 2.9*w.peoples[9], '안나 예이츠': 30.1*w.peoples[10]+15*w.peoples[10]+1.8*w.peoples[10],
           '판소리': 4.8*w.peoples[10],
           '안나 판소리': 2.1*w.peoples[10]
           }

snumaster = {'서울대학교': 37*w.snumaster[0]+5.9*w.snumaster[0]+18*w.snumaster[1]+31.6*w.snumaster[2]+4.2*w.snumaster[2]+54.8*w.snumaster[3]+5.5*w.snumaster[4]+4.9*w.snumaster[4]+15.9*w.snumaster[5],
             '서울대 캠퍼스': 9.8*w.snumaster[5],
             'snu': 5.9*w.snumaster[0]+5*w.snumaster[1]+2*w.snumaster[3], '서울대 교환학생': 12.7*w.snumaster[1],
             '교환학생가는법': w.snumaster[1], '관정도서관': w.snumaster[2], '서울대도서관': 2*w.snumaster[2], '서울대학식': 16.7*w.snumaster[4],
             '서울대 기숙사': 2.8*w.snumaster[4], '대학교 학식': 1.1*w.snumaster[4],
             '서울대 투어': 21.2*w.snumaster[5]
             }




wc = WordCloud(font_path='NanumGothic.otf', background_color="white", max_font_size=60)

sharowjabda_cloud = wc.generate_from_frequencies(sharowjabda)
sharowjabda_cloud.to_file('cloud_sharowjabda.jpg')

peoples_cloud = wc.generate_from_frequencies(peoples)
peoples_cloud.to_file('cloud_peoples.jpg')

snumaster_cloud = wc.generate_from_frequencies(snumaster)
snumaster_cloud.to_file('cloud_snumaster.jpg')

# plt.figure(figsize=(10, 8))
# plt.axis('off')
# plt.imshow(cloud)
# plt.show()