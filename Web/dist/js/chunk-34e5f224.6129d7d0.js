(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-34e5f224"],{"16c0":function(t,i,s){"use strict";s.r(i);var e=function(){var t=this,i=t.$createElement,s=t._self._c||i;return s("transition",{attrs:{name:"fade-transform",mode:"out-in"}},[s("div",{staticClass:"home"},[s("firstscreen"),s("gutterlicard"),s("myintroduce"),s("dynamics")],1)])},a=[],l=function(){var t=this,i=t.$createElement,s=t._self._c||i;return s("div",{staticClass:"FirstScreen"},[s("vue-particles",{staticClass:"lizi",attrs:{color:"#409EFF",particleOpacity:.7,particlesNumber:60,shapeType:"circle",particleSize:4,linesColor:"#409EFF",linesWidth:1,lineLinked:!0,lineOpacity:.4,linesDistance:150,moveSpeed:2,hoverEffect:!0,hoverMode:"grab",clickEffect:!0,clickMode:"push"}}),s("div",{staticClass:"contentpage main-content width-normal"},[s("div",{staticClass:"left-sidebar"},[s("div",{staticClass:"content-introduce"},[t._v(t._s(t.introduce))]),s("div",{staticClass:"content-longintroduction"},[t._v(t._s(t.longintroduction))]),s("div",{staticClass:"sidebar-box"},t._l(t.button,(function(i,e){return s("div",{key:e},[s("a",{attrs:{href:i.link}},[1==i.type?s("el-button",{staticClass:"elbutton",attrs:{type:"primary"}},[t._v(t._s(i.title))]):t._e(),2==i.type?s("el-button",{staticClass:"elbutton"},[t._v(t._s(i.title))]):t._e()],1)])})),0)]),s("div",{staticClass:"right-imgbox"},[s("live2d")],1)])],1)},c=[],n=function(){var t=this,i=t.$createElement,s=t._self._c||i;return s("vue-live2d",{attrs:{modelPath:t.modelPath,width:t.width,height:t.height,isScale:t.isScale,isMove:t.isMove}})},r=[],o={name:"app",data:function(){return{isScale:!1,isMove:!1,width:500,height:800,modelPath:[{order:1,path:"/live2d/2.json"}]}}},d=o,v=(s("7530"),s("2877")),u=Object(v["a"])(d,n,r,!1,null,"564a2b48",null),m=u.exports,p={name:"firstscreen",data:function(){return{introduce:"欢迎来到WeiVi的 个人主页",longintroduction:"我的主页上有我的设计作品 动画作品 软件 程序 游戏 获奖作品等众多内容 欢迎阅读  如果想快速了解我可以点击下方的按钮 前往",button:[{link:"/opus",title:"我的设计作品 >",type:1},{link:"/proj",title:"个人项目作品 >",type:2}]}},components:{Live2d:m}},C=p,_=(s("2d6e"),Object(v["a"])(C,l,c,!1,null,"0358dcde",null)),f=_.exports,h=function(){var t=this,i=t.$createElement,s=t._self._c||i;return s("div",{staticClass:"GutterLiCard main-content width-normal"},[s("div",{staticClass:"module-title"},[t._v(t._s(t.title))]),s("el-row",{attrs:{gutter:30}},t._l(t.data,(function(i,e){return s("div",{key:e,staticClass:"block"},[s("el-col",{attrs:{span:6}},[0==i.line_type?s("router-link",{attrs:{to:i.link}},[s("div",{staticClass:"item-imgbox"},[s("el-image",{staticClass:"item-img",attrs:{src:i.cover}})],1),s("div",{staticClass:"item-title"},[t._v(t._s(i.title))]),s("div",{staticClass:"item-introduce"},[t._v(t._s(i.introduce))]),s("div",{staticClass:"item-linkbutt"},[t._v("了解更多 >")])]):t._e(),1==i.line_type?s("a",{attrs:{href:i.link,target:"_blank"}},[s("div",{staticClass:"item-imgbox"},[s("el-image",{staticClass:"item-img",attrs:{src:i.cover}})],1),s("div",{staticClass:"item-title"},[t._v(t._s(i.title))]),s("div",{staticClass:"item-introduce"},[t._v(t._s(i.introduce))]),s("div",{staticClass:"item-linkbutt"},[t._v("了解更多 >")])]):t._e()],1)],1)})),0)],1)},g=[],b={name:"GutterLiCard",data:function(){return{title:"更多",data:[]}},components:{},created:function(){this.query_list()},methods:{query_list:function(t){var i=this;this.$http.index_morelink_list({}).then((function(t){200==t.code&&(i.data=t.data)})).catch((function(t){console.log("error",t)}))}}},y=b,x=(s("4516"),Object(v["a"])(y,h,g,!1,null,"4ef67428",null)),k=x.exports,w=function(){var t=this,i=t.$createElement,s=t._self._c||i;return s("div",{staticClass:"MyIntroduce"},[s("div",{staticClass:"main-content width-normal"},[s("div",{staticClass:"modulecontent-width"},[s("div",{staticClass:"myinfobox"},[s("div",{staticClass:"floadhead"},[s("img",{staticClass:"floadhead-img",attrs:{src:this.Common.httpUrl+"/static/head.png"}})]),s("div",{staticClass:"myinforightbox"},[s("div",{staticClass:"myinfo-myname"},[t._v(t._s(t.myname)+"的个人介绍")]),s("div",{staticClass:"myinfo-myintroduce"},[t._v(t._s(t.myintroduce))])])]),s("div",[s("el-row",{attrs:{gutter:5}},[s("el-col",{attrs:{span:8}},[s("div",{staticClass:"list"},[s("div",{staticClass:"list-page"},[s("div",{staticClass:"list-pagename"},[t._v("个人介绍")]),s("div",{staticClass:"list-pageitembox"},[t._v(" 本人初一因校园暴力被欺负缀学, 凭自己努力自学各种技能, 很喜欢动漫因此学会了视频制作和平面设计, 也因此就业过, 后来为了开发自己的动漫网站等接触了程序这行, 如今在一家科技公司担任开发 ")])]),s("div",{staticClass:"list-page"},[s("div",{staticClass:"list-pagename"},[t._v("个人成就")]),s("div",{staticClass:"list-pageitembox"},[s("div",{staticClass:"list-item"},[s("el-row",{attrs:{gutter:20}},t._l(t.honour,(function(i,e){return s("div",{key:e},[s("el-col",{attrs:{span:12}},[s("div",{staticClass:"list-imgitembox"},[s("div",{staticClass:"list-imgitemimgbox"},[s("el-image",{staticClass:"list-imgitem-img",attrs:{src:i.url,fit:"scale-down"}})],1),s("div",{staticClass:"list-imgitem-title"},[t._v(t._s(i.title))])])])],1)})),0)],1)])])])]),s("el-col",{attrs:{span:8}},[s("div",{staticClass:"list"},[s("div",{staticClass:"list-page"},[s("div",{staticClass:"list-pagename"},[t._v("个人荣誉")]),s("div",{staticClass:"list-pageitembox"},[s("div",{staticClass:"list-item"},[t._v("2018年全国大学生创新技术应用大赛获奖者")])])]),s("div",{staticClass:"list-page"},[s("div",{staticClass:"list-pagename"},[t._v("职业经验")]),s("div",{staticClass:"list-pageitembox"},[s("div",{staticClass:"list-item"},[t._v("淘宝美工设计")]),s("div",{staticClass:"list-item"},[t._v("影视后期制作")]),s("div",{staticClass:"list-item"},[t._v("动漫周边店店长")]),s("div",{staticClass:"list-item"},[t._v("视频制作团队运营和创始人")]),s("div",{staticClass:"list-item"},[t._v("淘宝电商工作室")]),s("div",{staticClass:"list-item"},[t._v("自主外包程序开发团队")]),s("div",{staticClass:"list-item"},[t._v("原创视频分享网站创始人及CEO")]),s("div",{staticClass:"list-item"},[t._v("后端开发工程师")])])])])]),s("el-col",{attrs:{span:8}},[s("div",{staticClass:"list"},[s("div",{staticClass:"list-page"},[s("div",{staticClass:"list-pagename"},[t._v("技能")]),s("div",{staticClass:"list-pageitembox"},[s("div",{staticClass:"list-item"},[t._v("UE UI 设计")]),s("div",{staticClass:"list-item"},[t._v("电商运营 天猫淘宝店装修")]),s("div",{staticClass:"list-item"},[t._v("MG动画设计 3D动画 建模")]),s("div",{staticClass:"list-item"},[t._v("WEB前端开发 小程序开发")]),s("div",{staticClass:"list-item"},[t._v("服务器后端开发")])])]),s("div",{staticClass:"list-page"},[s("div",{staticClass:"list-pagename"},[t._v("熟练技术和软件")]),s("div",{staticClass:"list-pageitembox"},[s("div",{staticClass:"list-item"},[t._v("PS AE AxureRP Ai ")]),s("div",{staticClass:"list-item"},[t._v("Maya C4D")]),s("div",{staticClass:"list-item"},[t._v("Python Node Javascripts")]),s("div",{staticClass:"list-item"},[t._v("HTML5 VUE2-3 CSS3 NW.js Element")]),s("div",{staticClass:"list-item"},[t._v("Mysql Elasticsearch MariaDB MongDB")]),s("div",{staticClass:"list-item"},[t._v("Scrapy Redis Tornado Django Flask")])])])])])],1)],1)])])])},j=[],E={name:"myintroduce",data:function(){return{myname:"WeiVi",myintroduce:"男 出生于 1999/04/19 最高学历 初一 - 兴趣 : 羽毛球 公路车骑行 音乐 烹饪 摄影 禅茶",honour:[{title:"尼噗动漫视频网创始人",url:"http://127.0.0.1:8080/static/il1.png"},{title:"外管境外旅客护照信息提交系统开发组长",url:"http://127.0.0.1:8080/static/il2.png"},{title:"可识别全球护照的OCR核心研发者(投入使用中)",url:"http://127.0.0.1:8080/static/il3.png"},{title:"Yami!~动漫周边店创始人",url:"http://127.0.0.1:8080/static/il4.png"}]}}},$=E,M=(s("cd97"),Object(v["a"])($,w,j,!1,null,"7de84054",null)),S=M.exports,O=function(){var t=this,i=t.$createElement,s=t._self._c||i;return s("div",{staticClass:"Dynamics"},[s("div",{staticClass:"headerbox",style:t.path},[s("div",{staticClass:"contentbox main-content width-normal"},[t._m(0),s("div",{staticClass:"content"},[s("div",{staticClass:"contentl"},[s("div",{staticClass:"content-title"},[t._v("个人项目")]),s("div",{staticClass:"content-list"},t._l(t.projects,(function(i,e){return s("div",{key:e,staticClass:"content-porj-item"},[s("el-row",{attrs:{gutter:20}},[s("el-col",{attrs:{span:11}},[s("a",{attrs:{href:"/page?id="+i.id}},[s("el-image",{staticClass:"content-porj-item-cover",attrs:{src:i.cover}})],1)]),s("el-col",{attrs:{span:13}},[s("a",{attrs:{href:"/page?id="+i.id}},[s("div",{staticClass:"content-porj-item-text-title"},[t._v(t._s(i.title))]),s("div",{staticClass:"content-porj-item-text-introduce"},[t._v(t._s(i.introduce))])])])],1)],1)})),0)]),s("div",{staticClass:"contentr"},[s("div",{staticClass:"content-title"},[t._v("公开文章")]),s("div",{staticClass:"content-list"},t._l(t.article,(function(i,e){return s("div",{key:e,staticClass:"content-avet-item"},[s("el-row",{attrs:{gutter:20}},[s("el-col",{attrs:{span:8}},[s("a",{attrs:{href:"/page?id="+i.id}},[s("el-image",{staticClass:"content-avet-item-cover",attrs:{src:i.cover}})],1)]),s("el-col",{attrs:{span:13}},[s("a",{attrs:{href:"/page?id="+i.id}},[s("div",{staticClass:"content-avet-item-title"},[t._v(t._s(i.title))]),s("div",{staticClass:"content-porj-item-text-introduce"},[t._v(t._s(i.introduce))])])])],1)],1)})),0)])])])])])},A=[function(){var t=this,i=t.$createElement,s=t._self._c||i;return s("div",{staticClass:"header"},[s("div",{staticClass:"headertitlech"},[t._v("我的动态")]),s("div",{staticClass:"headertitleen"},[t._v("Dynamics")])])}],D=(s("fb6a"),s("b1d4")),F={name:"dynamics",data:function(){return{path:{backgroundImage:"url("+D["a"].httpUrl+"/static/dynamics-background.png)"},projects:[],article:[]}},created:function(){this.query_list()},methods:{query_list:function(){var t=this;this.$http.index_dynamics_data().then((function(i){200==i.code&&(t.projects=i.data.project.slice(0,2),t.article=i.data.article.slice(0,3))})).catch((function(t){console.log("error",t)}))}}},P=F,U=(s("556e"),Object(v["a"])(P,O,A,!1,null,"d5873014",null)),q=U.exports,L=s("5c96"),W={name:"Home",components:{firstscreen:f,gutterlicard:k,myintroduce:S,dynamics:q},created:function(){this.$route.params&&("login"==this.$route.params.topage&&(this.$forceUpdate(),this.$router.go(0)),this.$route.params.msg&&Object(L["Message"])({message:this.$route.params.msg,type:"error",duration:5e3}))}},B=W,R=Object(v["a"])(B,e,a,!1,null,"53e48390",null);i["default"]=R.exports},"1a51":function(t,i,s){},"1dde":function(t,i,s){var e=s("d039"),a=s("b622"),l=s("2d00"),c=a("species");t.exports=function(t){return l>=51||!e((function(){var i=[],s=i.constructor={};return s[c]=function(){return{foo:1}},1!==i[t](Boolean).foo}))}},"2d3d":function(t,i,s){},"2d6e":function(t,i,s){"use strict";var e=s("9f9b"),a=s.n(e);a.a},4516:function(t,i,s){"use strict";var e=s("ca2b"),a=s.n(e);a.a},"556e":function(t,i,s){"use strict";var e=s("eab3"),a=s.n(e);a.a},7530:function(t,i,s){"use strict";var e=s("2d3d"),a=s.n(e);a.a},8418:function(t,i,s){"use strict";var e=s("c04e"),a=s("9bf2"),l=s("5c6c");t.exports=function(t,i,s){var c=e(i);c in t?a.f(t,c,l(0,s)):t[c]=s}},"9f9b":function(t,i,s){},ca2b:function(t,i,s){},cd97:function(t,i,s){"use strict";var e=s("1a51"),a=s.n(e);a.a},eab3:function(t,i,s){},fb6a:function(t,i,s){"use strict";var e=s("23e7"),a=s("861d"),l=s("e8b5"),c=s("23cb"),n=s("50c4"),r=s("fc6a"),o=s("8418"),d=s("b622"),v=s("1dde"),u=s("ae40"),m=v("slice"),p=u("slice",{ACCESSORS:!0,0:0,1:2}),C=d("species"),_=[].slice,f=Math.max;e({target:"Array",proto:!0,forced:!m||!p},{slice:function(t,i){var s,e,d,v=r(this),u=n(v.length),m=c(t,u),p=c(void 0===i?u:i,u);if(l(v)&&(s=v.constructor,"function"!=typeof s||s!==Array&&!l(s.prototype)?a(s)&&(s=s[C],null===s&&(s=void 0)):s=void 0,s===Array||void 0===s))return _.call(v,m,p);for(e=new(void 0===s?Array:s)(f(p-m,0)),d=0;m<p;m++,d++)m in v&&o(e,d,v[m]);return e.length=d,e}})}}]);
//# sourceMappingURL=chunk-34e5f224.6129d7d0.js.map