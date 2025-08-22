#导入
from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.faker import Faker

#准备数据
lst=[['可乐',23],['雪碧',45],['啤酒',76],['奶茶',13]]
c = (
    Pie()
   #.add("", [list(z) for z in zip(Faker.choose(), Faker.values())])
    .add("",lst)
    .set_global_opts(title_opts=opts.TitleOpts(title="2025年饮品销量占比情况"))
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
   .render("water.html")
)
#print([list(z) for z in zip(Faker.choose(), Faker.values())])