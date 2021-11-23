from pyecharts.faker import Faker
from pyecharts import options as opts  # 导入模块
from pyecharts.charts import Map  # 导入模块

customMap = (
    Map()
        .add("商家A",  # 图例
             [list(z) for z in zip(Faker.provinces, Faker.values())],  # 数据项
             "china"  # 地图
             )
        .set_global_opts(  # 设置全局项
        title_opts=opts.TitleOpts(  # 设置标题项
            title="中国地图"  # 设置标题名称
        )
    )
)
customMap.render("demo11.html") 
