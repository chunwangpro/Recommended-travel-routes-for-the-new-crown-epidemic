from django.http import HttpResponse
from django.shortcuts import render
from pyecharts.charts import Line, Map, Page
from pyecharts import options as opts

from .models import CyStat, ProvStat


def index(request):
    cy_stat = CyStat.objects.filter(cy_name='cn').order_by('-stat_dt')[:14]

    stat_list = [x.stat_dt for x in cy_stat]
    stat_list.reverse()

    today_confirm_list = [x.today_confirm for x in cy_stat]
    today_confirm_list.reverse()

    today_new_confirm_list = [x.today_new_confirm for x in cy_stat]
    today_new_confirm_list.reverse()

    def ncov_line():
        c = (
            Line()
            .add_xaxis(stat_list)
            .add_yaxis("现有确诊", today_confirm_list)
            .add_yaxis("新增确诊", today_new_confirm_list)
            .set_global_opts(title_opts=opts.TitleOpts(title="全国疫情数据"))
        )
        return c

    def ncov_map():
        prov_stats = ProvStat.objects.filter(cy_name='cn').all()
        c = (
            Map()
            .add("现有确诊", [[x.prov_name, x.today_confirm] for x in prov_stats], "china")
            .set_global_opts(
                title_opts=opts.TitleOpts(title="各省现有确诊"),
                visualmap_opts=opts.VisualMapOpts(max_=200),
            )
        )
        return c

    page = Page(layout=Page.SimplePageLayout)
    page.add(
        ncov_line(),
        ncov_map()
    )
    return HttpResponse(page.render_embed())
