# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1573125355.478
_enable_loop = True
_template_filename = 'E:/lanjing/lanjingtest/demo/templates/iwork/home.html'
_template_uri = '/iwork/home.html'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        APP_ID = context.get('APP_ID', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        SITE_URL = context.get('SITE_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'<!DOCTYPE html>\r\n<html>\r\n\r\n<head>\r\n    <meta charset="utf-8" />\r\n    <meta http-equiv="X-UA-Compatible" content="IE=edge">\r\n    <meta name="viewport" content="width=device-width, initial-scale=1">\r\n    <title></title>\r\n    <!-- \u82e5\u60a8\u9700\u8981\u4f7f\u7528Kendo UI Professional\uff0c\u8bf7\u8054\u7cfb\u7248\u6743\u4eba\u83b7\u5f97\u5408\u6cd5\u7684\u6388\u6743\u6216\u8bb8\u53ef\u3002 -->\r\n    <!-- Bootstrap css -->\r\n    <link href="https://magicbox.bk.tencent.com/static_api/v3/assets/bootstrap-3.3.4/css/bootstrap.min.css" rel="stylesheet">\r\n    <!-- kendo ui css -->\r\n    <link href="https://magicbox.bk.tencent.com/static_api/v3/assets/kendoui-2015.2.624/styles/kendo.common.min.css" rel="stylesheet">\r\n    <link href="https://magicbox.bk.tencent.com/static_api/v3/assets/kendoui-2015.2.624/styles/kendo.default.min.css" rel="stylesheet">\r\n    <!-- font-awesome -->\r\n    <link href="https://magicbox.bk.tencent.com/static_api/v3/assets/fontawesome/css/font-awesome.css" rel="stylesheet">\r\n    <!--\u84dd\u9cb8\u63d0\u4f9b\u7684\u516c\u7528\u6837\u5f0f\u5e93 -->\r\n    <link href="https://magicbox.bk.tencent.com/static_api/v3/bk/css/bk.css" rel="stylesheet">\r\n    <link href="https://magicbox.bk.tencent.com/static_api/v3/bk/css/bk_pack.css" rel="stylesheet">\r\n    <!-- \u5982\u679c\u8981\u4f7f\u7528Bootstrap\u7684js\u63d2\u4ef6\uff0c\u5fc5\u987b\u5148\u8c03\u5165jQuery -->\r\n    <script src="https://magicbox.bk.tencent.com/static_api/v3/assets/js/jquery-1.10.2.min.js"></script>\r\n    <!-- \u5305\u62ec\u6240\u6709bootstrap\u7684js\u63d2\u4ef6\u6216\u8005\u53ef\u4ee5\u6839\u636e\u9700\u8981\u4f7f\u7528\u7684js\u63d2\u4ef6\u8c03\u7528\u3000-->\r\n    <script src="https://magicbox.bk.tencent.com/static_api/v3/assets/echarts-2.0/echarts-all.js"></script>\r\n    <script src="https://magicbox.bk.tencent.com/static_api/v3/assets/bootstrap-3.3.4/js/bootstrap.min.js"></script>\r\n    <!-- \u5305\u62ec\u6240\u6709kendoui\u7684js\u63d2\u4ef6\u6216\u8005\u53ef\u4ee5\u6839\u636e\u9700\u8981\u4f7f\u7528\u7684js\u63d2\u4ef6\u8c03\u7528\u3000-->\r\n    <script src="https://magicbox.bk.tencent.com/static_api/v3/assets/kendoui-2015.2.624/js/kendo.all.min.js"></script>\r\n    <script src="https://magicbox.bk.tencent.com/static_api/v3/assets/echarts-2.0/echarts-all.js"></script>\r\n    <script src="https://magicbox.bk.tencent.com/static_api/v3/bk/js/bk.js"></script>\r\n    <!-- \u6570\u636e\u57cb\u70b9\u7edf\u8ba1 -->\r\n    <script src="http://magicbox.bk.tencent.com/static_api/analysis.js"></script>\r\n    <!-- \u4ee5\u4e0b\u4e24\u4e2a\u63d2\u4ef6\u7528\u4e8e\u5728IE8\u4ee5\u53ca\u4ee5\u4e0b\u7248\u672c\u6d4f\u89c8\u5668\u652f\u6301HTML5\u5143\u7d20\u548c\u5a92\u4f53\u67e5\u8be2\uff0c\u5982\u679c\u4e0d\u9700\u8981\u7528\u53ef\u4ee5\u79fb\u9664 -->\r\n    <!--[if lt IE 9]><script src="https://magicbox.bk.tencent.com/static_api/v3/assets/js/html5shiv.min.js"></script><script src="https://magicbox.bk.tencent.com/static_api/v3/assets/js/respond.min.js"></script><![endif]-->\r\n     <script type="text/javascript">\r\n\t    \t  var app_id = "')
        __M_writer(unicode(APP_ID))
        __M_writer(u'";\r\n\t\t\t    var site_url = "')
        __M_writer(unicode(SITE_URL))
        __M_writer(u'";\t  // app\u7684url\u524d\u7f00,\u5728ajax\u8c03\u7528\u7684\u65f6\u5019\uff0c\u5e94\u8be5\u52a0\u4e0a\u8be5\u524d\u7f00\r\n\t\t\t    var static_url = "')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'"; // \u9759\u6001\u8d44\u6e90\u524d\u7f00\r\n\t      </script>\r\n</head>\r\n\r\n<body class="bg-white" data-bg-color="bg-white">\r\n    <div class="king-page-box">\r\n        <div class="king-container clearfix">\r\n            <nav class="">\r\n                <div style="overflow:hidden; z-index: inherit;" class="navbar king-horizontal-nav1  f14">\r\n                    <div class="navbar-container">\r\n                        <div class="navbar-header pull-left">\r\n                            <a class="navbar-brand" href="javascript:;">\r\n                                <img src="https://magicbox.bk.tencent.com/static_api/v3/bk/images/logo.png" class="logo"> </a>\r\n                        </div>\r\n                        <ul class="nav navbar-nav pull-left m0">\r\n                            <li class="active"><a href="javascript:void(0);">\u9996\u9875</a></li>\r\n                            <li><a href="javascript:void(0);">\u5173\u4e8e\u6211\u4eec</a></li>\r\n                            <li><a href="javascript:void(0);">\u8054\u7cfb\u6211\u4eec</a></li>\r\n                        </ul>\r\n                        <div class="navbar-header pull-right">\r\n                            <ul class="nav">\r\n                                <li class="user-info">\r\n                                    <a href="javascript:;">\r\n                                        <img class="img-rounded" src="https://magicbox.bk.tencent.com/static_api/v3/components/horizontal_nav1/images/avatar.png">\r\n                                        <span>admin</span>\r\n                                    </a>\r\n                                </li>\r\n                            </ul>\r\n                        </div>\r\n                    </div>\r\n                </div>\r\n            </nav>\r\n            <div class="king-block king-block-bordered king-block-themed mb0">\r\n                <div class="king-block-header king-info">\r\n                    <ul class="king-block-options">\r\n                        <li>\r\n                            <!-- <button type="button"><i class="fa fa-cog"></i></button> -->\r\n                        </li>\r\n                    </ul>\r\n                    <h3 class="king-block-title">\u4f1a\u8bae\u5185\u5bb9\u5f55\u5165</h3>\r\n                </div>\r\n                <div class="king-block-content">\r\n                    <form class="form-horizontal">\r\n                        <div class="form-group clearfix ">\r\n                            <label class="col-sm-3 control-label bk-lh30 pt0">\u4e3b\u9898\uff1a</label>\r\n                            <div class="col-sm-9">\r\n                                <input type="text" class="form-control bk-valign-top" id="theme" placeholder="\u4f1a\u8bae\u5f55\u5165"> </div>\r\n                        </div>\r\n                        <div class="form-group clearfix ">\r\n                            <label class="col-sm-3 control-label bk-lh30 pt0">\u5185\u5bb9\uff1a</label>\r\n                            <div class="col-sm-9">\r\n                                <input type="text" class="form-control bk-valign-top" id="content" placeholder="\u5185\u5bb9"> </div>\r\n                        </div>\r\n                        <div class="form-group clearfix">\r\n                            <div class="col-sm-9 col-sm-offset-3">\r\n                                <button type="button" class="king-btn mr10  king-success" onclick="save_record(this)">\u63d0\u4ea4</button>\r\n                                <button type="button" class="king-btn king-default ">\u53d6\u6d88</button>\r\n                            </div>\r\n                        </div>\r\n                    </form>\r\n                </div>\r\n            </div>\r\n            <div class="king-block king-block-bordered king-block-themed mb0">\r\n                <div class="king-block-header king-info">\r\n                    <ul class="king-block-options">\r\n                        <li>\r\n                            <!-- <button type="button"><i class="fa fa-cog"></i></button> -->\r\n                        </li>\r\n                    </ul>\r\n                    <h3 class="king-block-title">\u4f1a\u8bae\u4fe1\u606f\u5c55\u793a</h3>\r\n                </div>\r\n                <div class="king-block-content">\r\n                    <div style="height:310px; overflow: auto;" id="list_1526104329322">\r\n                        <table class="table mb0 pr15 ranger-box ">\r\n                            <tbody></tbody>\r\n                        </table>\r\n                    </div>\r\n                    <!-- \u8bbe\u7f6e\u9762\u677fStart -->\r\n                    <template id="range_nodata_tpl">\r\n                        <tr>\r\n                            <td colspan="3">\u6ca1\u6709\u6570\u636e</td>\r\n                        </tr>\r\n                    </template>\r\n                    <template id="ranger_tpl">\r\n                        <tr>\r\n                            <td style="width: 42px;">#index#</td>\r\n                            <td style="width: 40%;">#theme#</td>\r\n                            <td>#content#</td>\r\n                        </tr>\r\n                    </template>\r\n                    <!-- \u8bbe\u7f6e\u9762\u677fEnd -->\r\n                </div>\r\n            </div>\r\n        </div>\r\n    </div>\r\n    <script>\r\n         function renderTpl(str, cfg) {\r\n            var re = /(#(.+?)#)/g;\r\n\r\n            return str.replace(re, function() {\r\n                var val = cfg[arguments[2]]+\'\';\r\n                if(typeof val == \'undefined\') {\r\n                    val = \'\';\r\n                }\r\n                return val;\r\n            });\r\n        }\r\n\r\n        function initRanger(conf){\r\n            // \u5f02\u6b65\u8bf7\u6c42\u540e\u53f0\u6570\u636e\r\n            $.ajax({\r\n                url: conf.url,\r\n                type: \'GET\',\r\n                dataType: conf.dataType,\r\n                success: function(res){\r\n                    //\u83b7\u53d6\u6570\u636e\u6210\u529f\r\n                    if(res.code == 0){\r\n                        var _html = \' \';\r\n                        var list = res.data;\r\n\r\n                        var tpl = $(\'#ranger_tpl\').html();\r\n                        if (list.length == 0) {\r\n                            _html = $(\'#ranger_nodata_tpl\').html();\r\n                        }else{\r\n                            for (var i=0,len=list.length; i < len; i++){\r\n                                var item = list[i];\r\n                                _html += renderTpl(tpl, item)\r\n                            }\r\n                        }\r\n                        $(conf.container).html(_html);\r\n                    }\r\n                }\r\n            });\r\n        }\r\n\r\n\r\n        //\u4fdd\u5b58\u4f1a\u8bae\u6570\u636e\r\n        function save_record(obj){\r\n            var theme = $(\'#theme\').val();\r\n            var content = $(\'#content\').val();\r\n            console.log(\'11\')\r\n            $.post(\'')
        __M_writer(unicode(SITE_URL))
        __M_writer(u"iwork/save_record/', {'theme': theme, 'content': content}, function(data){\r\n                if(data.result){\r\n                   initRanger({url: '")
        __M_writer(unicode(SITE_URL))
        __M_writer(u"iwork/records/',dataType: 'json',container: '#list_1526104329322 .ranger-box tbody'})\r\n                }else{\r\n                   alert(data.message)\r\n                }\r\n            }, 'json')\r\n            return\r\n        }\r\n    </script>\r\n    <script>\r\n        initRanger({url: '")
        __M_writer(unicode(SITE_URL))
        __M_writer(u"iwork/records/',dataType: 'json',container: '#list_1526104329322 .ranger-box tbody'})\r\n    </script>\r\n</body>\r\n\r\n</html>")
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"32": 177, "33": 179, "34": 179, "35": 188, "36": 188, "42": 36, "16": 0, "24": 1, "25": 34, "26": 34, "27": 35, "28": 35, "29": 36, "30": 36, "31": 177}, "uri": "/iwork/home.html", "filename": "E:/lanjing/lanjingtest/demo/templates/iwork/home.html"}
__M_END_METADATA
"""