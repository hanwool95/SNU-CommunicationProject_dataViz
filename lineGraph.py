import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

fontprop = fm.FontProperties(fname='NanumGothic.otf')

from data import Weight, Explore, Search

w = Weight()
e = Explore()
s = Search()

sharojabda_explore = 0
for i in range(len(w.sharojabda)):
    sharojabda_explore += w.sharojabda[i]*e.sharojabda[i]
sharojabda_explore = sharojabda_explore/w.total_sharojabda

peoples_explore = 0
for i in range(len(w.peoples)):
    peoples_explore += w.peoples[i]*e.peoples[i]
peoples_explore = peoples_explore/w.total_peoples
print(peoples_explore)

snumaster_explore = 0
for i in range(len(w.snumaster)):
    snumaster_explore += w.snumaster[i]*e.snumaster[i]
snumaster_explore = snumaster_explore/w.total_snumaster


sharojabda_search = 0
for i in range(len(w.sharojabda)):
    sharojabda_search += w.sharojabda[i]*s.sharojabda[i]
sharojabda_search = sharojabda_search/w.total_sharojabda

peoples_search = 0
for i in range(len(w.peoples)):
    peoples_search += w.peoples[i]*s.peoples[i]
peoples_search = peoples_search/w.total_peoples

snumaster_search = 0
for i in range(len(w.snumaster)):
    snumaster_search += w.snumaster[i]*s.snumaster[i]
snumaster_search = snumaster_search/w.total_snumaster

x_label = ['Sharojabda', 'SNUPeoples', 'SNUMaster']

explore_list = [sharojabda_explore, peoples_explore, snumaster_explore]
search_list = [sharojabda_search, peoples_search, snumaster_search]


plt.plot(x_label, explore_list, color='r', label='Explore')
plt.plot(x_label, search_list, color='b', label='Search')

for i in range(3):
    height = explore_list[i]
    plt.text(x_label[i], height - 5, '%.1f'%height, ha='center', va='bottom', size=12)

for i in range(3):
    height = search_list[i]
    plt.text(x_label[i], height + 2, '%.1f'%height, ha='center', va='bottom', size=12)

plt.ylabel('비율', fontproperties=fontprop)
plt.legend(loc='lower right')
plt.title('서울대 유튜브 콘텐츠 탐색 검색 비교', fontproperties=fontprop)

plt.savefig('search_explore_line.png')
plt.show()



