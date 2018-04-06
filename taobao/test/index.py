# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2018/4/5 下午8:52
"""
from pyquery import PyQuery as pq

content = """

<!doctype html>
<html>
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <meta name="renderer" content="webkit">
    <meta name="data-spm" content="a231k">
    <title>淘宝热卖</title>
    <link rel="stylesheet" type="text/css" href="//g.alicdn.com/thx/cube/1.1.0/cube-min.css">
    <script src="//g.alicdn.com/??kissy/k/1.3.2/kissy-min.js" charset="utf-8"></script>
  <link rel="stylesheet" type="text/css" href="//lego.alicdn.com/mm/lego2??p4p-frame/0.0.7/index.css,p4p/backtop/0.0.1/index.css,p4p/related-search/0.0.1/index.css,p4p/search-area/0.0.1/index.css,p4p/search-layout/0.0.1/index.css,p4p/search-result/0.0.1/index.css,p4p/shop-hotsell-btm/0.0.1/index.css,re/searchheader/0.0.5/index.css"><script type="text/javascript" src="//lego.alicdn.com/mm/lego2??p4p-frame/0.0.7/index.js,p4p/backtop/0.0.1/index.js,p4p/related-search/0.0.1/index.js,p4p/search-area/0.0.1/index.js,p4p/search-result/0.0.1/index.js,p4p/shop-hotsell-btm/0.0.1/index.js,re/searchheader/0.0.5/index.js" crossorigin="anonymous"></script></head>

  <body data-spm="8165028"><script>window.pvid="300_11.130.176.180_120070_1522932550630";window.bucket_info="";with(document)with(body)with(insertBefore(createElement("script"),firstChild))setAttribute("exparams","category=&userid=&aplus&pvid=300_11.130.176.180_120070_1522932550630&bucket_info=&",id="tb-beacon-aplus",src="//g.alicdn.com/alilog/mlog/aplus_v2.js")</script><script src="//g.alicdn.com/mm/easytrace-mobile/1.0.9/js/traceWithAplus-min.js"></script><script>with(document)with(body)with(insertBefore(createElement("script"),firstChild))setAttribute("exparams","req_url=https%3A%2F%2Fre.taobao.com%2Fsearch%3Fspm%3Da231k.8165028.0782702702.203.63732e63wGLcj1%26prepvid%3D300_10.177.76.199_119596_1522932011677%26extra%3D%26keyword%3D%25E8%25BF%259E%25E8%25A1%25A3%25E8%25A3%25992018%2520%2520%25E9%2595%25BF%26frontcatid%3D%26isinner%3D1%26refpid%3D420435_1006%26page%3D1%26rewriteKeyword%26_input_charset%3Dutf-8&category=&aplus",id="tb-beacon-aplus",src="//g.alicdn.com/alilog/mlog/aplus_wap.js")</script>
    <!-- lego2 import from /alp/atb/common_pc_taobao_top.html --><link rel="stylesheet" href="//g.alicdn.com/tb/global/3.4.15/global-min.css" />
<script src="//g.alicdn.com/tb/global/3.4.15/global-min.js"></script>
<div id="J_SiteNav" class="site-nav">
  <div id="J_SiteNavBd" class="site-nav-bd" style="width:1240px;">
    <ul id="J_SiteNavBdL" class="site-nav-bd-l"></ul>
    <ul id="J_SiteNavBdR" class="site-nav-bd-r"></ul>
  </div>
</div>
<script>TB.Global.init();</script>
    <div bx-container="true">
    <div bx-name="p4p/search-layout" bx-version="0.0.1" bx-guid="lego0" hasjs="false" hascss="true" bx-slot="search-layout" class="p4p-search-layout">
  
      <input type="hidden" id="_SEARCHKEYWORDS" value="%E8%BF%9E%E8%A1%A3%E8%A3%992018%20%20%E9%95%BF">
  
  <div bx-slot="searchheader" data-spm="007713800" bx-name="re/searchheader" bx-version="0.0.5" bx-guid="lego6" hasjs="true" hascss="true" class="re-searchheader"><!--爱淘宝:搜索头部-->
<div id="J_topsearch" class="topsearch" data-fixtop="true">
<div class="ai-topsearch" data-spm="020160114012">
  <div class="con-wrap clearfix">
    <div class="search-wrap">
      <div class="search">
        <div class="search-border clearfix">
          <form target="_blank" action="/search" id="J_searchForm">
            <span class="text-wrap">
              <input type="text" class="text" id="q" name="keyword" accesskey="s" placeholder="请输入搜索文字" autocomplete="off" x-webkit-speech="" x-webkit-grammar="builtin:translate" tabindex="0" aria-expanded="true" hidefocus="true" aria-owns="ks-menu957">
            </span>
            <input type="hidden" name="_input_charset" value="utf-8">
            <input type="hidden" name="page" value="0">
  	        <input type="hidden" name="isinner" value="0">
            <input type="submit" class="submit" value="" data-spm-click="gostr=/zz;locaid=dsearch">
          </form>
        </div>
        <ul class="mainNav" data-pid="420843_1006">
     	 </ul>
      </div>
    </div>
    <div class="ai-logo" data-spm="020160114013">
      <a href="//www.taobao.com/" class="logo" title="" target="_blank"></a>
    </div>
  </div>
</div>
</div></div> 
  <div class="section">
      <div bx-slot="relatedSearch" data-spm="0782702701" bx-name="p4p/related-search" bx-version="0.0.1" bx-guid="lego1" hasjs="true" hascss="true" class="p4p-related-search">

    
    <div class="related-search-outer">
        <dl class="related-search">
            <dt>您是不是想找:</dt>
            
                <dd><a href="https://srd.simba.taobao.com/rd?w=k2textlink&amp;f=https%3A%2F%2Fre.taobao.com%2Fsearch%3Fkeyword%3D%25E8%25BF%259E%25E8%25A1%25A3%25E8%25A3%2599%25E5%25A5%25B3%26catid%3D%26refpid%3D420435_1006%26_input_charset%3Dutf8&amp;k=0a4878fe4c27888a&amp;p=420984_1006&amp;b=_0_0&amp;pvid=e65835a444502501aef3be362129c92f&page=0">连衣裙女</a></dd>
            
                <dd><a href="https://srd.simba.taobao.com/rd?w=k2textlink&amp;f=https%3A%2F%2Fre.taobao.com%2Fsearch%3Fkeyword%3D%25E9%2595%25BF%25E6%25AC%25BE%25E8%25BF%259E%25E8%25A1%25A3%25E8%25A3%2599%26catid%3D%26refpid%3D420435_1006%26_input_charset%3Dutf8&amp;k=0a4878fe4c27888a&amp;p=420984_1006&amp;b=_0_0&amp;pvid=e65835a444502501aef3be362129c92f&page=0">长款连衣裙</a></dd>
            
                <dd><a href="https://srd.simba.taobao.com/rd?w=k2textlink&amp;f=https%3A%2F%2Fre.taobao.com%2Fsearch%3Fkeyword%3D%25E6%2598%25BE%25E7%2598%25A6%25E8%25BF%259E%25E8%25A1%25A3%25E8%25A3%2599%26catid%3D%26refpid%3D420435_1006%26_input_charset%3Dutf8&amp;k=0a4878fe4c27888a&amp;p=420984_1006&amp;b=_0_0&amp;pvid=e65835a444502501aef3be362129c92f&page=0">显瘦连衣裙</a></dd>
            
                <dd><a href="https://srd.simba.taobao.com/rd?w=k2textlink&amp;f=https%3A%2F%2Fre.taobao.com%2Fsearch%3Fkeyword%3D%25E6%2596%25B0%25E6%25AC%25BE%25E8%25BF%259E%25E8%25A1%25A3%25E8%25A3%2599%26catid%3D%26refpid%3D420435_1006%26_input_charset%3Dutf8&amp;k=0a4878fe4c27888a&amp;p=420984_1006&amp;b=_0_0&amp;pvid=e65835a444502501aef3be362129c92f&page=0">新款连衣裙</a></dd>
            
                <dd><a href="https://srd.simba.taobao.com/rd?w=k2textlink&amp;f=https%3A%2F%2Fre.taobao.com%2Fsearch%3Fkeyword%3D%25E8%25BF%259E%25E8%25A1%25A3%25E8%25A3%2599%25E5%25A4%258F%26catid%3D%26refpid%3D420435_1006%26_input_charset%3Dutf8&amp;k=0a4878fe4c27888a&amp;p=420984_1006&amp;b=_0_0&amp;pvid=e65835a444502501aef3be362129c92f&page=0">连衣裙夏</a></dd>
            
                <dd><a href="https://srd.simba.taobao.com/rd?w=k2textlink&amp;f=https%3A%2F%2Fre.taobao.com%2Fsearch%3Fkeyword%3D%25E9%2595%25BF%25E8%25A2%2596%25E8%25BF%259E%25E8%25A1%25A3%25E8%25A3%2599%26catid%3D%26refpid%3D420435_1006%26_input_charset%3Dutf8&amp;k=0a4878fe4c27888a&amp;p=420984_1006&amp;b=_0_0&amp;pvid=e65835a444502501aef3be362129c92f&page=0">长袖连衣裙</a></dd>
            
                <dd><a href="https://srd.simba.taobao.com/rd?w=k2textlink&amp;f=https%3A%2F%2Fre.taobao.com%2Fsearch%3Fkeyword%3D%25E6%25B0%2594%25E8%25B4%25A8%25E8%25BF%259E%25E8%25A1%25A3%25E8%25A3%2599%26catid%3D%26refpid%3D420435_1006%26_input_charset%3Dutf8&amp;k=0a4878fe4c27888a&amp;p=420984_1006&amp;b=_0_0&amp;pvid=e65835a444502501aef3be362129c92f&page=0">气质连衣裙</a></dd>
            
                <dd><a href="https://srd.simba.taobao.com/rd?w=k2textlink&amp;f=https%3A%2F%2Fre.taobao.com%2Fsearch%3Fkeyword%3D%25E4%25BF%25AE%25E8%25BA%25AB%25E8%25BF%259E%25E8%25A1%25A3%25E8%25A3%2599%26catid%3D%26refpid%3D420435_1006%26_input_charset%3Dutf8&amp;k=0a4878fe4c27888a&amp;p=420984_1006&amp;b=_0_0&amp;pvid=e65835a444502501aef3be362129c92f&page=0">修身连衣裙</a></dd>
            
        </dl>
    </div>
    

</div>
      <div bx-slot="searchResult" data-spm="0782702702" bx-name="p4p/search-result" bx-version="0.0.1" bx-guid="lego2" hasjs="true" hascss="true" class="p4p-search-result">


<div id="searchResult">
  <div class="searchResult-items">         
    <div id="J_waterfallWrapper" class="view waterfallWrapper">
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=633&amp;e=LX%2FjDU97IGCNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFM68%2Bdjv7U4KTpHfykepwFHxsxxqWb1SKdlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAkHqgPBHLLyY0B1kn1dB2sIqzxHWvq%2FZYVGnYnqP8PeYJVVbRVda3BWf64jcONzstKdGl4iT6QnisSpbIGYqp3mB6T%2BkMmHb15Jc20OkvRwHBhmW4dpCrXR9gYpZmAQ8WpgS2qKLLLwjF3YHgJKFBxOK%2BHlf%2B4ZklgxFHf0gnM0NaUFHD%2BKwwkV7kL8C4ILCkzTHEb%2F1tTYUc4cUhgxKeGSBj6vBpfeElppPFfnMDy7qklzbQ6S9HAdB6oDwRyy8mNAdZJ9XQdrCKs8R1r6v2WFRp2J6j%2FD3mCVVW0VXWtwVn%2BuI3Djc7LQDfAJ228KNMOpA%2BgdXO%2B1mwGB%2B61pu624gOXGCwfzSsA%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i2/TB1Cd_OcWSWBuNjSsrbYXG0mVXa_M2.SS2_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                     
                        <span class="pricedetail">&yen; <strong>199.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="18新款春夏度假全棉连衣裙大摆裙公主裙仙女">18新款春夏度假全棉连衣裙大摆裙公主裙仙女</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">greenlemon旗舰店</span> 
                    <span class="payNum">18人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                    
                        <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.8</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                        
                            <li><span class="morethan">服务态度:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                         
                        
                       
                            
                                
                                   <li><span class="lessthan">发货速度:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                    
                    <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=569&amp;e=Hkwt2LDuy%2BaNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFOf6VZME46pvOkAnZbWt4F5sJa8YzKY1khlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAtldQq9PgHIa0A0wz%2BmXxF7JUv6u6OD00N3zK6RPCrX7sSpbIGYqp3nTqyghTmQU2r5gESBqe3d4GM7VSKoLQXzgmDXg36XYkaFQ1LuyCd15eqHG7PTzw2PmOXq7C%2BD03zWupwpJ2NwSaUFHD%2BKwwkV7kL8C4ILCkzTHEb%2F1tTYUc4cUhgxKeGSBj6vBpfeEljs%2FZCnRmDsdvmARIGp7d3ih2xOdS%2BqXowjvEeHa1zrXyVL%2Brujg9NC1HqWx%2F17TOzduRK4HqBYXLei5PRhfbI4ClZ6KXEv5iA%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i4/32883064/TB2v5wVgL5TBuNjSspcXXbnGFXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>399.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="颜域品牌女装2018夏季装新款简约牛仔连衣裙">颜域品牌女装2018夏季装新款简约牛仔连衣裙</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">颜域旗舰店</span> 
                    <span class="payNum">108人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                    
                        <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.9</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                    
                    <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=569&amp;e=zu3BJ1uTzWSNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFNreynHo%2BhLKUgwe2xP%2F8J1OJBYVMMEzW9lK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAlGnYnqP8PeYJVVbRVda3BVqllIQdmSPrPMB9VZeGNOOZA7Lb%2FV2evr0kcFQlRHg2AEnRXeNAdn3KQLhLIYwnRd25ru268Y%2BwQZpFgUVdooWvKSQcDHUEjuC8nZjCexueNsiu365FlSv13RbE90ggzl%2B3kw0jeFx4nCmrz8yWcCFmos2UYFTsmcR%2FrsRadXjnJfmfhoS5wMpyY7Jpzpion9nyRjInV7JQCpKhegJIhdzIcFYv4Evl4s5bTi1yTRRLnTyKkPhGfcPqTuoMphFXVZucIamTV3qWA%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i3/40726213/TB2rxH_eVOWBuNjy0FiXXXFxVXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                     
                        <span class="pricedetail">&yen; <strong>258.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="锦瑟春夏季新款连衣裙文艺精棉盐缩高腰百褶">锦瑟春夏季新款连衣裙文艺精棉盐缩高腰百褶</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">锦瑟920</span> 
                    <span class="payNum">1人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.8</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=569&amp;e=J97MWMMt9naNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFO8QGxYIch7kDneunkClOWrOL%2BG3nY1Pz5lK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAlGnYnqP8PeYJVVbRVda3BVqllIQdmSPrPMB9VZeGNOOZA7Lb%2FV2evr0kcFQlRHg2LPlOBLKf%2FGB5QPNo5Cu5A7mo6bQ5PvSdvMa4k9nRxmOmJo%2BUAVHuttxNwgeqG1N8vHb%2Fvj%2BPhMB13RbE90ggzl%2B3kw0jeFx4nCmrz8yWcCFmos2UYFTsmcR%2FrsRadXjnJfmfhoS5wMpCgZJEO0UmLYulYIDBfQcCipKhegJIhdzIcFYv4Evl4s5bTi1yTRRLirNkBJUFQnL1oisYkeQeF67%2BRZL87tmMg%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i4/113818458/TB2KSGAi9BYBeNjy0FeXXbnmFXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                     
                        <span class="pricedetail">&yen; <strong>85.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="版学生文艺简约格子腰带收腰翻领长袖连衣裙">版学生文艺简约格子腰带收腰翻领长袖连衣裙</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">小肥外贸衣橱</span> 
                    <span class="payNum">14人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.7</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=665&amp;e=lh2J0pR447qNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFPBX9HYoUvpLQyzyVDE1aPWC8tjIeV%2FzrxlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAlGnYnqP8PeYJVVbRVda3BWkQ5PeOpouaLuWclgxOctnvGiCKXOLUyH77ug0pP8uAFN3HMX1R8j7aLqlXKdZ0cH3dmgF2CPlh7EqWyBmKqd5gE90OBnrI38jX85UBylpNgZXOKLzQugEE83xhgfIfpDlmAqg0JafqeTGOS%2Fl6CghRnt87VkfjxgYvXGFoE098GlBRw%2FisMJFe5C%2FAuCCwpM0xxG%2F9bU2FHOHFIYMSnhkgY%2BrwaX3hJbVyO%2F1m34biyNfzlQHKWk2nvRT9UwwvFKUI1xl8hZ0M5Zir8qkDWqwRP40BTj1KRhN82EMcSTIMOEGs8u%2ByfV3U3ccxfVHyPsFhqJZ3aQ2zchtO6lPzU%2FNk4jZYg%2F6DawqoDUveqqkuA%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i2/116386293/TB26aTNg29TBuNjy0FcXXbeiFXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>1134.00</strong></span>
                     
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="花朵刺绣图案收腰无袖连衣裙a字裙">花朵刺绣图案收腰无袖连衣裙a字裙</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">juicycouture官方旗舰店</span> 
                    <span class="payNum">24人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                    
                        <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.8</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                    
                    <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=633&amp;e=MeI9%2Fk%2BFfCONblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFNErx%2F9UAMM7GN4Ztg8BhfoWAl7lIvavL9lK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAi56xghqF%2B464XrrbsBL7GiJHR39%2FDFKEX8EGBrJ9VHKJVyCIrb1zMHJUv6u6OD00N3zK6RPCrX7sSpbIGYqp3lWoSDKSLwvv6CEKmwnTRrAs%2B%2FZbpca9Pin9xTtTiI%2Fm%2FUiEufFDroq%2B3khbm8K8IXPne93Nha7SCUjN56EhLBaaUFHD%2BKwwkWrssw2iWuY9iV23h0NZGTFF%2BM8GB%2FxQCOpR5tDnuvdgbELDHv80%2BMDz1LxJB3x5uyWU0fkDidPEO4tnqeaCaYeyF8DamiiwIwqSoXoCSIXcyHBWL%2BBL5eL%2B8lTxsa7qp%2F8d3u%2Fq9lL2mAQNti2rBO8nLX81cA5x0dbo%2Fo2kMl%2FXQ%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i4/96038709/TB2oiFUcuSSBuNjy0FlXXbBpVXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                     
                        <span class="pricedetail">&yen; <strong>189.00</strong></span>
                     
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="仙气长裙森女收腰连衣裙女雪纺夏款chic高腰">仙气长裙森女收腰连衣裙女雪纺夏款chic高腰</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">mumustye企业店</span> 
                    <span class="payNum">1人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.9</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=557&amp;e=awnfCIDXaVONblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFMlHK5GkLvq2XdidwDvCYp6IwiuT8XSoRJlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAk2ESNaMxWsaWxNThAFrr5IPhYHiGeYoSEfvCq2cllzaROJiCoAO%2Fj9pHCHlrIx4fg77puXMh7QW9z%2F0K6GviP6ZydsTsm5UHglVCFlwwUo5t5%2FqhxJ6C4m9k3El623PXTdjWqYikv2%2BLd7ioMK9mkufHeYfgjE0EgoCMoZ0JIR1I4dlC6OgE9KYho0DuJ7YHfwrSN3YNAu2M024uUVxePPH4M8OBVq%2BFHqNa3sGHCM8tR6lsf9e0zuO5EGyeL2JIDqpYA6TFZaBA7NnnX%2F%2FXjU%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i2/54367021/TB2A1oViY1YBuNjSszhXXcUsFXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>158.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="无袖雪纺连衣裙修身显瘦印花大摆v领长裙">无袖雪纺连衣裙修身显瘦印花大摆v领长裙</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">zhu2626911</span> 
                    <span class="payNum">3人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.7</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                         
                            <li><span class="morethan">如实描述:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                        

                       
                            
                                
                                   <li><span class="lessthan">服务态度:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                
                                   <li><span class="lessthan">发货速度:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=569&amp;e=dR6i5KuypUqNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFMJWE8c1m3v%2FMInZz0D%2BZqwTsP7lQ5NLQdlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAlGnYnqP8PeYJVVbRVda3BVqllIQdmSPrPMB9VZeGNOOZA7Lb%2FV2evr0kcFQlRHg2GfV89mq95tTT4jnZyiWBhtpSjFw57i60QbNPUrUj%2FxSOWFIkoLC5Lz6dcxiZLpAaVt6uBW%2BWOVp13RbE90ggzl%2B3kw0jeFx4nCmrz8yWcCFmos2UYFTsmcR%2FrsRadXjnJfmfhoS5wMpVwPj8NsJtVnfvaFHkdcuaSpKhegJIhdzIcFYv4Evl4s5bTi1yTRRLktsRFqjHM7f42saVW4kEtyAGvKAHBqfjg%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i4/14920476/TB2Y5CWb9MmBKNjSZTEXXasKpXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>369.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="丫头家 连衣裙2018春新款女装花边系带">丫头家 连衣裙2018春新款女装花边系带</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">qwewan</span> 
                    <span class="payNum">0人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">5.0</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>5.0</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>5.0</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>5.0</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=569&amp;e=6tRWoclhImCNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFPiln4VTFqDCGHn414EN3WwkpesAmuwsa5lK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAlGnYnqP8PeYJVVbRVda3BVqllIQdmSPrPMB9VZeGNOOZA7Lb%2FV2evr0kcFQlRHg2CL9g8ihoiyroSf%2FIq1iNGPD4vEukb2moYWEaJvkLWTI6GJkNBtw2C%2BCnv1BLN8sjkPE4uKSoveE13RbE90ggzkpUA8C0b0HJT8yvMaqv6Ovay9oRtWhUG9ksbeTWq%2BaffFF9Zs1X%2By9Iv2DyKGiLKvvhBKF2axVQFGnYnqP8PeYJVVbRVda3BUjsd9l4XLXsUxAIdKpeKZNqRkdUMAHis4IMRnQvxO8Ag%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i3/54260668/TB24jMqaBsmBKNjSZFsXXaXSVXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>498.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="真丝连衣裙女2018流行女装新款春装气质">真丝连衣裙女2018流行女装新款春装气质</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">皇点旗舰店</span> 
                    <span class="payNum">2人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                    
                        <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.8</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                    
                    <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=569&amp;e=O79ajzwNMNGNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFMgbghYsOcjJLTJUlvYf37JkXBtL4Xc8RxlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAlGnYnqP8PeYJVVbRVda3BVqllIQdmSPrPMB9VZeGNOOZA7Lb%2FV2evr0kcFQlRHg2GghLlZoqqlk7jylnQRpg%2Fws%2FNgStwh7MCpugjNLqcAxaWCdg5meUjUpzM2OjcwUxwM3m0vXKy6g13RbE90ggzl%2B3kw0jeFx4nCmrz8yWcCFmos2UYFTsmcR%2FrsRadXjnJfmfhoS5wMpZqX2YsIdrS1cprWqGC8uLCpKhegJIhdzIcFYv4Evl4s5bTi1yTRRLlnG4DET%2F4B4OueRONmNloyAr2LRUKQZ%2FA%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i1/129933436/TB2FY31a9tYBeNjSspaXXaOOFXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                     
                        <span class="pricedetail">&yen; <strong>79.90</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="2018春夏时尚大码百搭长袖显瘦休闲连衣裙">2018春夏时尚大码百搭长袖显瘦休闲连衣裙</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">xushuang_x</span> 
                    <span class="payNum">0人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">5.0</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>5.0</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>5.0</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>5.0</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=569&amp;e=ZO4Q439%2BdLSNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFN5eIC%2Bi2gYGCTsnhmjcJfPrVpPu1%2F01DhlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAlGnYnqP8PeYJVVbRVda3BVqllIQdmSPrPMB9VZeGNOOZA7Lb%2FV2evr0kcFQlRHg2CjAKjNm3ZmfPKa1IDptP239RPnUZ%2FZm6uZY8EuaxG2V%2B%2Bka5mEU3rzI%2Bf9ike3X%2BNYzXivmle7m13RbE90ggzl%2B3kw0jeFx4nCmrz8yWcCFmos2UYFTsmcR%2FrsRadXjnJfmfhoS5wMp%2FGZeMzGephNnyRjInV7JQCpKhegJIhdzIcFYv4Evl4s5bTi1yTRRLvyn6XM%2FpSb4SJAB9gQwlq2dIIkiX%2BvkpQ%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i1/30816026/TB2XCwogkyWBuNjy0FpXXassXXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>36.99</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="春夏装2018新款女装韩t系带中长款T恤连衣裙">春夏装2018新款女装韩t系带中长款T恤连衣裙</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">小宅女大购物</span> 
                    <span class="payNum">310人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.6</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                
                                   <li><span class="lessthan">如实描述:<b>4.6</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                
                                   <li><span class="lessthan">服务态度:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                
                                   <li><span class="lessthan">发货速度:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=569&amp;e=Se4CduGUInCNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFPdcALKiEbDlXwF2X5AZWOLhDJ%2Ft3%2Bay71lK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAlGnYnqP8PeYJVVbRVda3BVqllIQdmSPrPMB9VZeGNOOZA7Lb%2FV2evr0kcFQlRHg2IUaeOtmtV4w8mUKGzzf7bbp4lELcOn7irjxVCkW5XJtWm02avXB44atSqlIli0uF3bWzrRgyKxy13RbE90ggzl%2B3kw0jeFx4nCmrz8yWcCFmos2UYFTsmcR%2FrsRadXjnJfmfhoS5wMpw2gipfD9b51nyRjInV7JQCpKhegJIhdzIcFYv4Evl4s5bTi1yTRRLlE9rbsw8oiq1C6PGzsnElSIkGvZzXELwQ%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i3/110514606/TB2CPXObk7mBKNjSZFyXXbydFXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                     
                        <span class="pricedetail">&yen; <strong>183.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="旗袍长款2018新款修身显瘦纯棉格子连衣裙夏">旗袍长款2018新款修身显瘦纯棉格子连衣裙夏</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">鑫爵服饰</span> 
                    <span class="payNum">0人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.6</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                
                                   <li><span class="lessthan">如实描述:<b>4.6</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                
                                   <li><span class="lessthan">服务态度:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                
                                   <li><span class="lessthan">发货速度:<b>4.6</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=569&amp;e=kXIjohVoayKNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFPnwupoZ4%2FLOjnP8nd2kM%2FZxwaQ%2FoSHBvVlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAlGnYnqP8PeYJVVbRVda3BVqllIQdmSPrPMB9VZeGNOOZA7Lb%2FV2evr0kcFQlRHg2Ph8tB1TVdp8Nob%2FJdHS9RtZoPdw%2BOwMwkrapLXv6BPnUr5PFyVC7J%2BIzmmkedZjH%2F%2F1fgPaTuN%2F13RbE90ggzl%2B3kw0jeFx4nCmrz8yWcCFmos2UYFTsmcR%2FrsRadXjnJfmfhoS5wMp4HWe%2FIjKosR6zmyxnVj1BypKhegJIhdzIcFYv4Evl4s5bTi1yTRRLr4CbnHTU9GNh%2BzMC77cqa0zEqhAnKRhYA%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i3/40003836/TB2YBI8iSBYBeNjy0FeXXbnmFXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>145.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="短袖蕾丝连衣裙2018新款中老年中长款裙">短袖蕾丝连衣裙2018新款中老年中长款裙</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">女人衣场998</span> 
                    <span class="payNum">1人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.7</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                
                                   <li><span class="lessthan">发货速度:<b>4.3</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=569&amp;e=v9wOlXlzMpCNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFMS2KL8gyMQPfbbrHn%2BNjoxG2VVtReB6N9lK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAlGnYnqP8PeYJVVbRVda3BVqllIQdmSPrPMB9VZeGNOOZA7Lb%2FV2evr0kcFQlRHg2LrODdZeD%2BRDa%2BGllQB%2BnJkXmm5n5KB6LAbn%2F9KeybxS8Ldindbqj879CNd9NOalSjwE6n3qAmpg13RbE90ggzl%2B3kw0jeFx4nCmrz8yWcCFmos2UYFTsmcR%2FrsRadXjnJfmfhoS5wMpTB0Mf1Lwk3fpoOaEbrgUVCpKhegJIhdzIcFYv4Evl4s5bTi1yTRRLiJonYmaWWLDLpghTDUo95xDhTj%2FSn8D4Q%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i2/116631203/TB2HCjSb8jTBKNjSZFDXXbVgVXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                     
                        <span class="pricedetail">&yen; <strong>199.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="高端中长收腰开叉露肩连衣裙厂家2018">高端中长收腰开叉露肩连衣裙厂家2018</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">刘大牛专柜企业</span> 
                    <span class="payNum">4人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.8</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=569&amp;e=AD1t9oS1v4iNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFMNW8mIAZMJ3Ben0zaD3SIsfQPqr44zLBxlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAlGnYnqP8PeYJVVbRVda3BVqllIQdmSPrPMB9VZeGNOOZA7Lb%2FV2evr0kcFQlRHg2ExdTCvjTzZ7JVzUZ05htfiO3dy7WaHaaQujI3wNSvoxuc6s%2Bw%2FzhUsxDBBSbyVWmeQpmMkUFshn13RbE90ggzl%2B3kw0jeFx4nCmrz8yWcCFmos2UYFTsmcR%2FrsRadXjnJfmfhoS5wMpcQ%2BXxXcs5TbOLsHPUNShWypKhegJIhdzIcFYv4Evl4s5bTi1yTRRLsGcDsgq3uEsnQz54I%2Bk7x5Ou4qAqnB%2Fvw%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i1/11409834/TB2dsvkcVGWBuNjy0FbXXb4sXXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>288.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="新款气质木耳边领口系带印花雪纺长款连衣裙">新款气质木耳边领口系带印花雪纺长款连衣裙</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">爱穿不穿</span> 
                    <span class="payNum">16人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.9</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=609&amp;e=Mqps0wmpIoKNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFOpa7WrPkXIzZJEaT9QtpNdt2HykmKuw%2B9lK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAgOplIjdvKre3cQPpY1nykZRp2J6j%2FD3mCVVW0VXWtwVFRh9AAjqLSIO4nR1R%2BOjbrv7cSzSzJYzCGD1g22ffLPQd2NrawmT3rUD27k2GUn%2FJshdXwpaX3QD%2BWzaBiOmt5cTgjIgDnKxSuyNYOCsr0aFvnJw816XCU%2FWTk4F7CxtbMY6aNiKpIX2AD2b7C6%2F%2BFaoFiKnEBclqnngaLQ1Rdpp%2BMtEZ9uNO6J4gw%2FEREbr8MN0Y%2F%2FPPnQO4nR1R%2BOjbl6%2FGNIHod2ITfNhDHEkyDCkZkwYH7VoWOgBUBgvlG63qXDe8QybvOCdoYxNeMqUZFhaCsP2QQYQ" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i1/25251681/TB2TUH6fuGSBuNjSspbXXciipXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>108.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="雪纺连衣裙中长款2018新款女装复古温柔风">雪纺连衣裙中长款2018新款女装复古温柔风</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">灰思维</span> 
                    <span class="payNum">425人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.9</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=557&amp;e=PBKMVlg0chKNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFORL04yM%2FefemqSAomrOvotR2vpcdVUjTxlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAtldQq9PgHIa0A0wz%2BmXxF7JUv6u6OD00N3zK6RPCrX7JbQpkD5w6nYbgRRCnGuqi9iDWWLtA9b%2BS2Cn5ef6sZhQobBkathl8bn6t0z%2FHCUuTBUKM3FkC4N3aw2mz%2BGiOpXeL1MThlr%2Bc4cUhgxKeGSml461kPhhx%2FFF8u92Gni4nItS3Don8lGxc9Xj8%2BlCqc3Q49fLxwfRavXkqUZ5xP7ZXUKvT4ByGn6BcQvmGzsPurdjlfPGvKGgpVOcNsBX77MvCkrKRagVDIlMpJQYIV4%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i3/1898706006972657458/TB2arS.l.hnpuFjSZFEXXX0PFXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>69.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="大码夏装连衣裙女装薄款简约潮弹性包臀黑裙">大码夏装连衣裙女装薄款简约潮弹性包臀黑裙</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">瑞格ruigee</span> 
                    <span class="payNum">32人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.8</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=557&amp;e=IC%2BL6VyGF6eNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFMsTYXd1%2Bg23SOwPLNgav8bmfS66%2FrPT3tlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAreQDVRf3BT4XE%2BZyAkywY6uuW%2BlivNlfir4gh8pZE43870Eyiqh%2FXouSmqrgSZmE6jcFOy2VBCWyumkT47S52J%2B1dXfuN3Zy8hC%2FYX2EBKDFg21gxKQmsxaVvFyM33wEvOa1dWpxJjqr5ayKmcbo4m%2FUb96qihbRqutn8yROWq9F%2BM8GB%2FxQCOpR5tDnuvdgX5aQwyciB27kraQap8tb679lu35n1bw5Rh8Ai4iGX%2F5Hocb%2Bjvs2cXzbJ36kuDxSJoAz%2FmmCgIoKPn2TJIhKzg%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i2/22244872/TB2Y8sNex6I8KJjSszfXXaZVXXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>398.00</strong></span>
                     
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="宽松长袖针织衫修身显瘦包臀裙两件套装">宽松长袖针织衫修身显瘦包臀裙两件套装</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">dplay旗舰店</span> 
                    <span class="payNum">3人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                    
                        <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.8</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                         
                            <li><span class="morethan">如实描述:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                    
                    <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=577&amp;e=vK7CwYQcMQ%2BNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFOeic%2FoQ0EynM85L9RF5mFZ9R24Q12P%2BmNlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAlGnYnqP8PeYJVVbRVda3BVqllIQdmSPrPMB9VZeGNOOZA7Lb%2FV2evr0kcFQlRHg2AQnANbB7G9Am5I9O%2Fypu35dxJnV9FhPo5NeFoTDTA1%2BairG7lXkX7InqcOEuZsiFEFP1meibOav13RbE90ggzkpUA8C0b0HJT8yvMaqv6Ovay9oRtWhUG9ksbeTWq%2BaffFF9Zs1X%2By9BCcA1sHsb0BipfIrdvBW7FGnYnqP8PeYJVVbRVda3BUjsd9l4XLXsYU%2FlBw%2FCqnMrjudJNKG5MksRWg6JB6oKr%2BgSQ6CKrN2" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i1/126837598/TB2trg1kwfH8KJjy1zcXXcTzpXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>539.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="高档真丝连衣裙2018春装镂空刺绣长款A字裙">高档真丝连衣裙2018春装镂空刺绣长款A字裙</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">幽莱香旗舰店</span> 
                    <span class="payNum">9人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                    
                        <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.9</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                    
                    <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=557&amp;e=1aZ6l9Wd9iaNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFPgL9%2FwnRS6v8N8C4x6dVBedx2AGSWW0JVlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAk2ESNaMxWsaWxNThAFrr5IPhYHiGeYoSEfvCq2cllzaROJiCoAO%2Fj81q%2B%2BktOKz3yyg5NhqhXM1otFmLPyeffwGR9ChWeJJ7VPV2H7pUS4nCXuGE%2BbydpZf8DTBMKaU9DdjWqYikv2%2BGMHwaFGvZKiWMiX7iRXnPnr6MoY9ZRSp51GtG4rzQNNJy7WdIi%2BSKNiKD9tAqmwpkU1ww4UfcVzm8N8wu%2B2ipZbo%2BnFdXwRRHocb%2Bjvs2cV0v9R8F6cshOaxdWVoUDBlraIfRDT9v8k%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i4/28949716/TB2JI6di4SYBuNjSspjXXX73VXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>299.00</strong></span>
                     
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="显瘦a字长裙流行时尚碎花连衣裙女潮">显瘦a字长裙流行时尚碎花连衣裙女潮</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">riwins服饰旗舰店</span> 
                    <span class="payNum">5人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                    
                        <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.8</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                    
                    <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=557&amp;e=%2FJ9FUCgViX2NblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFMxM5VCtfDriEvQln9te4qd%2FFcqa9rYTz1lK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAuETc02MkuA%2FAwp%2BRVHsRR3O1lszgjM4toiE53VD5qJjROJiCoAO%2Fj%2BPDMLXrfG63KscdU5dziuF%2Bfc6S2jitX%2BuBsHe5nYyrVLtS9GQtdgUC6ditqVuEWm%2FCpu5GBW1M4bJTTVz2LoxBQEyxp4FgYwLK1q0%2BYIKxWsvaEbVoVBvZLG3k1qvmn3xRfWbNV%2FsvdgqcZ7CJQ1e4Ho%2Fj%2Bry2JtRp2J6j%2FD3mCVVW0VXWtwVI7HfZeFy17HC0aitaMJ%2FFipAbGDN1MXyX0O0FVacoig%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i3/17114234/TB2NgkvfY1YBuNjSszeXXablFXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>59.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="宽松连衣裙灯笼袖夏2018大码女装女印花短袖">宽松连衣裙灯笼袖夏2018大码女装女印花短袖</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">韩衣控</span> 
                    <span class="payNum">0人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.7</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                         
                            <li><span class="morethan">如实描述:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=621&amp;e=ATbcBiFYlmaNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFMijEGpx0%2FgfBRjvpMj60GscJKRLGeF6wRlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAn0KArMP%2FkP5K9ePhu%2BqSZNgglhyqn2vCc7WWzOCMzi297n2ECXvvWcgVVSidROS4wEqao9Wtt%2B5CGD1g22ffLOC839XCB5QgbAsZec7ERtJEfhOH7WHM0zhRcJN%2B96aPxhmumaUBNx6QqolaLrpjSATyx1nNMz6b5XeL1MThlr%2BcYAM45QEjC%2FSRp1PCazpBZqLNlGBU7JnEf67EWnV45yX5n4aEucDKYLzf1cIHlCBkxzkjkHO0%2FudEK8QLCAGrn0KArMP%2FkP5JVyCIrb1zMHJUv6u6OD00NvYqJOMcB9NWsxktYQqtEKRcDbpBMijILU1LRV7ZCwbEPN3EuzymPY%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i1/113368690/TB23J6Ngf9TBuNjy1zbXXXpepXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>239.00</strong></span>
                     
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="夏季女露肩连衣裙一字牛仔春领夏中裙长袖">夏季女露肩连衣裙一字牛仔春领夏中裙长袖</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">mixblu旗舰店</span> 
                    <span class="payNum">7人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                    
                        <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.7</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                
                                   <li><span class="lessthan">如实描述:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                
                                   <li><span class="lessthan">服务态度:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                    
                    <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=665&amp;e=XBqca6ONm2qNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFNHKtW7R4ua9%2FuxbFKixp9gMcpzoFvdOxdlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAhVtYrM0HtyF8YGqmWL5PJHncKzD7dLW19kJbXgOQFYwANEcLruFq7XJUv6u6OD00KC9FBulM27PD8R7WxFBl5Uc%2F0%2BIle2x71uyBPEP%2FLgrcwht%2BuwZIA1NLwiM16u0jZwed1yIV9KIcU%2BXKBDzZzbjU%2B%2F%2FWuHDtGm8tl%2B0XVwfrkvLtyvuAbs3Y1qmIpL9vi3e4qDCvZpLnx3mH4IxNBIKAjKGdCSEdSOHZQujoBPSmIaNA7ie2B1DSceOkBgZtIIBmZJzarLL1w1sCXfy5SbFsnh0VIba3IVLqtkI6yueefup6l75S9TIXwNqaKLAjCpKhegJIhdzIcFYv4Evl4sj%2BI8mrHlWFiQtca%2FkU%2BxOeJByGylI5%2F2%2FoEkOgiqzdg%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i4/1471606044791093449/TB2AyonXSvHfKJjSZFPXXbttpXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>78.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="三亚沙滩裙仙海边度假韩国显瘦波西米亚长裙">三亚沙滩裙仙海边度假韩国显瘦波西米亚长裙</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">我们和沙滩有个约会</span> 
                    <span class="payNum">88人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.8</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=569&amp;e=oU5lu4mr1MGNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFOoWR%2B3n5AJSVkniSE29BdEFYtCkSHiuyFlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAlGnYnqP8PeYJVVbRVda3BVqllIQdmSPrPMB9VZeGNOOZA7Lb%2FV2evr0kcFQlRHg2GPQF7wTBnzwjFNBBCLRpTFGNQpumMakF6y3IsvE6TmoESqtcQo7Pj6FPsM9a3Lxf85ncccUsOZa13RbE90ggzl%2B3kw0jeFx4nCmrz8yWcCFmos2UYFTsmcR%2FrsRadXjnJfmfhoS5wMpILTtH8BbGY8ufR4DEetF6ipKhegJIhdzIcFYv4Evl4s5bTi1yTRRLgZ7%2Bj%2F%2F1EU%2B699aZC3KV%2BDgDtLK8D251g%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i4/112611889/TB2hG6FaKuSBuNjSsplXXbe8pXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>390.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="2018春季新款女装欧洲站宽松印花亚麻印">2018春季新款女装欧洲站宽松印花亚麻印</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">蒙爵服饰企业商城</span> 
                    <span class="payNum">62人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                        <span class="icon"><span class="icon-golden"></span></span>
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.9</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                    <span class="icon"><span class="icon-golden"></span></span>
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=557&amp;e=OeuDo%2FgWIZ6NblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFNQ%2Fkkk3SZu4A0hKm7T%2BVy32R3tH2Vh1x9lK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAk2ESNaMxWsaWxNThAFrr5IPhYHiGeYoSEfvCq2cllzaROJiCoAO%2Fj%2BOESe8PdXEw2NleVrc6wVg7ULenC8o0LV3bobTUtoGAOKY9jiMfhMRCtetqnkOpfvQ4iN9OV5%2BTzdjWqYikv2%2BLd7ioMK9mkufHeYfgjE0EgoCMoZ0JIR1I4dlC6OgE9KYho0DuJ7YHeFEeVDKCO6OfkZsNA1JCeDH4M8OBVq%2BFHqNa3sGHCM8tR6lsf9e0ztU47Gx2ReC2cGmJScDhfWJM6RhP8bDLug%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i5/TB1nfZ7iKuSBuNjSsplYXHe8pXa_M2.SS2_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>238.00</strong></span>
                     
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="棉麻连衣裙夏季新款V领刺绣民族风七分袖">棉麻连衣裙夏季新款V领刺绣民族风七分袖</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">徐美晨9999</span> 
                    <span class="payNum">0人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.3</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                
                                   <li><span class="lessthan">如实描述:<b>4.3</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                
                                   <li><span class="lessthan">服务态度:<b>4.5</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                
                                   <li><span class="lessthan">发货速度:<b>4.4</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=577&amp;e=%2BcWXwdFdD46NblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFPSnQfnZoSKpml6hb%2FhyMH4gkpit5gGwX9lK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAlGnYnqP8PeYJVVbRVda3BVqllIQdmSPrPMB9VZeGNOOZA7Lb%2FV2evr0kcFQlRHg2AkaE8hc4oC4ZSibMiuAZl17L24YFNu5uZPZdET%2BYCiiMmuh3Jl8CEAeCRmAtzqEBfNO%2FCi58Dbr13RbE90ggzkpUA8C0b0HJT8yvMaqv6Ovay9oRtWhUG9ksbeTWq%2BaffFF9Zs1X%2By9CRoTyFzigLhk1y5H4%2FEmSVGnYnqP8PeYJVVbRVda3BUjsd9l4XLXsYzbrF%2BMtaxbl9QwrBCZYuyNTFB8pn5oZL%2BgSQ6CKrN2" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i3/117346131/TB23wKPaDqWBKNjSZFAXXanSpXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>358.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="卓芙莱2018新款连衣裙春假两件连衣裙a">卓芙莱2018新款连衣裙春假两件连衣裙a</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">卓芙莱旗舰店</span> 
                    <span class="payNum">0人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                    
                        <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.9</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                    
                    <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=569&amp;e=Mxo4yjBqu%2B2NblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFPbF2GpdNzEbgYb0ZDD5Wh%2Bxgk%2BqTWDj75lK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAlGnYnqP8PeYJVVbRVda3BVqllIQdmSPrPMB9VZeGNOOZA7Lb%2FV2evr0kcFQlRHg2LjZkhfS34ePGwwwA7Ndc9OTwJzICVJT3deSVyjUU38HYxlvF6agnNEQc1SUC51zX4vrwlOThKI613RbE90ggzl%2B3kw0jeFx4nCmrz8yWcCFmos2UYFTsmcR%2FrsRadXjnJfmfhoS5wMpRVoASJFjNjRFEMnDdFKv7SpKhegJIhdzIcFYv4Evl4s5bTi1yTRRLvqpCr%2BSWIiExnp4cQG7M7VmVGaxfKNH7Q%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i4/29672914/TB2ptFjjkKWBuNjy1zjXXcOypXa_!!2-saturn_solar.png_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>1210.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="歌中歌五分袖绣花长裙珠片显瘦圆领连衣裙">歌中歌五分袖绣花长裙珠片显瘦圆领连衣裙</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">yigue亦谷商店</span> 
                    <span class="payNum">1人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.6</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                
                                   <li><span class="lessthan">如实描述:<b>4.6</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                
                                   <li><span class="lessthan">服务态度:<b>4.6</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=569&amp;e=6mswcToRAW%2BNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFOrt%2FJv5uo97%2FPiJPWufrk3fN2LkDDIme9lK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAlGnYnqP8PeYJVVbRVda3BVqllIQdmSPrPMB9VZeGNOOZA7Lb%2FV2evr0kcFQlRHg2IGkqtfWwgBhtDc2X0jMC%2FmZHkZUJvrTWhl2PXg9Yu6mT%2BTZqtzyg3sjpJKP5wXwG12QS4QrRuVLld4vUxOGWv5zhxSGDEp4ZKaXjrWQ%2BGHH8UXy73YaeLici1LcOifyUTn0CMeAshEXdOP%2BCOe5uySq4Y9HdgrFJH6BcQvmGzsPurdjlfPGvKHU1kWDeYOnwZj7hmJN%2FSGjMMFlzMSMzQIYyLV8sJL6vw%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i2/28868700/TB2.Jceg1uSBuNjy1XcXXcYjFXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>49.40</strong></span>
                     
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="装2018新款女韩版时尚荷叶边长裙连衣裙">装2018新款女韩版时尚荷叶边长裙连衣裙</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">mliam</span> 
                    <span class="payNum">24人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.6</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                
                                   <li><span class="lessthan">如实描述:<b>4.6</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                
                                   <li><span class="lessthan">服务态度:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                        
                            <li><span class="morethan">发货速度:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=569&amp;e=%2BsiB3E6ky5KNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFPg9GSs63d%2FI2zt5nUQcsq35DKDiWD%2BAvdlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAlGnYnqP8PeYJVVbRVda3BVqllIQdmSPrPMB9VZeGNOOZA7Lb%2FV2evr0kcFQlRHg2BLv%2BXdbbSjd50ASB6pYMdUMoObwDfnZ5iQe6aZxoP7%2FFP4hqsRnmo9A%2FwnknU0fTLxSf52sRUvG13RbE90ggzl%2B3kw0jeFx4nCmrz8yWcCFmos2UYFTsmcR%2FrsRadXjnJfmfhoS5wMpURPBpHCs1%2F7OLsHPUNShWypKhegJIhdzIcFYv4Evl4s5bTi1yTRRLrTeH7B9y3poLNYN9KSnKZSLI7TyX50ohA%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i2/30073013/TB2497ZcmcqBKNjSZFgXXX_kXXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                     
                        <span class="pricedetail">&yen; <strong>138.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="两件套连衣裙女2018无袖长裙polo领网纱裙子">两件套连衣裙女2018无袖长裙polo领网纱裙子</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">德国小男孩</span> 
                    <span class="payNum">0人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">0.0</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                         
                            <li><span class="morethan">如实描述:<b>0.0</b></span><span class="listup-tgr-arrow"></span></li>
                        

                        
                            <li><span class="morethan">服务态度:<b>0.0</b></span><span class="listup-tgr-arrow"></span></li>
                         
                        
                        
                            <li><span class="morethan">发货速度:<b>0.0</b></span><span class="listup-tgr-arrow"></span></li>
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=601&amp;e=MMq%2FlIygdIeNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFOqF3krv%2BWayq8M2v84YWcW9hz8LxerC8llK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAm%2BsAPHmvWQuejgc5uYMfB3pNJ%2B6Svl%2B%2F07Hkm6KOv2hiwjxz2UsNZXv88Pfy6xvPEoehFNtEKpeclqRgYR7LZ5fPNsKKYxg9W1OsgR6Yo%2B%2BtYN77ZW%2FmeAWY4dYpUJGim1zSDyjNXh8j2nI2n%2FGutiV3i9TE4Za%2FnGADOOUBIwv0kadTwms6QWaizZRgVOyZxH%2BuxFp1eOc5V2H449RTbms5fBDlCuW%2FzKVEYOTP4r07cgFy0xYDui7xyrB%2Bdy6ncnBfb7kcz623ufNoYwiaYJm2pvUERdYlmvb84WZSVcNtTS0UL72WYL7LFI3VhOYSA%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i2/1530806016479566688/TB21xI8lwJlpuFjSspjXXcT.pXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>588.00</strong></span>
                     
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="古青婚礼妈妈装连衣裙套装婚庆婆婆两件套">古青婚礼妈妈装连衣裙套装婚庆婆婆两件套</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">guqing古青旗舰店</span> 
                    <span class="payNum">1人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                    
                        <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.9</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                    
                    <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=697&amp;e=SXerg1J%2FI3iNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFO7K33afqg6we7%2FDNKkhbtZveHyW6kDeR5lK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAuZgYxHmnc1GR2zjv%2FTt7lsIUq7%2Fjeff1Inxp%2Bej%2BBJ72USZR0dMyhUQXCiZl46CLiXKTZlyziS7j9DUki0TB6VvrADx5r1kLpQlimViF%2BoVROJiCoAO%2Fj8%2FOoF7OCBg5zq2my3NWvDl4zLW8Mei9DIGdhMTofywhqSqeVA1dG%2FSC2JnbMQXOoU536LIXKfMTTdjWqYikv2%2BGMHwaFGvZKiWMiX7iRXnPnr6MoY9ZRSp51GtG4rzQNNJy7WdIi%2BSKG8a5eectJu7RHqFrfUrKjDZRJlHR0zKFa%2BdnKPVPyGpifGn56P4Enssp7n%2BylGg5uzT0eHDRKvPgZCdYx9XhULdxA%2BljWfKRuZgYxHmnc1GR2zjv%2FTt7lvLT%2B4Y35KsKgQH46S9or6kCdqUweb68qXIP1I7oLKyUQ%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i4/109852050/TB2OyhpfHGYBuNjy0FoXXciBFXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>99.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="ins超火的连衣裙韩版印花女装2018新款夏季">ins超火的连衣裙韩版印花女装2018新款夏季</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">卡莱娅旗舰店</span> 
                    <span class="payNum">184人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                    
                        <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.8</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                    
                    <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=569&amp;e=6sDEj9pLYXiNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFMOtk%2BGZm1uWORRld8HnajIzNRatqjJ0K9lK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAlGnYnqP8PeYJVVbRVda3BVqllIQdmSPrPMB9VZeGNOOZA7Lb%2FV2evr0kcFQlRHg2EYR49LUsJDX1jT2NblsxX1ViwzX2btXKA5ycy%2Fch7qW%2Buw20EnTFGIpJIfre150LmUvubfnmpzzld4vUxOGWv5zhxSGDEp4ZKaXjrWQ%2BGHH8UXy73YaeLici1LcOifyUexsv0rikoEJAlz%2BijbINo%2FfnzHxwxicUn6BcQvmGzsPurdjlfPGvKHU1kWDeYOnwU%2F4cExi049dJYfTQCEo3%2BLi%2BiSZIhlxGQ%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i2/14596706/TB20ioahFGWBuNjy0FbXXb4sXXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                     
                        <span class="pricedetail">&yen; <strong>85.00</strong></span>
                     
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="腰中长款连衣裙女春款2018港味时尚裙子">腰中长款连衣裙女春款2018港味时尚裙子</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">173当铺</span> 
                    <span class="payNum">23人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.6</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                
                                   <li><span class="lessthan">如实描述:<b>4.6</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                
                                   <li><span class="lessthan">服务态度:<b>4.6</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                
                                   <li><span class="lessthan">发货速度:<b>4.6</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=569&amp;e=iOf%2BTkqFYu2NblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFMxI7XFXF6asSHbQ7wGf0Y2BMr3uYWtkG9lK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAlGnYnqP8PeYJVVbRVda3BVqllIQdmSPrPMB9VZeGNOOZA7Lb%2FV2evr0kcFQlRHg2GZaKVFmTxRL4QPUg4MAJQc49PkEC4kq3OX1TLWP3DIyeqoXWfyKktTsHFs4RadcQElAJH0T0pLT13RbE90ggzl%2B3kw0jeFx4nCmrz8yWcCFmos2UYFTsmcR%2FrsRadXjnJfmfhoS5wMp41RFCsRVVpTR31G2Fi7n5ypKhegJIhdzIcFYv4Evl4s5bTi1yTRRLqe1JtPhBE%2B9oo%2FRTebuvjE7fxgW1pJCkA%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i4/121826219/TB2QFCqjmCWBuNjy0FhXXb6EVXa_!!2-saturn_solar.png_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>1290.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="雅莹2018夏五分袖圆领重工刺绣钉珠连衣裙">雅莹2018夏五分袖圆领重工刺绣钉珠连衣裙</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">今冠商贸</span> 
                    <span class="payNum">3人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">5.0</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>5.0</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>5.0</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>5.0</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=601&amp;e=AwfOgwPYxaGNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFMevw0eLYuHIPjdxKYpOjYK43LRM%2B8OqLVlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAnBhv3huMRWv%2BzQecH3nSHa6bS5tGa1rvQOplIjdvKre3cQPpY1nykY8Z%2Bs74%2FaxqO%2FWh%2FHwtwTjsgfoJFK3s6ddtqHe1YGCMZcHCloxDpiJ6G%2F8g%2BFFGexdAIGck3AFTDY4SMipTksKJ5Q590G82UlP1k5OBewsbWzGOmjYiqSF9gA9m%2Bwuv%2FhWqBYipxAXJap54Gi0NUXaafjLRGfbjTvyw79fggCmG2NsKgxunTFKxYH6%2B84fcb7VDqVoc8ardsvVn54R6%2FvTsnOTXVcHsugUjA2cxisyVtLihxUig322YIjoR4ljuye%2FoEkOgiqzdg%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i1/26910303/TB2_7Caa2iSBuNkSnhJXXbDcpXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                     
                        <span class="pricedetail">&yen; <strong>85.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="拉夏碎花衬衫式雪纺连衣裙20012081">拉夏碎花衬衫式雪纺连衣裙20012081</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">静静gj1</span> 
                    <span class="payNum">69人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.8</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=609&amp;e=%2BcjGJW6XW32NblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFOTTUjYS5d2omfnEYwLRhNO9lqI2QRGaPZlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAhjgQxKvSk2WvtyBLhtx4kzB4NaWZ04CSAasWF5Ct0AVJShbkS7xwKmuuW%2BlivNlfjxn6zvj9rGoHceVYMMW2httaszSXAuxLH%2BOgPPIRjPjW9mDtgrUdMRYJLwcvXcFLB75ZzvowLZmS22HTjkKcv%2BUMa88Qn7f4tLBFyaJnTroVlBBgvoGCgkenN%2FcA6xV%2FnOHFIYMSnhkgY%2BrwaX3hJbfcgLAdyZbaW84KQbKj06tGOBDEq9KTZbMjLhtk1JjKq65b6WK82V%2BBqxYXkK3QBXGuLGN9UiqgcHg1pZnTgJIf9qbqhBT1T8j6lMk6OjTeofVFbyMI4gm" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i2/17000238/TB2Y1CPa9YH8KJjSspdXXcRgVXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>159.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="白色拖地气质淑女长裙显瘦吊带连衣裙长裙夏">白色拖地气质淑女长裙显瘦吊带连衣裙长裙夏</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">jennny_2007</span> 
                    <span class="payNum">202人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                        <span class="icon"><span class="icon-golden"></span></span>
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.8</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                    <span class="icon"><span class="icon-golden"></span></span>
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=653&amp;e=B76ynB37oqqNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFORDwIbr%2FFBmO4SCpElGuaa6yIT%2Bq3O9wllK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAujd7ccjrQ%2FmA7SzroaqJD7v1cUcSOsIKAG3YXDvBpYy%2Fl1F6UKNXVp%2BTscf0YBGI87WWzOCMzi2iITndUPmomNE4mIKgA7%2BP6cYVzmLz%2BE9LTpOBoFRe5fmdp8qe5f%2FYjhCsFH%2BADjCCfukPuNAUGTS9viysXlS3fHghg%2BJCPnXN2NapiKS%2Fb4t3uKgwr2aS58d5h%2BCMTQSCgIyhnQkhHUjh2ULo6AT0piGjQO4ntgdYQuAQPmGEwOHE8%2FLfw4akWKqwrB46c2BEfibOfe8n0ooMbc55%2BD6%2FwUSiUnbxu8syF8DamiiwIwqSoXoCSIXcyHBWL%2BBL5eLPAIksiWczczZ3PghLWVRBsNWQuycNuPHv6BJDoIqs3Y%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i1/28950858/TB2wQ4fh1ySBuNjy1zdXXXPxFXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>420.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="高端大摆印花半透明背心裙长裙欧根纱连衣裙">高端大摆印花半透明背心裙长裙欧根纱连衣裙</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">bbvvabcshiwan</span> 
                    <span class="payNum">0人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">0.0</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                         
                            <li><span class="morethan">如实描述:<b>0.0</b></span><span class="listup-tgr-arrow"></span></li>
                        

                        
                            <li><span class="morethan">服务态度:<b>0.0</b></span><span class="listup-tgr-arrow"></span></li>
                         
                        
                        
                            <li><span class="morethan">发货速度:<b>0.0</b></span><span class="listup-tgr-arrow"></span></li>
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=653&amp;e=gLfeWCl1fBqNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFNNJmGdJubN8jw436PmQlFAw5B4PXeo0fNlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAhiQDflkxY8xWch0YiuJclvJUv6u6OD00GX8qh93ux6MtOZb4NXvfCQgVVSidROS42aycvW%2FxnxHcWT8Ty%2FVFIhbsgTxD%2Fy4KzeElrBABghniAD6K0yGByX%2F6rp9XjTciAVNdYn7DMK%2FE5kIxYXRSsEuYsnbumCGfpEDQNb%2BCAC80beyPH3ohD6vlrIqZxujib9Rv3qqKFtGq62fzJE5ar0X4zwYH%2FFAI6lHm0Oe692B6gq3hCeT63cEAZGUJ12nIH0KArMP%2FkP5NJVOda2sCyCa0T6XzpNLXlGnYnqP8PeYJVVbRVda3BXBaUbzTituyOmee2zX9UHUW0L05yvrVPOwuPJcb19BEu2l4dkq1GIOy85EDjWt8nc%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i3/1942606021760442324/TB2BeVgo4hmpuFjSZFyXXcLdFXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>468.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="女性西装领连衣裙女子女人女士裙修身连身裙">女性西装领连衣裙女子女人女士裙修身连身裙</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">谷姬旗舰店</span> 
                    <span class="payNum">0人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                    
                        <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.8</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                         
                            <li><span class="morethan">如实描述:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                    
                    <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=685&amp;e=Ly%2BxlOyaiUONblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFPm9Ji%2FXVbBYJXf0ofvlXU8pMNNEjFA0RZlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAhs81n4SfDioPORp7amIicCVhj54CsizBjZEdVzOn4jiA7SzroaqJD4jA3fR2O2XBc7WWzOCMzi2wrg9aWB4Z46uuW%2BlivNlfjxn6zvj9rGoppHrmKzmDiI432sUk5E9b7UnbCIP0lTFrp3hscSNzZNInX5MnRl5MK6WYt0ioJSCYZ%2BQKSopd1VIHRbF%2FnFeT9LBFyaJnTroHeFqc5xSBhgmUwNpAAA0EVaoFiKnEBclqnngaLQ1RdosyCnoMuKQpEL8b%2FWK2mDGsi1qoUnN3MLAgEUhrVrBlR9L1B%2FgZGqIEfibOfe8n0pbE1OEAWuvkpwrsqWEz2DI4S1%2BopEVBlQa3zVFwWje2b%2Fx28AaLmNoSaE61OFJq4mDs1YhHv6x2tY1bCTf2Ymsv6BJDoIqs3Y%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i3/15854139/TB2PgZHdb1YBuNjSszhXXcUsFXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>278.00</strong></span>
                     
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="2018春装简约时尚收腰直筒中袖印花连衣裙">2018春装简约时尚收腰直筒中袖印花连衣裙</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">如奕旗舰店</span> 
                    <span class="payNum">5人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                    
                        <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.8</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                
                                   <li><span class="lessthan">如实描述:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                        
                            <li><span class="morethan">服务态度:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                         
                        
                        
                            <li><span class="morethan">发货速度:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                    
                    <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=569&amp;e=6W%2FgljvzZdWNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFNMeczWMHf%2BJnfCWNjgV%2B11Unz3sE2pyoBlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAn5GuhUWgnfw2b%2Fi7ijztxHJUv6u6OD00Lh%2BZjBFWcdD%2FnDrnV3kL3XmnNPuq8Y3mBI0Ip5XdJGUW%2BCa6Ss9QCo2HyseOcnAOy4kJfc4rWrwasYkZ6sdOmsfCtFfl6l56Dpb%2F41bJ5Mu0sEXJomdOuhWUEGC%2BgYKCR6c39wDrFX%2Bc4cUhgxKeGSBj6vBpfeElnKZzJeIvqU2xn%2B8DneiobRRp2J6j%2FD3mCVVW0VXWtwV4oPPAD4qg1eO273sJ4rE9JGSMkDNzWGbYAgZetS3yIkvVwUSLQP1Fg%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i2/44575617/TB2o5R1hkyWBuNjy0FpXXassXXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>189.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="韩版气质中长款荷叶边v领裙碎花雪纺连衣裙">韩版气质中长款荷叶边v领裙碎花雪纺连衣裙</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">sally小钥</span> 
                    <span class="payNum">0人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.9</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>5.0</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>5.0</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=569&amp;e=Tk7%2FuqPTvgeNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFMOtk%2BGZm1uWORRld8HnajItFnOvdTqQwplK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAlGnYnqP8PeYJVVbRVda3BVqllIQdmSPrPMB9VZeGNOOZA7Lb%2FV2evr0kcFQlRHg2NpH%2BIJNIpk8MSKAtItuowTtoTfe3joH6a1s4l8Mu%2BSgBsCx3fw3RPHiPNH%2BuXxezswJipaom8bZ13RbE90ggzl%2B3kw0jeFx4nCmrz8yWcCFmos2UYFTsmcR%2FrsRadXjnJfmfhoS5wMp7c2Qzfx%2BJ8L4jWqY%2FgA%2FRCpKhegJIhdzIcFYv4Evl4s5bTi1yTRRLlu4hcNY%2FDD%2FyEBaXtvz764ZuvP822P2hQ%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i2/14596706/TB2.sCWe_JYBeNjy1zeXXahzVXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                     
                        <span class="pricedetail">&yen; <strong>75.00</strong></span>
                     
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="边宽松长裙女春装2018港味学生连衣裙潮">边宽松长裙女春装2018港味学生连衣裙潮</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">173当铺</span> 
                    <span class="payNum">19人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.6</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                
                                   <li><span class="lessthan">如实描述:<b>4.6</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                
                                   <li><span class="lessthan">服务态度:<b>4.6</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                
                                   <li><span class="lessthan">发货速度:<b>4.6</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=569&amp;e=yMxVXuBxKaKNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFPIkXl2SAP2GcO3x%2FsIkWoij%2F1smUJ0u7hlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAlGnYnqP8PeYJVVbRVda3BVqllIQdmSPrPMB9VZeGNOOZA7Lb%2FV2evr0kcFQlRHg2CNLqAJcRvZIT9j%2F2F4JvNZASdDO03fXkevSdZ0OAaaGBt9Meba9wzEzZWlWraE1fgabvqqd7Rj813RbE90ggzl%2B3kw0jeFx4nCmrz8yWcCFmos2UYFTsmcR%2FrsRadXjnPygdwiL5n5CSI0t2U8A1SjxXxpldr1A2ipKhegJIhdzIcFYv4Evl4s5bTi1yTRRLnHptQSfm8EMgeUtKHqM2%2Fm6WRTqURo3pA%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i1/1952605020958039175/TB2jwdDgrplpuFjSspiXXcdfFXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>88.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="2018新款女装春天春秋款韩版秋裙学生">2018新款女装春天春秋款韩版秋裙学生</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">bfqynifhv</span> 
                    <span class="payNum">3人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.5</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                
                                   <li><span class="lessthan">如实描述:<b>4.5</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                
                                   <li><span class="lessthan">服务态度:<b>4.6</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                
                                   <li><span class="lessthan">发货速度:<b>4.6</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=653&amp;e=nk4Ww9tb9%2FCNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFMR%2FFBgtUl5jZnWR%2F0SGROsF1cBgTlrQdllK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAnBhv3huMRWv%2BzQecH3nSHa6bS5tGa1rvTwDG7B03Cdm8tS3BhGBabm58%2F7SQglnNUOKsSSoc9DNeEST94%2FTF5P%2BcOudXeQvdSQrsbhbGIe1d26UFlacr2JLpUdR8Fr1OVwq8qGO%2Fjk5pm3AasvarcplrEy8lAycQHHSBAUrH37qbyRGzNiJqpTSwRcmiZ066FZQQYL6BgoJHpzf3AOsVf5zhxSGDEp4ZIGPq8Gl94SWazz358Xffby%2F3uelVCAL5DwDG7B03Cdm8tS3BhGBabmPuzk52iALdy56xghqF%2B46Hd5%2FBv6ZW4PaoAy45mCvw87WWzOCMzi2lYMZn2hCeXkW40iMsJYqcSL4jmagEPxPCw04kkb%2FkCU%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i4/28344297/TB20Qb9gkyWBuNjy0FpXXassXXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>219.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="2018春夏小清新款女生装雪纺复古碎花连衣裙">2018春夏小清新款女生装雪纺复古碎花连衣裙</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">名嫒公寓</span> 
                    <span class="payNum">13人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">5.0</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>5.0</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>5.0</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>5.0</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=621&amp;e=2jiLWNm%2B9eiNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFPjJcPgBH8SauHyZIiPcn19kRYQ1ZhOKOxlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAgOplIjdvKre3cQPpY1nykZRp2J6j%2FD3mCVVW0VXWtwVFRh9AAjqLSIO4nR1R%2BOjbrv7cSzSzJYzCGD1g22ffLNerek7IlIh460ramOhiUbyVfW3WmfNqNE%2B52KojNneFQJtrlAyW2c4MXl0S2dakA7%2Bz17RQzSmipXeL1MThlr%2Bc4cUhgxKeGSml461kPhhx%2FFF8u92Gni4nItS3Don8lHsbL9K4pKBCf687%2BI%2Fewx%2Fp4A6vliPmNndPQYC3dTFswMKfkVR7EUdztZbM4IzOLZiGaBHcPmb9d3ED6WNZ8pG80WRMwv4B4Lx%2FvUV1Vjbt6b5vOZ33c7Av6BJDoIqs3Y%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i2/119333769/TB29PGbaOjQBKNjSZFnXXa_DpXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>299.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="衬衫中长款收腰条纹连衣裙2018春新款女拼接">衬衫中长款收腰条纹连衣裙2018春新款女拼接</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">maria45</span> 
                    <span class="payNum">2人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">5.0</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>5.0</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>5.0</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>5.0</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=569&amp;e=ulJnvwFn1GKNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFN438KSUEwbhVyAC%2FwCjnqOFh0DKqYPRtdlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAlGnYnqP8PeYJVVbRVda3BVqllIQdmSPrPMB9VZeGNOOZA7Lb%2FV2evr0kcFQlRHg2N1dcDzNEPpq2ysIcMtTIAl%2FkYboe4EqXcIZW2JYHcu0jYtm2tgIoYOsrueYfPSkOOCr2YEBo3y413RbE90ggzl%2B3kw0jeFx4nCmrz8yWcCFmos2UYFTsmcR%2FrsRadXjnJfmfhoS5wMpJ%2BhQQ4UsNm2mbQTjMBaOZipKhegJIhdzIcFYv4Evl4s5bTi1yTRRLgtWiCCV0DgyKEtoC5oDmgjhLpHSnYbAfw%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i4/116773682/TB2oq82jeuSBuNjy1XcXXcYjFXa_!!2-saturn_solar.png_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>1270.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="滕氏2018春季中长款长袖立领纯色钉珠连衣裙">滕氏2018春季中长款长袖立领纯色钉珠连衣裙</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">a淘淘乐z</span> 
                    <span class="payNum">2人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.5</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                
                                   <li><span class="lessthan">如实描述:<b>4.5</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                
                                   <li><span class="lessthan">服务态度:<b>4.6</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                
                                   <li><span class="lessthan">发货速度:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=569&amp;e=4ix%2FsqN%2Buk%2BNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFN6RAJ136IthJ2GSHTMPMgKWkajy7xqT%2FZlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAlGnYnqP8PeYJVVbRVda3BVqllIQdmSPrPMB9VZeGNOOZA7Lb%2FV2evr0kcFQlRHg2Iok23DhWlOnTncJvZFB1IN3VRGro01ldtc79Z5Ea%2BzLX7vwY%2FZQYJ3LofKFFv35%2B0mAMsHMsqizld4vUxOGWv5zhxSGDEp4ZKaXjrWQ%2BGHH8UXy73YaeLici1LcOifyUexsv0rikoEJVU07DPSlqMPC%2FcaSe42Hqn6BcQvmGzsPurdjlfPGvKHU1kWDeYOnwUR2XHtz0HWAdBjMKtXRf8fl7HsIssW4VQ%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i1/16283524/TB2CMkpccUrBKNjSZPxXXX00pXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>85.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="轻熟系带纯色翻领长袖雪纺连衣裙露背长裙">轻熟系带纯色翻领长袖雪纺连衣裙露背长裙</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">xkxk87</span> 
                    <span class="payNum">0人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.7</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                
                                   <li><span class="lessthan">服务态度:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=589&amp;e=Ened7e%2F0QfqNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFOqghKDedD7cLYWqqC%2FxtfMnTqQhAWNnCxlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAgasWF5Ct0AVUoFhu2SdZPKkQ5PeOpouaH8EGBrJ9VHKiITndUPmomNE4mIKgA7%2BP1sY8%2Fzvtf9H9K9B1mKGmWvQUgtrVP16vfLE47MOmfjqxBoYHeZd8TNMPz%2Bc1WQ%2FQt45wbIG%2FN6LhslNNXPYujEY28poxsvxEfVrghaOUmOWFyRkxCwuymAjh2ULo6AT0piGjQO4ntgdNRwZCVXyRFUTXCBbTjm9t6XzeZ3IL1U3EmGhDZodnlwtHaGBT2cJZbcE1DZ9sfB3iOblLstsU9kPB0PBQebgNyBU1vuleekzv6BJDoIqs3Y%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i1/25556680/TB2J.xqhnlYBeNjSszcXXbwhFXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>599.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="伊华预售吊带裙 荷叶边连衣裙雪纺 碎花">伊华预售吊带裙 荷叶边连衣裙雪纺 碎花</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">evaouxiu旗舰店</span> 
                    <span class="payNum">13人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                    
                        <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.8</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                    
                    <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=601&amp;e=05d33EkoSbWNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFOpXJJJvO8vYidZMWzHD83UwLngf8Tc%2BuhlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAgasWF5Ct0AVe551xPP0CYbfnXbyHSbRwFGnYnqP8PeYJVVbRVda3BWViNY%2BG3b9ZfSRwVCVEeDYPbhTSNDx3cQOqapOlOpNQNqkN9gmTEj0nPnjvCZaSXTLbBCOWdNwKHaZiCG7svy3ZroeiMr1f1uV3i9TE4Za%2FnGADOOUBIwv0kadTwms6QWaizZRgVOyZxH%2BuxFp1eOcU%2BOxnlTRTypjT9CfnWy9iJjZj3gYFENyjQ2PBwxHRSUqSoXoCSIXcyHBWL%2BBL5eL%2BMeiRgsNUnD6yHBdcoWF27sbiVg0qlU5FSncizP2wnn5uXyJryC2FQ%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i4/TB1xqPVRFXXXXbkXVXXYXGcGpXX_M2.SS2_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>168.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="春夏款两件套大码吊带连衣裙V领套裙A字摆裙">春夏款两件套大码吊带连衣裙V领套裙A字摆裙</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">艾尼薇女装旗舰店</span> 
                    <span class="payNum">1人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                    
                        <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.8</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                
                                   <li><span class="lessthan">服务态度:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                        
                            <li><span class="morethan">发货速度:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                    
                    <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=569&amp;e=34vs6%2F%2FTMeiNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFM5RW51tYALao6GuQvW5d5LXkvo94XwmrxlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAuETc02MkuA%2FAwp%2BRVHsRR3O1lszgjM4toiE53VD5qJjROJiCoAO%2Fj%2BdMTh2ZnAbkFCwjmBv2Gp%2FoHbf443efYaIsneeEjOqm0hSCSBV0mbNtcuzvCCKQd8ME5JS%2B8M3xjdjWqYikv2%2BGMHwaFGvZKiWMiX7iRXnPnr6MoY9ZRSp51GtG4rzQNNJy7WdIi%2BSKBjrliW8FDAsURrSuUpn%2F7a3DsZErzyjYs7WWzOCMzi2wrg9aWB4Z446emnRJIGXezeY4nWZD5xiU%2Fxww65zPH9%2Fs4MgaoBmJw%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i1/103336171/TB2oN_TXxPI8KJjSspoXXX6MFXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>338.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="圆领连衣裙短袖女2018新款春夏装春夏夏款">圆领连衣裙短袖女2018新款春夏装春夏夏款</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">祺妃旗舰店</span> 
                    <span class="payNum">72人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                    
                        <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.9</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                    
                    <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=569&amp;e=V3o4uxWl93qNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFPCOXckTo3cexaKEnU6HVvd1aurnnz0%2FXVlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAlGnYnqP8PeYJVVbRVda3BVqllIQdmSPrPMB9VZeGNOOZA7Lb%2FV2evr0kcFQlRHg2NCBv7xAc%2BtqpebeXhT%2F9LOvuK9fwvu7v4w7w98ScJ4zk7WGbHSr2zKjBYHV6c%2F%2Fr7RO0cZaLLwild4vUxOGWv5zhxSGDEp4ZKaXjrWQ%2BGHH8UXy73YaeLici1LcOifyUTn0CMeAshEXz13ow3bnwxvfnzHxwxicUn6BcQvmGzsPurdjlfPGvKHU1kWDeYOnwRl4%2BKLuSyjU3NvJipk38fhLWGfaLbKjjg%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i1/11280325/TB2l2GoiQCWBuNjy0FaXXXUlXXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>128.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="2018夏气质名媛长袖网纱露肩包臀杏色连衣裙">2018夏气质名媛长袖网纱露肩包臀杏色连衣裙</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">宝葫芦女生店</span> 
                    <span class="payNum">0人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.6</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                
                                   <li><span class="lessthan">如实描述:<b>4.6</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                
                                   <li><span class="lessthan">服务态度:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                
                                   <li><span class="lessthan">发货速度:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=557&amp;e=6zA%2Fn4tlwoqNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFN8iCppyGuF29GNhhT%2FbJfUPTYhjxdprfNlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAk2ESNaMxWsaWxNThAFrr5IPhYHiGeYoSEfvCq2cllzaROJiCoAO%2Fj%2BngGhWQ%2FZ6LHjZS2SdA2W%2BMp52rUABg7yhCxd8w%2BgySx4sgzVX0xKWFGOJZ0bHfKeZeL%2BvjSfuETdjWqYikv2%2BLd7ioMK9mkufHeYfgjE0EgoCMoZ0JIR1I4dlC6OgE9KYho0DuJ7YHdn6PDmj053BDtLmqomFQJvH4M8OBVq%2BFHqNa3sGHCM8tR6lsf9e0zvSRW48DYb5t1%2FGJkOmRUb6GA9NCf8LkaQ%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i2/117201985/TB2b5oKiCBYBeNjy0FeXXbnmFXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                     
                        <span class="pricedetail">&yen; <strong>128.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="中长款春夏季新款v领复古温柔风沙滩长裙子">中长款春夏季新款v领复古温柔风沙滩长裙子</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">柒柒52165</span> 
                    <span class="payNum">18人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                        <span class="icon"><span class="icon-golden"></span></span>
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.7</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                    <span class="icon"><span class="icon-golden"></span></span>
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=569&amp;e=POEEBOQj6OmNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFOdr9qBPSe586WVDVHAcKL9U9iV%2Bb9K4ExlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAtldQq9PgHIa0A0wz%2BmXxF7JUv6u6OD00N3zK6RPCrX7JbQpkD5w6nZNYg4a34WO5gZbNU9fzM9raPvZwNoQEVm5vaUIzq1wyV7kjP9wZg1zQY9cJbpUeCsqqv83HtiJG9d0WxPdIIM5ft5MNI3hceJwpq8%2FMlnAhZqLNlGBU7JnEf67EWnV45yX5n4aEucDKRvQ%2FkgHIGfA%2F9dzY5f0vKmNg6QWNsCwvSpKhegJIhdzIcFYv4Evl4t6Bg6wxg%2FGsGtba28nyHiabHmVebCSdruTW8iRWcKvXQ%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i1/100159498/TB22F_ebZIrBKNjSZK9XXagoVXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                     
                        <span class="pricedetail">&yen; <strong>78.00</strong></span>
                     
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="胖mm欧美运动时尚娃娃衫显瘦蕾丝连衣裙">胖mm欧美运动时尚娃娃衫显瘦蕾丝连衣裙</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">绿色深林888</span> 
                    <span class="payNum">0人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.8</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=653&amp;e=yIzQO7Y77TKNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFPzwMIq7Zr%2F3h%2BI0%2F4gecIZacH21%2FzDaURlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAuYh7%2BQYo7NL4LSodO3LBZPC2jV6Ix8bRb0qe0wjAlKp6GwPPujrhnKyDhTgP3P2GNldQq9PgHIaox5CemGvyaMHjFsfOg%2B67KhtiJenBrhs8re1LtsJWNZQgNP%2BTIFaxLkhIjZ2Z%2BKspH9RESudYhnBfvZbLXd0TLitBKsnqSoCsnGX5XL0LgxpQUcP4rDCRauyzDaJa5j2JXbeHQ1kZMUX4zwYH%2FFAI6lHm0Oe692BwkIz81XobWNCfFsF2gwaNlKmT%2B8FiK9IQ7I9u9LVZbk8vb549ZkQOcCFqyHqpCahXFT1K7e5uVJGEqALkUsUTdDaMXMEJ%2B5JrubaNyFnIxb2%2Bc5RZTIitZT1ZVE399qjFXyfu9Yhamk%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i1/45701505/TB2Gmlma0knBKNjSZKPXXX6OFXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>89.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="大码女装夏季新款胖mm休闲时尚显瘦两件套装">大码女装夏季新款胖mm休闲时尚显瘦两件套装</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">东方美_正品女装</span> 
                    <span class="payNum">1368人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.6</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                
                                   <li><span class="lessthan">如实描述:<b>4.6</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                        
                            <li><span class="morethan">服务态度:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                         
                        
                        
                            <li><span class="morethan">发货速度:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=569&amp;e=PvHs3Ajm7KONblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFOXJljM%2FKQMnJbOF7yxeSAD4ns%2BbsntwztlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAlGnYnqP8PeYJVVbRVda3BVqllIQdmSPrPMB9VZeGNOOZA7Lb%2FV2evr0kcFQlRHg2FXtKbQ9lV6LYzC3aooJtBBExTSfzcKx8JUEfOdNbH2tzwe3DfFt33OQZePwRRIyzVUCRqWB6X4%2Fld4vUxOGWv5zhxSGDEp4ZKaXjrWQ%2BGHH8UXy73YaeLici1LcOifyUTn0CMeAshEX18eHEJG2Sg4E6hh%2FcYveg36BcQvmGzsPurdjlfPGvKHU1kWDeYOnwVR%2BREZv6PwUupaynY1SYVjfnbet2kKjGg%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i2/15873628/TB2a86Yb_CWBKNjSZFtXXaC3FXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>249.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="条纹裙女2018新款连衣裙a型宽松中长款">条纹裙女2018新款连衣裙a型宽松中长款</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">chaneyli</span> 
                    <span class="payNum">0人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.9</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=601&amp;e=ArgpOUwTb%2BCNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFMevw0eLYuHIC9AhBCC3lkOpL8AGdh%2FuPBlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAnBhv3huMRWv%2BzQecH3nSHa6bS5tGa1rvQOplIjdvKre3cQPpY1nykY8Z%2Bs74%2FaxqKaR65is5g4itveLaHj3fDrNLXb2VRCj9%2BmrEe7Jx6MeoCYdg3IxSJAN0T5V2dTv3chcOWPT4b9bQ2r3qAiuAahP1k5OBewsbWzGOmjYiqSF9gA9m%2Bwuv%2FhWqBYipxAXJap54Gi0NUXaYZaxDuGYG%2Bzc6lfZr6DXimNsKgxunTFKxYH6%2B84fcb7VDqVoc8ardsvVn54R6%2FvTsnOTXVcHsugUjA2cxisyVqQ7RheVn9MHYIjoR4ljuye%2FoEkOgiqzdg%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i3/26910303/TB2Rnr7d3mTBuNjy1XbXXaMrVXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                     
                        <span class="pricedetail">&yen; <strong>109.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="拉夏中长款刺绣系带连衣裙20012012">拉夏中长款刺绣系带连衣裙20012012</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">静静gj1</span> 
                    <span class="payNum">0人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.8</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=641&amp;e=S7YyPR5AtGCNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFPLdIJBYOIrheMwZrlVQ79TN%2F6qMgU7BlxlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAi56xghqF%2B464XrrbsBL7GiJHR39%2FDFKEX8EGBrJ9VHKJVyCIrb1zMHJUv6u6OD00N3zK6RPCrX72aTiq0VG5kt4M2lkfJYabS7jvCSDH9gfmZMMQ0ToAczc3hiFWqGeNGTedWHIfpvVYgR%2BQ5j1lFRx%2Bh%2B2sUkWB3O8G3NOp015TaEnHIzswPdHSnOQT6nMrp4qNumM5htmrpQQBNFK13vnUa0bivNA00nLtZ0iL5Io547QC6%2BwTwqi%2FROQRVOOJBT5Fwtuj5%2Fk3pWK48VcGgll%2FKofd7sejH6BcQvmGzsPurdjlfPGvKHpG9gHevEUS6ufQCHkoXB5L2%2FlkvdjBONRknPTw9kzVrmXFnbEne5B" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i1/131102693/TB2LHSOg9CWBuNjy0FhXXb6EVXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>169.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="绣花合唱演出服优雅成人连衣裙长裙现代礼服">绣花合唱演出服优雅成人连衣裙长裙现代礼服</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">胡甜甜919</span> 
                    <span class="payNum">4人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">5.0</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>5.0</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>5.0</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=569&amp;e=XDa7wyHH6a%2BNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFMkzxNoSFNArY8%2Fh4l5THJezpP3ZUfGMDNlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAlAvFkEHFWmvBvMOqWKerGpAif3Npr46uoJ2ZqQmVcBVsSpbIGYqp3m9yXq9v4vwcvvy8zikdJEbfpvFYRFPIgUk9gL2QXVVV3K8o36UBbhfyNSXKAE6nr7ugcdSfI5OnrntZDtezgzBaUFHD%2BKwwkWrssw2iWuY9iV23h0NZGTFF%2BM8GB%2FxQCOpR5tDnuvdgYzwFYn6QP4HgeO7YoCeltD1KL9eUvH3TMnTMHu7EXMMegaLYB1x0ANYjd9NPv89dJofRgDRc6UNJv1mIkl1F9wpqspzowqsxQ%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i1/27098720/TB26c5LaFooBKNjSZFPXXXa2XXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>268.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="2018春夏装新款明星同款荷叶边印花连衣裙仙">2018春夏装新款明星同款荷叶边印花连衣裙仙</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">xiaozhu猪猪</span> 
                    <span class="payNum">1303人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                        <span class="icon"><span class="icon-golden"></span></span>
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.7</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                    <span class="icon"><span class="icon-golden"></span></span>
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=569&amp;e=ktIEH5O8lWONblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFM5RW51tYALao6GuQvW5d5LAjMIpAio4pZlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAuETc02MkuA%2FAwp%2BRVHsRR3O1lszgjM4toiE53VD5qJjROJiCoAO%2Fj9Kmgpu3nbWCWZ819ShAOBqCcQEms4IfSDgiTQXLy9OKSdANtyC0RPUqlbCg9ZrvyQEZ6rpLPR%2BsTdjWqYikv2%2BGMHwaFGvZKiWMiX7iRXnPnr6MoY9ZRSp51GtG4rzQNNJy7WdIi%2BSKKq3q%2BJUl3YmeAX4r7yDV3y3DsZErzyjYs7WWzOCMzi2wrg9aWB4Z4433QmOqI%2BDIpPoVmzpRx22U%2Fxww65zPH9%2Fs4MgaoBmJw%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i1/103336171/TB2H2xQhrsTMeJjy1zeXXcOCVXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>299.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="中长裙连衣裙蕾丝2018新款春装女春秋季粉色">中长裙连衣裙蕾丝2018新款春装女春秋季粉色</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">祺妃旗舰店</span> 
                    <span class="payNum">12人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                    
                        <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.9</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                    
                    <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=653&amp;e=Hp1ngOdNuL6NblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFOsWnkcrHaZxV29Yll19zO6iaFKMxO3xKllK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAjTisYAfoUt9%2BBR6lkt0VY4NN%2B5jdpWSSWX8qh93ux6MfoFxC%2BYbOw%2B6t2OV88a8oX8EGBrJ9VHKiITndUPmomNE4mIKgA7%2BPyO3BqotBvcCNLTe3qM8FwHooKCMZ2xp727X7gU7jO%2BbUkiy3Y%2BuxKkqfvaPwbl%2Fl49XpjtLcpVbhslNNXPYujEFATLGngWBjAsrWrT5ggrFay9oRtWhUG9ksbeTWq%2BaffFF9Zs1X%2By90Gh%2BNgyRcH8jdvDQT%2FXo49%2BddvIdJtHAFW1iszQe3IXxgaqZYvk8kSOx32XhctexZfyqH3e7Hox%2BgXEL5hs7D7q3Y5XzxryhMUP3aSuVPMTuB2nZDL2uhB%2BUqeMmnk4Wv6BJDoIqs3Y%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i2/1260006071422097860/TB2DmNMuMxlpuFjy0FoXXa.lXXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>88.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="雪纺修身显气质长款大摆方领沙滩裙碎花长裙">雪纺修身显气质长款大摆方领沙滩裙碎花长裙</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">芭啦发888</span> 
                    <span class="payNum">522人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.6</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                
                                   <li><span class="lessthan">如实描述:<b>4.6</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=641&amp;e=023F2UpHLQuNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFOmkqLC3GXpQVYLNfmJilgYPfNkW7hemRZlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAn5GuhUWgnfw2b%2Fi7ijztxHJUv6u6OD00KC9FBulM27Pce4vOfTLuD1kfHCYt7VlqrJuZ%2BYZtCmJ66xZMsGz5CBE4mIKgA7%2BP1jgzW2gWqkTGWmbMA%2BxWdd0gl5Lpipw9m9zH8yuGDUrNz8knnpSEDON2n6s7%2FteOgrfnZy7YR8JN2NapiKS%2Fb4YwfBoUa9kqJYyJfuJFec%2Bevoyhj1lFKnnUa0bivNA00nLtZ0iL5IoYnoMXBiptEXhj98q27SmDv5dRelCjV1axXTgxHokVeB%2FBBgayfVRyn6BcQvmGzsPurdjlfPGvKF%2BRroVFoJ38J8ZawgJDlLOjStd%2F61al3Fu3JsEeDgtbt3tD2LMSUZN" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i2/1332805024240519602/TB2RywdiilnpuFjSZFgXXbi7FXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>529.00</strong></span>
                     
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="名师路2017新款夏气质时尚印花连衣裙短">名师路2017新款夏气质时尚印花连衣裙短</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">名师路旗舰店</span> 
                    <span class="payNum">63人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                    
                        <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.9</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                    
                    <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=557&amp;e=f3DBEYSAkZ6NblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFOEHBMUSHhFArJ1mAEwLQ0sF5fIdXlCqB1lK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAk2ESNaMxWsaWxNThAFrr5IPhYHiGeYoSEfvCq2cllzaROJiCoAO%2Fj99KXFl%2BO9%2F0DGGTQiy4EeqLMNdLn1BqIaUE5WnZTZzBdqHoeC%2FyHB6%2FwevIb6dU6yIiHDkVnP6JTdjWqYikv2%2BLd7ioMK9mkufHeYfgjE0EgoCMoZ0JIR1I4dlC6OgE9KYho0DuJ7YHVjfVgpnaxvqoKdjXURRXlbH4M8OBVq%2BFHqNa3sGHCM8tR6lsf9e0ztwRPBDQ4tg%2BxqYMi0jTK%2BG8DfxzZe%2BEAk%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i1/120349609/TB2dU6hcER1BeNjy0FmXXb0wVXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>28.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="短袖新款v领打底黑裙夏季显瘦莫代尔长裙">短袖新款v领打底黑裙夏季显瘦莫代尔长裙</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">八七良品美衣</span> 
                    <span class="payNum">1372人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.6</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                
                                   <li><span class="lessthan">如实描述:<b>4.6</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                
                                   <li><span class="lessthan">服务态度:<b>4.6</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                
                                   <li><span class="lessthan">发货速度:<b>4.6</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=601&amp;e=6XpvJ2DqIjKNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFMWmO1qvJwDldk33oQTs9PSCJEhcpxMeqtlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAgasWF5Ct0AVe551xPP0CYbfnXbyHSbRwFGnYnqP8PeYJVVbRVda3BWViNY%2BG3b9ZfSRwVCVEeDYIX2mkOFyMTgCzV5ok8rDNhu5lngei9EBemMsiqHLhMfUTs18Ikb%2FNWgO61ClNUVhy2gAbmXLMEPXdFsT3SCDOSlQDwLRvQclPzK8xqq%2Fo69rL2hG1aFQb2Sxt5Nar5p98UX1mzVf7L0hfaaQ4XIxOOrWH5Mx09OD35128h0m0cBRp2J6j%2FD3mCVVW0VXWtwV1cIdFzGvh6PgVycUAflLXrd67qB6PXdg5S%2FMJbNwJiIoMCA2uCCVuQ%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i3/117256082/TB2e6KxbFooBKNjSZFPXXXa2XXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>198.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="韩版时尚牛仔长裙修身吊带显瘦大摆连衣裙">韩版时尚牛仔长裙修身吊带显瘦大摆连衣裙</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">芷娜旗舰店</span> 
                    <span class="payNum">3人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                    
                        <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.7</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                
                                   <li><span class="lessthan">如实描述:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                
                                   <li><span class="lessthan">服务态度:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                
                                   <li><span class="lessthan">发货速度:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                    
                    <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=569&amp;e=cyfnv8r3QYCNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFMiJGTZ4f9v4mkFg2cIhPaxMSouejUDBwllK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAlGnYnqP8PeYJVVbRVda3BVqllIQdmSPrPMB9VZeGNOOZA7Lb%2FV2evr0kcFQlRHg2O%2FyPZKqZ4qIE8ivUxUj7lIMErNJ7e1eoiDl4TPqU5LZFCIRUf43y2wVjtMfYI7pbkyMq1Iyo%2Fk013RbE90ggzl%2B3kw0jeFx4nCmrz8yWcCFmos2UYFTsmcR%2FrsRadXjnJfmfhoS5wMpvZK7MOnUD50ECnRe0CL06ipKhegJIhdzIcFYv4Evl4s5bTi1yTRRLhrA1FzjmVsUauzagVLiYCPHl%2BsIhuI7dQ%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i3/48917532/TB2hioahkKWBuNjy1zjXXcOypXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                     
                        <span class="pricedetail">&yen; <strong>139.00</strong></span>
                     
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="清新甜美2018春彼得潘领玫瑰印花长袖松">清新甜美2018春彼得潘领玫瑰印花长袖松</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">兔兔窝衣橱</span> 
                    <span class="payNum">0人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">5.0</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>5.0</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>5.0</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>5.0</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=621&amp;e=oyzSL0afVCKNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFP7DcgIBxVBJjR0VvMPn%2FqA2ry2YxNwFIxlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAlUtwMxFhna7n1tXGEIKl5vJUv6u6OD00KC9FBulM27Pp8VK8YWQkVZl%2FKofd7sejEfvCq2cllzaROJiCoAO%2Fj%2FtOUemismfNoSO55Cw2oPqnxWe8uCDktL1NP%2B8Iquctj3PNmw%2FPrK2PyCi1aEbEe5dJ0cEQopUYYbJTTVz2LoxBQEyxp4FgYwLK1q0%2BYIKxWsvaEbVoVBvZLG3k1qvmn3xRfWbNV%2FsvYi4whLXtp9%2Byv%2Fmm1BmynVSvmpQ5Z1pJkt4DsLfz67hYY3JaFDRRjlDirEkqHPQzXfFk3R0N1ptBYaiWd2kNs3RjaLKfWxUlrYeXRxYk7PxDsEUZuM%2BqLY%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i3/14436006/TB2rx04cLjM8KJjSZFsXXXdZpXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>129.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="波西米亚长裙白色一字领露肩吊带连衣裙">波西米亚长裙白色一字领露肩吊带连衣裙</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">靓仔简</span> 
                    <span class="payNum">18人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                        <span class="icon"><span class="icon-golden"></span></span>
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.9</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                    <span class="icon"><span class="icon-golden"></span></span>
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=569&amp;e=Xc5Fyv5dBteNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFNduOYSsYv4Z6NIF4Yq8zlGqidFPiqyBOJlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAn5GuhUWgnfw2b%2Fi7ijztxHJUv6u6OD00Lh%2BZjBFWcdD%2FnDrnV3kL3XfoEW5Linc2z3%2FQQMZ%2FaVqbQ7NU6BXo99eL4NV%2FyE%2Bq6WmEJPqlA%2FRcATvHfJnx8USwnD4CYh7zx6uAg%2FVin6LaUFHD%2BKwwkWrssw2iWuY9iV23h0NZGTFF%2BM8GB%2FxQCOpR5tDnuvdgUgVhcTXY%2F6RNtXZq8EmLzwqSoXoCSIXcyHBWL%2BBL5eLIrxa0xTJv%2F5QeakRKGnUeAzrU6UbYi7mrx9yM%2BXPl3xbbcZGmWKdzw%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i3/35585830/TB2TcTehDlYBeNjSszcXXbwhFXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>138.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="春夏新款印花长袖连衣裙雪纺V领碎花裙">春夏新款印花长袖连衣裙雪纺V领碎花裙</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">胡庭煌2012</span> 
                    <span class="payNum">7人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.8</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=557&amp;e=IMEdM%2FNj6E%2BNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFMLe4AjAT0bajhUeU2mdYojE1ZQgs%2BXyQtlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAk2ESNaMxWsaWxNThAFrr5IPhYHiGeYoSEfvCq2cllzaROJiCoAO%2Fj%2FLhRNo0bZkb5HRG%2BMHeaYbCBdJ1k2hqKPTBUVrgK%2FYmGdLQVuHRQR%2B8LOjChWaSHEM0ww9FC6H3TdjWqYikv2%2BLd7ioMK9mkufHeYfgjE0EgoCMoZ0JIR1I4dlC6OgE9KYho0DuJ7YHayVwk2fhkyX3mmG8NHDRhvH4M8OBVq%2BFHqNa3sGHCM8tR6lsf9e0zs4tx%2B8zbpD0eBW2bpqGbXIEGLuuAo8Ao4%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i1/17521077/TB249G5gv5TBuNjSspcXXbnGFXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>468.00</strong></span>
                     
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="v领印花显瘦磅真丝连衣裙桑蚕丝长裙大摆莹">v领印花显瘦磅真丝连衣裙桑蚕丝长裙大摆莹</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">雨露清荷98</span> 
                    <span class="payNum">9人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.7</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=537&amp;e=COsg0kppUdONblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFO98Q6mzXYZFQ5yKglw%2BYUYYkskLz1H4SRlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAm81lKtnL42XodI7St1NGIXMxnQ2FeilNQhg9YNtn3yzA6FJQkrzrEaDFSH0icsKcxi0mMjEVX%2FJS%2BQpoCdUA%2Fq%2F8EQz%2FF1qLzmkYhaxGw%2F4IUapmpv77ZiV3i9TE4Za%2FnOHFIYMSnhkppeOtZD4YcfxRfLvdhp4uJyLUtw6J%2FJR7Gy%2FSuKSgQlGJ6RMmX6Btakr6Q%2BjMECjUC7TriokDHGB%2FvW0xnzxDIv9LB9JC%2BUBHJJ08Wg7eWzw0sgj93bNGg%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i2/49430742/TB2aSzUfKuSBuNjSsplXXbe8pXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>77.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="赫本小黑裙连衣裙夏装新款女温柔风吊带裙">赫本小黑裙连衣裙夏装新款女温柔风吊带裙</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">博文xx666</span> 
                    <span class="payNum">282人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.7</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=557&amp;e=UUn%2F57aLd%2FCNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFOXr7IjYLHgl%2FlJ7EBVBxeDFsOWBQ6ag4BlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAreQDVRf3BT4YfJF9vcmomBbE1OEAWuvkmi5YA07wUI2ilpva1sR0%2BhrOboExOFz4KE7veEvH16M31%2FJdcfmeSgjluEKmp88mZS57S%2B1LADKPP%2BBAb5uiBZI3J9G0suo5obJTTVz2LoxBQEyxp4FgYwLK1q0%2BYIKxWsvaEbVoVBvZLG3k1qvmn3xRfWbNV%2FsvZSTHc2r8%2Fyxj5Lft031DUg%2F2LBvjY9FbX8EGBrJ9VHKlYMZn2hCeXkuqsfoz8JVqaoJEyKOSmWajeJZ%2Fg13NMU%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i1/106373036/TB2Gza2bkyWBuNjy0FpXXassXXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>259.00</strong></span>
                     
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="连衣裙开叉仙女露肩显瘦气质长裙">连衣裙开叉仙女露肩显瘦气质长裙</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">ac653617187</span> 
                    <span class="payNum">1621人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.7</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=537&amp;e=lKLlS1m%2BdByNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFNzmTmcFHogSqznZYAWf1mAY6y97FPtrDZlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAhkfAsRta6OBM46rnCeezlxrosTkIRof7mokXTUL1hCMyYGWnuCrI%2FH8Kc7f5aSSI9sS61TP3umni8Cr6kyzJt%2Fbf015yiLIZsPswEx7a9POJmkyAAw0kN5P1k5OBewsbWzGOmjYiqSF9gA9m%2Bwuv%2FhWqBYipxAXJap54Gi0NUXaFzigoDmqprZwFE35bemSMCkDJDLcd1URO%2FdLlb8%2Bl5wQptme905LcZLAUBQhYvkRMnm0FtejhurJwcB%2Bl%2FeRxw%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i1/11049960/TB2AH..bVGWBuNjy0FbXXb4sXXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                     
                        <span class="pricedetail">&yen; <strong>269.00</strong></span>
                     
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="张.大奕吾欢喜的衣橱 两件套雪纺衫">张.大奕吾欢喜的衣橱 两件套雪纺衫</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">小番茄0506</span> 
                    <span class="payNum">872人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                        <span class="icon"><span class="icon-golden"></span></span>
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.7</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                    <span class="icon"><span class="icon-golden"></span></span>
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=557&amp;e=UI8BmYO1tFWNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFPHEOQbTw%2F0Q2kHtxNJsmaaP933brTuEptlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAk2ESNaMxWsaWxNThAFrr5IPhYHiGeYoSEfvCq2cllzaROJiCoAO%2Fj%2FqTDaAJfpxmN6VSlSHGqndazsU77ZTF216P2MRObQqraVP8i00J%2FX8iM0Nt1NQxU1fdNUwC3014jdjWqYikv2%2BLd7ioMK9mkufHeYfgjE0EgoCMoZ0JIR1I4dlC6OgE9KYho0DuJ7YHX2NI9Lik1u4c95Codmxn4HH4M8OBVq%2BFHqNa3sGHCM8tR6lsf9e0zsedPd17dMmibC%2FMJZN%2B5L2GfDgf15zrPI%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i1/16452518/TB2SHlajhSYBuNjSspjXXX73VXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>160.20</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="碎花雪纺连衣裙2018夏季新款七分袖绑带长裙">碎花雪纺连衣裙2018夏季新款七分袖绑带长裙</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">wangby_2010</span> 
                    <span class="payNum">0人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.8</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=589&amp;e=dTbiQ3S7I6yNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFOEyho%2Bu1K9oKd5D%2BhYHedPkgmv1nPz4UdlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAgasWF5Ct0AVUoFhu2SdZPKfC8tUq5uW93%2BODv%2FfxT3W%2Fl1F6UKNXVqViNY%2BG3b9ZfSRwVCVEeDYurUcFsE5koUML7f0X462ihcCbIqXur7RZVekZfTKmvXOwVziMcCXAEVcw8BDpYJY110%2BDHOGMO3XdFsT3SCDOX7eTDSN4XHicKavPzJZwIWaizZRgVOyZxH%2BuxFp1eOcl%2BZ%2BGhLnAyl7H6pOdnIr8eZ7OFO0C%2B9RyF8DamiiwIxbE1OEAWuvkrC9ovaYKln5Zd8fmSE190UK1jJoJ94GrDIJo0PMhwx4L6F2YTWjZBU%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i3/114521830/TB2FsHaaLImBKNjSZFlXXc43FXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>129.00</strong></span>
                     
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="泰国海岛度假吊带长裙低胸高腰雪纺连衣裙女">泰国海岛度假吊带长裙低胸高腰雪纺连衣裙女</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">韩潮时尚衣库</span> 
                    <span class="payNum">25人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.9</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>5.0</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=601&amp;e=tIiltDFJ5D%2BNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFMnT9Wc0xqRrQL8T8j%2FnIT%2FN5gnxnQfSJ1lK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAgasWF5Ct0AVe551xPP0CYbfnXbyHSbRwFGnYnqP8PeYJVVbRVda3BWViNY%2BG3b9ZfSRwVCVEeDYRB8%2FLs3OX%2BWIe%2FJ0f87h8jCWPJvqVtxOcTMUpD9rJWybWbmZSg5pI2iMKxp%2FJekYiqvoxboOhWVP1k5OBewsbWzGOmjYiqSF9gA9m%2Bwuv%2FhWqBYipxAXJap54Gi0NUXau3f3cw25Bg1KrQV40dcYNvzoPJUrlUc33NyP0UpKI1tDirEkqHPQzXfFk3R0N1pt2o1VOlG3MrwTjeMSJKBabhEP1PuMTjDWY3mSujr3Hs%2Fm8PLaGh1hYQ%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i2/1669306064014206725/TB2cXvytgxlpuFjSszgXXcJdpXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                     
                        <span class="pricedetail">&yen; <strong>168.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="韩版渡假feel吊带连衣裙圆领短袖印花裙">韩版渡假feel吊带连衣裙圆领短袖印花裙</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">123830weiwei</span> 
                    <span class="payNum">87人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                        <span class="icon"><span class="icon-golden"></span></span>
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.7</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                    <span class="icon"><span class="icon-golden"></span></span>
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=557&amp;e=JC1o3Z%2Fq5%2FyNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFO%2F3jgDgYtLq62isNOtgxjxn57bIOJ2rgBlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAk2ESNaMxWsaWxNThAFrr5IPhYHiGeYoSEfvCq2cllzaROJiCoAO%2Fj%2BYY0VaaOTDvgzULkWtFEyD9cpq4UxsuCFlrtCXsrnF3cusgdCJXptZtTbwwdsjUl7go3M2B3G%2BYjdjWqYikv2%2BLd7ioMK9mkufHeYfgjE0EgoCMoZ0JIR1I4dlC6OgE9KYho0DuJ7YHXg%2FHqxrXMt6xcwpM6U2cELH4M8OBVq%2BFHqNa3sGHCM8tR6lsf9e0zttR1NV%2FFl06VUEl8fT5%2BrK2WcYQoSobuA%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i2/132131903/TB24WQ3ih1YBuNjy1zcXXbNcXXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                     
                        <span class="pricedetail">&yen; <strong>158.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="黑红拼色性感v领雪纺长裙配腰带收腰">黑红拼色性感v领雪纺长裙配腰带收腰</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">我喜欢这样的我们</span> 
                    <span class="payNum">2人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">5.0</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>5.0</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>5.0</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>5.0</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=569&amp;e=8oHChwwLi4aNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFPsuvqO0DkbX2ti5shH%2FlsOJd0HxpzoVMplK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAn5GuhUWgnfw2b%2Fi7ijztxHJUv6u6OD00Lh%2BZjBFWcdD%2FnDrnV3kL3XqW6lpY8mJipMH1ELKt%2BfW5QE12CS8nk12Dn35NXmGRo0qhZrkmbMrciWiZp%2BEypgVa9fa%2BXOeptwMWxOY4nYAaUFHD%2BKwwkWrssw2iWuY9iV23h0NZGTFF%2BM8GB%2FxQCOpR5tDnuvdgY%2FF1wpIqtzpv2mZoP7Z3BAqSoXoCSIXcyHBWL%2BBL5eLIrxa0xTJv%2F5QeakRKGnUePU1Kt8JV1m4rgO0865L8iNtQnQOhaT8Yw%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i2/32601379/TB208mTbWQoBKNjSZJnXXaw9VXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>65.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="网纱拼接V领喇叭袖百褶收腰碎花短袖连衣裙">网纱拼接V领喇叭袖百褶收腰碎花短袖连衣裙</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">韩版靓丽衣橱</span> 
                    <span class="payNum">4人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.6</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                
                                   <li><span class="lessthan">如实描述:<b>4.6</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                        
                            <li><span class="morethan">服务态度:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=633&amp;e=PoIVOIQFzWaNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFODyyUifIUZdltpsSVAipgxZ2%2FMbVWpix1lK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAmY4Ezhsqt8hZVZOfnY79Ca4Jb71m5pmONTbX8zw4nKmX92%2BUHdX9gXhLX6ikRUGVA0DWFS%2BDPI9W7IE8Q%2F8uCt1hsswZjyeXGEK9fg8ZH1%2F%2F%2BEXD7gX4aMEy27WXFyZ3NNGnSCcSJj7jCEB0%2BpoAX2Y4Fd06eFsaq0OpixXvx4ur5ayKmcbo4m%2FUb96qihbRqutn8yROWq9F%2BM8GB%2FxQCOpR5tDnuvdgV%2BOg9s%2FqwkE9DF8GSxVHShlH0hibMKDxduLzoTkEgKDAaO%2FnBkeKkThLX6ikRUGVLJr%2BafQZLPjKZReSpcE5wrSHwnlEWX1Bs6XsB8O68ifpySaCT%2B8hvvNHLZQVFREWQ%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i3/122244371/TB2TJ6YgY1YBuNjSszhXXcUsFXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>378.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="显瘦修身印花复古a字大摆连衣裙女夏季">显瘦修身印花复古a字大摆连衣裙女夏季</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">绒惑旗舰店</span> 
                    <span class="payNum">1人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                    
                        <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.9</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                    
                    <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=569&amp;e=VK3XE7kVvWqNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFOSE9yAERBhRwiXYn6nN1crKXQ1bODtqeBlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAlGnYnqP8PeYJVVbRVda3BVqllIQdmSPrPMB9VZeGNOOZA7Lb%2FV2evr0kcFQlRHg2E7CCK7DTg3fLLMc4cA%2FSFxTujQwW24iKeC3cSCS1V%2Ft%2B4ZAHvJGrU5VIowK4WL%2FoYxns1C6thYO13RbE90ggzl%2B3kw0jeFx4nCmrz8yWcCFmos2UYFTsmcR%2FrsRadXjnJfmfhoS5wMp3h9OWkNHGqe6%2Bu443F%2FPJypKhegJIhdzIcFYv4Evl4s5bTi1yTRRLnlwichVqUl0lUUtZYUbUYGfdfh3CNJe9g%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i4/TB1g2JGceuSBuNjy1XcYXIYjFXa_M2.SS2_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                     
                        <span class="pricedetail">&yen; <strong>198.00</strong></span>
                     
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="2018新款春夏季洋气棉短袖连衣裙女长裙">2018新款春夏季洋气棉短袖连衣裙女长裙</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">异木棉456</span> 
                    <span class="payNum">188人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                        <span class="icon"><span class="icon-golden"></span></span>
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.8</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                    <span class="icon"><span class="icon-golden"></span></span>
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=577&amp;e=kOHcvtStnL6NblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFPSnQfnZoSKplsbB6BD3YEnHtBJbDXMfCxlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAlGnYnqP8PeYJVVbRVda3BVqllIQdmSPrPMB9VZeGNOOZA7Lb%2FV2evr0kcFQlRHg2AUY6Cf0a0LbUhXV46wU1rG6FfEgkEhIHYnVgr7UijZecIBL7RWqBR5jmldV2y4PIxcm18Q01mp713RbE90ggzkpUA8C0b0HJT8yvMaqv6Ovay9oRtWhUG9ksbeTWq%2BaffFF9Zs1X%2By9BRjoJ%2FRrQttimeqwZTLogFGnYnqP8PeYJVVbRVda3BUjsd9l4XLXsdDW9xe0BYz6FrLyBNvEvjGNTFB8pn5oZL%2BgSQ6CKrN2" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i2/117346131/TB2lF98gCtYBeNjSspkXXbU8VXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>388.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="蕾丝连衣裙夏2018新款镂空修身气质a字裙子">蕾丝连衣裙夏2018新款镂空修身气质a字裙子</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">卓芙莱旗舰店</span> 
                    <span class="payNum">292人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                    
                        <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.9</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                    
                    <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=653&amp;e=GJH3OY%2By%2FxKNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFPEh3QZlyL6bScMvKW2T1Aak62oChA4urRlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAjTisYAfoUt9RurVlncm%2Fs6uuW%2BlivNlfte0dQzba3JjBlMGOgx0QbJhjcloUNFGOUOKsSSoc9DNeEST94%2FTF5P%2BcOudXeQvdW%2F5AXR%2FYXHO0NWw%2FEJK81ejQ4i0Hida3taTF9ZXXRGwwbBP7XyLwR52V94ZxNhZ2C5qIslZ2kCJixR9UJ33tXlpQUcP4rDCRXuQvwLggsKTNMcRv%2FW1NhRzhxSGDEp4ZIGPq8Gl94SW8HRak%2F3qpyJH5CnutVkhQzTisYAfoUt9%2BBR6lkt0VY4NN%2B5jdpWSSQH7IyWGokz5%2Fl1F6UKNXVp%2BTscf0YBGI87WWzOCMzi2itszdz8VAamFNRBZVCWMU1ogzc5WpzYDyb2Hx5KANco%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i1/1893306052087527420/TB2Qg.muUdnpuFjSZPhXXbChpXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>179.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="收腰v领五分袖大摆红色连衣裙雪纺长裙">收腰v领五分袖大摆红色连衣裙雪纺长裙</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">沙滩宠儿旗舰店</span> 
                    <span class="payNum">7人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                    
                        <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.9</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                    
                    <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=621&amp;e=8B7E90LNe2uNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFMT51eFyFAy1T9oKWYBbLVozLHhQNgz8ZBlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAgOplIjdvKre3cQPpY1nykZRp2J6j%2FD3mCVVW0VXWtwVFRh9AAjqLSIO4nR1R%2BOjbrv7cSzSzJYzCGD1g22ffLOZoY7zW0mNawUdb7TVUBhNK%2B97Zh9amIzsq5hUEib%2BCWcbhZV27u1K%2B9PuPQCTSogl11i2e0AFHJXeL1MThlr%2BcYAM45QEjC%2FSRp1PCazpBZqLNlGBU7JnEf67EWnV45yX5n4aEucDKZmhjvNbSY1rUTGve8eeYGmDkOjhKmMUyuu%2BOHW0kQlV4S1%2BopEVBlQRv1VDwUE5s7Jzk11XB7Lo8UFlqve3y9Afa1GCjI8i%2BVUKTqLlqomPv6BJDoIqs3Y%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i2/14022115/TB2jZKJXrorBKNjSZFjXXc_SpXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>218.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="2018新款春夏装文艺范中国风中式立领盘">2018新款春夏装文艺范中国风中式立领盘</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">天母严选旗舰店</span> 
                    <span class="payNum">2人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                    
                        <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.9</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                    
                    <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=577&amp;e=5NFuEOTKSHeNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFMmYuBJA2AdNeyV3jDqlyfOLePLVjaqkK9lK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAlGnYnqP8PeYJVVbRVda3BVqllIQdmSPrPMB9VZeGNOOZA7Lb%2FV2evr0kcFQlRHg2FgnNjj8ux6Qj3ZTffNfo42ZnvMgUnvTUEf%2B3YQvdK%2FElNm3bz%2BYNqybluURiT6%2Bkh5vQn5BLhm213RbE90ggzkpUA8C0b0HJT8yvMaqv6Ovay9oRtWhUG9ksbeTWq%2BaffFF9Zs1X%2By9WCc2OPy7HpBhDJevOjw3I1GnYnqP8PeYJVVbRVda3BUjsd9l4XLXsUy2dQIRB6X5w23Nccf90k8wTalKH%2BN0kb%2BgSQ6CKrN2" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i1/131028595/TB2UQKDbcyYBuNkSnfoXXcWgVXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>218.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="夏季新品通勤圆领无袖连衣裙中长款不规则裙">夏季新品通勤圆领无袖连衣裙中长款不规则裙</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">奥芭诺旗舰店</span> 
                    <span class="payNum">0人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                    
                        <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">5.0</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>5.0</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>5.0</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>5.0</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                    
                    <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=557&amp;e=V57ZMauGiCqNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFMHq3%2BHXrco7CLd1GnMmnUHArklDuMUw3BlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAk2ESNaMxWsaWxNThAFrr5IPhYHiGeYoSEfvCq2cllzaROJiCoAO%2Fj9BpDxrxIvjdsoSbF777m6hAdAoaX2azZ%2FWIDAxjNhUwvt6f50E5gTmVYGct7enaGcYfgWdgHaQYIbJTTVz2LoxBQEyxp4FgYwLK1q0%2BYIKxWsvaEbVoVBvZLG3k1qvmn3xRfWbNV%2FsvUj%2BlsP0BPM5Lk1TfG5UMsNXyVW0N8SUINKMJKGcjCAfzsCCF9Vb1kgM26gK31Hp6L3ynLwqGK4xQTvPxHLcnGs%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i3/1814606068315772377/TB2pQWlt3NlpuFjy0FfXXX3CpXa_!!2-saturn_solar.png_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>75.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="女装休闲韩版宽松A字裙大码显瘦连衣裙女夏">女装休闲韩版宽松A字裙大码显瘦连衣裙女夏</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">y0394</span> 
                    <span class="payNum">63人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                        <span class="icon"><span class="icon-golden"></span></span>
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.7</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                    <span class="icon"><span class="icon-golden"></span></span>
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=569&amp;e=nqsg8fs1CMyNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFM5ln6jde28dLo4oMGuWJPt%2BUeArIoaP49lK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAlGnYnqP8PeYJVVbRVda3BVqllIQdmSPrPMB9VZeGNOOZA7Lb%2FV2evr0kcFQlRHg2AjiGPCQW%2BCYeFg0hs2yTuyJj6MzVYX5cIt9R7q%2FRCjBBGX6dZuRhRFVs%2Fpv12hlcK24T5XwPmzN13RbE90ggzl%2B3kw0jeFx4nCmrz8yWcCFmos2UYFTsmcR%2FrsRadXjnJfmfhoS5wMpI7iZoOaTsaMs63tmcd06CSpKhegJIhdzIcFYv4Evl4s5bTi1yTRRLg4hV1aX3AGsY%2F1lEFHOSDmdm0Al9wNV4A%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i2/131777056/TB2YiDiduuSBuNjSsplXXbe8pXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>68.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="2018新款女装夏装韩版中长款夏季">2018新款女装夏装韩版中长款夏季</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">穗美人服装店</span> 
                    <span class="payNum">3人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.7</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=569&amp;e=ymzodsJ2B%2FSNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFMxI7XFXF6asTVJBgyrvEr3NAju4B8pGfVlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAlGnYnqP8PeYJVVbRVda3BVqllIQdmSPrPMB9VZeGNOOZA7Lb%2FV2evr0kcFQlRHg2KxlXRsjaDFzcHoJJoYbE82gMmVyBvSh2ylXoMsZ2IrhDh89MrnOtz0%2F52ZP994iB7tsmbm1%2B8Cw13RbE90ggzl%2B3kw0jeFx4nCmrz8yWcCFmos2UYFTsmcR%2FrsRadXjnJfmfhoS5wMpZwNbv8s%2B6vDwV9L3iT7BXypKhegJIhdzIcFYv4Evl4s5bTi1yTRRLneRXvXo7WLWqgSG4An%2BIns7fxgW1pJCkA%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i3/121826219/TB2iVf6jmtYBeNjSspaXXaOOFXa_!!2-saturn_solar.png_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>1270.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="雅莹中长款长款荷叶袖真丝印花显瘦连衣裙">雅莹中长款长款荷叶袖真丝印花显瘦连衣裙</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">今冠商贸</span> 
                    <span class="payNum">1人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">5.0</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>5.0</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>5.0</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>5.0</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=569&amp;e=WNm63ratBPmNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFOVrC58oHR%2FmsEOPjvVHvquci8MVszHCvtlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAlGnYnqP8PeYJVVbRVda3BVqllIQdmSPrPMB9VZeGNOOZA7Lb%2FV2evr0kcFQlRHg2PHvOvOKgBOsQ6rIixuFN1SH0xXPDO9vwh0psmXJDLoehDyj%2B37smCmKqO2qaeRVvWoOHwyCYtBR13RbE90ggzkpUA8C0b0HJT8yvMaqv6Ovay9oRtWhUG9ksbeTWq%2BaffFF9Zs1X%2By98e8684qAE6zcQE6AGqw3gVGnYnqP8PeYJVVbRVda3BUjsd9l4XLXsfkiPevRZH0jcWUH5OwZ4ZodJEUEeS7s7w%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i1/33726205/TB22sAabWmWBuNjy1XaXXXCbXXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                     
                        <span class="pricedetail">&yen; <strong>369.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="EST+II/艺诗2018春季新款简约纯">EST+II/艺诗2018春季新款简约纯</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">estii旗舰店</span> 
                    <span class="payNum">6人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                    
                        <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.9</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                    
                    <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=569&amp;e=CbsbtVHU25uNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFOXQOuxtyee4ydMVJyAobN9Q5vWZJw6r0ZlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAlGnYnqP8PeYJVVbRVda3BVqllIQdmSPrPMB9VZeGNOOZA7Lb%2FV2evr0kcFQlRHg2MjlVUt6fh6cbU6OowTAk%2FW%2BAECk7%2BwhrGKDXs64h0zWlfpBgn6PslwwT6YaCop1F9p5%2B7j2vjmyld4vUxOGWv5zhxSGDEp4ZKaXjrWQ%2BGHH8UXy73YaeLici1LcOifyUY0SS1Hq78LolvQUiNPHw0YuCj4y1Q2e7n6BcQvmGzsPurdjlfPGvKHU1kWDeYOnwa0O5%2Fdub3hJqp922mBywnyiP%2Fyblg3AXA%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i2/10469178/TB285ymcWmWBuNjy1XaXXXCbXXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>135.00</strong></span>
                     
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="印花连衣裙长裙2018夏季新款系带收腰">印花连衣裙长裙2018夏季新款系带收腰</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">wanzgbc</span> 
                    <span class="payNum">0人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.8</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=569&amp;e=DhDD9zHcxnKNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFOXQOuxtyee4ydMVJyAobN9LlFIB%2FdVih9lK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAlGnYnqP8PeYJVVbRVda3BVqllIQdmSPrPMB9VZeGNOOZA7Lb%2FV2evr0kcFQlRHg2O54KaspR6CQwrvGT0WQmQSSq7S%2BhazYu2XL9ZHDuxCAKQ61%2F3nvZgQK840rh9GMYzuUNg%2Ful5KHld4vUxOGWv5zhxSGDEp4ZKaXjrWQ%2BGHH8UXy73YaeLici1LcOifyUY0SS1Hq78LouLRIO9LXil8vm8GRjl2Z%2B36BcQvmGzsPurdjlfPGvKHU1kWDeYOnwfGwtIDhCNmXZN8egL9NjNOiP%2Fyblg3AXA%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i1/10469178/TB2vf6vcSBYBeNjy0FeXXbnmFXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>159.00</strong></span>
                     
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="连衣裙中长裙夏季2018春夏新款露肩鱼尾">连衣裙中长裙夏季2018春夏新款露肩鱼尾</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">wanzgbc</span> 
                    <span class="payNum">0人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.8</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=665&amp;e=9vvFWLGFpsmNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFPTOhsUPdzQaAxjjGTxgU6b%2B1zNwrMF3tZlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAhjgQxKvSk2WvtyBLhtx4kzB4NaWZ04CSMl0%2F2F6foAnNLoRFS1EVlPJUv6u6OD00AH7IyWGokz5%2Fl1F6UKNXVqViNY%2BG3b9ZfSRwVCVEeDYTrj7IjHlAKzGZf1GHt%2B0RU0%2FBIU%2Bgt5AnItceJU8GcvgPuQcfDp08PZ1CUGUG9yBntp2a0BHbObXdFsT3SCDOX7eTDSN4XHicKavPzJZwIWaizZRgVOyZxH%2BuxFp1eOcl%2BZ%2BGhLnAynzYHJoAY%2FOtNrPOFR5ZCF19B1dhJZGp2kmHEQU5vTPyCmkTXmeMg%2FEyF8DamiiwIwqSoXoCSIXcyHBWL%2BBL5eLcwH5H4mb3QLcmBEWOKDVd9SwG9IWzJwQEldX9m2gWSEiVTgEGrc9cw%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i3/32791316/TB2MVPEdPgy_uJjSZR0XXaK5pXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>108.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="新款波西米亚水墨印花长裙大摆雪纺连衣裙">新款波西米亚水墨印花长裙大摆雪纺连衣裙</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">惠优衣坊</span> 
                    <span class="payNum">3人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.5</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                
                                   <li><span class="lessthan">如实描述:<b>4.5</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                
                                   <li><span class="lessthan">服务态度:<b>4.6</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                
                                   <li><span class="lessthan">发货速度:<b>4.6</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=569&amp;e=wZ2kvnJd8o2NblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFNGFPFJGI72J26TEC%2BxXQqdlYaeJ11qFWRlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAlGnYnqP8PeYJVVbRVda3BVqllIQdmSPrPMB9VZeGNOOZA7Lb%2FV2evr0kcFQlRHg2IkeN0qcvdVP4qv32Jv%2F7HBJN0T8NHzJhY%2BYwGOry043DJiU%2B0OxApLius9MhfhqZ6Lb3P3XwUnY13RbE90ggzl%2B3kw0jeFx4nCmrz8yWcCFmos2UYFTsmcR%2FrsRadXjnJfmfhoS5wMp6wLAJhY0fK8D5j%2BIauX7sCpKhegJIhdzIcFYv4Evl4s5bTi1yTRRLhexD5kf4UNPYIYpc0Np05pvccBuKh6Hww%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i1/103167878/TB2IiztaY3nBKNjSZFMXXaUSFXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                     
                        <span class="pricedetail">&yen; <strong>23.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="连衣裙女夏2018新款韩版宽松时尚气质优">连衣裙女夏2018新款韩版宽松时尚气质优</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">mdm251803059</span> 
                    <span class="payNum">0人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">5.0</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>5.0</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>5.0</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>5.0</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=569&amp;e=549g1Iy3sWmNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFOO6SUdKlWYpaHcdErS1VwDSKFWdb%2BtQdplK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAuETc02MkuA%2FAwp%2BRVHsRR3O1lszgjM4toiE53VD5qJjROJiCoAO%2Fj%2FF%2B%2BJMWculAHL6GhhnB7bEIqEQ4sWQnlEndWuabgBI6KhP1BfCXbfWTnvqf1XqoFh1qkU50ke82zdjWqYikv2%2BGMHwaFGvZKiWMiX7iRXnPnr6MoY9ZRSp51GtG4rzQNNJy7WdIi%2BSKGucjJ4fTSFkTwyzXcZKn3a3DsZErzyjYs7WWzOCMzi2wrg9aWB4Z45gTo1rSf1SwQmDfVBwCMVVi%2FCeo40U8spcsMa%2FKh72EQ%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i1/128437000/TB2hkD7dx1YBuNjy1zcXXbNcXXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>2580.60</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="春连衣裙女2018时尚淑女新款两件套">春连衣裙女2018时尚淑女新款两件套</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">岱格丽旗舰店</span> 
                    <span class="payNum">0人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                    
                        <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">5.0</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>5.0</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>5.0</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                    
                    <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=569&amp;e=vcA2HQZN9zCNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFPSzNJKFP9quxPXhOUiRjKekIACgAchdetlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAlGnYnqP8PeYJVVbRVda3BVqllIQdmSPrPMB9VZeGNOOZA7Lb%2FV2evr0kcFQlRHg2AYa2rXLNhXdW%2BhW1xw3Tii%2BuUZVYux5f2QBQe%2Fw4e%2By3aQvg8FB%2BnYdA11TJ77asqFHe75W94CN13RbE90ggzl%2B3kw0jeFx4nCmrz8yWcCFmos2UYFTsmcR%2FrsRadXjnFPjsZ5U0U8qOxxAlwEjS7SvT8lC6eLogCpKhegJIhdzIcFYv4Evl4s5bTi1yTRRLmKxbNuxXzEpVTOhw2NaScGxcKw0uXGs0A%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i2/127405113/TB2jsvMdgaTBuNjSszfXXXgfpXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>59.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="女款夏季新款显瘦2018短袖夏装气质过膝">女款夏季新款显瘦2018短袖夏装气质过膝</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">刘家家服饰</span> 
                    <span class="payNum">3人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.7</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=641&amp;e=8EhhsTLDSSKNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFNg8EyXfpJZ1heStqsTQx276BF%2FtZQar3dlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAn8EGBrJ9VHKiF1i7Vpw2UUybraxWi1TZnDdmWpu0ze74S1%2BopEVBlRkfHCYt7Vlqi56xghqF%2B46qkALid6IRjlE4mIKgA7%2BP0SjnGJCeWDJVnH9bgG4wYo2t0IU1pBvqfTcB9emrIIbxudzgVjiL2Z2hZpP8S1aQsgQT2ndrFcKN2NapiKS%2Fb4YwfBoUa9kqJYyJfuJFec%2Bevoyhj1lFKnnUa0bivNA00nLtZ0iL5Io76b9UFSbotsObvub18tsoUfCfTtYyUwbqC8JukPLCRciI3E20nPdbv5dRelCjV1afk7HH9GARiPO1lszgjM4tpWDGZ9oQnl5LYaMVchXKmlLVnfkMdSmJdcXvoksJxpC" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i1/56806980/TB2DJ.Ha4SYBuNjSsphXXbGvVXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>129.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="歌施兰2017春夏波西米亚松紧腰长裙大摆">歌施兰2017春夏波西米亚松紧腰长裙大摆</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">歌施兰旗舰店</span> 
                    <span class="payNum">0人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                    
                        <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.8</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                    
                    <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=621&amp;e=y5h1MyzvKYSNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFNqkxq38iRj2bpFvTnBGV8tBD%2FgyNWMTW1lK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAhjgQxKvSk2WvtyBLhtx4kzB4NaWZ04CSAasWF5Ct0AVJShbkS7xwKmuuW%2BlivNlfjxn6zvj9rGoymlCGW1zohtZkDPKdIp6mMWlHmacREn1W4M1wUrwL6WEvoyAQAF4HJrthbo6gnXvQmBqo052e8uGXAUv9bWF2k%2FWTk4F7CxtbMY6aNiKpIX2AD2b7C6%2F%2BFaoFiKnEBclqnngaLQ1RdrWLyPg0FMbklz9DovekU5zB5PsHrkHTt0LLwazeQ8%2BctkJbXgOQFYw%2BMeiRgsNUnAWfGlypsu4mMQgs0RBp4QAdiuuMx2PLaFrw60AT25CWr5TYjQd8WhJCZe7iR4TRhE%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i2/113384267/TB2_ESZe3fH8KJjy1zcXXcTzpXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>99.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="2017海边度假夏秋沙滩裙雪纺波西米亚长裙女">2017海边度假夏秋沙滩裙雪纺波西米亚长裙女</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">宫廷衣装</span> 
                    <span class="payNum">116人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                        <span class="icon"><span class="icon-golden"></span></span>
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.8</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                    <span class="icon"><span class="icon-golden"></span></span>
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=569&amp;e=O8fisbgtWl%2BNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFN5eIC%2Bi2gYGHOfnGldNEggMeOU4z9XAVJlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAlGnYnqP8PeYJVVbRVda3BVqllIQdmSPrPMB9VZeGNOOZA7Lb%2FV2evr0kcFQlRHg2PVDrEQTLBZeCcJlDDpzgiXx2dArSewMD37g6iJbhqaBxmTkMnM57oNHhbEQP%2BbwKfkI%2B0alPjXvld4vUxOGWv5zhxSGDEp4ZKaXjrWQ%2BGHH8UXy73YaeLici1LcOifyUexsv0rikoEJfVCtdL%2Fv5wTfnzHxwxicUn6BcQvmGzsPurdjlfPGvKHU1kWDeYOnwfNCTVfH0T9HYBflCpTOb7D%2FbIyHZWCKqg%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i3/30816026/TB2RXdZf.R1BeNjy0FmXXb0wVXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>59.99</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="连衣裙韩版2018女装中长款喇叭袖碎花百褶裙">连衣裙韩版2018女装中长款喇叭袖碎花百褶裙</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">小宅女大购物</span> 
                    <span class="payNum">112人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.6</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                
                                   <li><span class="lessthan">如实描述:<b>4.6</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                
                                   <li><span class="lessthan">服务态度:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                
                                   <li><span class="lessthan">发货速度:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=621&amp;e=Kc4GWjBRSfiNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFN7XSSEolpICTU7owO0p6j%2FyJsjq7yIOTNlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAlGnYnqP8PeY3g9HUIorPp6uuW%2BlivNlfk39GhC664ejCvvb2BeYGacmHEQU5vTPyDM94qXBOf5silpva1sR0%2BiCHXfMBduN4DgdksHn2m2jAXs4TRnFkQjtApTdkQPLmalGKTuUF3BbX2oGYYhIzNRP2abE4asmPIbJTTVz2LoxGNvKaMbL8RH1a4IWjlJjlhckZMQsLspgI4dlC6OgE9KYho0DuJ7YHYIdd8wF243gi0PRBOD3gLkDv5xQtt%2BxxA8MN9OfK9Y1A6MXZ0oNmvx%2FB%2BCOEDDo9MhfA2poosCMqr3BKF8PQrrdtQIt5URcooHq%2Btj5WsisfwQl%2BS%2FDAic%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i4/29667898/TB2KPS0b9BYBeNjy0FeXXbnmFXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>299.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="雪国天娇2017夏季女装新款雪纺无袖修身">雪国天娇2017夏季女装新款雪纺无袖修身</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">雪国天娇服饰旗舰店</span> 
                    <span class="payNum">1人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                    
                        <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.9</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                    
                    <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=577&amp;e=U6KkvafyjUONblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFO5NnaMvBaI06eMbJtjkJqwow38TYiKocNlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAlGnYnqP8PeYJVVbRVda3BVqllIQdmSPrPMB9VZeGNOOZA7Lb%2FV2evr0kcFQlRHg2B81Ff79J1YAgKI9o%2Fsb8K8L1dQ3Tt6Xc3Kpn55DWNuYztdVkxo8O3KaWHfivk4JrlJKx5gfOZSA13RbE90ggzkpUA8C0b0HJT8yvMaqv6Ovay9oRtWhUG9ksbeTWq%2BaffFF9Zs1X%2By9HzUV%2Fv0nVgAzzxNihVZefFGnYnqP8PeYJVVbRVda3BUjsd9l4XLXsUQrOpM58Xpaak9Ey%2B0jtE3cfn5OEr5wcL%2BgSQ6CKrN2" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i1/119517956/TB2t.UtfwmTBuNjy1XbXXaMrVXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>179.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="心机性感黑色女神范拼接网纱中长款连衣裙仙">心机性感黑色女神范拼接网纱中长款连衣裙仙</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">月半迷城旗舰店</span> 
                    <span class="payNum">3人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                    
                        <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.9</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                    
                    <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=601&amp;e=k9HVDQMYq0eNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFOwMV0rTcwlkXReg8mVwopC53kt9QABySNlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAgasWF5Ct0AVe551xPP0CYbfnXbyHSbRwFGnYnqP8PeYJVVbRVda3BWViNY%2BG3b9ZfSRwVCVEeDYm23wkpQNOa%2FVH6HeLBF%2BRS1KOkGjBSsMjAi8XFEeETc9wmKI1%2FE3YIOV2zqhwZGYb8O%2BKzoDPEPXdFsT3SCDOSlQDwLRvQclPzK8xqq%2Fo69rL2hG1aFQb2Sxt5Nar5p98UX1mzVf7L2bbfCSlA05ry1l%2FqHBXWDU35128h0m0cBRp2J6j%2FD3mCVVW0VXWtwV1cIdFzGvh6PgVycUAflLXrw7KIvB4PhkHhjR38%2F6DxpvZaeqdKn%2BIA%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i3/43511796/TB28W.8X4GYBuNjy0FnXXX5lpXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>285.00</strong></span>
                     
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="小清新女装卫衣吊带裙两件套连衣裙风琴裙摆">小清新女装卫衣吊带裙两件套连衣裙风琴裙摆</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">seatosky旗舰店</span> 
                    <span class="payNum">11人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                    
                        <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.8</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                    
                    <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=601&amp;e=fT1LpfEuNoKNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFPHpkQgSoYyKM35nnCr5%2FWU5MqSpagut1hlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAgasWF5Ct0AVe551xPP0CYbfnXbyHSbRwFGnYnqP8PeYJVVbRVda3BWViNY%2BG3b9ZfSRwVCVEeDYKGF%2FAG5YWUBjNrgPQ4HGXbmRfwRU0onPj1Pj8HZyOj%2Bo%2Fxd4VkTh2Bhtw4MIZoxxsaRBS9r9Tu1P1k5OBewsbWzGOmjYiqSF9gA9m%2Bwuv%2FhWqBYipxAXJap54Gi0NUXaSTq54%2Fs%2FMwn0YKVs1xTYf%2FzoPJUrlUc33NyP0UpKI1tDirEkqHPQzXfFk3R0N1pt2o1VOlG3MrxwWBy5D5EeOfAZ21tMl%2FxbTiC2llyqpK7hvc1qqXK3tw%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i3/1565806014578120043/TB24K.qlbFkpuFjy1XcXXclapXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>268.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="两人故事民族风连衣裙中长款复古大摆吊带裙">两人故事民族风连衣裙中长款复古大摆吊带裙</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">两人原创</span> 
                    <span class="payNum">4人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                        <span class="icon"><span class="icon-golden"></span></span>
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.7</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                    <span class="icon"><span class="icon-golden"></span></span>
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=653&amp;e=coxV9YZFWtyNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFNtlVcOmj2VIMDi%2BcoGBRjfThSMcKFlfR5lK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAt87SzxT4aycl87F0NdOtVUNYaRZrPyMb1GnYnqP8PeYJVVbRVda3BUjsd9l4XLXsWX8qh93ux6MR%2B8KrZyWXNpE4mIKgA7%2BP%2B5HiPyg1yHMevGFaZuPHdQX76Shjkw1l59ZsZU4qT%2F1e2YmWeJqTsyR7xjoQcL18gQv39%2B9YstjN2NapiKS%2Fb4t3uKgwr2aS58d5h%2BCMTQSCgIyhnQkhHUjh2ULo6AT0piGjQO4ntgd39vtJwSmFiR1qa4l2FRTO2KqwrB46c2BEfibOfe8n0ooMbc55%2BD6%2FwUSiUnbxu8syF8DamiiwIwqSoXoCSIXcyHBWL%2BBL5eLDFP0NUwAg8rBw%2BL1nk95PM6k1Tjw24Rbv6BJDoIqs3Y%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i3/97369656/TB2TxQvfYSYBuNjSspfXXcZCpXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>79.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="2018雪纺连衣裙夏季30-40岁妈妈装印花长裙">2018雪纺连衣裙夏季30-40岁妈妈装印花长裙</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">13682298392baby</span> 
                    <span class="payNum">14人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.6</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                
                                   <li><span class="lessthan">如实描述:<b>4.6</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                        
                            <li><span class="morethan">服务态度:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=569&amp;e=bQDkm4RiU1ONblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFPSzNJKFP9quxPXhOUiRjKeVvLbif5C2GtlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAlGnYnqP8PeYJVVbRVda3BVqllIQdmSPrPMB9VZeGNOOZA7Lb%2FV2evr0kcFQlRHg2FQE0iVT6%2F6sNz5CUfrWegdiOho%2Bjon0XW%2FZQvaaFH77Yy0ndv4besKo3qxh1ZCAlveI4qEtIKGC13RbE90ggzl%2B3kw0jeFx4nCmrz8yWcCFmos2UYFTsmcR%2FrsRadXjnJfmfhoS5wMpNfLBAcjLS%2ByWm%2F6dV41y3ypKhegJIhdzIcFYv4Evl4s5bTi1yTRRLoECYvTLpIXTw3DyYuRrLe2xcKw0uXGs0A%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i1/127405113/TB2DNx9iAOWBuNjSsppXXXPgpXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>59.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="2018夏装bf仙气长裙森女学生原宿风">2018夏装bf仙气长裙森女学生原宿风</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">刘家家服饰</span> 
                    <span class="payNum">0人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.7</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=621&amp;e=IOa3V4Qm0lCNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFPzH2tn0RRL8Hg6ZgIQIMMZLtgFMOmaavJlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAlUtwMxFhna7n1tXGEIKl5vJUv6u6OD00KC9FBulM27Pp8VK8YWQkVZl%2FKofd7sejEfvCq2cllzaROJiCoAO%2Fj%2Bbo4HYrgjWJncZIDvTsMEE2TRSdfM8sAPOblOauRJ1C0pXyeiw5Wa8reLgGttKc5wI%2Bm%2BHVDq8cIbJTTVz2LoxBQEyxp4FgYwLK1q0%2BYIKxWsvaEbVoVBvZLG3k1qvmn3xRfWbNV%2Fsvankr8vuKMQf1P5WC0cfQg1SvmpQ5Z1pJkt4DsLfz67hYY3JaFDRRjlDirEkqHPQzXfFk3R0N1ptBYaiWd2kNs0JyGfz26TYwNjPwDWcBlG9rtmg1hLvh2c%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i4/1176406035160439869/TB29X4ioNdkpuFjy0FbXXaNnpXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>92.00</strong></span>
                     
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="新款性感挂脖露肩优雅长裙露背系带连衣裙">新款性感挂脖露肩优雅长裙露背系带连衣裙</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">wildjtl</span> 
                    <span class="payNum">243人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                        <span class="icon"><span class="icon-golden"></span></span>
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.7</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                    <span class="icon"><span class="icon-golden"></span></span>
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=569&amp;e=jppGJdKkWoyNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFO1HKKDsfThI%2Bwy%2BJ4WE3dML5qqhY%2FmmP5lK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAlGnYnqP8PeYJVVbRVda3BVqllIQdmSPrPMB9VZeGNOOZA7Lb%2FV2evr0kcFQlRHg2DkTdwS51GLuEGIfJ8oG99%2B8HGO3FGsZLecvp5w5Iq%2FmaNNyRtSo2m7J75TLMsJ0LOPts66lWwIY13RbE90ggzl%2B3kw0jeFx4nCmrz8yWcCFmos2UYFTsmcR%2FrsRadXjnJfmfhoS5wMpUr%2FZbtbegG%2FvmX%2BupD%2BQtypKhegJIhdzIcFYv4Evl4s5bTi1yTRRLlj%2BfPXccdSoh0qCA%2Fxb7jfdlnrBW8CeTA%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i2/130575885/TB2oxf3hbuWBuNjSszgXXb8jVXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                     
                        <span class="pricedetail">&yen; <strong>46.99</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="2018春季韩版喇叭袖单排扣长袖连衣裙女">2018春季韩版喇叭袖单排扣长袖连衣裙女</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">hello橙子1</span> 
                    <span class="payNum">0人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.6</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                
                                   <li><span class="lessthan">如实描述:<b>4.6</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                
                                   <li><span class="lessthan">服务态度:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                
                                   <li><span class="lessthan">发货速度:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=609&amp;e=txkYILjGL0qNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFO3qbtThSVo6MuXC9LwmiYVXp7LD51GE75lK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAm%2BsAPHmvWQuomN%2FGgzJB7HK26R1lZGI6V376inIgDq5jv6yX%2BqG01K11i3F9hzzNoXsehxk5pCxqsT6laMdQ3X02maYDgztZKx0u3%2FsB5UCUuirXKT1oGsVljotv5A8Uy4aTh9VSUAu8o%2FHN6j0gWF9uonHdIxY2YbJTTVz2LoxGNvKaMbL8RH1a4IWjlJjlhckZMQsLspgI4dlC6OgE9KYho0DuJ7YHfTaZpgODO1knenf43CdqdIc%2B5ChDYMk0fAE0lf2Bm%2FJ86M8OkfTERtOT3eUDOvP3MqRrJcAfxhMHth6SeXZJJcyoGEctvZbP0EeVbD0P2Qd" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i1/32148518/TB2dPP3c79WBuNjSspeXXaz5VXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>498.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="真丝旗袍连衣裙2018夏新款蕾丝奥黛改良短袖">真丝旗袍连衣裙2018夏新款蕾丝奥黛改良短袖</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">唐奕服饰旗舰店</span> 
                    <span class="payNum">137人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                    
                        <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.9</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                        
                            <li><span class="morethan">服务态度:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                    
                    <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=537&amp;e=wZ4gOZlOTSGNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFPL21qRPDCX2oq1wV%2F5UtRdW2%2FchdRDVz9lK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAhkfAsRta6OBM46rnCeezlxrosTkIRof7nHfuWcSOlrrEtPuUm1K1%2F9iDLGIabdAOphr1r9MdwWvqG7pCpI4siLhJN0%2BB73Ro4rq4dW6eP5%2FSjrB10wZ5xJP1k5OBewsbWzGOmjYiqSF9gA9m%2Bwuv%2FhWqBYipxAXJap54Gi0NUXarNpoWA14zwtx1AiOiyKO8CkDJDLcd1URO%2FdLlb8%2Bl5wQptme905LcRqLFMHB9NkVVfjp4UsHD9Kx90PhivTQbg%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i2/130854135/TB2BZPMiCtYBeNjSspkXXbU8VXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                     
                        <span class="pricedetail">&yen; <strong>139.00</strong></span>
                     
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="小心机v领白衬衫韩国时尚设计宽松长袖衬衣">小心机v领白衬衫韩国时尚设计宽松长袖衬衣</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">大花媛hh</span> 
                    <span class="payNum">115人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.9</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=569&amp;e=VOa77zSx4oaNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFNawp2ODDQGAWBAfb95uqbWp%2F8%2BrzDpVNRlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAlGnYnqP8PeYJVVbRVda3BVqllIQdmSPrPMB9VZeGNOOZA7Lb%2FV2evr0kcFQlRHg2LKLwVp%2B%2BaXGke9jJ9G6qVIAs%2FgGwUFnS5EVwUGhDpkyLnDUAUbJdHnjp969HMystxxawLAKJNqk13RbE90ggzl%2B3kw0jeFx4nCmrz8yWcCFmos2UYFTsmcR%2FrsRadXjnJfmfhoS5wMp3CCik5avQxcs63tmcd06CSpKhegJIhdzIcFYv4Evl4s5bTi1yTRRLun2Fz70SmdNxpc3M2K8OVncrN8FDzwRGA%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i2/118725532/TB2qTeejh9YBuNjy0FfXXXIsVXa_!!2-saturn_solar.png_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>1350.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="玛俪琳新款长袖雪纺显瘦方领纯色百褶连衣裙">玛俪琳新款长袖雪纺显瘦方领纯色百褶连衣裙</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">正品代购8188</span> 
                    <span class="payNum">1人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.6</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                
                                   <li><span class="lessthan">如实描述:<b>4.6</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                
                                   <li><span class="lessthan">服务态度:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                
                                   <li><span class="lessthan">发货速度:<b>4.6</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=577&amp;e=2dsmyc%2F8otiNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFOg%2FwL7ZGJUVk6AovMcROPYiB4W0FP88GZlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAlGnYnqP8PeYJVVbRVda3BVqllIQdmSPrPMB9VZeGNOOZA7Lb%2FV2evr0kcFQlRHg2Nf6x%2Fk5VPzy47F9aiHNsgc86l7EgWOgmUk9AcOx%2BILh7bLItJIF2bNsPp7iIr7O7zKJFUuorced13RbE90ggzkpUA8C0b0HJT8yvMaqv6Ovay9oRtWhUG9ksbeTWq%2BaffFF9Zs1X%2By91%2FrH%2BTlU%2FPIzzxNihVZefFGnYnqP8PeYJVVbRVda3BUjsd9l4XLXsXfRxZhzVmnsF0sSs43aumbUmnqNzUYl6b%2BgSQ6CKrN2" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i2/TB1XPurgbuWBuNjSszgYXH8jVXa_M2.SS2_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>588.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="2018夏装新款重磅真丝连衣裙宽松印花桑蚕丝">2018夏装新款重磅真丝连衣裙宽松印花桑蚕丝</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">真缔雅旗舰店</span> 
                    <span class="payNum">4人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                    
                        <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.8</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                    
                    <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=653&amp;e=UuT7AyTCg2iNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFPnUzdWkhckmfftfilKVBoq%2BcXVxiS8LLRlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAuYh7%2BQYo7NL4LSodO3LBZPC2jV6Ix8bRb0qe0wjAlKp6GwPPujrhnKyDhTgP3P2GNldQq9PgHIaox5CemGvyaMHjFsfOg%2B67Hkys6FPTnFOeNjkdF2c0VE9qa1rjGijMO1xzEY5Bx%2BqGUVi7B1DOMy0dHpuY3rVYaNZo7JPR0msxxmRdUF1elxpQUcP4rDCRauyzDaJa5j2JXbeHQ1kZMUX4zwYH%2FFAI6lHm0Oe692BWGlNnwQ6RJIdf%2BK3sXYXGVKmT%2B8FiK9IQ7I9u9LVZbk8vb549ZkQOcCFqyHqpCahXFT1K7e5uVJGEqALkUsUTdDaMXMEJ%2B5JrubaNyFnIxY35oQhNJaOgfi3szaUEKueqmzpfzdHyPY%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i4/117490519/TB2gVxqfA9WBuNjSspeXXaz5VXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>59.80</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="胖mm两件套格子连衣裙夏女大码200斤显瘦">胖mm两件套格子连衣裙夏女大码200斤显瘦</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">薛光贤炫</span> 
                    <span class="payNum">5人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.7</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                         
                            <li><span class="morethan">如实描述:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=589&amp;e=bpuScqAF2giNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFM5YedimHPpbU2UyTMs3HQ1u%2BRr2O%2BfY65lK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAgasWF5Ct0AVUoFhu2SdZPKfC8tUq5uW93%2BODv%2FfxT3W%2Fl1F6UKNXVqViNY%2BG3b9ZfSRwVCVEeDYgocQwwvg9kkLVf3%2F5a42ZrvoyLTmPmjmANtMzqvNaAujxx%2Fk9nG9dTYmacjg%2BrNcyHCbj8s1A9TXdFsT3SCDOX7eTDSN4XHicKavPzJZwIWaizZRgVOyZxH%2BuxFp1eOcl%2BZ%2BGhLnAylPCS46RF4k3SkrhnpgF2IByF8DamiiwIxbE1OEAWuvkrC9ovaYKln5Zd8fmSE190XLmzx7cHK%2FntHu4NZht3Wfi1keoUW5zm4%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i2/34689712/TB25YP0gf1TBuNjy0FjXXajyXXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>358.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="夏装刺绣V领羽毛连衣裙度假长裙吊带裙女">夏装刺绣V领羽毛连衣裙度假长裙吊带裙女</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">早起的小蜗牛53</span> 
                    <span class="payNum">8人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.8</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=589&amp;e=%2BCoXHNo%2FWvONblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFOTTUjYS5d2ovxxF2TeSdfcMu0by7pCLJFlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAgasWF5Ct0AVUoFhu2SdZPKfC8tUq5uW93%2BODv%2FfxT3W%2Fl1F6UKNXVqViNY%2BG3b9ZfSRwVCVEeDYLGYXI4tmtsv55cuuqloaKnDmXj1AdKcKmQ9NzKtHVt9dhrbnuEVkRC%2FDoQXogU6zIOFLK9i%2Bq7CV3i9TE4Za%2FnOHFIYMSnhkppeOtZD4YcfxRfLvdhp4uJyLUtw6J%2FJRgZaXLF6OMeABgvai2kUvFpPy2H5eCBVeAfsjJYaiTPn%2BXUXpQo1dWtXCHRcxr4ej4FcnFAH5S14aXRo%2FhQuSKhTXlHJ4RG%2BjU3lVJWRpmkQ%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i4/17000238/TB2_nCDabsTMeJjSszhXXcGCFXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>159.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="沙滩裙海边度假波西米亚中长款吊带连衣裙仙">沙滩裙海边度假波西米亚中长款吊带连衣裙仙</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">jennny_2007</span> 
                    <span class="payNum">383人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                        <span class="icon"><span class="icon-golden"></span></span>
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.8</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                    <span class="icon"><span class="icon-golden"></span></span>
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=601&amp;e=a25%2FteOdu%2FGNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFOirGAT67FgPM2SSwwmFEnH%2FzXp3gXJX8dlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAgasWF5Ct0AVe551xPP0CYbfnXbyHSbRwFGnYnqP8PeYJVVbRVda3BWViNY%2BG3b9ZfSRwVCVEeDYHWziROjjVECLgUyFTwDsXhgyiJGBBM00N%2BBE5pcHUXFVGm998zMwX2f6DhNoQ76o3dlQrwIbs4GV3i9TE4Za%2FnOHFIYMSnhkppeOtZD4YcfxRfLvdhp4uJyLUtw6J%2FJRFXleKOrf5Tr43GKrBc9mIoiXTk6UU01vgaGmOYITa8J%2BgXEL5hs7D7q3Y5XzxryhBqxYXkK3QBWj%2FNA%2Flp36i9Zy8bCCDTUt1saRAgwFsjnc0HSPu1nGHw%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i3/1023406072190442635/TB2t0QKuxXkpuFjy0FiXXbUfFXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                     
                        <span class="pricedetail">&yen; <strong>95.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="2018夏明星同款连衣裙中长黄色露肩吊带长裙">2018夏明星同款连衣裙中长黄色露肩吊带长裙</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">周牧薇</span> 
                    <span class="payNum">2人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.3</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                
                                   <li><span class="lessthan">如实描述:<b>4.3</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                
                                   <li><span class="lessthan">服务态度:<b>4.4</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                
                                   <li><span class="lessthan">发货速度:<b>4.3</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=601&amp;e=rUpE5R6lwvWNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFPaAF9hY1KFsYjFlgTxCifTGwU6je7f2Z1lK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAiZjPFISSa3jt9GbRww8Aqt%2BgXEL5hs7D7q3Y5XzxryhvPwY2CJh1MKy09h%2B2RyDcP5w651d5C91RBYELz115SKv8ekxQJ%2FFTWc3uSAVwd6baFM0Za5Jlf2mWRd1zy7VdAkegtHJnv9Fq%2Bv9uVwmuEFBqtxGTCxbc9LBFyaJnTroHeFqc5xSBhgmUwNpAAA0EVaoFiKnEBclqnngaLQ1RdqtO0DfEXeHH6%2Fx6TFAn8VNulQYk7JpFORxhMb5Mu7jQU3zYQxxJMgwlR%2FwVN%2BL7EP6hy4zgvZm8pZ132liM0nNMqBhHLb2Wz%2BUaoVY6PavDQ%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i1/32794171/TB28FhjbSCWBuNjy0FhXXb6EVXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>752.00</strong></span>
                     
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="OBEG/欧碧倩飞飞袖收腰显瘦连衣裙">OBEG/欧碧倩飞飞袖收腰显瘦连衣裙</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">obeg旗舰店</span> 
                    <span class="payNum">93人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                    
                        <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.9</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                    
                    <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=569&amp;e=flFuZ986LW%2BNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFOLLey3jt4JMxWgrrpvyNFmb0muPoX3dnBlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAuETc02MkuA%2FAwp%2BRVHsRR3O1lszgjM4toiE53VD5qJjROJiCoAO%2Fj%2FSSj3VVSPhBo%2F79KaliU8i0gVG2FKBen1Hw00U5mS1jwvxOP9yunSUr9xWk3hTlWtMJnS3TzQY3zdjWqYikv2%2BGMHwaFGvZKiWMiX7iRXnPnr6MoY9ZRSp51GtG4rzQNNJy7WdIi%2BSKO2EDZZWN5zeKAzE0FLPm0m3DsZErzyjYs7WWzOCMzi2wrg9aWB4Z47dod4oB9LpZP3sYutmu79t5tTFXPx1m8z0Q%2FH%2BWJ%2BwMA%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i1/1420206096231301116/TB2j9KqcHAlyKJjSZFwXXXtqpXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>305.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="2018春装新款女装长袖金丝绒连衣裙小黑裙">2018春装新款女装长袖金丝绒连衣裙小黑裙</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">missgama旗舰店</span> 
                    <span class="payNum">25人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                    
                        <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                        <span class="icon"><span class="icon-ju"></span></span>
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.9</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                    <span class="icon"><span class="icon-ju"></span></span>
                    
                    
                    <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=569&amp;e=Wt5wZqphfw6NblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFPQA5kY3GkEje80pHQfMv6DWwYVUq9CzfdlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAlGnYnqP8PeYJVVbRVda3BVqllIQdmSPrPMB9VZeGNOOZA7Lb%2FV2evr0kcFQlRHg2LjYw%2FyIKdwWeKSqZuzrJipoZV5M%2BLn6aeEveis0MxhE%2FiBIqhXngirzqTRF9EfY8S65V%2BKE4FBzld4vUxOGWv5zhxSGDEp4ZKaXjrWQ%2BGHH8UXy73YaeLici1LcOifyUcMztCpJXIfevQ9AhTcr20PfnzHxwxicUn6BcQvmGzsPurdjlfPGvKHU1kWDeYOnwfR1rDzlNA47TMRVdELVfR821uACiuv2Xw%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i2/1037506053155847458/TB2zEMcrrtlpuFjSspfXXXLUpXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                     
                        <span class="pricedetail">&yen; <strong>98.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="2018夏新明星同款黄色吊带连衣裙百搭长裙">2018夏新明星同款黄色吊带连衣裙百搭长裙</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">潮流前线_201265</span> 
                    <span class="payNum">0人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.2</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                
                                   <li><span class="lessthan">如实描述:<b>4.2</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                
                                   <li><span class="lessthan">服务态度:<b>4.3</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                
                                   <li><span class="lessthan">发货速度:<b>4.1</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=589&amp;e=nG5QvhPlqBCNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFOPXW1WFn%2FL%2B8nn2zBPdMSnGz%2FVNwkJxeFlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAi56xghqF%2B46%2Fl1F6UKNXVrVwh0XMa%2BHo0M4M74OYKIziITndUPmomNE4mIKgA7%2BP18pAUcfZujN7oYubX8Rrl07ZlcH7tCaCGAoNfPX1TLJmUHdz27hzNTT%2BW9dFrpXnYhCrq7S808XN2NapiKS%2Fb4t3uKgwr2aS58d5h%2BCMTQSCgIyhnQkhHUjh2ULo6AT0piGjQO4ntgdGdCejyK%2BXW5%2BwnlBqnprn6XzeZ3IL1U3EmGhDZodnlwtHaGBT2cJZbcE1DZ9sfB3z4FOfCTIA20IsOrN76bsI0aHJLC2xDKKv6BJDoIqs3Y%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i2/56296339/TB2IvwGaFmWBuNjSspdXXbugXXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>48.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="波西米亚长裙甜美连衣裙夏白色无袖拖地蕾丝">波西米亚长裙甜美连衣裙夏白色无袖拖地蕾丝</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">小豆淑女坊</span> 
                    <span class="payNum">68人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.6</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                
                                   <li><span class="lessthan">如实描述:<b>4.6</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                
                                   <li><span class="lessthan">服务态度:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                        
                            <li><span class="morethan">发货速度:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=557&amp;e=DUW%2BLAaspOyNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFOUVlxhJGwKgHdJvdbbyFvPKQiHyNzeTTRlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAk2ESNaMxWsaWxNThAFrr5ILoI%2Bz9tkeNLv7cSzSzJYzCGD1g22ffLOVcU4Q4L8l6xjzBBONVcMA3iaAOaC%2BjiT%2FkBSEaXmj7gFhTreZRJIZ74HsG2nLG%2BMWB9d4jJp3QJXeL1MThlr%2Bc4cUhgxKeGSml461kPhhx%2FFF8u92Gni4nItS3Don8lE59AjHgLIRF7otiv36eifznyvbU45Bq%2FhNhEjWjMVrGlsTU4QBa6%2BSr6EoYKGD9TMkiO5v%2BeMCtMK4CAY6B1HvKAZOT5AhO9Y%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i1/111478886/TB2lG62bRnTBKNjSZPfXXbf1XXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>129.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="性感吊带连衣裙长裙韩版女装2018新款潮春装">性感吊带连衣裙长裙韩版女装2018新款潮春装</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">鸿杉服饰有限公司</span> 
                    <span class="payNum">0人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                        <span class="icon"><span class="icon-golden"></span></span>
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.7</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                         
                            <li><span class="morethan">如实描述:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                        

                        
                            <li><span class="morethan">服务态度:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                    <span class="icon"><span class="icon-golden"></span></span>
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=557&amp;e=kjSYvsL9dsWNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFOBkCJAdYXye57GCuxCZFhbzmlZ71C1Lx9lK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAk2ESNaMxWsaWxNThAFrr5IPhYHiGeYoSEfvCq2cllzaROJiCoAO%2Fj%2FAt%2Bcc650Pjwu6epypzFE9M3Yms848JfoqYCOvJtazxrhMxUjhAo5vdb6kEyu6beKVH%2Fa74W7NEzdjWqYikv2%2BLd7ioMK9mkufHeYfgjE0EgoCMoZ0JIR1I4dlC6OgE9KYho0DuJ7YHT%2BEYqxI07amS%2B5zcPd%2B9G7H4M8OBVq%2BFHqNa3sGHCM8tR6lsf9e0zsllcUoJ0tRC9FJsNhObRNqXSwI4yoAYeE%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i1/117845998/TB2jXKEhVuWBuNjSspnXXX1NVXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>88.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="裙子春季2018新款女长款学生高腰显瘦连衣裙">裙子春季2018新款女长款学生高腰显瘦连衣裙</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">魅力坊服饰有限总公司</span> 
                    <span class="payNum">7人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.5</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                
                                   <li><span class="lessthan">如实描述:<b>4.5</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                
                                   <li><span class="lessthan">服务态度:<b>4.5</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                
                                   <li><span class="lessthan">发货速度:<b>4.6</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=601&amp;e=tFs9dQkNhmWNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFPzH2tn0RRL8LRe7XfOE9Nx%2BGJzMGkjGnxlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAgasWF5Ct0AVe551xPP0CYbfnXbyHSbRwFGnYnqP8PeYJVVbRVda3BWViNY%2BG3b9ZfSRwVCVEeDYscbiR3IPJX%2F1uSdivIRr%2FqFZQp8rWUTN0pJ%2FQNkgCEPzvLgaTTs1%2BqAwdutm2KfhFbwO64RfkHSV3i9TE4Za%2FnOHFIYMSnhkppeOtZD4YcfxRfLvdhp4uJyLUtw6J%2FJRoykxGNLVor925NHK3BM9gtn7FDy28giigaGmOYITa8J%2BgXEL5hs7D7q3Y5XzxryhBqxYXkK3QBWj%2FNA%2Flp36i2jbZcriPlwiaCkBxCvS3Kj8ujI8sLQmwQ%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i3/1176405011141446504/TB2viPdeShlpuFjSspkXXa1ApXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                     
                        <span class="pricedetail">&yen; <strong>185.00</strong></span>
                     
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="高腰大摆格纹系带印花灯笼袖蝴蝶结连衣裙">高腰大摆格纹系带印花灯笼袖蝴蝶结连衣裙</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">wildjtl</span> 
                    <span class="payNum">1人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                        <span class="icon"><span class="icon-golden"></span></span>
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.7</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                    <span class="icon"><span class="icon-golden"></span></span>
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=569&amp;e=VE4T8WLIQcKNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFPzZQkkvyb0IxcdItbJaVJ0wgZ%2F0JU5ZLxlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAlGnYnqP8PeYJVVbRVda3BVqllIQdmSPrPMB9VZeGNOOZA7Lb%2FV2evr0kcFQlRHg2Agyt3mMkpEXFVZq4Zzy4PFhopEIki5u4Yyg7aUF26uxqyU3SSfqsYnwttk7ltqWnmV96KS9WpOe13RbE90ggzl%2B3kw0jeFx4nCmrz8yWcCFmos2UYFTsmcR%2FrsRadXjnJfmfhoS5wMpcT7dQ4T0z4XvmX%2BupD%2BQtypKhegJIhdzIcFYv4Evl4s5bTi1yTRRLm7bAQimB1yOYrczSpr%2Byv4MPAoa5LqDwQ%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i4/110348144/TB2Fw65fXOWBuNjy0FiXXXFxVXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                     
                        <span class="pricedetail">&yen; <strong>599.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="新款春装女桑蚕丝刺绣长袖松紧腰修身连衣裙">新款春装女桑蚕丝刺绣长袖松紧腰修身连衣裙</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">拜占庭的森林</span> 
                    <span class="payNum">27人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.8</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=697&amp;e=VU3UecYR1NeNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFO1mq7XkTiR6VkFP2VEP%2FwXdP1DDogrDzNlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAn5GuhUWgnfw2b%2Fi7ijztxHJUv6u6OD00KC9FBulM27Pce4vOfTLuD1kfHCYt7Vlqsl0%2F2F6foAnWkiA6OtnMEYeClbwuPCh3n%2BTZmtJGGAxt4DgakVgWDMIYPWDbZ98s9dHB2WsJ7aihA9UPp6T%2F5077kXjiWg7avG%2FcGNJ9uY88hDXtmYeb99niE396CzpGraIV7bVStBVld4vUxOGWv5xgAzjlASML9JGnU8JrOkFmos2UYFTsmcR%2FrsRadXjnJfmfhoS5wMp10cHZawntqK0Lzc0KPSp1NJ2WkWll2IEx9evDuJAJNhKUV3RNEJSrURJDjNW4J5TYY3JaFDRRjlDirEkqHPQzXfFk3R0N1ptsfKvFijb%2FfKS%2Fdz61qmDU8P32ORhcZHO7mI7cF6U5tjA1Kw5XXtG7g%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i3/123356239/TB2h5mjhxWYBuNjy1zkXXXGGpXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>88.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="碎花雪纺连衣裙荷叶边不规则中长款吊带裙子">碎花雪纺连衣裙荷叶边不规则中长款吊带裙子</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">依辰美旗舰店</span> 
                    <span class="payNum">18人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                    
                        <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.9</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                    
                    <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=569&amp;e=%2BmA%2B35aL2g2NblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFO8QGxYIch7kDneunkClOWrm74APcDdi55lK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAlGnYnqP8PeYJVVbRVda3BVqllIQdmSPrPMB9VZeGNOOZA7Lb%2FV2evr0kcFQlRHg2BPLT3p4UPXA8b1I643S8HXV6WM0noNJrzQYy10gkUgIChQmEUr4qKwbBpK%2Fyz7ejUYFlH8%2BX8Zl13RbE90ggzl%2B3kw0jeFx4nCmrz8yWcCFmos2UYFTsmcR%2FrsRadXjnJfmfhoS5wMpA96WSZcTuSeaFgw3PdBXsipKhegJIhdzIcFYv4Evl4s5bTi1yTRRLp4B1v0wg9eqig7%2FF98FtK27%2BRZL87tmMg%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i3/113818458/TB27Odbi79WBuNjSspeXXaz5VXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                     
                        <span class="pricedetail">&yen; <strong>72.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="2018春装系带收腰裹身裙系带长袖衬衫连衣裙">2018春装系带收腰裹身裙系带长袖衬衫连衣裙</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">小肥外贸衣橱</span> 
                    <span class="payNum">0人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.7</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=589&amp;e=5kZ8mxAqboiNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFPn%2Bgdc1no3yeyV3jDqlyfO4diaK9kk3ztlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAgasWF5Ct0AVJShbkS7xwKmuuW%2BlivNlfiXKTZlyziS7lCWKZWIX6hVE4mIKgA7%2BP%2FZEo1p1q9R0vfDWWzd%2Bf0jsEOznbqyq5esdiy8IPsNbM%2BADqjZquv%2Fsnu41CqCJlusZYR%2B9gK2fN2NapiKS%2Fb4t3uKgwr2aS58d5h%2BCMTQSCgIyhnQkhHUjh2ULo6AT0piGjQO4ntgd0yD7FuBXnYCniE9O4nqeX9kJbXgOQFYwEmGhDZodnlxdwcuoQDF1x7cE1DZ9sfB3ispGpmDV3irjB6A7PjJWTpgH9vbJVwIUCZe7iR4TRhE%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i2/131257527/TB2C3QFiKuSBuNjSsplXXbe8pXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>134.40</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="女装ins仙吊带连衣裙网纱长裙复古初恋裙">女装ins仙吊带连衣裙网纱长裙复古初恋裙</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">qlh05041221</span> 
                    <span class="payNum">0人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">5.0</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>5.0</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>5.0</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>5.0</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=569&amp;e=FTaWVQ4OCYGNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFPIkXl2SAP2GcO3x%2FsIkWoikP91a0V9WEplK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAlGnYnqP8PeYJVVbRVda3BVqllIQdmSPrPMB9VZeGNOOZA7Lb%2FV2evr0kcFQlRHg2KwCzn4UOGfigc9609mxg6gkV4K50MORHr8SPGmAIyhyVa%2B%2BVeX4ZAW0XqA3yXnPk8Mm9CLw0aSz13RbE90ggzl%2B3kw0jeFx4nCmrz8yWcCFmos2UYFTsmcR%2FrsRadXjnPygdwiL5n5CApf6%2B5pHS%2BcoJqI68%2BegjCpKhegJIhdzIcFYv4Evl4s5bTi1yTRRLkxJt4teH5gADqQ9Ul2hxG66WRTqURo3pA%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i4/52559526/TB2wpCBbZLJ8KJjy0FnXXcFDpXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>85.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="女装2018新款春秋时尚淑女韩版百搭">女装2018新款春秋时尚淑女韩版百搭</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">bfqynifhv</span> 
                    <span class="payNum">1人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.5</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                
                                   <li><span class="lessthan">如实描述:<b>4.5</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                
                                   <li><span class="lessthan">服务态度:<b>4.6</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                
                                   <li><span class="lessthan">发货速度:<b>4.6</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=653&amp;e=yvKEOPOFCMONblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFOLsP9CexYec2EsC%2BRnCTqczBJ0juqtMWtlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAhiQDflkxY8xWch0YiuJclvJUv6u6OD00GX8qh93ux6MtOZb4NXvfCQgVVSidROS42aycvW%2FxnxHcWT8Ty%2FVFIhbsgTxD%2Fy4KythDDUBXP2ia60U0woB1d7SYstJTPC5T6whkzGtnirZ81TqKRajbOqu3TF44QqvZaU2qwbi7sQp%2Fl50QrV%2F7xKvlrIqZxujib9Rv3qqKFtGq62fzJE5ar0X4zwYH%2FFAI6lHm0Oe692B7XrGUP816REypnPYiLu4pn0KArMP%2FkP5NJVOda2sCyCa0T6XzpNLXlGnYnqP8PeYJVVbRVda3BXBaUbzTituyOmee2zX9UHUWsxktYQqtEJfaX2T13tCaNvfPZ2y%2BV7y08IhaEjhY7g%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i3/122504611/TB2mSCjaQZmBKNjSZPiXXXFNVXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>398.00</strong></span>
                     
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="oneanother 短裙夏连衣裙撞色 气质 背心">oneanother 短裙夏连衣裙撞色 气质 背心</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">anotherone旗舰店</span> 
                    <span class="payNum">3人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                    
                        <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.9</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                    
                    <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=589&amp;e=WNhEqbLkI0WNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFMKzsCafaBKZTGa0m%2BOiA4IJxYsgVVBs4RlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAgasWF5Ct0AVUoFhu2SdZPIjsd9l4XLXsWX8qh93ux6MR%2B8KrZyWXNpE4mIKgA7%2BP0TeqGxM3cw8ZLoyxo%2BKd14xN6EwYXjR6i5r%2FY9wm5PJWKEKAv50d%2F6FEktLJ%2FmeXNtgAfLSFktcN2NapiKS%2Fb4t3uKgwr2aS58d5h%2BCMTQSCgIyhnQkhHUjh2ULo6AT0piGjQO4ntgdSnIH81QGRMp0SKsdmKIS06XzeZ3IL1U3EmGhDZodnlwtHaGBT2cJZbcE1DZ9sfB3wQt1DrWvZ%2BsnNzCvDxsmVEsCmeCurW9Lv6BJDoIqs3Y%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i2/40995592/TB2QCdbjgaTBuNjSszfXXXgfpXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>168.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="夏新彩条针织连衣裙吊带裙防晒条纹长裙">夏新彩条针织连衣裙吊带裙防晒条纹长裙</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">潇峣仙</span> 
                    <span class="payNum">2人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.8</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=569&amp;e=clhrrZ9UNtiNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFM4PFO2R7SvWtV4L1f%2BhiGDHs5xHnSnsYRlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAlGnYnqP8PeYJVVbRVda3BVqllIQdmSPrPMB9VZeGNOOZA7Lb%2FV2evr0kcFQlRHg2BMbQ1ke4O82XPE%2FrfT3bTAHi72Sa6T6nFAP3jny2X4762nOJI1%2FWr6ssj7Ez0Xq%2BntrJFCVCgiF13RbE90ggzkpUA8C0b0HJT8yvMaqv6Ovay9oRtWhUG9ksbeTWq%2BaffFF9Zs1X%2By9ExtDWR7g7zZONZdbDWq56FGnYnqP8PeYJVVbRVda3BUjsd9l4XLXsePCCEPdzwxgzFnfB0JniGdohveC2uZy8w%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i2/30348240/TB2dNQ0bjQnBKNjSZSgXXXHGXXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>1600.00</strong></span>
                     
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="卡迪黛尔2018夏碎花真丝连衣裙V领雪纺长裙">卡迪黛尔2018夏碎花真丝连衣裙V领雪纺长裙</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">cadidl旗舰店</span> 
                    <span class="payNum">0人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                    
                        <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.9</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                    
                    <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=569&amp;e=NUvG7GfdCMKNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFP5eXGTGU1JBMySj%2FRIEMcPrlGiOYpvIM9lK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAuETc02MkuA%2FAwp%2BRVHsRR3O1lszgjM4toiE53VD5qJjROJiCoAO%2Fj%2Fn4OfgpF6U6Vjj2JYOYJnEzM21TVffIcrpjQy9dNza05YcP7QflzTo9t%2F4utGdP8DLpNoJ%2FSH2pDdjWqYikv2%2BGMHwaFGvZKiWMiX7iRXnPnr6MoY9ZRSp51GtG4rzQNNJy7WdIi%2BSKAWhB%2BkELSsBqn4Fa0DQz6G3DsZErzyjYs7WWzOCMzi2wrg9aWB4Z47vBcSt8XzAbfH8uZjGXbccPG8ydb8Ev4ERwAthEE6cLQ%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i4/109634624/TB2hFPdcb3nBKNjSZFMXXaUSFXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>2479.80</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="女装连衣裙大摆修身春2018女夏季新款复古夏">女装连衣裙大摆修身春2018女夏季新款复古夏</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">法玛莎旗舰店</span> 
                    <span class="payNum">0人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                    
                        <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.8</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                    
                    <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=569&amp;e=XR%2FGK%2BxgcVONblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFP5eXGTGU1JBMySj%2FRIEMcPBgprXO9QUPJlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAuETc02MkuA%2FAwp%2BRVHsRR3O1lszgjM4toiE53VD5qJjROJiCoAO%2Fj%2FerEYVpcSx74gLC8s2OA8LzM21TVffIcpQCyPXlbqw4ygQeJiwIZ1pK%2B55DouJAR%2FfRV%2F2VGVlsTdjWqYikv2%2BGMHwaFGvZKiWMiX7iRXnPnr6MoY9ZRSp51GtG4rzQNNJy7WdIi%2BSKEtGCSJjEj51Is4kcbzID2u3DsZErzyjYs7WWzOCMzi2wrg9aWB4Z45kqM8a1NWbqyQeN54atIoUPG8ydb8Ev4ERwAthEE6cLQ%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i1/109634624/TB21uJiahSYBuNjSsphXXbGvVXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>2709.60</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="连衣裙新春修身女裙ol春2018新款圆领拉链">连衣裙新春修身女裙ol春2018新款圆领拉链</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">法玛莎旗舰店</span> 
                    <span class="payNum">0人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                    
                        <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.8</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                    
                    <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=545&amp;e=GA2oktrv7DyNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFNsSj%2FJ%2FdEYYt1hOOb08HIP7BQPAIydwMplK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAuWEhyIibhueg8m5YUorz8%2F2zBxtuJva51uyBPEP%2FLgr4ou9Osm%2BuKHs8O9tSiQdLt%2BBRsC0tmflVcBv23IdcZTNKS4%2FVTFrWffiC%2FMZgWPnQDbD2EBNexYWST07UClKrkdKc5BPqcyunio26YzmG2aulBAE0UrXe%2BdRrRuK80DTScu1nSIvkihw360A%2FMR8n8hC82T6J7NRqNmIny%2B075I790uVvz6XnGHUdrEDvidKuZwexehe8xzK3Qn867ZGSqWKzK9YJUdk" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i2/32740589/TB2VU3fbCtYBeNjSspkXXbU8VXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>208.70</strong></span>
                     
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="于.momo 张.大.奕AL.U新款连衣裙nan.astore">于.momo 张.大.奕AL.U新款连衣裙nan.astore</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">wxyz_ing</span> 
                    <span class="payNum">22071人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                        <span class="icon"><span class="icon-golden"></span></span>
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.7</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                         
                            <li><span class="morethan">如实描述:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                    <span class="icon"><span class="icon-golden"></span></span>
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=665&amp;e=204qU6AoDd2NblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFO92yCyX%2BuUo6Rs8%2FpdcMn%2FiICAof8R5jJlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAhjgQxKvSk2WvtyBLhtx4kzB4NaWZ04CSMl0%2F2F6foAnNLoRFS1EVlPJUv6u6OD00AH7IyWGokz5%2Fl1F6UKNXVqViNY%2BG3b9ZfSRwVCVEeDY44x7po%2BJXzt7qIGB1P8The%2FEHokk9qWE6%2Blo61zi89aHBwYVM9vBk7k4coR7%2BPzlrXeq5m%2FLKVXXdFsT3SCDOSlQDwLRvQclPzK8xqq%2Fo69rL2hG1aFQb2Sxt5Nar5p98UX1mzVf7L3jjHumj4lfO3h2TlPwa%2FIATTJ5JJ3%2FOaXJdP9hen6AJ2U9%2FPLvde64rrlvpYrzZX5Rp2J6j%2FD3mCVVW0VXWtwVQCa8UrHesZ%2B1NoIh3jamwJVT%2FNofzeB6Bvnr90Fpw%2Frifdgmqu0y3Q%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i4/123695365/TB2ncTCfxWYBuNjy1zkXXXGGpXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>89.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="沙滩裙夏季雪纺吊带碎花连衣裙波西米亚长裙">沙滩裙夏季雪纺吊带碎花连衣裙波西米亚长裙</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">玛丽日记旗舰店</span> 
                    <span class="payNum">0人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                    
                        <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.8</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                         
                            <li><span class="morethan">如实描述:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                        

                        
                            <li><span class="morethan">服务态度:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                         
                        
                        
                            <li><span class="morethan">发货速度:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                    
                    <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=557&amp;e=b7FFdylVLRWNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFOh6CXJAB1UacsHoB%2FdeLJZ8ZaSWHHW3wBlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAk2ESNaMxWsaWxNThAFrr5IPhYHiGeYoSEfvCq2cllzaROJiCoAO%2Fj%2FZVbF8ODL9L7ZmsNrdEC1nCrkF3JD%2FVYoA2EKy7pKW0HNIW8P%2FKBZ%2B1XD1GfogIvoSHIssCklayjdjWqYikv2%2BLd7ioMK9mkufHeYfgjE0EgoCMoZ0JIR1I4dlC6OgE9KYho0DuJ7YHTTd7OY%2BC7ayl8lm7cWEhSjH4M8OBVq%2BFHqNa3sGHCM8tR6lsf9e0zv2dAqq%2FLdA4tkJsomR%2FLnizxkB9oEZLNg%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i3/115248305/TB21351grGYBuNjy0FoXXciBFXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>69.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="8新款韩版高腰显瘦V领印花荷叶边裙中长款">8新款韩版高腰显瘦V领印花荷叶边裙中长款</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">8号线专柜女装</span> 
                    <span class="payNum">5人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.6</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                
                                   <li><span class="lessthan">如实描述:<b>4.6</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                
                                   <li><span class="lessthan">服务态度:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                
                                   <li><span class="lessthan">发货速度:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=653&amp;e=nUVtoMcyJaCNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFMJIY3Oj31CED2SYF0EsTeSsatz2vIvdahlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAiNJ80%2BhDvhDG0Ed2ZNmOXVMPFs4YW0c4AVDK0yO8D%2BS2lzphWpIyTWcK7KlhM9gyOEtfqKRFQZUDQNYVL4M8j1bsgTxD%2Fy4K%2Biz0xtFUfW9lYDmoPgefmS5gR4QLbPS7ufd%2BYuk0eo4yQsQTYmtZmj1vpQh5sID26yhzMb1Ye9PFkk9O1ApSq6vlrIqZxujib9Rv3qqKFtGq62fzJE5ar0X4zwYH%2FFAI6lHm0Oe692BF2ABhulL6ftn2hfGmmecuTCB1%2Fy8K5PuIKKQwnsIxGq5VddC6bXUfVGnYnqP8PeYJVVbRVda3BVsOIRE9JiJh8wYqU2j6WBJWsxktYQqtEKL13GkwGUCj8TbT616EkZgvHaT2xGUp5c%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i2/60563529/TB2IHskiXuWBuNjSspnXXX1NVXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>169.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="中长款七分袖外搭针织连衣裙显瘦百搭长裙子">中长款七分袖外搭针织连衣裙显瘦百搭长裙子</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">上下左右旗舰店</span> 
                    <span class="payNum">101人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                    
                        <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.8</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                    
                    <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=569&amp;e=%2FeFJFromi22NblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFOO6SUdKlWYpZ%2BlENXphLLOrfEcRMyDfDxlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAuETc02MkuA%2FAwp%2BRVHsRR3O1lszgjM4toiE53VD5qJjROJiCoAO%2Fj9tcpJd3KL1CTBiTxLKmm7RIqEQ4sWQnlG5ULfHD4gG2JooaQzCtn%2FlYh5PYOfo%2FmJU8Rc9dh9h5jdjWqYikv2%2BGMHwaFGvZKiWMiX7iRXnPnr6MoY9ZRSp51GtG4rzQNNJy7WdIi%2BSKFaP4odkZ2fXlIRs2Yb40xy3DsZErzyjYs7WWzOCMzi2wrg9aWB4Z46pZTl0wr%2FldGwubPBrHNL9i%2FCeo40U8spcsMa%2FKh72EQ%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i6/TB1NI4wfTlYBeNjSszcYXHwhFXa_M2.SS2_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>2734.80</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="荷叶袖连衣裙气质女装长裙印花2018女夏春">荷叶袖连衣裙气质女装长裙印花2018女夏春</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">岱格丽旗舰店</span> 
                    <span class="payNum">0人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                    
                        <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">5.0</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>5.0</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>5.0</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                    
                    <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=557&amp;e=jx%2BcFMfwEXKNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFOgH6PgATG41uOLvx8Uz4vsfTEB0LN0xMBlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAuETc02MkuA%2FAwp%2BRVHsRR3O1lszgjM4toiE53VD5qJjROJiCoAO%2Fj%2ByeHbgy7ZlEspgD8wuNf3OfnwHZnpyKP9iLefxzDd7s2KUk28rkivyj%2B8cenqhXQNCzBIku4Vt74bJTTVz2LoxBQEyxp4FgYwLK1q0%2BYIKxWsvaEbVoVBvZLG3k1qvmn3xRfWbNV%2FsvX2NmAGobdKoOdPnJKvw2gNRp2J6j%2FD3mCVVW0VXWtwVI7HfZeFy17EeSG%2BWy3PdxO%2F9c5YUmA6uRGytdBXWSwE%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i2/10832134/TB2ZNLWjmtYBeNjSspkXXbU8VXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                     
                        <span class="pricedetail">&yen; <strong>1199.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="字母连衣裙裙摆长袖刺绣纯棉xsmoco春季">字母连衣裙裙摆长袖刺绣纯棉xsmoco春季</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">同心的记忆</span> 
                    <span class="payNum">0人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                        <span class="icon"><span class="icon-golden"></span></span>
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.8</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                    <span class="icon"><span class="icon-golden"></span></span>
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=577&amp;e=uCQCAaH7aDWNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFOT28bv0SAn%2FQvoZ7XRyUUG%2BL7otOfGAF5lK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAlGnYnqP8PeYJVVbRVda3BVqllIQdmSPrPMB9VZeGNOOZA7Lb%2FV2evr0kcFQlRHg2AxOA8iEex%2FsywmhM%2B5kGyvvCniOI2pCddPlPlNFQgcMbvRHQa5oRcrCBxJ%2Fib5qp10y8oe%2Fpzib13RbE90ggzkpUA8C0b0HJT8yvMaqv6Ovay9oRtWhUG9ksbeTWq%2BaffFF9Zs1X%2By9DE4DyIR7H%2ByxUjarnf%2B8SlGnYnqP8PeYJVVbRVda3BUjsd9l4XLXseiETggMViXpF2knk4Ch7K34DT1UjK3Sur%2BgSQ6CKrN2" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i3/122759570/TB2zCPxegmTBuNjy1XbXXaMrVXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>178.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="连衣裙圆领印花长袖带项链韩版宽松一步裙">连衣裙圆领印花长袖带项链韩版宽松一步裙</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">荷婷衣坊旗舰店</span> 
                    <span class="payNum">1人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                    
                        <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.9</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                    
                    <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=641&amp;e=N2VYid6SmjONblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFM1idnJ%2B5%2FFizaFavEl7uQg89yJ5%2FmY5y1lK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAuYh7%2BQYo7NL4LSodO3LBZPC2jV6Ix8bRb0qe0wjAlKp6GwPPujrhnKyDhTgP3P2GNldQq9PgHIaox5CemGvyaMHjFsfOg%2B67Ei1RGd7cpd0kZk4jreR7pPYQ%2BGh0ZBZ%2BDKNSHO0ppZM7VQXy59L36wx0Gu2rK0gWv1t%2BgWjrxzzN2NapiKS%2Fb4t3uKgwr2aS58d5h%2BCMTQSCgIyhnQkhHUjh2ULo6AT0piGjQO4ntgd8lcHQ2GC28fKSFk%2B1PPSoC6RdXcYDaS4Q7I9u9LVZblFYRL3aweuJQXOXG368duydh4YUl9BzIrQg1EjzJQTucLaNXojHxtFAzMkdCiXKWGzURD7bB7GcPBX4biZgvng" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i3/14538363/TB2X0Fddk9WBuNjSspeXXaz5VXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>89.00</strong></span>
                     
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="斤胸围七分裤套装两件套300 150">斤胸围七分裤套装两件套300 150</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">batfox</span> 
                    <span class="payNum">73人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.7</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                         
                            <li><span class="morethan">如实描述:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=601&amp;e=JZ2SKvjWQHqNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFPwOXEpmfcqqh%2FywttQMtdD3Cb1e13IqfdlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAgasWF5Ct0AVe551xPP0CYbfnXbyHSbRwFGnYnqP8PeYJVVbRVda3BWViNY%2BG3b9ZfSRwVCVEeDYVdj25fEgKhzhcYOQlZLgd7olxiHqig%2F0h6WONU8eK9JsVcZOGoM9XLc9JZIoPAbQ3mCJwxfbBCyV3i9TE4Za%2FnOHFIYMSnhkppeOtZD4YcfxRfLvdhp4uJyLUtw6J%2FJRJerWJm1JvioFQlAGnzTHKIiXTk6UU01vgaGmOYITa8J%2BgXEL5hs7D7q3Y5XzxryhBqxYXkK3QBWj%2FNA%2Flp36ixfImDjNuxffy%2Bs7DLbN9%2FxRwCXIaX9aMA%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i3/1691706045034835986/TB2U5egtypnpuFjSZFIXXXh2VXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>69.00</strong></span>
                     
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="淑女印花海边沙滩渡假吊带大摆中长连衣裙">淑女印花海边沙滩渡假吊带大摆中长连衣裙</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">大白日梦想家</span> 
                    <span class="payNum">0人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.7</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                         
                            <li><span class="morethan">如实描述:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=653&amp;e=L2N14kX2LpONblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFPGHbtqkPcQwqXGP8w9XzCjSHIcRhe6SA9lK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAhiQDflkxY8xWch0YiuJclvJUv6u6OD00GX8qh93ux6MtOZb4NXvfCQgVVSidROS42aycvW%2FxnxHcWT8Ty%2FVFIhbsgTxD%2Fy4K566XHNWDgAFA0EM3qHovYTZLtZjfKWI82Yl4hQAdTRL4BLdTxOs3cwbT%2BjpG2tyRxpbefRYApltFkk9O1ApSq6vlrIqZxujib9Rv3qqKFtGq62fzJE5ar0X4zwYH%2FFAI6lHm0Oe692Bvzp%2FZk3QcMCaUXfT7x3dpn0KArMP%2FkP5NJVOda2sCyCa0T6XzpNLXlGnYnqP8PeYJVVbRVda3BXBaUbzTituyOmee2zX9UHUWsxktYQqtEKE8Io%2BmPK2ug4%2FWscL4Kdv%2FhwTHSUebS4%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i2/TB15WMdfpOWBuNjy0FiYXFFxVXa_M2.SS2_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>588.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="onebuye晚白 春夏性感西装深v 领口 高腰">onebuye晚白 春夏性感西装深v 领口 高腰</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">onebuye服饰旗舰店</span> 
                    <span class="payNum">1人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                    
                        <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.8</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                         
                            <li><span class="morethan">如实描述:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                    
                    <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=653&amp;e=lGXFEoe%2FyyyNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFO0wBk%2Fw6h8aNH%2FnP5%2FzgH%2BwCd7XKO8401lK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAuYh7%2BQYo7NL4LSodO3LBZPC2jV6Ix8bRb0qe0wjAlKp6GwPPujrhnKyDhTgP3P2GNldQq9PgHIaox5CemGvyaMHjFsfOg%2B67O181S1phUOnNZbmXvwZGlysVP2v%2F7kl1JEK8NM%2Blvn6rxpTqxhcl%2FHIc%2BFuqDYFV9dcOMiQDsVpHjg3%2FGsG0ZVHSnOQT6nMrp4qNumM5htmrpQQBNFK13vnUa0bivNA00nLtZ0iL5IoMMQS5UYb12BCKK9B4gw76MTzQXH7vm%2F%2BhbtC%2BODlHC5Gp5RIsAukkIInNWZ3AKZwNbkrWs13jmXiCktHGPJT%2BQ%2FLqCOhPadtW6ap8%2Fqkaz6lMGpeTV%2BiYqwTMUAw8b7hu7AbBUYcncM%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i3/14695849/TB2fDUyi29TBuNjy1zbXXXpepXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>188.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="加大码西装胖mm西装马甲阔腿裤两件套200斤">加大码西装胖mm西装马甲阔腿裤两件套200斤</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">诺诺123654</span> 
                    <span class="payNum">18人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.7</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=589&amp;e=I5IvtNwCAC2NblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFOh6CXJAB1UaX5TO3yQkEGf%2B6zAbBl7fUBlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAgasWF5Ct0AVUoFhu2SdZPKfC8tUq5uW93%2BODv%2FfxT3W%2Fl1F6UKNXVqViNY%2BG3b9ZfSRwVCVEeDYHGVi1%2FREApzMXxcKXTlgZ9yMv6sjn7t9jMxtnBigXs5seghVYjYDkdkzwoA9Np4hOHmicuqdQbDXdFsT3SCDOX7eTDSN4XHicKavPzJZwIWaizZRgVOyZxH%2BuxFp1eOcl%2BZ%2BGhLnAykYiAg%2BwcVhu2DStW7CT4VLyF8DamiiwIxbE1OEAWuvkrC9ovaYKln5Zd8fmSE190VxN1%2BESQtGeLeCeA4HDOknSP9LBd9THZg%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i1/115248305/TB2sDnygxSYBuNjSspjXXX73VXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>75.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="8新款度假吊带裙高腰显瘦中长款短袖两件套">8新款度假吊带裙高腰显瘦中长款短袖两件套</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">8号线专柜女装</span> 
                    <span class="payNum">8人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.6</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                
                                   <li><span class="lessthan">如实描述:<b>4.6</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                
                                   <li><span class="lessthan">服务态度:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                
                                   <li><span class="lessthan">发货速度:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=577&amp;e=gZNw4Yflw%2FmNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFPBwzTT6qHHXD0r5SRkVLkX54KP4Mq5vNtlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAlGnYnqP8PeYJVVbRVda3BVqllIQdmSPrPMB9VZeGNOOZA7Lb%2FV2evr0kcFQlRHg2Go2Hv0Ahz0i8S9OKQvzVFI5cLKM%2BvNGhzlmCNE%2BC4u5YFbYA67KHO9bQTYnHr%2Bfh9skrwOhHA5Z13RbE90ggzkpUA8C0b0HJT8yvMaqv6Ovay9oRtWhUG9ksbeTWq%2BaffFF9Zs1X%2By9ajYe%2FQCHPSLq2niZ3QQE21GnYnqP8PeYJVVbRVda3BUjsd9l4XLXsR%2FmeFcoN0R7kwfG9NpNItVhUn0ueLhhKb%2BgSQ6CKrN2" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i3/114860126/TB2ffH9cuGSBuNjSspbXXciipXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>188.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="韩版收腰连衣裙中长款2018新款春装百搭">韩版收腰连衣裙中长款2018新款春装百搭</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">薰蔻旗舰店</span> 
                    <span class="payNum">0人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                    
                        <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.8</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                    
                    <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=601&amp;e=srxB8W1vleeNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFMn%2FPK9mKqBqnzwMABLiAiVGWiMxWSKNiplK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAm%2BsAPHmvWQuejgc5uYMfB3pNJ%2B6Svl%2B%2F07Hkm6KOv2hiwjxz2UsNZXv88Pfy6xvPEoehFNtEKpekFDr1CpAVAErMpYLcDgtPk8m1N%2BhVF%2BWhI7yxkkTmVWPsHoRK9PMigqgO%2Fw0K%2BeC5IK75IoJvSrXdFsT3SCDOX7eTDSN4XHicKavPzJZwIWaizZRgVOyZxH%2BuxFp1eOcl%2BZ%2BGhLnAyl4FpYl3XaOLsUEHztA%2F8mR7cgFy0xYDui7xyrB%2Bdy6ncnBfb7kcz623ufNoYwiaYJm2pvUERdYlpmYymfkNA%2F6AOeHAlaIGNglOPyxsXNNLw%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i2/111205109/TB2lwTAcYuWBuNjSszgXXb8jVXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>288.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="春夏装参加婚礼婚庆喜庆妈妈装礼服连衣裙子">春夏装参加婚礼婚庆喜庆妈妈装礼服连衣裙子</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">茜语丽</span> 
                    <span class="payNum">0人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.9</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=589&amp;e=hvzo88kmSICNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFOLJPhagFyNJWaopVISlWc9n%2BASQOQfC6hlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAgasWF5Ct0AVUoFhu2SdZPKfC8tUq5uW93%2BODv%2FfxT3W%2Fl1F6UKNXVqViNY%2BG3b9ZfSRwVCVEeDYW0zTUKB4tyQLclnfM%2FAgZa28JoORf%2F76ROdaoz%2FDSkzL9z5s3y9X5ko2a2hAUL2tmBa%2BZzYVWoSV3i9TE4Za%2FnOHFIYMSnhkppeOtZD4YcfxRfLvdhp4uJyLUtw6J%2FJRjRJLUervwug2R%2FHQxoNV9oma6D8RrPjuAfsjJYaiTPn%2BXUXpQo1dWtXCHRcxr4ej4FcnFAH5S167TDUZNOjvnyJiq%2By7efVO9G%2FOm111Zyc%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i2/11667884/TB2xgCnaTdYBeNkSmLyXXXfnVXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                     
                        <span class="pricedetail">&yen; <strong>108.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="色吊带长裙夜店泰国三亚海边无袖连衣裙女夏">色吊带长裙夜店泰国三亚海边无袖连衣裙女夏</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">xiaorui792</span> 
                    <span class="payNum">1人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.7</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=653&amp;e=FnNO9LXgIuaNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFOLsP9CexYec1KRF%2B0o0H%2FcT%2F1dcR9yOvZlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAhiQDflkxY8xWch0YiuJclvJUv6u6OD00GX8qh93ux6MtOZb4NXvfCQgVVSidROS42aycvW%2FxnxHcWT8Ty%2FVFIhbsgTxD%2Fy4Ky6SzyDQdaEJX1tbPyjSIK%2FSYstJTPC5T49zUuhgntouwpnkukUsIYBhQcVHhi1%2FvomjyAdNWd2AHjg3%2FGsG0ZWvlrIqZxujib9Rv3qqKFtGq62fzJE5ar0X4zwYH%2FFAI6lHm0Oe692BB5mq%2Bo18BGxBAvb14C0tFX0KArMP%2FkP5NJVOda2sCyCa0T6XzpNLXlGnYnqP8PeYJVVbRVda3BXBaUbzTituyOmee2zX9UHUWsxktYQqtEJu6ZORhNczUtvfPZ2y%2BV7y08IhaEjhY7g%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i2/122504611/TB2.XC5aHZnBKNjSZFrXXaRLFXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>498.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="女装欧美裙子 夏连衣裙字a背心 无袖 甜美">女装欧美裙子 夏连衣裙字a背心 无袖 甜美</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">anotherone旗舰店</span> 
                    <span class="payNum">2人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                    
                        <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.9</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                    
                    <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=589&amp;e=q7LD0ncFlamNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFM%2BEHZEtAJpWlhE8f85B2RBUNJPtMzyUbFlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAgasWF5Ct0AVUoFhu2SdZPLncKzD7dLW19kJbXgOQFYwAevVGJo6cIn%2BcOudXeQvdeuw%2B5nYR3yOCVXrHuhsd4qZOT1E4btacoAAqGMvoLyN073foRsRwsIS%2B5sYabgvy8ESl5lF44tnd%2BfvUU9HUjfSwRcmiZ066B3hanOcUgYYJlMDaQAANBFWqBYipxAXJap54Gi0NUXaD%2BHkfmifai0JVese6Gx3ig1h64zMyK5KbvboTu3U3SDZCW14DkBWMPjHokYLDVJw%2BshwXXKFhdsnJJ4efmmqqsSvRIwWPw%2FePrwSGAbseNg%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i2/45218293/TB2C6.vclsmBKNjSZFsXXaXSVXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>389.00</strong></span>
                     
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="卓芯2018夏装一字肩性感吊带裙拼接A字裙">卓芯2018夏装一字肩性感吊带裙拼接A字裙</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">zx卓芯旗舰店</span> 
                    <span class="payNum">0人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                    
                        <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.8</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                         
                            <li><span class="morethan">如实描述:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                    
                    <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=569&amp;e=6IOhbYZ67qqNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFOlVIoWBg3hYHaxunYHySyKSkUjq40IJ%2FxlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAlGnYnqP8PeYJVVbRVda3BVqllIQdmSPrPMB9VZeGNOOZA7Lb%2FV2evr0kcFQlRHg2CY1dOuS7M%2BiGujI4uzK2NQ%2FvYlJ44L9POipSSfKNA%2FR%2BRuTat6A3SypShMhSo7IJnm4w4S3Ej9P13RbE90ggzkpUA8C0b0HJT8yvMaqv6Ovay9oRtWhUG9ksbeTWq%2BaffFF9Zs1X%2By9JjV065Lsz6LzrTdOpDFHv1GnYnqP8PeYJVVbRVda3BUjsd9l4XLXsUSv4s7NdsOwxeSUIY5FrHJScpF7RNmalw%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i4/58012190/TB26IRohmBYBeNjy0FeXXbnmFXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>418.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="连衣裙2018春夏新款v领大摆双层长裙">连衣裙2018春夏新款v领大摆双层长裙</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">senku旗舰店</span> 
                    <span class="payNum">0人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                    
                        <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.9</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                    
                    <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=653&amp;e=dQ4Yxq8ipqiNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFPKDW3nU0ATzkm6HY7Gs2fizPImpIQd0oFlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAuYh7%2BQYo7NL4LSodO3LBZPC2jV6Ix8bRb0qe0wjAlKp6GwPPujrhnKyDhTgP3P2GNldQq9PgHIaox5CemGvyaMHjFsfOg%2B67EHcHdNWzrbVpf1NC4IxRbpWk4PH7xrzZSnEK5RcdlppzbwnlWHZudpUBY%2BhIE2xS%2B8g5Bi5NS4UeqYgx7dxhZNpQUcP4rDCRauyzDaJa5j2JXbeHQ1kZMUX4zwYH%2FFAI6lHm0Oe692BtjjfPKYJ2vafudF5enQBH1KmT%2B8FiK9IQ7I9u9LVZbk8vb549ZkQOcCFqyHqpCahXFT1K7e5uVJGEqALkUsUTdDaMXMEJ%2B5JrubaNyFnIxbM7PVD2N9pcjC00F4OUW828GiSGxCnebQ%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i2/113441301/TB2TIqIdb1YBuNjSszeXXablFXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>79.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="加大码女装胖mm洋气龄两套装胖妹妹衬衫裙">加大码女装胖mm洋气龄两套装胖妹妹衬衫裙</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">shanni_shine</span> 
                    <span class="payNum">34人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.6</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                
                                   <li><span class="lessthan">如实描述:<b>4.6</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                        
                            <li><span class="morethan">服务态度:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=577&amp;e=KNgzAXuNs%2ByNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFMspXo3x2u376ICP52UIOsk7IB0bGSIpdllK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAlGnYnqP8PeYJVVbRVda3BVqllIQdmSPrPMB9VZeGNOOZA7Lb%2FV2evr0kcFQlRHg2AIbpZP%2BYIy5zmNWbFMLwLIlKOehr%2Bshz2OlZr3BxR%2BUxeJjNzEMIGWujtBc0YGqiTPBnn%2Fdi4EH13RbE90ggzkpUA8C0b0HJT8yvMaqv6Ovay9oRtWhUG9ksbeTWq%2BaffFF9Zs1X%2By9Ahulk%2F5gjLkRRoPdOyv3wlGnYnqP8PeYJVVbRVda3BUjsd9l4XLXsTdr1TAfv%2BE4ybLNFE3IZKEEPDClrLlkIL%2BgSQ6CKrN2" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i3/131967510/TB20EHph.R1BeNjy0FmXXb0wVXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>1925.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="立领连衣裙2018中国风五分袖开叉长款A字裙">立领连衣裙2018中国风五分袖开叉长款A字裙</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">杜迪玛旗舰店</span> 
                    <span class="payNum">0人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                    
                        <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">5.0</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>5.0</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>5.0</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>5.0</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                    
                    <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=641&amp;e=EaR5H4QxNU%2BNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFPiEksCa6pDn9%2BM43hBXb41h12Tg1e9p4hlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAn8EGBrJ9VHKiF1i7Vpw2UUybraxWi1TZnDdmWpu0ze74S1%2BopEVBlRkfHCYt7Vlqi56xghqF%2B46qkALid6IRjlE4mIKgA7%2BP%2FwkRX%2B71GXX%2F79cnDXZcX%2BR34rFWw3pwlM6d6OkGXYg3%2B%2F5pb%2BfdzUGMYBQqPJooME4HKrOgDP%2BN2NapiKS%2Fb4t3uKgwr2aS58d5h%2BCMTQSCgIyhnQkhHUjh2ULo6AT0piGjQO4ntgdXadu8Hb0DB8s%2B7K1iKL3k78HKPXjT2WoaDY5yufLKNEnVcDOwKup0tkJbXgOQFYwRP40BTj1KRhN82EMcSTIMBXzmNDM0o3orII9N5CnZiYtiQfingos2hMXfaBFq0VE" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i1/129158202/TB27ZLLhQyWBuNjy0FpXXassXXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                     
                        <span class="pricedetail">&yen; <strong>78.80</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="实拍夏季假两件蕾丝裙淑女带领连衣裙长裙">实拍夏季假两件蕾丝裙淑女带领连衣裙长裙</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">lele12300</span> 
                    <span class="payNum">0人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.8</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                
                                   <li><span class="lessthan">发货速度:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=601&amp;e=ihyR%2BY54XzuNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFNQfI3nUuRuLDpn%2Bcr7fpkJjazGxK%2FnwlNlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAgasWF5Ct0AVe551xPP0CYbfnXbyHSbRwFGnYnqP8PeYJVVbRVda3BWViNY%2BG3b9ZfSRwVCVEeDYUZ9EqCewESJ25HVno78PAKwimqf3GdZ59i7Qft9UEyR4umdNcisPoAimn2uQZvixFF1iEUuYEMvXdFsT3SCDOX7eTDSN4XHicKavPzJZwIWaizZRgVOyZxH%2BuxFp1eOcU%2BOxnlTRTyo3AhlzuJSD5R7UdTBGRAuSjQ2PBwxHRSUqSoXoCSIXcyHBWL%2BBL5eL%2BMeiRgsNUnD6yHBdcoWF24G6wj0MFV%2BgVYVHBw%2FM5JSncuROyP8LqA%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i1/1358606047855670940/TB21yB0t0BopuFjSZPcXXc9EpXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>287.00</strong></span>
                     
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="显瘦露背沙滩海边渡假吊带开叉大摆连衣长裙">显瘦露背沙滩海边渡假吊带开叉大摆连衣长裙</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">车的宝</span> 
                    <span class="payNum">551人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.8</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=601&amp;e=RZ%2BeloMd2daNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFPMqjBU9m1H0DpCdku8Qib5PA6FgRNFRKFlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAgasWF5Ct0AVe551xPP0CYbfnXbyHSbRwFGnYnqP8PeYJVVbRVda3BWViNY%2BG3b9ZfSRwVCVEeDY164lYT86p6eht4LnXY0IWhgDg0BzR4sTI2XgQkst37kOeef%2B1NYUNJg7o2AsPxQ41SlzsG0TGxbXdFsT3SCDOSlQDwLRvQclPzK8xqq%2Fo69rL2hG1aFQb2Sxt5Nar5p98UX1mzVf7L3XriVhPzqnpw5%2FQHIUJ8Aj35128h0m0cBRp2J6j%2FD3mCVVW0VXWtwV1cIdFzGvh6PgVycUAflLXl7955SDw5mGa24K6x0zww6A88N9hNV%2FSA%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i2/33226903/TB2b7T8g1ySBuNjy1zdXXXPxFXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>159.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="2018新款女装春装连衣裙修身性感时尚长裙">2018新款女装春装连衣裙修身性感时尚长裙</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">卡路丝旗舰店</span> 
                    <span class="payNum">9人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                    
                        <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.8</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                    
                    <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=577&amp;e=YStqt2PZigGNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFOeic%2FoQ0EynM85L9RF5mFZXl0QnWO4%2BIdlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAlGnYnqP8PeYJVVbRVda3BVqllIQdmSPrPMB9VZeGNOOZA7Lb%2FV2evr0kcFQlRHg2PMNT2AVtJ%2BKXXA6clucsDHhg2oQFW5F5yw%2FyqGWPjO3gDtUS%2BKBtoAytP%2Fn7ab%2BaW01iQ0o7RRY13RbE90ggzkpUA8C0b0HJT8yvMaqv6Ovay9oRtWhUG9ksbeTWq%2BaffFF9Zs1X%2By98w1PYBW0n4qF9UsdCoXaQ1GnYnqP8PeYJVVbRVda3BUjsd9l4XLXsSX3qALg2OFqM%2Bh70szUq3YsRWg6JB6oKr%2BgSQ6CKrN2" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i1/126837598/TB2ROfMj46I8KJjy0FgXXXXzVXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>649.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="弹力缎磅真丝条纹修身显瘦过膝长款连衣裙女">弹力缎磅真丝条纹修身显瘦过膝长款连衣裙女</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">幽莱香旗舰店</span> 
                    <span class="payNum">2人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                    
                        <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.9</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                    
                    <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=589&amp;e=9w1pHMvmpz2NblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFNsbH56l721V4PV%2FN4HvC%2F4X%2BMZPrBC32BlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAgasWF5Ct0AVUoFhu2SdZPKfC8tUq5uW93%2BODv%2FfxT3W%2Fl1F6UKNXVqViNY%2BG3b9ZfSRwVCVEeDYPfaUZ%2B4y%2FcywaoYx4EAMM6URXb3f7eqQ4aR1xl0xvOS1M%2F6WDORaV33MOPIY%2FqXX2J2EiTijhpKV3i9TE4Za%2FnOHFIYMSnhkppeOtZD4YcfxRfLvdhp4uJyLUtw6J%2FJRvZ3FigmP2ouzu3%2FzjHb5W1JxsELwLCpZAfsjJYaiTPn%2BXUXpQo1dWtXCHRcxr4ej4FcnFAH5S14wIEvpPrVoUQcpAFx4f1ZOocidmAKroSY%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i2/1469905017322187669/TB2rmC1g4xmpuFjSZFNXXXrRXXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>59.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="雪纺无袖长裙显瘦可调节吊带裙两件套连衣裙">雪纺无袖长裙显瘦可调节吊带裙两件套连衣裙</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">dongguan076922</span> 
                    <span class="payNum">14人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.7</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=577&amp;e=UlGR66mkXfqNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFMspXo3x2u376ICP52UIOskh2cAYnp0jvllK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAlGnYnqP8PeYJVVbRVda3BVqllIQdmSPrPMB9VZeGNOOZA7Lb%2FV2evr0kcFQlRHg2JBnsATwOo242VoMhqJaKpKiPB0pZVyfgURjScJ%2FZhMlB951je302G%2FhPIZvulmWgrENl8RlP93Q13RbE90ggzkpUA8C0b0HJT8yvMaqv6Ovay9oRtWhUG9ksbeTWq%2BaffFF9Zs1X%2By9kGewBPA6jbghPsc80KK%2B91GnYnqP8PeYJVVbRVda3BUjsd9l4XLXscBx336MqnuiNsOhA411tKEEPDClrLlkIL%2BgSQ6CKrN2" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i1/131967510/TB2FArMib9YBuNjy0FgXXcxcXXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>2380.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="2018印花连衣裙长款半高领喇叭袖收腰网纱裙">2018印花连衣裙长款半高领喇叭袖收腰网纱裙</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">杜迪玛旗舰店</span> 
                    <span class="payNum">0人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                    
                        <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">5.0</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>5.0</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>5.0</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>5.0</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                    
                    <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=569&amp;e=vQ6lI05gFpyNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFOL2ykbCFbe0NJnwIrt4lS9APxonQ7GYbNlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAlGnYnqP8PeYJVVbRVda3BVqllIQdmSPrPMB9VZeGNOOZA7Lb%2FV2evr0kcFQlRHg2JvzCr24bG8from6jyCV8ceZI%2Brpkh5BJCAKAA%2BbQAFCFuoyETHnyw1hGqTWiHvz%2B4SXzoAsfIFCld4vUxOGWv5zhxSGDEp4ZKaXjrWQ%2BGHH8UXy73YaeLici1LcOifyUY0SS1Hq78Lo9wImtil9vc%2FC%2FcaSe42Hqn6BcQvmGzsPurdjlfPGvKHU1kWDeYOnwatDSKHAvKX3AljtV00gF1VRXY04T2s5jA%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i2/15339046/TB2SA2aekfb_uJkSndVXXaBkpXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>169.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="内搭女装2018连衣裙修身v领纯色中长裙">内搭女装2018连衣裙修身v领纯色中长裙</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">cheng3402</span> 
                    <span class="payNum">0人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.2</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                
                                   <li><span class="lessthan">如实描述:<b>4.2</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                
                                   <li><span class="lessthan">服务态度:<b>3.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>5.0</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=569&amp;e=wBLm5pP8vvuNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFOL2ykbCFbe0NJnwIrt4lS9tNFlVJqyHcdlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAlGnYnqP8PeYJVVbRVda3BVqllIQdmSPrPMB9VZeGNOOZA7Lb%2FV2evr0kcFQlRHg2GcRnYK1zpru%2Fzr6bIZtq254WemEjK0h7V6eO5oiMOB82CFpzaNwAlmK3tAfSpO1wc4Ea4Dz8oyald4vUxOGWv5zhxSGDEp4ZKaXjrWQ%2BGHH8UXy73YaeLici1LcOifyUexsv0rikoEJMyfB%2FRXGsF8uCj4y1Q2e7n6BcQvmGzsPurdjlfPGvKHU1kWDeYOnwZHY6mVQMlwN1HsqiWVAPBxRXY04T2s5jA%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i1/15339046/TB20dlXX8jTBKNjSZFuXXb0HFXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>169.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="长袖2018连衣裙春季韩版修身衬衫裙">长袖2018连衣裙春季韩版修身衬衫裙</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">cheng3402</span> 
                    <span class="payNum">0人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.2</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                
                                   <li><span class="lessthan">如实描述:<b>4.2</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                
                                   <li><span class="lessthan">服务态度:<b>3.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>5.0</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=569&amp;e=HkWdv5ezFreNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFPSgK1wJI5tevK5TM5Du%2FP4yzwTfSp1Sq5lK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAlGnYnqP8PeYJVVbRVda3BVqllIQdmSPrPMB9VZeGNOOZA7Lb%2FV2evr0kcFQlRHg2Cn%2F0YJi1x5l05IQzVIl3YwWWZuqxtZvux93xzN2Dvnv4pXDwYr1YMjcXX0Mx%2Fae6%2FvBSdAyA%2BFY13RbE90ggzl%2B3kw0jeFx4nCmrz8yWcCFmos2UYFTsmcR%2FrsRadXjnJfmfhoS5wMpKHs5rA940ddrS1IEp7ebzipKhegJIhdzIcFYv4Evl4s5bTi1yTRRLiIKhitZXBfmapGwen%2FIkoOc8vA%2BsT7zVw%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i1/116022514/TB2o_tGcx9YBuNjy0FfXXXIsVXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                     
                        <span class="pricedetail">&yen; <strong>39.80</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="2018春季新款中长款印花宽松显瘦棉麻连衣裙">2018春季新款中长款印花宽松显瘦棉麻连衣裙</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">动人的菇凉</span> 
                    <span class="payNum">5人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.7</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=589&amp;e=bBAhhY31L6mNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFMm8fs93uoxiCCQKPPrBdswyVpTclfbztxlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAgasWF5Ct0AVUoFhu2SdZPIjsd9l4XLXsWX8qh93ux6MR%2B8KrZyWXNpE4mIKgA7%2BP3EdDVXn7RHq0UOdVk3j73grO3bBcGdq8yooitUhtbHsrMhMLHX5Ool%2BSZVnTSsG6DhKthP35GxvN2NapiKS%2Fb4t3uKgwr2aS58d5h%2BCMTQSCgIyhnQkhHUjh2ULo6AT0piGjQO4ntgdls5rRX%2BGvQqtxfW23wKPnqXzeZ3IL1U3EmGhDZodnlwtHaGBT2cJZbcE1DZ9sfB3FLN%2FY0jONjP6dK3GdB6WnsfyHwjbigWoIoNmY5VucMo%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i3/107287356/TB2vvsmikKWBuNjy1zjXXcOypXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>48.18</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="韩国chic复古仙女长裙碎花吊带荷叶边连衣裙">韩国chic复古仙女长裙碎花吊带荷叶边连衣裙</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">小葵ttb232425</span> 
                    <span class="payNum">72人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.5</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                
                                   <li><span class="lessthan">如实描述:<b>4.5</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                
                                   <li><span class="lessthan">服务态度:<b>4.6</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                
                                   <li><span class="lessthan">发货速度:<b>4.5</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=569&amp;e=oQyP3t9uLrONblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFPVGeTc3HVFEWxdcFzXdudtTFWUB0h2jrBlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAuETc02MkuA%2FAwp%2BRVHsRR3O1lszgjM4toiE53VD5qJjROJiCoAO%2Fj93gE9lOTbFBtcYZcCDv896AMV5srSMeLFL%2FAl9DLfhwymtVr%2F06aSZogg7Ow0Qnn%2FVb85n9nt96jdjWqYikv2%2BLd7ioMK9mkufHeYfgjE0EgoCMoZ0JIR1I4dlC6OgE9KYho0DuJ7YHaa9MMLMEJgJUiepxTzN98o0cmWMVPTLQE3zYQxxJMgwefup6l75S9QMPLSLnIUkk%2Bj4%2BJ3toDb6Z25aYBEmZY8ig2ZjlW5wyg%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i4/122573366/TB2miR1almWBuNkSndVXXcsApXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                     
                        <span class="pricedetail">&yen; <strong>79.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="长裙连衣裙学院风2018格子夏文艺无袖背带">长裙连衣裙学院风2018格子夏文艺无袖背带</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">liang491777</span> 
                    <span class="payNum">0人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.7</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                        
                            <li><span class="morethan">发货速度:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=653&amp;e=j5VOJXUf5KWNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFP%2B7KNh5PR7TYvU2iCk1ikd6ElSJeHA3YhlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAuYh7%2BQYo7NL4LSodO3LBZPC2jV6Ix8bRb0qe0wjAlKp6GwPPujrhnKyDhTgP3P2GNldQq9PgHIaox5CemGvyaMHjFsfOg%2B67EZqeXE8xJsVpD8Vg76cRgun6qon9K42ZJolFhYH0xO%2F5bjSWSSD3%2Bfia0qqtHwADMC8VxeFj%2BBmpMju8MxwbZRHSnOQT6nMrp4qNumM5htmrpQQBNFK13vnUa0bivNA00nLtZ0iL5IoMIia5IizpSENPgABoKg97sTzQXH7vm%2F%2BhbtC%2BODlHC5Gp5RIsAukkIInNWZ3AKZwNbkrWs13jmXiCktHGPJT%2BQ%2FLqCOhPadt3Ib9jbRrTIUcSICRQbRjG1O7W9fcZU58IoNmY5VucMo%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i2/33583946/TB2dQNdeeSSBuNjy0FlXXbBpVXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>78.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="胖MM大码女装夏装时尚潮2018新款阔腿裤套装">胖MM大码女装夏装时尚潮2018新款阔腿裤套装</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">广州安防比色兔</span> 
                    <span class="payNum">2958人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                        <span class="icon"><span class="icon-golden"></span></span>
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.7</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                    <span class="icon"><span class="icon-golden"></span></span>
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=569&amp;e=6wO2Uq0RU7CNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFMhm5w25kneeHTBDQQOHtQFuaWgR%2FbStDplK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAlGnYnqP8PeYJVVbRVda3BVqllIQdmSPrPMB9VZeGNOOZA7Lb%2FV2evr0kcFQlRHg2JW9A4IohFkcdA1H5XUqxYzYoffnKPbJXsKCLMcsOa%2Fga2odXjQVuPATYEgWqHxe7sqAvjQmwiKD13RbE90ggzl%2B3kw0jeFx4nCmrz8yWcCFmos2UYFTsmcR%2FrsRadXjnJfmfhoS5wMpzgOXTePgl9%2BmbQTjMBaOZipKhegJIhdzIcFYv4Evl4s5bTi1yTRRLgSELUWUaIpwBYf3B%2FNpDolWgndS0ZJxjA%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i4/47174382/TB2CHRwbHZnBKNjSZFhXXc.oXXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>288.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="桑蚕丝连衣裙100%真丝2018新款夏装中长款">桑蚕丝连衣裙100%真丝2018新款夏装中长款</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">冰糖一口</span> 
                    <span class="payNum">33人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">5.0</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>5.0</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=577&amp;e=7vYAN2aWptaNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFPCUm72NtWn3vLRP2Xv%2FsTiGyz3oF4MTDllK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAgasWF5Ct0AVUoFhu2SdZPKkQ5PeOpouaH8EGBrJ9VHKiITndUPmomNE4mIKgA7%2BPwY216eYiyrVdwkhl9zHDS2f2vFiVPHVZIQr6gSo%2Fz6UxC%2Fv%2BzgEwrbYaO1wd2fJ942Qm1WaqlKXhslNNXPYujEFATLGngWBjAsrWrT5ggrFay9oRtWhUG9ksbeTWq%2BaffFF9Zs1X%2By93ZIKvoPTtgKOvjSDcZocdJTw5dpqtEtffwQYGsn1UcpCjncicWzwCU85xy%2B2Uw55ynhAGuZP7znWtS0kiuvyzPNzKzyDbxpH" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i2/45553138/TB2.HRba9BYBeNjy0FeXXbnmFXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>1923.35</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="misstouch 吊带裙不规则连衣裙 碎花 气质">misstouch 吊带裙不规则连衣裙 碎花 气质</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">tb_9263659</span> 
                    <span class="payNum">15人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                        <span class="icon"><span class="icon-golden"></span></span>
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.9</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                    <span class="icon"><span class="icon-golden"></span></span>
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=665&amp;e=%2FVrTpnjlCxKNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFNqkxq38iRj2akMdeAZ9FEQlVeb%2FWsGpOZlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAhjgQxKvSk2WvtyBLhtx4kzB4NaWZ04CSH8EGBrJ9VHKP7XrELIqmQoNYaRZrPyMb1GnYnqP8PeYJVVbRVda3BWViNY%2BG3b9ZfSRwVCVEeDY88XQF3WD3h2sfEB3BMEmsWL8a6h2P18G9Qthw4hWD%2F4agK%2BOhPSYQGDyc470NkDH0PqTSbYDJwqV3i9TE4Za%2FnOHFIYMSnhkppeOtZD4YcfxRfLvdhp4uJyLUtw6J%2FJRuSkBs0iDQwtVrRXSmIMT2ScMxP%2ByF2gSZYaU66SgcvUDtLOuhqokPm%2FiH3MPXxoOZfyqH3e7Hox%2BgXEL5hs7D7q3Y5XzxryhhDXCxSRXa1zsmNGOpqKp4NUhCH6%2BIPqasmaXi1dNF%2BBy%2F7j0uhM7vg%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i4/113384267/TB2XKWQasz85uJjSZFoXXXjcpXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>79.90</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="渡假长裙印花显瘦雪纺两件套波西米亚连衣裙">渡假长裙印花显瘦雪纺两件套波西米亚连衣裙</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">宫廷衣装</span> 
                    <span class="payNum">306人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                        <span class="icon"><span class="icon-golden"></span></span>
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.8</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                    <span class="icon"><span class="icon-golden"></span></span>
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=633&amp;e=7Pd9uLjxs%2FONblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFPCkREXC9F4ndYVWnoLChm7nmohtTufid9lK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAi56xghqF%2B464SxO9inyAdCuuW%2BlivNlflGnYnqP8PeYJVVbRVda3BWf64jcONzstKdGl4iT6QnisSpbIGYqp3ksrfEr7xPhZ9IUsquwAEMNU5mDIe3Cww8id9Ub8AMH%2BIa3OQEZJjHhhBbeIVrl6%2FP820udyRGDFXqmIMe3cYWTaUFHD%2BKwwkV7kL8C4ILCkzTHEb%2F1tTYUc4cUhgxKeGSBj6vBpfeEljIhg0jnS2HK0hSyq7AAQw0uesYIahfuOuEsTvYp8gHQrrlvpYrzZX5Rp2J6j%2FD3mCVVW0VXWtwVn%2BuI3Djc7LQDfAJ228KNMIrei42QaTBGV6jwjnFrVR5JPEh4xw3shQ%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i1/24936880/TB2.UQTbHArBKNjSZFLXXc_dVXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                     
                        <span class="pricedetail">&yen; <strong>599.00</strong></span>
                     
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="Lao2018夏季新款裙子漏肩女神范吊带连衣裙">Lao2018夏季新款裙子漏肩女神范吊带连衣裙</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">lagogo服饰旗舰店</span> 
                    <span class="payNum">12人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                    
                        <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.8</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                    
                    <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=653&amp;e=8F9Q%2BHXus8WNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFODyyUifIUZdltpsSVAipgxmv1bJsCOBYNlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAnBhv3huMRWv%2BzQecH3nSHa6bS5tGa1rvTwDG7B03Cdm8tS3BhGBabm58%2F7SQglnNUOKsSSoc9DNeEST94%2FTF5P%2BcOudXeQvdaDFdr7la1FR8OCNEwkaKLLJETQ3zDdc7XTQn0jViuI52BQDtSgpLTxFLx7hbXMTbKmiG%2Fi6ztPNAJSeZ10RLVHSwRcmiZ066B3hanOcUgYYJlMDaQAANBFWqBYipxAXJap54Gi0NUXajNZb%2FNt75%2Fnw4I0TCRoosiaWoHDOQdNkBF9VBXOsqTU2%2BjSjQx2kkbkJyxwjkm2LFD%2FzPAFcd6EkQ5s%2FXrAen%2BEtfqKRFQZUzsCCF9Vb1kgGGJqQ1mnTHrGQ8OHPG4UgD3iPyueV680%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i1/122244371/TB2NF7EbH3nBKNjSZFMXXaUSFXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>468.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="时尚七分袖显瘦大码长款碎花真丝A字连衣裙">时尚七分袖显瘦大码长款碎花真丝A字连衣裙</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">绒惑旗舰店</span> 
                    <span class="payNum">0人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                    
                        <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.9</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                    
                    <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=545&amp;e=gWiDcerxZuWNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFOINGBzNaBpvAw%2FsSFiqrzg%2F4hGgHgN8WRlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAuWEhyIibhueg8m5YUorz8%2F2zBxtuJva5yVGQ%2B%2F68GFfTSVhaVN8%2BewvUu4NKPXteVM5F0zqGwPrqqBzx%2FF3om0Fc7pfnq4b0QQN8OeeRssb2F3VR1ITZ%2BKGyU01c9i6MQUBMsaeBYGMCytatPmCCsVrL2hG1aFQb2Sxt5Nar5p98UX1mzVf7L2m3ott5ELu2HOrZaXj%2B85fyJxiDb0devUtxfqMCz5fx3TGm9fxDpZao%2FU2Kluv2XLqXsyhLTEXxL%2BgSQ6CKrN2" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i3/17369326/TB2HHVRhYSYBuNjSspfXXcZCpXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>79.90</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="高腰显瘦牛仔背带裤九分裤学生宽松连体裤潮">高腰显瘦牛仔背带裤九分裤学生宽松连体裤潮</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">飞雪紫紫</span> 
                    <span class="payNum">3人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.6</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                
                                   <li><span class="lessthan">如实描述:<b>4.6</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                        
                            <li><span class="morethan">服务态度:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                         
                        
                        
                            <li><span class="morethan">发货速度:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=601&amp;e=FWjrowT7TfyNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFPit2U%2FUHeTDiSxovmsLXoEoVfreyMVBbBlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAgasWF5Ct0AVe551xPP0CYbfnXbyHSbRwFGnYnqP8PeYJVVbRVda3BWViNY%2BG3b9ZfSRwVCVEeDYIiKEdKJNKtg5PP6QxeV1YE8ZUuq14TO5T6C9CtV9eBWUnJVA%2B5X6b874pc5qN1FM%2B3vWzOeIeYPXdFsT3SCDOX7eTDSN4XHicKavPzJZwIWaizZRgVOyZxH%2BuxFp1eOcl%2BZ%2BGhLnAykgBOQqD13mT9VhXkjjqNuAjQ2PBwxHRSUqSoXoCSIXcyHBWL%2BBL5eL%2BMeiRgsNUnD6yHBdcoWF205paom1fWrr7PdWhmZKln1mM4V%2F5AqRTA%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i2/52630271/TB2UfiNhpuWBuNjSszbXXcS7FXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                     
                        <span class="pricedetail">&yen; <strong>35.88</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="波点连衣裙潮百搭学院风宽松显瘦大摆裙女夏">波点连衣裙潮百搭学院风宽松显瘦大摆裙女夏</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">丫头日系韩版女装</span> 
                    <span class="payNum">11人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.6</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                
                                   <li><span class="lessthan">如实描述:<b>4.6</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                
                                   <li><span class="lessthan">服务态度:<b>4.6</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                
                                   <li><span class="lessthan">发货速度:<b>4.6</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=577&amp;e=yiyf6ktgAxCNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFPuTcT%2FwsalTsHJdRdJSS55mw2fA1WJNCRlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAlGnYnqP8PeYJVVbRVda3BVqllIQdmSPrPMB9VZeGNOOZA7Lb%2FV2evr0kcFQlRHg2MquSlgFAzVKdzd2G47HexX%2FoL%2FOsZcjC7CxQTWhPpInMRRtT9EBw0cMn%2FaKetCx0jV03Thua0TS13RbE90ggzkpUA8C0b0HJT8yvMaqv6Ovay9oRtWhUG9ksbeTWq%2BaffFF9Zs1X%2By9yq5KWAUDNUpty1RemWhvk1GnYnqP8PeYJVVbRVda3BUjsd9l4XLXsV2Lc1omhBFfawl7U0CrvgyRdjTd1sXvd7%2BgSQ6CKrN2" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i3/116132624/TB2vWG6hf9TBuNjy1zbXXXpepXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>1986.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="连衣裙女2018新圆领套头渐变色显瘦A字裙">连衣裙女2018新圆领套头渐变色显瘦A字裙</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">woonam旗舰店</span> 
                    <span class="payNum">0人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                    
                        <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.9</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                    
                    <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=577&amp;e=SEK6jiQDm%2BWNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFPuTcT%2FwsalTsHJdRdJSS55OlBRkCNfxXZlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAlGnYnqP8PeYJVVbRVda3BVqllIQdmSPrPMB9VZeGNOOZA7Lb%2FV2evr0kcFQlRHg2AfpqsokI5f5KnMOtqSL0rdxV5PEcjwVOIxDSih3h4ZuKoOkZFaQ1qUujynZlnq8uxwBaamDKyUw13RbE90ggzkpUA8C0b0HJT8yvMaqv6Ovay9oRtWhUG9ksbeTWq%2BaffFF9Zs1X%2By9B%2BmqyiQjl%2FkLdIxgG%2FjwulGnYnqP8PeYJVVbRVda3BUjsd9l4XLXsTv74fw2ws8035gShjdAc8qRdjTd1sXvd7%2BgSQ6CKrN2" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i1/116132624/TB2_o02b5MnBKNjSZFzXXc_qVXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>2013.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="连衣裙轻薄修身2018夏绣花款背心裙">连衣裙轻薄修身2018夏绣花款背心裙</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">woonam旗舰店</span> 
                    <span class="payNum">0人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                    
                        <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.9</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                    
                    <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=641&amp;e=aDATf%2Bp66MeNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFMRHUOQGb%2BamG6TEC%2BxXQqdzeN74AH69W1lK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAn8EGBrJ9VHKiF1i7Vpw2UUybraxWi1TZnDdmWpu0ze74S1%2BopEVBlRkfHCYt7Vlqi56xghqF%2B46qkALid6IRjlE4mIKgA7%2BP0x5GYbNf3sEnpYKYt%2BK6AsAPErOf7fP0ujuSKrDTUIxfUIhegfaKI6Xw6Bun3JSi%2Bb4vmeuXHCDN2NapiKS%2Fb4t3uKgwr2aS58d5h%2BCMTQSCgIyhnQkhHUjh2ULo6AT0piGjQO4ntgdxqv9y2RKvoMFOwy0nra2dL8HKPXjT2WoaDY5yufLKNEnVcDOwKup0tkJbXgOQFYwRP40BTj1KRhN82EMcSTIMK%2BhKGChg%2FUzvyJ8%2BmvAqToKli1eH3fFfeqByMtyLJ4u" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i3/127649409/TB2p131cbZnBKNjSZFrXXaRLFXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                     
                        <span class="pricedetail">&yen; <strong>158.80</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="长裙新款仙学生端庄大气明星同款显瘦">长裙新款仙学生端庄大气明星同款显瘦</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">zyb_123321</span> 
                    <span class="payNum">0人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">0.0</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                         
                            <li><span class="morethan">如实描述:<b>0.0</b></span><span class="listup-tgr-arrow"></span></li>
                        

                        
                            <li><span class="morethan">服务态度:<b>0.0</b></span><span class="listup-tgr-arrow"></span></li>
                         
                        
                        
                            <li><span class="morethan">发货速度:<b>0.0</b></span><span class="listup-tgr-arrow"></span></li>
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=621&amp;e=mRR3OSxVXAONblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFNy7CWdqAdhZzsKUXTyydpi%2BDRyk2JTTH5lK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAlUtwMxFhna7n1tXGEIKl5vJUv6u6OD00KC9FBulM27Pp8VK8YWQkVZl%2FKofd7sejEfvCq2cllzaROJiCoAO%2Fj8d0Tvmr4ArDySBMxwZ1nHNrl0ESlFoA4M35fCzT2YIhV88N6bzRC2Fks4BZJBPxtqF1VrbADD3aDdjWqYikv2%2BLd7ioMK9mkufHeYfgjE0EgoCMoZ0JIR1I4dlC6OgE9KYho0DuJ7YHQIv35yUR0bRO6Rf%2FE48WKor14%2BG76pJk6HNSeYbSkTYZfyqH3e7Hox%2BgXEL5hs7D7q3Y5XzxryhFBRX6yUEQQ8aoLrdooo35WaSmAF9cV%2BBMQ1zaIjRpMY%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i1/126282701/TB2vH8HghWYBuNjy1zkXXXGGpXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>65.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="夏季新款女装性感礼服裙一字领露肩连衣裙">夏季新款女装性感礼服裙一字领露肩连衣裙</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">永恒6401</span> 
                    <span class="payNum">2人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.4</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                
                                   <li><span class="lessthan">如实描述:<b>4.4</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                
                                   <li><span class="lessthan">服务态度:<b>4.5</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                
                                   <li><span class="lessthan">发货速度:<b>4.5</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=577&amp;e=CkU7yyxcIsSNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFNzmTmcFHogSqznZYAWf1mACoKHe3syjMplK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAs79n7S%2B4QLMLabUBMrKItTtGsps77rmgmy%2BQVDttsj8Jy7LCL4aBzlE4mIKgA7%2BP026yamGS%2FXrBVg4DVevkL1n9bjuJEki%2FQrbXA0NonUlTsv5qf8AK9qUmWEdow0bPsXs%2BXM1eMtsN2NapiKS%2Fb4t3uKgwr2aS58d5h%2BCMTQSCgIyhnQkhHUjh2ULo6AT0piGjQO4ntgdHsJfa1UEI7QZ%2FfP3AHqq8pk4KddnySkWov9SviIdXvSGMqBj7ClwtRs896jcou93kRVPuJilPfAyebQW16OG6snBwH6X95HH" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i2/11049960/TB21nBUf7SWBuNjSszdXXbeSpXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                     
                        <span class="pricedetail">&yen; <strong>169.00</strong></span>
                     
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="张i大奕吾欢喜的衣橱 雪纺碎花连衣裙长裙">张i大奕吾欢喜的衣橱 雪纺碎花连衣裙长裙</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">小番茄0506</span> 
                    <span class="payNum">826人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                        <span class="icon"><span class="icon-golden"></span></span>
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.7</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                    <span class="icon"><span class="icon-golden"></span></span>
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=537&amp;e=yjCKut6BBXSNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFPGnxCc4GWFF1TJc1PuY1DgyAg4WmmOQ7xlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAhkfAsRta6OBM46rnCeezlzlkgFDLygWMvSRwVCVEeDYEQ7wcK0iuJ8QpiScOf3F7jn3L2JZLBdWl%2FrKjeVSjAonWSZgUiHWMAc5ULiV6phSxl570p6jOGbXdFsT3SCDOX7eTDSN4XHicKavPzJZwIWaizZRgVOyZxH%2BuxFp1eOcl%2BZ%2BGhLnAymHIB48BQjWXJZJpQAd6Jsbg8m5YUorz8%2FjqShs6g8MDeztPgt0lpquhEoPSqMqRWxjLNe6%2BsvbYg%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i2/25910929/TB2zHPhiGSWBuNjSsrbXXa0mVXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>127.50</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="金蘑菇菇 张.大奕 原宿风牛仔背带裙">金蘑菇菇 张.大奕 原宿风牛仔背带裙</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">jimmyxiaolu</span> 
                    <span class="payNum">0人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                        <span class="icon"><span class="icon-golden"></span></span>
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.6</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                
                                   <li><span class="lessthan">如实描述:<b>4.6</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                
                                   <li><span class="lessthan">服务态度:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                        
                            <li><span class="morethan">发货速度:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                    <span class="icon"><span class="icon-golden"></span></span>
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=633&amp;e=C%2Ft8kjl0YPqNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFMJAupWqmBptXK6zTV3ByUOZVpC%2BzV6L1FlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAmY4Ezhsqt8hZVZOfnY79Ca4Jb71m5pmONTbX8zw4nKmX92%2BUHdX9gXhLX6ikRUGVA0DWFS%2BDPI9W7IE8Q%2F8uCv2wV7gMQvu5TUpalGHj49cJDgWvBccKAH2CXj665FRS%2FHt61rIM5z%2FzTBikL%2Bj7%2BhhuEr6JSWSzR44N%2FxrBtGVr5ayKmcbo4m%2FUb96qihbRqutn8yROWq9F%2BM8GB%2FxQCOpR5tDnuvdgT5WNtNedlGVRDGR75GZT0llH0hibMKDxduLzoTkEgKDAaO%2FnBkeKkThLX6ikRUGVLJr%2BafQZLPjKZReSpcE5wrSHwnlEWX1BvQdGCaNTUG0zNa2A7HOPVRusSlpHitl8A%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i1/117056024/TB2p5hZh1uSBuNjSsziXXbq8pXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>149.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="蕾丝连衣裙女夏2018新款韩版小清新两件套春">蕾丝连衣裙女夏2018新款韩版小清新两件套春</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">妲恋旗舰店</span> 
                    <span class="payNum">0人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                    
                        <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.9</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                    
                    <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=545&amp;e=5inGWn2bO2mNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFO8D0NpiEwxKyhjYEQg%2FJMg7EScqJwk1LplK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAuWEhyIibhueg8m5YUorz8%2F2zBxtuJva51uyBPEP%2FLgrDme9aL6eoAz0jn8qVsq2AUhWRfKXprj%2FEtXPyErwDDQyICPGAZ1rik8OILj7Es44eiwKbYhKIxYeODf8awbRlUdKc5BPqcyunio26YzmG2aulBAE0UrXe%2BdRrRuK80DTScu1nSIvkigdtRrHk5CcXzBhsgyRZjsaqNmIny%2B075I790uVvz6XnBCm2Z73TktxtVs7JT3coG2d6GVkzuN8eUh2EBDH67rJ" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i1/33608328/TB2qC.gfHGYBuNjy0FoXXciBFXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                     
                        <span class="pricedetail">&yen; <strong>136.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="2018新款流行女装无袖印花仙显瘦雪纺长裙">2018新款流行女装无袖印花仙显瘦雪纺长裙</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">罗绪德688</span> 
                    <span class="payNum">17人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.7</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=569&amp;e=wVqJaVDQBvyNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFMLocvIFk9l9JgARQqOpUM2YEjnQ4g3dAhlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAlGnYnqP8PeYJVVbRVda3BVqllIQdmSPrPMB9VZeGNOOZA7Lb%2FV2evr0kcFQlRHg2L80SaaJ17yA45FBREGR10ivIaGfpwXoM4nmeEBvGjqoOV282yDzT2x6DMGYPddqMNyQf%2B0tUxKJ13RbE90ggzl%2B3kw0jeFx4nCmrz8yWcCFmos2UYFTsmcR%2FrsRadXjnJfmfhoS5wMp7rEIBBs1gu7NPPGXpL038CpKhegJIhdzIcFYv4Evl4s5bTi1yTRRLkQsg%2Be%2B1tIz9jmNXw4L8MbdPOBQbagoiA%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i3/15652525/TB2t8FQb3mTBuNjy1XbXXaMrVXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                     
                        <span class="pricedetail">&yen; <strong>99.00</strong></span>
                     
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="雪纺连衣裙复古印花中长裙2018夏季新款">雪纺连衣裙复古印花中长裙2018夏季新款</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">zhangwan1329030</span> 
                    <span class="payNum">0人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.7</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                         
                            <li><span class="morethan">如实描述:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                        

                        
                            <li><span class="morethan">服务态度:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=609&amp;e=q%2F647r5bs6WNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFPh5p14F2YfCUvQBB3KpJsAvqJBxOUU74tlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAhjgQxKvSk2WvtyBLhtx4kzB4NaWZ04CSAasWF5Ct0AVJShbkS7xwKmuuW%2BlivNlfjxn6zvj9rGoqWtA9xMp0g5obeJrrtSXuX8NsXITPUJ6WgbgP5tZwCD31SBNG8P2UjcuO7FBu%2BRIh7Dgy6CW9oPRt7I8feiEPkdKc5BPqcyunio26YzmG2aulBAE0UrXe%2BdRrRuK80DTScu1nSIvkiig1bDqGTyiPehG5wwkZFGo%2FNnNo930wyFUutQowmhXdy0doYFPZwlltwTUNn2x8Hd0%2BVCxTamCF9yYERY4oNV3u%2FLThYu%2FYzed69NmeFw2iDgKTdWZqWQV" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i3/T1sHe.XXtcXXcsjyE6_061916.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>139.00</strong></span>
                     
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="花色波西米亚风情长裙飘逸吊带连衣裙夏多色">花色波西米亚风情长裙飘逸吊带连衣裙夏多色</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">caiyige668</span> 
                    <span class="payNum">0人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.6</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                
                                   <li><span class="lessthan">如实描述:<b>4.6</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                
                                   <li><span class="lessthan">服务态度:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                        
                            <li><span class="morethan">发货速度:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=665&amp;e=02L45XWxuj%2BNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFOvmklV3T7tS5lM7TS%2FQoMRFjSicyJeOmllK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAhjgQxKvSk2WvtyBLhtx4kzB4NaWZ04CSH8EGBrJ9VHKP7XrELIqmQoNYaRZrPyMb1GnYnqP8PeYJVVbRVda3BWViNY%2BG3b9ZfSRwVCVEeDY5ZVA4wzC8%2FJscFRxOxES2GUQJIiwB9QhIC%2FerVAJX%2BOujzDFfQAUXfU77i%2BWoLzOMcYY2oYnYynXdFsT3SCDOX7eTDSN4XHicKavPzJZwIWaizZRgVOyZxH%2BuxFp1eOcl%2BZ%2BGhLnAykk5ff8d22agj120yT3Ophd9B1dhJZGp2kmHEQU5vTPyCmkTXmeMg%2FEyF8DamiiwIwqSoXoCSIXcyHBWL%2BBL5eLcwH5H4mb3QLcmBEWOKDVd2FU0pl%2Fl%2B0CO%2BX3WCsuhJ2ULBrrVX4gZw%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i3/128495858/TB2nPeWcxWYBuNjy1zkXXXGGpXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>79.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="雪纺渡假连衣裙2017新款波西米亚长裙">雪纺渡假连衣裙2017新款波西米亚长裙</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">心妍宝贝1688</span> 
                    <span class="payNum">34人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.9</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=601&amp;e=ZDjsBnJBJEONblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFOYZqhKYpdQdfTFLqcVaIjuBbBqJhSVaVtlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAgasWF5Ct0AVe551xPP0CYbfnXbyHSbRwFGnYnqP8PeYJVVbRVda3BWViNY%2BG3b9ZfSRwVCVEeDYmrC9vk%2Fb5vtgyK9sWxaGpebvPu3rk3muQVRCViwm%2FKWtwzNR%2B44cz0SPJeGcu6CLx2voU0OX1Y7XdFsT3SCDOX7eTDSN4XHicKavPzJZwIWaizZRgVOyZxH%2BuxFp1eOcU%2BOxnlTRTyr3io8fDZMnSpVutcGPVgf9jQ2PBwxHRSUqSoXoCSIXcyHBWL%2BBL5eL%2BMeiRgsNUnD6yHBdcoWF2%2BLmAhsLDdM3i2vb7qfufH%2BlktgJXUZMmg%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i2/11441255/TB2yak7oxPI8KJjSspoXXX6MFXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                     
                        <span class="pricedetail">&yen; <strong>538.00</strong></span>
                     
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="不等式剪裁19姆米真丝缎吊带大摆连衣裙">不等式剪裁19姆米真丝缎吊带大摆连衣裙</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">胖九点com</span> 
                    <span class="payNum">3人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                        <span class="icon"><span class="icon-golden"></span></span>
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.8</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                    <span class="icon"><span class="icon-golden"></span></span>
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=569&amp;e=LJHQwlO%2B8uGNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFPcid5O%2BQoQ0mOa5WzWQ7S5jijg6iJPoYVlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAlGnYnqP8PeYJVVbRVda3BVqllIQdmSPrPMB9VZeGNOOZA7Lb%2FV2evr0kcFQlRHg2B6zSGg%2FRkp2iLW%2FNVV4Ly%2BTtkw%2Bg%2BlAanTrPKXuvwFxUYmL1oOpLecQBo81tWXm7dL72tzBUiK813RbE90ggzl%2B3kw0jeFx4nCmrz8yWcCFmos2UYFTsmcR%2FrsRadXjnJfmfhoS5wMpMbYYaAWX57j4jWqY%2FgA%2FRCpKhegJIhdzIcFYv4Evl4s5bTi1yTRRLoaZyTmSKwTkpDCU9DJaTbP7XMSPgWgL%2Bg%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i1/21171321/TB2O7D6cVuWBuNjSspnXXX1NVXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                     
                        <span class="pricedetail">&yen; <strong>75.99</strong></span>
                     
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="折扣剪标2018新款长袖印花连衣裙蓬蓬裙">折扣剪标2018新款长袖印花连衣裙蓬蓬裙</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">gongzhi021</span> 
                    <span class="payNum">0人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.8</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=601&amp;e=iuklTraMkFKNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFNMTCQkrAagF1s4whkFpNa8bAB%2FEUnJJEBlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAgasWF5Ct0AVe551xPP0CYbfnXbyHSbRwFGnYnqP8PeYJVVbRVda3BWViNY%2BG3b9ZfSRwVCVEeDYBW6dQquTu5P4ZoNVGJw1p43efgj4wLq694zvGBgWPbTNNOKV57nosoBRXVXVfanatI3yx50KqinXdFsT3SCDOX7eTDSN4XHicKavPzJZwIWaizZRgVOyZxH%2BuxFp1eOcl%2BZ%2BGhLnAynt%2BlkBtjGN8ZR5xB8bkpDmjQ2PBwxHRSUqSoXoCSIXcyHBWL%2BBL5eL%2BMeiRgsNUnD6yHBdcoWF2xb2X%2FKm9CoaEWDyEBvos1AABA0AbnsDHw%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i4/111045953/TB24r5uhnlYBeNjSszcXXbwhFXa_!!2-saturn_solar.png_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                     
                        <span class="pricedetail">&yen; <strong>113.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="纯黑色性感V领小心机修身高腰雪纺连衣裙">纯黑色性感V领小心机修身高腰雪纺连衣裙</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">elurde</span> 
                    <span class="payNum">0人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">5.0</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>5.0</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>5.0</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>5.0</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=577&amp;e=OjzU9doQfAuNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFM5YedimHPpbSOmUZLbZkG3sDGEvrqjA9plK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAlAvFkEHFWmvBvMOqWKerGpAif3Npr46uoJ2ZqQmVcBVp8Zsy1baQw72xNZuPUZT0OhzB8y%2BpgGW2ZmQ2jHZ1k%2FFi2yApW9oKpTpYsUbu7VAryFR3V8FB9OawdjTzHzgANObx8KdRnw0N2NapiKS%2Fb4t3uKgwr2aS58d5h%2BCMTQSCgIyhnQkhHUjh2ULo6AT0piGjQO4ntgdmwaxI6DZ%2FqNEISNVA8rkIIGzU4eQ5XpWrwqqQIboxpt6iNZJAni4vpvXBoc0ULQcrKJ6kkvU37hReETKAwhxMaHELAfoXlNk" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i1/1017251739/TB2__4fXktjV1BjSsplXXc0NpXa_!!1017251739.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>130.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="同款针织拼接条纹衬衫上衣百褶半身裙套装">同款针织拼接条纹衬衫上衣百褶半身裙套装</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">早起的小蜗牛53</span> 
                    <span class="payNum">8人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.8</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=569&amp;e=egWto2z08haNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFP74YD68nSL%2Bfo6rLJdfn0TqTrf9OOKKWRlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAlGnYnqP8PeYJVVbRVda3BVqllIQdmSPrPMB9VZeGNOOZA7Lb%2FV2evr0kcFQlRHg2HVGXgjwn7ld%2FE%2BuJJMUjKCCV%2BZB4mv%2FWLphuQGQYvanUbxNDmwilm5hgALIHTTpgzV9O2SOPnvZ13RbE90ggzl%2B3kw0jeFx4nCmrz8yWcCFmos2UYFTsmcR%2FrsRadXjnJfmfhoS5wMpv9keO6lTjSFmRHI7qnjGUipKhegJIhdzIcFYv4Evl4s5bTi1yTRRLk%2Ft6qnJ4eu77mPq9aMdS4cKncQqF72cxg%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i1/60141448/TB2J444ev9TBuNjy0FcXXbeiFXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>34.98</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="带连衣裙女2018夏装休闲港味宽松中长裙">带连衣裙女2018夏装休闲港味宽松中长裙</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">枯米枯米</span> 
                    <span class="payNum">138人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.6</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                
                                   <li><span class="lessthan">如实描述:<b>4.6</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                        
                            <li><span class="morethan">服务态度:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                         
                        
                        
                            <li><span class="morethan">发货速度:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=569&amp;e=5Nd9ypJzlyCNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFPoR5qPgtOinr5Wt8SmcVeJDpf4exM0CyBlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAlGnYnqP8PeYJVVbRVda3BVqllIQdmSPrPMB9VZeGNOOZA7Lb%2FV2evr0kcFQlRHg2Mr8yn1DcycJqjQbiC0zUOWkpk%2B%2FmgAL1%2B0H8jyxUDCsHmNfQ8TAhMvwmwska7SH7ous1BrZMB8G13RbE90ggzl%2B3kw0jeFx4nCmrz8yWcCFmos2UYFTsmcR%2FrsRadXjnJfmfhoS5wMpPNmlKPcIeWlm8fiYc5ALICpKhegJIhdzIcFYv4Evl4s5bTi1yTRRLgf33u4M%2BWVBfd5bpocKUS0S2dJT6uoSAA%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i2/123884272/TB2Jgc4cuGSBuNjSspbXXciipXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>1462.50</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="连衣裙女海边波西米亚裙沙滩裙连帽长裙长袖">连衣裙女海边波西米亚裙沙滩裙连帽长裙长袖</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">花海落樱</span> 
                    <span class="payNum">13人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                        <span class="icon"><span class="icon-golden"></span></span>
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.9</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                    <span class="icon"><span class="icon-golden"></span></span>
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=653&amp;e=pTOX4miJ2KyNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFO6DAXkNFa0pjm82wqeggU412qlN8jagdVlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAhiQDflkxY8xWch0YiuJclvJUv6u6OD00Cuk5%2F7JHObY2lzphWpIyTULoI%2Bz9tkeNL5u6%2B%2FQXXGa3UcoWpRdLxo8Z%2Bs74%2FaxqGoi%2BWmf9rZ6BfgclLwM3v%2FkGlQKegVciqTsV4Yb51w0d3INup4kS2m1kuFDyMMm9OFu0xgovYtVEYVTTPUYfHXSwRcmiZ066FZQQYL6BgoJHpzf3AOsVf5zhxSGDEp4ZIGPq8Gl94SWukUuP8nBiAE0j8uN4kRjNp70U%2FVMMLxSlCNcZfIWdDOWYq%2FKpA1qsET%2BNAU49SkYTfNhDHEkyDDhBrPLvsn1d1N3HMX1R8j7BYaiWd2kNs1jHmq%2Bpig%2BhFhVAiAeYDclCaJjp7F7OIE%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i3/1379806069993457067/TB2qH7ashRDOuFjSZFzXXcIipXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>258.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="海颖蕾丝无袖连衣裙修身显瘦中长款A字裙">海颖蕾丝无袖连衣裙修身显瘦中长款A字裙</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">gzsfmy_yxgs</span> 
                    <span class="payNum">0人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.8</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=653&amp;e=jO0%2F5ZF0fmWNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFOsWnkcrHaZxV29Yll19zO6h2KtUCtqm1tlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAsl0%2F2F6foAnR%2Bg9KIheOH03gOUd8dEMDlGnYnqP8PeYJVVbRVda3BUjsd9l4XLXsWX8qh93ux6MR%2B8KrZyWXNpE4mIKgA7%2BP%2BaHSlmG5NbLdV7uoRdOgg9M4P2A%2FplnxfptpjStTWwNGM7yghd21Qk%2BSq2C2yEqjXaKCYTh5TNZN2NapiKS%2Fb4t3uKgwr2aS58d5h%2BCMTQSCgIyhnQkhHUjh2ULo6AT0piGjQO4ntgd7n1CRHjKc%2F8JcPo4vhUy%2FWKqwrB46c2BEfibOfe8n0ooMbc55%2BD6%2FwUSiUnbxu8syF8DamiiwIwqSoXoCSIXcyHBWL%2BBL5eLDFP0NUwAg8oqm1G1DROLT1kw8Yp6sXKVk5bS%2BIHQrgw%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i3/112172600/TB2_Yv9f29TBuNjy1zbXXXpepXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>88.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="圆领雪纺大摆连衣裙修身气质印花沙滩长裙">圆领雪纺大摆连衣裙修身气质印花沙滩长裙</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">芭啦发888</span> 
                    <span class="payNum">20人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.6</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                
                                   <li><span class="lessthan">如实描述:<b>4.6</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=569&amp;e=4zkg1cIG0dWNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFNc%2FG45XefMvT9yY7jcCcyB3fBsIlBntnRlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAlGnYnqP8PeYJVVbRVda3BVqllIQdmSPrPMB9VZeGNOOZA7Lb%2FV2evr0kcFQlRHg2BWgG1HQ3JBaZWqpEEY3%2FmoJFttAvbJOEeq5CEiw5DBF5VftU8JMkaNp%2F6hlFCK3yrMoN9UjMNcZ13RbE90ggzl%2B3kw0jeFx4nCmrz8yWcCFmos2UYFTsmcR%2FrsRadXjnJfmfhoS5wMp2tdn3m2e371HN6izzRTY%2FypKhegJIhdzIcFYv4Evl4s5bTi1yTRRLovW7xQSL4OZGA39%2Fgp%2F9KZ%2Fq1w5fbBCmg%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i4/123133587/TB2hRx8eVmWBuNjSspdXXbugXXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                     
                        <span class="pricedetail">&yen; <strong>1299.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="碎花雪纺连衣裙2018春款中长款七分袖修身裙">碎花雪纺连衣裙2018春款中长款七分袖修身裙</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">浏览过的品牌</span> 
                    <span class="payNum">4人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                        <span class="icon"><span class="icon-golden"></span></span>
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.9</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                    <span class="icon"><span class="icon-golden"></span></span>
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=569&amp;e=PxkMjsRYwMuNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFN438KSUEwbhVyAC%2FwCjnqOxAgsH09VnlVlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAlGnYnqP8PeYJVVbRVda3BVqllIQdmSPrPMB9VZeGNOOZA7Lb%2FV2evr0kcFQlRHg2FD%2Flt%2BK3kGmik3IAeK7BdBuw2pGYLjZsIiDuNb5Vtp2U0UxwcwIQZ3h%2F3YXXgQQ1z%2BULH%2Fp9LT513RbE90ggzl%2B3kw0jeFx4nCmrz8yWcCFmos2UYFTsmcR%2FrsRadXjnJfmfhoS5wMpRRhKFfRVqh4aHMeGt5U4OCpKhegJIhdzIcFYv4Evl4s5bTi1yTRRLi18R%2Fs3jLQjr1wTGMQs5BLhLpHSnYbAfw%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i4/116773682/TB27yw.i7KWBuNjy1zjXXcOypXa_!!2-saturn_solar.png_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>1120.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="滕氏春季长袖翻领中长款一步包臀蕾丝连衣裙">滕氏春季长袖翻领中长款一步包臀蕾丝连衣裙</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">a淘淘乐z</span> 
                    <span class="payNum">0人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.5</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                
                                   <li><span class="lessthan">如实描述:<b>4.5</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                
                                   <li><span class="lessthan">服务态度:<b>4.6</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                
                                   <li><span class="lessthan">发货速度:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=589&amp;e=W47dsxE5ZtqNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFNxu63VMJAe7oP1bwGBkKg3HD%2BjTbZqss9lK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAgasWF5Ct0AVUoFhu2SdZPKfC8tUq5uW93%2BODv%2FfxT3W%2Fl1F6UKNXVqViNY%2BG3b9ZfSRwVCVEeDYouMeoyaZ5dseuErPWUgBPc7Lpb3SW6pC%2FKBHst17A1rNMXUdzE6o21k%2FcZWxQbS427PYJRfjzz7XdFsT3SCDOX7eTDSN4XHicKavPzJZwIWaizZRgVOyZxH%2BuxFp1eOcl%2BZ%2BGhLnAykirj0lUoqZzhHohy42guHEyF8DamiiwIxbE1OEAWuvkrC9ovaYKln5Zd8fmSE190VMNAgJ%2FzRQsV88ZUH%2BpgV8c%2BauUm1hr0I%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i3/131877462/TB2jnQQgVuWBuNjSszbXXcS7FXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>1230.30</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="巴厘岛沙滩裙海边度假显瘦海滩裙衣服女裙子">巴厘岛沙滩裙海边度假显瘦海滩裙衣服女裙子</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">水中丽人</span> 
                    <span class="payNum">12人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">5.0</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>5.0</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>5.0</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>5.0</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=621&amp;e=PE2RbJek6X%2BNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFPm9Ji%2FXVbBYJXf0ofvlXU8OQcLM3PqgXRlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAlGnYnqP8PeY3g9HUIorPp6uuW%2BlivNlfk39GhC664ejCvvb2BeYGacmHEQU5vTPyDM94qXBOf5silpva1sR0%2BhGeIj3w9V1Gu8tckbfNLfASPmx9dXpUVWHxO8e%2Fr51M4REyN0kE3UjvomJAHndu0d0yKxwRRwbGtd0WxPdIIM5KVAPAtG9ByU%2FMrzGqr%2Bjr2svaEbVoVBvZLG3k1qvmn3xRfWbNV%2FsvVacFiyVfuMaXBZ6JWPr%2BTuVADpKqcd9ccl0%2F2F6foAnWoGybExXOdG8O5s04qdCYtvYqJOMcB9N5DRMa%2B3PwLmLISqPGgzOmdrfiMgWV7P7%2FOwXF%2BL2oT4%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i3/15854139/TB2TDWJccIrBKNjSZK9XXagoVXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>89.00</strong></span>
                     
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="韩版时尚碎花女装短袖水墨印花雪纺连衣裙">韩版时尚碎花女装短袖水墨印花雪纺连衣裙</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">如奕旗舰店</span> 
                    <span class="payNum">2人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                    
                        <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.8</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                
                                   <li><span class="lessthan">如实描述:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                        
                            <li><span class="morethan">服务态度:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                         
                        
                        
                            <li><span class="morethan">发货速度:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                    
                    <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=569&amp;e=7pdp4GIsq4ONblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFMwtueFKni9Nfm2u0%2F%2FTcSpsYIKdBkTv9NlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAlGnYnqP8PeYJVVbRVda3BVqllIQdmSPrPMB9VZeGNOOZA7Lb%2FV2evr0kcFQlRHg2Nnv2ig2eNyySxMr6LmTPL6X%2BAOYHtWASj2PRTMRiPG5GWzMqmXYqu4B0HlqJwM9EQCxBmBOwzuZ13RbE90ggzl%2B3kw0jeFx4nCmrz8yWcCFmos2UYFTsmcR%2FrsRadXjnJfmfhoS5wMp5OAp%2BZXEACoOmo6y4qWSZSpKhegJIhdzIcFYv4Evl4s5bTi1yTRRLswb5cEEQWsW7Qt0vuwUm6yLfBaNiqscDw%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i3/TB1kzoleL5TBuNjSspmYXGDRVXa_M2.SS2_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>49.00</strong></span>
                     
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="2018两件套吊带连衣裙中长款短袖显瘦气质裙">2018两件套吊带连衣裙中长款短袖显瘦气质裙</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">wayne215336846</span> 
                    <span class="payNum">1人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.7</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=601&amp;e=ZGkz%2FHL0b4uNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFP2riFXM0qeTRthFTQUWdj9t1nID3phJVxlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAgasWF5Ct0AVe551xPP0CYbfnXbyHSbRwFGnYnqP8PeYJVVbRVda3BWViNY%2BG3b9ZfSRwVCVEeDYhHRVd9tVZat%2BoTk2a22gFZ6%2B4Ld8cTQZffVIGbfP8lLPOAZegQeXSErMRgEU9DIRmoKVhujFfhmV3i9TE4Za%2FnGADOOUBIwv0kadTwms6QWaizZRgVOyZxH%2BuxFp1eOc%2FKB3CIvmfkIgefUtSBeKi5CTBGBjEnfpjQ2PBwxHRSUqSoXoCSIXcyHBWL%2BBL5eL%2BMeiRgsNUnD6yHBdcoWF2x4vrYDumTeetranzrKxFTwt9jPGrsBKNA%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i3/44737477/TB2VDPGg7yWBuNjy0FpXXassXXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>79.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="纯色吊带打底裙 黑色大码背心裙大摆连衣裙">纯色吊带打底裙 黑色大码背心裙大摆连衣裙</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">横行道旗舰店</span> 
                    <span class="payNum">340人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                    
                        <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.9</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                    
                    <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=557&amp;e=o%2FbwMrJ33g%2BNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFM68%2Bdjv7U4KQR9JvpwnhhLt2f4ND6FdlhlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAk2ESNaMxWsaWxNThAFrr5IPhYHiGeYoSEfvCq2cllzaROJiCoAO%2Fj8KOTtpVHX1PvMZZoX922P2yj2%2FtD%2BPqNMKKDm1%2FAgUKF%2F2d%2Bf0s4Umodo%2FQcT4fFoFF5PaDaurWTdjWqYikv2%2BGMHwaFGvZKiWMiX7iRXnPnr6MoY9ZRSp51GtG4rzQNNJy7WdIi%2BSKHVlphdp4NBSnErTvTH6r3Hm8N8wu%2B2ipZbo%2BnFdXwRRHocb%2Bjvs2cV%2FgPiytDveUhc8yQM5ZXySzkAcDvYNlK8%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i1/1989906031329648762/TB2D8nmqSVmpuFjSZFFXXcZApXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                     
                        <span class="pricedetail">&yen; <strong>299.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="春夏新款长裙筒裙V领江南文艺中式中国风">春夏新款长裙筒裙V领江南文艺中式中国风</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">greenlemon旗舰店</span> 
                    <span class="payNum">2人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                    
                        <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.8</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                        
                            <li><span class="morethan">服务态度:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                         
                        
                       
                            
                                
                                   <li><span class="lessthan">发货速度:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                    
                    <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=557&amp;e=Q32dDZewj3eNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFO77ObxBkHM6Z%2F4po4TeUa5diNbzr9zKANlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAreQDVRf3BT4XE%2BZyAkywY6uuW%2BlivNlfjxn6zvj9rGoppHrmKzmDiKcNJnySz0iM%2FXBptw05JFrMj9GrEK%2BTA863btK%2FL9%2BZeWKjJi%2FX2Z9yFAONCPLwskgswIYQmuK20%2FWTk4F7CxtbMY6aNiKpIX2AD2b7C6%2F%2BFaoFiKnEBclqnngaLQ1RdoD6ep3wt6rW3ZxDbD9C0GpRmS4FaYej%2Fyu%2B8U1iefN4dkJbXgOQFYwgdfz95EZ3HMeGfqd7GN8ibZxXl0%2Fij9l9EPx%2FlifsDA%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i2/115264262/TB24j42XP7nBKNjSZLeXXbxCFXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                     
                        <span class="pricedetail">&yen; <strong>399.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="唐嫣款粉色亮片V领连衣裙鱼尾长裙晚礼服女">唐嫣款粉色亮片V领连衣裙鱼尾长裙晚礼服女</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">刘氏外贸企业</span> 
                    <span class="payNum">3人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.7</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=577&amp;e=56Km2vzxaECNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFNj0LkpvPUxOj6Cc82IXmYYjwYlhc2HoitlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAlGnYnqP8PeYJVVbRVda3BVqllIQdmSPrPMB9VZeGNOOZA7Lb%2FV2evr0kcFQlRHg2MX%2Bulok8atVxvfw%2BtDT%2FR89KqttFQkwg3y4q9Ky4%2Bsw5XDhTQ872tQKAhkJ7G7%2BiAskZSlU3MIZ13RbE90ggzkpUA8C0b0HJT8yvMaqv6Ovay9oRtWhUG9ksbeTWq%2BaffFF9Zs1X%2By9xf66WiTxq1XB25GW4lNAp1GnYnqP8PeYJVVbRVda3BUjsd9l4XLXsYO3dX%2BCBuZZ4DjKJpVWCU%2B7dx1QWfoqO7%2BgSQ6CKrN2" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i2/117204576/TB2vYwrgh1YBuNjy1zcXXbNcXXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                     
                        <span class="pricedetail">&yen; <strong>2858.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="立领长袖连衣裙2018裙摆开叉中长款印花">立领长袖连衣裙2018裙摆开叉中长款印花</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">ukukxx女装旗舰店</span> 
                    <span class="payNum">0人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                    
                        <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.8</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                         
                            <li><span class="morethan">如实描述:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                    
                    <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=569&amp;e=ARhgcd3Y3SSNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFODwlyB%2B9eyYu1DEHQz%2BRmSmIkKuH2AdUtlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAlGnYnqP8PeYJVVbRVda3BVqllIQdmSPrPMB9VZeGNOOZA7Lb%2FV2evr0kcFQlRHg2GSZJQyXfqaaI02v380Ggdn6DM%2FZ0vFbJ39CTJtlUXK%2B1eGzRwQf7xmh1%2BdHIU6IeTP41evxloQ%2F13RbE90ggzl%2B3kw0jeFx4nCmrz8yWcCFmos2UYFTsmcR%2FrsRadXjnJfmfhoS5wMpdIq5x7PKQjKACWpmuog%2BbCpKhegJIhdzIcFYv4Evl4s5bTi1yTRRLpFZdTf4FYVC8Q3Cn5UoCpjRs5fhivGI%2Bg%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i4/114256388/TB2_W37eh1YBuNjy1zcXXbNcXXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>1788.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="欧洲站春装2018新款显瘦连衣裙欧货潮中长裙">欧洲站春装2018新款显瘦连衣裙欧货潮中长裙</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">考拉时尚指南</span> 
                    <span class="payNum">2人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                        <span class="icon"><span class="icon-golden"></span></span>
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">5.0</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>5.0</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>5.0</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>5.0</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                    <span class="icon"><span class="icon-golden"></span></span>
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=557&amp;e=vrMb39uCuVSNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFMJWE8c1m3v%2FDznB7BDRsQefmMefKWbyrdlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAk2ESNaMxWsaWxNThAFrr5IPhYHiGeYoSEfvCq2cllzaROJiCoAO%2Fj%2FpbTVWEMKFPM8AdEcKDu2zZl4AxgpxzQ7DIPhx18ks5MQmrskPi1NGn5Vm2rRd%2FB4UDba%2BarMkAobJTTVz2LoxBQEyxp4FgYwLK1q0%2BYIKxWsvaEbVoVBvZLG3k1qvmn3xRfWbNV%2FsvQ%2BqH8VwEp7%2F08D5%2B%2FmApQxXyVW0N8SUINKMJKGcjCAfzsCCF9Vb1kiAyYj%2FjjF5P1npn6fGwfzHLBzkdpOQuM4%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i2/14920476/TB2PquthUR1BeNjy0FmXXb0wVXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>268.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="2018新款夏新款长裙气质V领撞色高腰连衣裙">2018新款夏新款长裙气质V领撞色高腰连衣裙</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">qwewan</span> 
                    <span class="payNum">0人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">5.0</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>5.0</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>5.0</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>5.0</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=589&amp;e=AtwdqOkozp%2BNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFO%2FXuSikESofuENJYC9Cz4cJyieyRTmEyxlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAgasWF5Ct0AVUoFhu2SdZPKfC8tUq5uW93%2BODv%2FfxT3W%2Fl1F6UKNXVqViNY%2BG3b9ZfSRwVCVEeDYB%2FUAuq8tKTvRynkt6WC9ZmRZESAbzVOa%2FrPCBs5h6cGlZ2GrSNrLfTPPJnZVvnZH66nkC9gHiamV3i9TE4Za%2FnOHFIYMSnhkppeOtZD4YcfxRfLvdhp4uJyLUtw6J%2FJRHDuCgX1Ug%2BIQPuFsSiXb9%2FG9SHtUXr6dAfsjJYaiTPn%2BXUXpQo1dWtXCHRcxr4ej4FcnFAH5S14H%2FeoSTYxqKaViKUSlmuTlSzhexUJhmPI%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i4/1012606030761141964/TB2kbNOqHlmpuFjSZFlXXbdQXXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                     
                        <span class="pricedetail">&yen; <strong>66.00</strong></span>
                     
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="天丝棉文艺女装打底连衣长裙宽松大码">天丝棉文艺女装打底连衣长裙宽松大码</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">ansmap1</span> 
                    <span class="payNum">129人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                        <span class="icon"><span class="icon-golden"></span></span>
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.8</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                    <span class="icon"><span class="icon-golden"></span></span>
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=569&amp;e=tc6BeCSzDfCNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFMgBfOtqmWnoW5hUJoL7rA1Ih2gzPddgPdlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAn5GuhUWgnfw2b%2Fi7ijztxHJUv6u6OD00Lh%2BZjBFWcdD%2FnDrnV3kL3Ve6ECyGK3kQZHPJ5MBoiCUf6nOlUvaxIfZzkp4IDgawh4Slhn4y%2BQs3TLPawH6XRY3nVN9uXalk9G3sjx96IQ%2BR0pzkE%2BpzK6eKjbpjOYbZq6UEATRStd751GtG4rzQNNJy7WdIi%2BSKNIOvzXTB3f4dLJfKcULYYh%2BgXEL5hs7D7q3Y5XzxryhXsqv%2FSgeY36LteSk3bTVYO%2B%2FfTBzhojazQ79doqMa5SC1qSGycj4wg%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i3/1700706082477349926/TB22qL8wbXlpuFjy1zbXXb_qpXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                     
                        <span class="pricedetail">&yen; <strong>136.00</strong></span>
                     
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="绵绸碎花和风蝴蝶结背心v领繁花夏季连衣裙">绵绸碎花和风蝴蝶结背心v领繁花夏季连衣裙</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">薰衣娃娃</span> 
                    <span class="payNum">1人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.9</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=577&amp;e=MS5NEh0B%2FgaNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFNj0LkpvPUxOj6Cc82IXmYYmBRgQCTjLwRlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAlGnYnqP8PeYJVVbRVda3BVqllIQdmSPrPMB9VZeGNOOZA7Lb%2FV2evr0kcFQlRHg2AVZDOYUCcXjM1x6ZOgjFX5sXuxHwwhktEugavdTK%2FccP2l6QcbrgFs9%2BUnHU1YxFYxsErqZ%2BZDh13RbE90ggzkpUA8C0b0HJT8yvMaqv6Ovay9oRtWhUG9ksbeTWq%2BaffFF9Zs1X%2By9BVkM5hQJxeMpfTdSr7h6Y1GnYnqP8PeYJVVbRVda3BUjsd9l4XLXsbtT1rRx%2FTvZA8YKRJ6gH3a7dx1QWfoqO7%2BgSQ6CKrN2" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i1/117204576/TB2WpuhguuSBuNjSsziXXbq8pXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>1626.10</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="长袖连衣裙2018镂空中长款修身a字裙">长袖连衣裙2018镂空中长款修身a字裙</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">ukukxx女装旗舰店</span> 
                    <span class="payNum">0人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                    
                        <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.8</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                         
                            <li><span class="morethan">如实描述:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                    
                    <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=569&amp;e=pn9pGuDHpaeNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFPSgK1wJI5tevK5TM5Du%2FP4L6woGUjRkIFlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAlGnYnqP8PeYJVVbRVda3BVqllIQdmSPrPMB9VZeGNOOZA7Lb%2FV2evr0kcFQlRHg2LoGT%2BvSQxA5lJ8EFAz2vgJ35P92HP2FXn2jPDh4UFd8AXtbtmlhfdpEGqqFqlulgCUGh5jFSMV413RbE90ggzl%2B3kw0jeFx4nCmrz8yWcCFmos2UYFTsmcR%2FrsRadXjnJfmfhoS5wMpCO1qmJESvxwdmgP%2F2TJjFypKhegJIhdzIcFYv4Evl4s5bTi1yTRRLllqFIh7eJvHgBne%2BiNvr56c8vA%2BsT7zVw%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i3/116022514/TB2et1TcQyWBuNjy0FpXXassXXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                     
                        <span class="pricedetail">&yen; <strong>56.80</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="夏季新品中长款条纹圆点撞色显瘦衬衫连衣裙">夏季新品中长款条纹圆点撞色显瘦衬衫连衣裙</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">动人的菇凉</span> 
                    <span class="payNum">14人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.7</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=569&amp;e=aOWFfVpH5m%2BNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFNJqIPaF%2Fi1NFCZ0wyqSlfoikjZASZiCQtlK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAlGnYnqP8PeYJVVbRVda3BVqllIQdmSPrPMB9VZeGNOOZA7Lb%2FV2evr0kcFQlRHg2CcxmidjTHRVVSm72foE3HzD6BYy3CEVx6au5noA8ODbgDKImpRrMWuHNzR1lf18AjR2zv4kA37W13RbE90ggzl%2B3kw0jeFx4nCmrz8yWcCFmos2UYFTsmcR%2FrsRadXjnJfmfhoS5wMpXu87PUaUoIoLNrRQDgNLESpKhegJIhdzIcFYv4Evl4s5bTi1yTRRLnyt74I0FCNtMBr7YPSz1pwoLgUfArNmFw%3D%3D" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i2/107118092/TB2uoYogY5YBuNjSspoXXbeNFXa_!!1-saturn_solar.gif_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                     
                        <span class="pricedetail">&yen; <strong>89.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="2018新款学院风卡通绣花可爱猫咪小鱼刺">2018新款学院风卡通绣花可爱猫咪小鱼刺</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">domneves</span> 
                    <span class="payNum">0人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">5.0</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>5.0</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>5.0</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>5.0</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                     
                    
                </p>
            </div>
            </a>
        </div>          
        
        <div class="item">
          <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B92018%20%20%B3%A4&amp;s=1894636897&amp;k=577&amp;e=jnyxov8s09WNblXBXuClYL%2BgSQ6CKrN21HeOwY%2BGJkGb6Klc0%2FS1Oqj9dLd0caUvAJLj7zaETFPynr%2FESnonlMZ1Nk44TRCpz0Pvw%2FGzgTplK7Q29GJWYJa1u%2FWUSIeEamG4QLtrItjmPLSJJwhcMP%2FLuzRa%2FuVKk2cS%2BR5obtbQT7F42qYP07aDdFPc1BWNXfAgsuYFTtiABHH0Pppp9Tk0qBfywxHSKXzk97jsuJboFK9Is9J0kM2mjNUw8na99Hx%2BPX1rGXQEeNTisVDLAlGnYnqP8PeYJVVbRVda3BVqllIQdmSPrPMB9VZeGNOOZA7Lb%2FV2evr0kcFQlRHg2HSpzJHFn6qiUsal%2FvZsPcQtfm8b6PQd6eCp4NXBUlTOYCvYd6yhGBnHI8jGp7pw2vM9bVzYX4sE13RbE90ggzkpUA8C0b0HJT8yvMaqv6Ovay9oRtWhUG9ksbeTWq%2BaffFF9Zs1X%2By9dKnMkcWfqqLhuJmkORQjdlGnYnqP8PeYJVVbRVda3BUjsd9l4XLXsfLRYEDg%2FjG6Bdd6AM%2F0CRq4UnLlTdUhVb%2BgSQ6CKrN2" target="_blank">
            <div class="imgContainer">
                <span class="imgLink">
                    <img data-ks-lazyload="https://img.alicdn.com/imgextra/i3/126855292/TB21vGGgY1YBuNjSszeXXablFXa_!!0-saturn_solar.jpg_260x260.jpg" src="//g.alicdn.com/s.gif">
                </span>
            </div>
            <div class="info"> 
                <!--价格包邮-->
                <p class="price">
                    
                        <span class="pricedetail">&yen; <strong>719.00</strong></span>
                     
                    
                        <span class="postalicon">包邮</span>
                     
                </p>
                <!--价格包邮end-->
                <!--标题-->
                <span class="title" title="韩版时尚立领长袖收腰系带中长款蕾丝连衣裙">韩版时尚立领长袖收腰系带中长款蕾丝连衣裙</span>
                <!--标题end-->
                <!--店铺名称&&付款人数-->
                <p class="shopName">
                    <span class="shopNick">珂媄琳旗舰店</span> 
                    <span class="payNum">0人付款</span>
                </p>
                <!--店铺名称&&付款人数end-->
                <!--描述相符&& logo-->
                <div class="moreInfo">
                    
                        <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                    
                    <div class="dsr-info">

                    <span class="active dsr-info-tgr" href="javascript:;">
                        <span class="icon-btn-dsr">如实描述:</span> 
                        <span class="dsr-info-num">4.9</span>
                        <span class="dropdown-tgr-arrow"></span>
                    </span> 
                    <ul class="dsr-info-list">
                        
                            
                                 
                                   <li><span class="morethan">如实描述:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                        

                       
                            
                                 
                                   <li><span class="morethan">服务态度:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                        
                       
                            
                                 
                                   <li><span class="morethan">发货速度:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                                
                            
                         
                    </ul>
                </div>
                </div>
                <!--描述相符&& logo end-->
                <p class="markers">
                    
                    
                    
                    
                    <span class="icon"><span class="icon-tmall"></span></span>
                     
                    
                </p>
            </div>
            </a>
        </div>          
         
    </div>
    <div id="J_waterfallPagination" class="pagination"></div>
  </div>
</div>

</div>
      <div bx-slot="shopHotsellBtm" data-spm="0782702703" bx-name="p4p/shop-hotsell-btm" bx-version="0.0.1" bx-guid="lego3" hasjs="true" hascss="true" class="p4p-shop-hotsell-btm">


<div class="ManagerHotSale">
    <div class="subTitle">
        <em>掌柜热卖</em> 
        <div id="J_p4plink" data-url="//odin.re.taobao.com/search_stext?catid=&frcatid=&keyword=%E8%BF%9E%E8%A1%A3%E8%A3%992018%20%20%E9%95%BF&tlpid=&refpid=420435_1006&debug=">
          <ul class="p4p-rec-list">
          </ul>
        </div>
        <a href="http://zhitongche.taobao.com" target="_blank" class="p4p-apply">我也要出现在这里</a>
    </div>
    <div class="item-wraper">
         
            <div class="item">
            <div class="imgContainer">
                <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B9%C5%AE&amp;s=698544732&amp;k=537&amp;e=lpX7g7%2BXS9bB32smj6IgslMyOisyLnsAGU0Pp6CHmPk7mYY8UiIwbFwTKE8o70MIovRJbhHG0XqGkSPlNHm8vdKzTVj7kEudPs9diGAI0rZg%2FE2VYzfhiBpzSL2fYjDO%2BxiIEfwpUdiYa1wDMo83oSy%2FTWWQ8UvMc5tgXD4hrJzQN448CQ9F0BG3BAhv6PP1lAuc8rPLlYMYraCmnUWuOtRIUivJaZtJM2pbOtPRk4kIMml1lwoL%2BiUUvbRaBI3Av%2Fd%2F32TqXClHdSFZJYK0wzMc2usOU8wBkkuf9dNPzeW9qmVb867D0%2FpKBN%2FjBhP3jfi%2Ba0W8TAU5VqtILvmcT%2FV7P0SkR1tITPgfHbyMDf0Y8CYDaqFcSD2w8pN35bv4QSFXIK87MQ5QxNZ%2F5yT4RTPMuIBB9m%2BEst7oPgI0ivzEDBhvRY3i6s6onPwXBh3VTcLf6%2FDLH%2FTzmLtCNfXdRFZFmYUkLG5Bxop8B%2BxvTYRPdxI7%2FozXzk2RQ5B7bVLVt6exSUC0Tl3Q3OPWWLr03A%3D%3D" class="imgLink" target="_blank"><img src="https://img.alicdn.com/imgextra/i1/23454997/TB2hIXideGSBuNjSspbXXciipXa_!!0-saturn_solar.jpg_220x220.jpg"></a>   
            </div>
             
            <p class="titleWrap"><a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B9%C5%AE&amp;s=698544732&amp;k=537&amp;e=lpX7g7%2BXS9bB32smj6IgslMyOisyLnsAGU0Pp6CHmPk7mYY8UiIwbFwTKE8o70MIovRJbhHG0XqGkSPlNHm8vdKzTVj7kEudPs9diGAI0rZg%2FE2VYzfhiBpzSL2fYjDO%2BxiIEfwpUdiYa1wDMo83oSy%2FTWWQ8UvMc5tgXD4hrJzQN448CQ9F0BG3BAhv6PP1lAuc8rPLlYMYraCmnUWuOtRIUivJaZtJM2pbOtPRk4kIMml1lwoL%2BiUUvbRaBI3Av%2Fd%2F32TqXClHdSFZJYK0wzMc2usOU8wBkkuf9dNPzeW9qmVb867D0%2FpKBN%2FjBhP3jfi%2Ba0W8TAU5VqtILvmcT%2FV7P0SkR1tITPgfHbyMDf0Y8CYDaqFcSD2w8pN35bv4QSFXIK87MQ5QxNZ%2F5yT4RTPMuIBB9m%2BEst7oPgI0ivzEDBhvRY3i6s6onPwXBh3VTcLf6%2FDLH%2FTzmLtCNfXdRFZFmYUkLG5Bxop8B%2BxvTYRPdxI7%2FozXzk2RQ5B7bVLVt6exSUC0Tl3Q3OPWWLr03A%3D%3D" target="_blank" class="title" title="$!{k.title}">2018春装新款女装 ins超火裙子 v</a></p>
             
            <div class="info">
              
              <p class="price"><a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B9%C5%AE&amp;s=698544732&amp;k=537&amp;e=lpX7g7%2BXS9bB32smj6IgslMyOisyLnsAGU0Pp6CHmPk7mYY8UiIwbFwTKE8o70MIovRJbhHG0XqGkSPlNHm8vdKzTVj7kEudPs9diGAI0rZg%2FE2VYzfhiBpzSL2fYjDO%2BxiIEfwpUdiYa1wDMo83oSy%2FTWWQ8UvMc5tgXD4hrJzQN448CQ9F0BG3BAhv6PP1lAuc8rPLlYMYraCmnUWuOtRIUivJaZtJM2pbOtPRk4kIMml1lwoL%2BiUUvbRaBI3Av%2Fd%2F32TqXClHdSFZJYK0wzMc2usOU8wBkkuf9dNPzeW9qmVb867D0%2FpKBN%2FjBhP3jfi%2Ba0W8TAU5VqtILvmcT%2FV7P0SkR1tITPgfHbyMDf0Y8CYDaqFcSD2w8pN35bv4QSFXIK87MQ5QxNZ%2F5yT4RTPMuIBB9m%2BEst7oPgI0ivzEDBhvRY3i6s6onPwXBh3VTcLf6%2FDLH%2FTzmLtCNfXdRFZFmYUkLG5Bxop8B%2BxvTYRPdxI7%2FozXzk2RQ5B7bVLVt6exSUC0Tl3Q3OPWWLr03A%3D%3D" target="_blank">&yen; <strong>119.90</strong></a>
               
              </p>
              <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B9%C5%AE&amp;s=698544732&amp;k=537&amp;e=lpX7g7%2BXS9bB32smj6IgslMyOisyLnsAGU0Pp6CHmPk7mYY8UiIwbFwTKE8o70MIovRJbhHG0XqGkSPlNHm8vdKzTVj7kEudPs9diGAI0rZg%2FE2VYzfhiBpzSL2fYjDO%2BxiIEfwpUdiYa1wDMo83oSy%2FTWWQ8UvMc5tgXD4hrJzQN448CQ9F0BG3BAhv6PP1lAuc8rPLlYMYraCmnUWuOtRIUivJaZtJM2pbOtPRk4kIMml1lwoL%2BiUUvbRaBI3Av%2Fd%2F32TqXClHdSFZJYK0wzMc2usOU8wBkkuf9dNPzeW9qmVb867D0%2FpKBN%2FjBhP3jfi%2Ba0W8TAU5VqtILvmcT%2FV7P0SkR1tITPgfHbyMDf0Y8CYDaqFcSD2w8pN35bv4QSFXIK87MQ5QxNZ%2F5yT4RTPMuIBB9m%2BEst7oPgI0ivzEDBhvRY3i6s6onPwXBh3VTcLf6%2FDLH%2FTzmLtCNfXdRFZFmYUkLG5Bxop8B%2BxvTYRPdxI7%2FozXzk2RQ5B7bVLVt6exSUC0Tl3Q3OPWWLr03A%3D%3D" target="_blank" class="sales">销量：7075</a>
              <div class="dsr-info">
                  <a class="active dsr-info-tgr" href="javascript:;">
                      <span class="icon-btn-dsr">如实描述:</span> 
                      <span class="dsr-info-num">4.7</span>
                      <span class="dropdown-tgr-arrow"></span>
                  </a> 
                  <ul class="dsr-info-list">
                      
                          
                               
                                 <li><span class="morethan">如实描述:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                              
                          
                      

                     
                          
                               
                                 <li><span class="morethan">服务态度:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                              
                          
                       
                      
                     
                          
                               
                                 <li><span class="morethan">发货速度:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                              
                          
                      
                  </ul>
              </div>
            </div>
        </div>
         
            <div class="item">
            <div class="imgContainer">
                <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B9%C5%AE&amp;s=698544732&amp;k=537&amp;e=jxGJDEMLetbB32smj6IgslMyOisyLnsAGU0Pp6CHmPk7mYY8UiIwbFwTKE8o70MIovRJbhHG0XqT8zFg%2BAnrpZAza1djm92xur9PPKcTcKFg%2FE2VYzfhiBpzSL2fYjDO%2BxiIEfwpUdiYa1wDMo83oSy%2FTWWQ8UvMc5tgXD4hrJzQN448CQ9F0BG3BAhv6PP1lAuc8rPLlYMYraCmnUWuOtRIUivJaZtJM2pbOtPRk4kIMml1lwoL%2BiUUvbRaBI3Av%2Fd%2F32TqXCnxN6uQGfdIok3PCacexgSbBaAieIlVe%2FG9qmVb867D038UwmRXILtyc58vX8ASTRmqTvxxqDi807oGx0rUys5fm5yKqiOR6fSfAt5AQd2Kmr142vHEq8Xoks6909j5E0tQxNZ%2F5yT4RTPMuIBB9m%2BEst7oPgI0ivzEDBhvRY3i6s6onPwXBh3VBZnvArl5pXIOpi0RDUa4PFZFmYUkLG5Bxop8B%2BxvTYRPdxI7%2FozXzvdbGCxwKFq%2BrkD1sWNdvlPJFkrIVxrNMQ%3D%3D" class="imgLink" target="_blank"><img src="https://img.alicdn.com/imgextra/i2/28329668/TB2jSJKjkyWBuNjy0FpXXassXXa_!!0-saturn_solar.jpg_220x220.jpg"></a>   
            </div>
             
            <p class="titleWrap"><a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B9%C5%AE&amp;s=698544732&amp;k=537&amp;e=jxGJDEMLetbB32smj6IgslMyOisyLnsAGU0Pp6CHmPk7mYY8UiIwbFwTKE8o70MIovRJbhHG0XqT8zFg%2BAnrpZAza1djm92xur9PPKcTcKFg%2FE2VYzfhiBpzSL2fYjDO%2BxiIEfwpUdiYa1wDMo83oSy%2FTWWQ8UvMc5tgXD4hrJzQN448CQ9F0BG3BAhv6PP1lAuc8rPLlYMYraCmnUWuOtRIUivJaZtJM2pbOtPRk4kIMml1lwoL%2BiUUvbRaBI3Av%2Fd%2F32TqXCnxN6uQGfdIok3PCacexgSbBaAieIlVe%2FG9qmVb867D038UwmRXILtyc58vX8ASTRmqTvxxqDi807oGx0rUys5fm5yKqiOR6fSfAt5AQd2Kmr142vHEq8Xoks6909j5E0tQxNZ%2F5yT4RTPMuIBB9m%2BEst7oPgI0ivzEDBhvRY3i6s6onPwXBh3VBZnvArl5pXIOpi0RDUa4PFZFmYUkLG5Bxop8B%2BxvTYRPdxI7%2FozXzvdbGCxwKFq%2BrkD1sWNdvlPJFkrIVxrNMQ%3D%3D" target="_blank" class="title" title="$!{k.title}">镂空刺绣方领喇叭袖荷叶摆裙仙气质连衣裙</a></p>
             
            <div class="info">
              
              <p class="price"><a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B9%C5%AE&amp;s=698544732&amp;k=537&amp;e=jxGJDEMLetbB32smj6IgslMyOisyLnsAGU0Pp6CHmPk7mYY8UiIwbFwTKE8o70MIovRJbhHG0XqT8zFg%2BAnrpZAza1djm92xur9PPKcTcKFg%2FE2VYzfhiBpzSL2fYjDO%2BxiIEfwpUdiYa1wDMo83oSy%2FTWWQ8UvMc5tgXD4hrJzQN448CQ9F0BG3BAhv6PP1lAuc8rPLlYMYraCmnUWuOtRIUivJaZtJM2pbOtPRk4kIMml1lwoL%2BiUUvbRaBI3Av%2Fd%2F32TqXCnxN6uQGfdIok3PCacexgSbBaAieIlVe%2FG9qmVb867D038UwmRXILtyc58vX8ASTRmqTvxxqDi807oGx0rUys5fm5yKqiOR6fSfAt5AQd2Kmr142vHEq8Xoks6909j5E0tQxNZ%2F5yT4RTPMuIBB9m%2BEst7oPgI0ivzEDBhvRY3i6s6onPwXBh3VBZnvArl5pXIOpi0RDUa4PFZFmYUkLG5Bxop8B%2BxvTYRPdxI7%2FozXzvdbGCxwKFq%2BrkD1sWNdvlPJFkrIVxrNMQ%3D%3D" target="_blank">&yen; <strong>328.00</strong></a>
               
              </p>
              <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B9%C5%AE&amp;s=698544732&amp;k=537&amp;e=jxGJDEMLetbB32smj6IgslMyOisyLnsAGU0Pp6CHmPk7mYY8UiIwbFwTKE8o70MIovRJbhHG0XqT8zFg%2BAnrpZAza1djm92xur9PPKcTcKFg%2FE2VYzfhiBpzSL2fYjDO%2BxiIEfwpUdiYa1wDMo83oSy%2FTWWQ8UvMc5tgXD4hrJzQN448CQ9F0BG3BAhv6PP1lAuc8rPLlYMYraCmnUWuOtRIUivJaZtJM2pbOtPRk4kIMml1lwoL%2BiUUvbRaBI3Av%2Fd%2F32TqXCnxN6uQGfdIok3PCacexgSbBaAieIlVe%2FG9qmVb867D038UwmRXILtyc58vX8ASTRmqTvxxqDi807oGx0rUys5fm5yKqiOR6fSfAt5AQd2Kmr142vHEq8Xoks6909j5E0tQxNZ%2F5yT4RTPMuIBB9m%2BEst7oPgI0ivzEDBhvRY3i6s6onPwXBh3VBZnvArl5pXIOpi0RDUa4PFZFmYUkLG5Bxop8B%2BxvTYRPdxI7%2FozXzvdbGCxwKFq%2BrkD1sWNdvlPJFkrIVxrNMQ%3D%3D" target="_blank" class="sales">销量：12</a>
              <div class="dsr-info">
                  <a class="active dsr-info-tgr" href="javascript:;">
                      <span class="icon-btn-dsr">如实描述:</span> 
                      <span class="dsr-info-num">4.8</span>
                      <span class="dropdown-tgr-arrow"></span>
                  </a> 
                  <ul class="dsr-info-list">
                      
                          
                               
                                 <li><span class="morethan">如实描述:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                              
                          
                      

                     
                          
                               
                                 <li><span class="morethan">服务态度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                              
                          
                       
                      
                     
                          
                               
                                 <li><span class="morethan">发货速度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                              
                          
                      
                  </ul>
              </div>
            </div>
        </div>
         
            <div class="item">
            <div class="imgContainer">
                <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B9%C5%AE&amp;s=698544732&amp;k=537&amp;e=9YIpE0GkGiLB32smj6IgslMyOisyLnsAGU0Pp6CHmPk7mYY8UiIwbFwTKE8o70MIovRJbhHG0XowBntrZbqP6uM9fZttsglEbTrYncm3KNBg%2FE2VYzfhiBpzSL2fYjDO%2BxiIEfwpUdiYa1wDMo83oSy%2FTWWQ8UvMc5tgXD4hrJzQN448CQ9F0BG3BAhv6PP1lAuc8rPLlYMYraCmnUWuOtRIUivJaZtJM2pbOtPRk4kIMml1lwoL%2BiUUvbRaBI3Av%2Fd%2F32TqXCnxN6uQGfdIok3PCacexgSbBaAieIlVe%2FG9qmVb867D0yTrc%2BkRRgMtkbdPOuGcZx32jGYyL1R%2FdSvw%2BXCktPEec4jmHg0Ke8lnWa2d3S6qrNKZf8BN7PNVJaZd31iBNACRTZ%2Bcsu9%2FNcxuvQiCe%2F2yl4hYJrHB%2BbjEDBhvRY3i6s6onPwXBh3V0zqtTaOIILyTa1Zud8t8NFZFmYUkLG5Bxop8B%2BxvTYRPdxI7%2FozXztyUjie0nNjIz9pToe14ZJK1k%2Fzy2A2xSQ%3D%3D" class="imgLink" target="_blank"><img src="https://img.alicdn.com/imgextra/i4/32635820/TB2PwYrh7CWBuNjy0FaXXXUlXXa_!!0-saturn_solar.jpg_220x220.jpg"></a>   
            </div>
            
            <p class="titleWrap"><span class="icon-tmall"></span><a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B9%C5%AE&amp;s=698544732&amp;k=537&amp;e=9YIpE0GkGiLB32smj6IgslMyOisyLnsAGU0Pp6CHmPk7mYY8UiIwbFwTKE8o70MIovRJbhHG0XowBntrZbqP6uM9fZttsglEbTrYncm3KNBg%2FE2VYzfhiBpzSL2fYjDO%2BxiIEfwpUdiYa1wDMo83oSy%2FTWWQ8UvMc5tgXD4hrJzQN448CQ9F0BG3BAhv6PP1lAuc8rPLlYMYraCmnUWuOtRIUivJaZtJM2pbOtPRk4kIMml1lwoL%2BiUUvbRaBI3Av%2Fd%2F32TqXCnxN6uQGfdIok3PCacexgSbBaAieIlVe%2FG9qmVb867D0yTrc%2BkRRgMtkbdPOuGcZx32jGYyL1R%2FdSvw%2BXCktPEec4jmHg0Ke8lnWa2d3S6qrNKZf8BN7PNVJaZd31iBNACRTZ%2Bcsu9%2FNcxuvQiCe%2F2yl4hYJrHB%2BbjEDBhvRY3i6s6onPwXBh3V0zqtTaOIILyTa1Zud8t8NFZFmYUkLG5Bxop8B%2BxvTYRPdxI7%2FozXztyUjie0nNjIz9pToe14ZJK1k%2Fzy2A2xSQ%3D%3D" target="_blank" class="title" title="$!{k.title}">黑色百褶裙圆领修身连衣裙女春装2018新款</a></p>
             
            <div class="info">
              
              <p class="price"><a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B9%C5%AE&amp;s=698544732&amp;k=537&amp;e=9YIpE0GkGiLB32smj6IgslMyOisyLnsAGU0Pp6CHmPk7mYY8UiIwbFwTKE8o70MIovRJbhHG0XowBntrZbqP6uM9fZttsglEbTrYncm3KNBg%2FE2VYzfhiBpzSL2fYjDO%2BxiIEfwpUdiYa1wDMo83oSy%2FTWWQ8UvMc5tgXD4hrJzQN448CQ9F0BG3BAhv6PP1lAuc8rPLlYMYraCmnUWuOtRIUivJaZtJM2pbOtPRk4kIMml1lwoL%2BiUUvbRaBI3Av%2Fd%2F32TqXCnxN6uQGfdIok3PCacexgSbBaAieIlVe%2FG9qmVb867D0yTrc%2BkRRgMtkbdPOuGcZx32jGYyL1R%2FdSvw%2BXCktPEec4jmHg0Ke8lnWa2d3S6qrNKZf8BN7PNVJaZd31iBNACRTZ%2Bcsu9%2FNcxuvQiCe%2F2yl4hYJrHB%2BbjEDBhvRY3i6s6onPwXBh3V0zqtTaOIILyTa1Zud8t8NFZFmYUkLG5Bxop8B%2BxvTYRPdxI7%2FozXztyUjie0nNjIz9pToe14ZJK1k%2Fzy2A2xSQ%3D%3D" target="_blank">&yen; <strong>308.00</strong></a>
              <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B9%C5%AE&amp;s=698544732&amp;k=537&amp;e=9YIpE0GkGiLB32smj6IgslMyOisyLnsAGU0Pp6CHmPk7mYY8UiIwbFwTKE8o70MIovRJbhHG0XowBntrZbqP6uM9fZttsglEbTrYncm3KNBg%2FE2VYzfhiBpzSL2fYjDO%2BxiIEfwpUdiYa1wDMo83oSy%2FTWWQ8UvMc5tgXD4hrJzQN448CQ9F0BG3BAhv6PP1lAuc8rPLlYMYraCmnUWuOtRIUivJaZtJM2pbOtPRk4kIMml1lwoL%2BiUUvbRaBI3Av%2Fd%2F32TqXCnxN6uQGfdIok3PCacexgSbBaAieIlVe%2FG9qmVb867D0yTrc%2BkRRgMtkbdPOuGcZx32jGYyL1R%2FdSvw%2BXCktPEec4jmHg0Ke8lnWa2d3S6qrNKZf8BN7PNVJaZd31iBNACRTZ%2Bcsu9%2FNcxuvQiCe%2F2yl4hYJrHB%2BbjEDBhvRY3i6s6onPwXBh3V0zqtTaOIILyTa1Zud8t8NFZFmYUkLG5Bxop8B%2BxvTYRPdxI7%2FozXztyUjie0nNjIz9pToe14ZJK1k%2Fzy2A2xSQ%3D%3D" target="_blank" style="color:#aaa;"><span class="origin-price">&yen;615.00</span></a>
               
              </p>
              <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B9%C5%AE&amp;s=698544732&amp;k=537&amp;e=9YIpE0GkGiLB32smj6IgslMyOisyLnsAGU0Pp6CHmPk7mYY8UiIwbFwTKE8o70MIovRJbhHG0XowBntrZbqP6uM9fZttsglEbTrYncm3KNBg%2FE2VYzfhiBpzSL2fYjDO%2BxiIEfwpUdiYa1wDMo83oSy%2FTWWQ8UvMc5tgXD4hrJzQN448CQ9F0BG3BAhv6PP1lAuc8rPLlYMYraCmnUWuOtRIUivJaZtJM2pbOtPRk4kIMml1lwoL%2BiUUvbRaBI3Av%2Fd%2F32TqXCnxN6uQGfdIok3PCacexgSbBaAieIlVe%2FG9qmVb867D0yTrc%2BkRRgMtkbdPOuGcZx32jGYyL1R%2FdSvw%2BXCktPEec4jmHg0Ke8lnWa2d3S6qrNKZf8BN7PNVJaZd31iBNACRTZ%2Bcsu9%2FNcxuvQiCe%2F2yl4hYJrHB%2BbjEDBhvRY3i6s6onPwXBh3V0zqtTaOIILyTa1Zud8t8NFZFmYUkLG5Bxop8B%2BxvTYRPdxI7%2FozXztyUjie0nNjIz9pToe14ZJK1k%2Fzy2A2xSQ%3D%3D" target="_blank" class="sales">销量：102</a>
              <div class="dsr-info">
                  <a class="active dsr-info-tgr" href="javascript:;">
                      <span class="icon-btn-dsr">如实描述:</span> 
                      <span class="dsr-info-num">4.9</span>
                      <span class="dropdown-tgr-arrow"></span>
                  </a> 
                  <ul class="dsr-info-list">
                      
                          
                               
                                 <li><span class="morethan">如实描述:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                              
                          
                      

                     
                          
                               
                                 <li><span class="morethan">服务态度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                              
                          
                       
                      
                     
                          
                               
                                 <li><span class="morethan">发货速度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                              
                          
                      
                  </ul>
              </div>
            </div>
        </div>
         
            <div class="item">
            <div class="imgContainer">
                <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B9%C5%AE&amp;s=698544732&amp;k=537&amp;e=83o1%2FOYDcAXB32smj6IgslMyOisyLnsAGU0Pp6CHmPk7mYY8UiIwbFwTKE8o70MIovRJbhHG0XogS4TLJDZDN8eoTABHI0LegDa%2B60N7Qxlg%2FE2VYzfhiBpzSL2fYjDO%2BxiIEfwpUdiYa1wDMo83oSy%2FTWWQ8UvMc5tgXD4hrJzQN448CQ9F0BG3BAhv6PP1lAuc8rPLlYMYraCmnUWuOtRIUivJaZtJM2pbOtPRk4kIMml1lwoL%2BiUUvbRaBI3Av%2Fd%2F32TqXClHdSFZJYK0wzMc2usOU8wBkkuf9dNPzeXPahZ92WsoMJ4%2BN%2F%2Botl3uZx6ymYzwQU%2BPBBEsh8uBx7FHlGr%2FL3AV4K%2BsVDW%2BhPo1eT3fkQozWwYa5C5fUzuIMZz%2FqmxunvcgWwjp1cA3dInC3KSWZfKpeMVooVCTsVA6bxJ1Dw2EBxpOAPeApIVpt2o8PIrXNaq181bPMKryLifWCeQInmQyje7Y29n64QHgARyoxidqVumSI5b4DtnJdsEtpNSwtVjVL105Sc5F6Q%3D%3D" class="imgLink" target="_blank"><img src="https://img.alicdn.com/imgextra/i1/111892814/TB2tdeMgpmWBuNjSspdXXbugXXa_!!0-saturn_solar.jpg_220x220.jpg"></a>   
            </div>
             
            <p class="titleWrap"><a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B9%C5%AE&amp;s=698544732&amp;k=537&amp;e=83o1%2FOYDcAXB32smj6IgslMyOisyLnsAGU0Pp6CHmPk7mYY8UiIwbFwTKE8o70MIovRJbhHG0XogS4TLJDZDN8eoTABHI0LegDa%2B60N7Qxlg%2FE2VYzfhiBpzSL2fYjDO%2BxiIEfwpUdiYa1wDMo83oSy%2FTWWQ8UvMc5tgXD4hrJzQN448CQ9F0BG3BAhv6PP1lAuc8rPLlYMYraCmnUWuOtRIUivJaZtJM2pbOtPRk4kIMml1lwoL%2BiUUvbRaBI3Av%2Fd%2F32TqXClHdSFZJYK0wzMc2usOU8wBkkuf9dNPzeXPahZ92WsoMJ4%2BN%2F%2Botl3uZx6ymYzwQU%2BPBBEsh8uBx7FHlGr%2FL3AV4K%2BsVDW%2BhPo1eT3fkQozWwYa5C5fUzuIMZz%2FqmxunvcgWwjp1cA3dInC3KSWZfKpeMVooVCTsVA6bxJ1Dw2EBxpOAPeApIVpt2o8PIrXNaq181bPMKryLifWCeQInmQyje7Y29n64QHgARyoxidqVumSI5b4DtnJdsEtpNSwtVjVL105Sc5F6Q%3D%3D" target="_blank" class="title" title="$!{k.title}">松本公司纯原轻奢2018春装新款秋法式刺</a></p>
             
            <div class="info">
              
              <p class="price"><a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B9%C5%AE&amp;s=698544732&amp;k=537&amp;e=83o1%2FOYDcAXB32smj6IgslMyOisyLnsAGU0Pp6CHmPk7mYY8UiIwbFwTKE8o70MIovRJbhHG0XogS4TLJDZDN8eoTABHI0LegDa%2B60N7Qxlg%2FE2VYzfhiBpzSL2fYjDO%2BxiIEfwpUdiYa1wDMo83oSy%2FTWWQ8UvMc5tgXD4hrJzQN448CQ9F0BG3BAhv6PP1lAuc8rPLlYMYraCmnUWuOtRIUivJaZtJM2pbOtPRk4kIMml1lwoL%2BiUUvbRaBI3Av%2Fd%2F32TqXClHdSFZJYK0wzMc2usOU8wBkkuf9dNPzeXPahZ92WsoMJ4%2BN%2F%2Botl3uZx6ymYzwQU%2BPBBEsh8uBx7FHlGr%2FL3AV4K%2BsVDW%2BhPo1eT3fkQozWwYa5C5fUzuIMZz%2FqmxunvcgWwjp1cA3dInC3KSWZfKpeMVooVCTsVA6bxJ1Dw2EBxpOAPeApIVpt2o8PIrXNaq181bPMKryLifWCeQInmQyje7Y29n64QHgARyoxidqVumSI5b4DtnJdsEtpNSwtVjVL105Sc5F6Q%3D%3D" target="_blank">&yen; <strong>98.00</strong></a>
               
              </p>
              <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B9%C5%AE&amp;s=698544732&amp;k=537&amp;e=83o1%2FOYDcAXB32smj6IgslMyOisyLnsAGU0Pp6CHmPk7mYY8UiIwbFwTKE8o70MIovRJbhHG0XogS4TLJDZDN8eoTABHI0LegDa%2B60N7Qxlg%2FE2VYzfhiBpzSL2fYjDO%2BxiIEfwpUdiYa1wDMo83oSy%2FTWWQ8UvMc5tgXD4hrJzQN448CQ9F0BG3BAhv6PP1lAuc8rPLlYMYraCmnUWuOtRIUivJaZtJM2pbOtPRk4kIMml1lwoL%2BiUUvbRaBI3Av%2Fd%2F32TqXClHdSFZJYK0wzMc2usOU8wBkkuf9dNPzeXPahZ92WsoMJ4%2BN%2F%2Botl3uZx6ymYzwQU%2BPBBEsh8uBx7FHlGr%2FL3AV4K%2BsVDW%2BhPo1eT3fkQozWwYa5C5fUzuIMZz%2FqmxunvcgWwjp1cA3dInC3KSWZfKpeMVooVCTsVA6bxJ1Dw2EBxpOAPeApIVpt2o8PIrXNaq181bPMKryLifWCeQInmQyje7Y29n64QHgARyoxidqVumSI5b4DtnJdsEtpNSwtVjVL105Sc5F6Q%3D%3D" target="_blank" class="sales">销量：72</a>
              <div class="dsr-info">
                  <a class="active dsr-info-tgr" href="javascript:;">
                      <span class="icon-btn-dsr">如实描述:</span> 
                      <span class="dsr-info-num">4.8</span>
                      <span class="dropdown-tgr-arrow"></span>
                  </a> 
                  <ul class="dsr-info-list">
                      
                          
                               
                                 <li><span class="morethan">如实描述:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                              
                          
                      

                     
                          
                               
                                 <li><span class="morethan">服务态度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                              
                          
                       
                      
                     
                          
                               
                                 <li><span class="morethan">发货速度:<b>4.9</b></span><span class="listup-tgr-arrow"></span></li>
                              
                          
                      
                  </ul>
              </div>
            </div>
        </div>
         
            <div class="item">
            <div class="imgContainer">
                <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B9%C5%AE&amp;s=698544732&amp;k=537&amp;e=xQwnlude0BfB32smj6IgslMyOisyLnsAGU0Pp6CHmPk7mYY8UiIwbFwTKE8o70MIovRJbhHG0Xq5X5Nh4TwlWW0RqG7W4Cu%2Ffu4jnHzHxt5g%2FE2VYzfhiBpzSL2fYjDO%2BxiIEfwpUdiYa1wDMo83oSy%2FTWWQ8UvMc5tgXD4hrJzQN448CQ9F0BG3BAhv6PP1lAuc8rPLlYMYraCmnUWuOtRIUivJaZtJM2pbOtPRk4kIMml1lwoL%2BiUUvbRaBI3Av%2Fd%2F32TqXCnxN6uQGfdIok3PCacexgSbBaAieIlVe%2FG9qmVb867D07zDAwgWrQA%2F7W8Ihf%2F%2F9%2F9brC5Uds1htT2kaHbhBF8Jo0JKPmkl268chnkHsL0xISNC4pyBtpzJh%2FnOktBghdlQxNZ%2F5yT4RTPMuIBB9m%2BEst7oPgI0ivzEDBhvRY3i6s6onPwXBh3VRrUX6PIg%2BZtB2iOqOJuD0VZFmYUkLG5Bxop8B%2BxvTYRPdxI7%2FozXzt8ecim%2FWPekpIYSKUBelTNfuqnxFf0WEQ%3D%3D" class="imgLink" target="_blank"><img src="https://img.alicdn.com/imgextra/i2/31883698/TB2kN8og_tYBeNjy1XdXXXXyVXa_!!0-saturn_solar.jpg_220x220.jpg"></a>   
            </div>
             
            <p class="titleWrap"><a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B9%C5%AE&amp;s=698544732&amp;k=537&amp;e=xQwnlude0BfB32smj6IgslMyOisyLnsAGU0Pp6CHmPk7mYY8UiIwbFwTKE8o70MIovRJbhHG0Xq5X5Nh4TwlWW0RqG7W4Cu%2Ffu4jnHzHxt5g%2FE2VYzfhiBpzSL2fYjDO%2BxiIEfwpUdiYa1wDMo83oSy%2FTWWQ8UvMc5tgXD4hrJzQN448CQ9F0BG3BAhv6PP1lAuc8rPLlYMYraCmnUWuOtRIUivJaZtJM2pbOtPRk4kIMml1lwoL%2BiUUvbRaBI3Av%2Fd%2F32TqXCnxN6uQGfdIok3PCacexgSbBaAieIlVe%2FG9qmVb867D07zDAwgWrQA%2F7W8Ihf%2F%2F9%2F9brC5Uds1htT2kaHbhBF8Jo0JKPmkl268chnkHsL0xISNC4pyBtpzJh%2FnOktBghdlQxNZ%2F5yT4RTPMuIBB9m%2BEst7oPgI0ivzEDBhvRY3i6s6onPwXBh3VRrUX6PIg%2BZtB2iOqOJuD0VZFmYUkLG5Bxop8B%2BxvTYRPdxI7%2FozXzt8ecim%2FWPekpIYSKUBelTNfuqnxFf0WEQ%3D%3D" target="_blank" class="title" title="$!{k.title}">夏装女装修身显瘦大码短袖桑蚕丝连衣裙真丝</a></p>
             
            <div class="info">
              
              <p class="price"><a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B9%C5%AE&amp;s=698544732&amp;k=537&amp;e=xQwnlude0BfB32smj6IgslMyOisyLnsAGU0Pp6CHmPk7mYY8UiIwbFwTKE8o70MIovRJbhHG0Xq5X5Nh4TwlWW0RqG7W4Cu%2Ffu4jnHzHxt5g%2FE2VYzfhiBpzSL2fYjDO%2BxiIEfwpUdiYa1wDMo83oSy%2FTWWQ8UvMc5tgXD4hrJzQN448CQ9F0BG3BAhv6PP1lAuc8rPLlYMYraCmnUWuOtRIUivJaZtJM2pbOtPRk4kIMml1lwoL%2BiUUvbRaBI3Av%2Fd%2F32TqXCnxN6uQGfdIok3PCacexgSbBaAieIlVe%2FG9qmVb867D07zDAwgWrQA%2F7W8Ihf%2F%2F9%2F9brC5Uds1htT2kaHbhBF8Jo0JKPmkl268chnkHsL0xISNC4pyBtpzJh%2FnOktBghdlQxNZ%2F5yT4RTPMuIBB9m%2BEst7oPgI0ivzEDBhvRY3i6s6onPwXBh3VRrUX6PIg%2BZtB2iOqOJuD0VZFmYUkLG5Bxop8B%2BxvTYRPdxI7%2FozXzt8ecim%2FWPekpIYSKUBelTNfuqnxFf0WEQ%3D%3D" target="_blank">&yen; <strong>198.00</strong></a>
              <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B9%C5%AE&amp;s=698544732&amp;k=537&amp;e=xQwnlude0BfB32smj6IgslMyOisyLnsAGU0Pp6CHmPk7mYY8UiIwbFwTKE8o70MIovRJbhHG0Xq5X5Nh4TwlWW0RqG7W4Cu%2Ffu4jnHzHxt5g%2FE2VYzfhiBpzSL2fYjDO%2BxiIEfwpUdiYa1wDMo83oSy%2FTWWQ8UvMc5tgXD4hrJzQN448CQ9F0BG3BAhv6PP1lAuc8rPLlYMYraCmnUWuOtRIUivJaZtJM2pbOtPRk4kIMml1lwoL%2BiUUvbRaBI3Av%2Fd%2F32TqXCnxN6uQGfdIok3PCacexgSbBaAieIlVe%2FG9qmVb867D07zDAwgWrQA%2F7W8Ihf%2F%2F9%2F9brC5Uds1htT2kaHbhBF8Jo0JKPmkl268chnkHsL0xISNC4pyBtpzJh%2FnOktBghdlQxNZ%2F5yT4RTPMuIBB9m%2BEst7oPgI0ivzEDBhvRY3i6s6onPwXBh3VRrUX6PIg%2BZtB2iOqOJuD0VZFmYUkLG5Bxop8B%2BxvTYRPdxI7%2FozXzt8ecim%2FWPekpIYSKUBelTNfuqnxFf0WEQ%3D%3D" target="_blank" style="color:#aaa;"><span class="origin-price">&yen;490.00</span></a>
               
              </p>
              <a href="https://click.simba.taobao.com/cc_im?p=%C1%AC%D2%C2%C8%B9%C5%AE&amp;s=698544732&amp;k=537&amp;e=xQwnlude0BfB32smj6IgslMyOisyLnsAGU0Pp6CHmPk7mYY8UiIwbFwTKE8o70MIovRJbhHG0Xq5X5Nh4TwlWW0RqG7W4Cu%2Ffu4jnHzHxt5g%2FE2VYzfhiBpzSL2fYjDO%2BxiIEfwpUdiYa1wDMo83oSy%2FTWWQ8UvMc5tgXD4hrJzQN448CQ9F0BG3BAhv6PP1lAuc8rPLlYMYraCmnUWuOtRIUivJaZtJM2pbOtPRk4kIMml1lwoL%2BiUUvbRaBI3Av%2Fd%2F32TqXCnxN6uQGfdIok3PCacexgSbBaAieIlVe%2FG9qmVb867D07zDAwgWrQA%2F7W8Ihf%2F%2F9%2F9brC5Uds1htT2kaHbhBF8Jo0JKPmkl268chnkHsL0xISNC4pyBtpzJh%2FnOktBghdlQxNZ%2F5yT4RTPMuIBB9m%2BEst7oPgI0ivzEDBhvRY3i6s6onPwXBh3VRrUX6PIg%2BZtB2iOqOJuD0VZFmYUkLG5Bxop8B%2BxvTYRPdxI7%2FozXzt8ecim%2FWPekpIYSKUBelTNfuqnxFf0WEQ%3D%3D" target="_blank" class="sales">销量：375</a>
              <div class="dsr-info">
                  <a class="active dsr-info-tgr" href="javascript:;">
                      <span class="icon-btn-dsr">如实描述:</span> 
                      <span class="dsr-info-num">4.7</span>
                      <span class="dropdown-tgr-arrow"></span>
                  </a> 
                  <ul class="dsr-info-list">
                      
                          
                               
                                 <li><span class="morethan">如实描述:<b>4.7</b></span><span class="listup-tgr-arrow"></span></li>
                              
                          
                      

                     
                          
                               
                                 <li><span class="morethan">服务态度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                              
                          
                       
                      
                     
                          
                               
                                 <li><span class="morethan">发货速度:<b>4.8</b></span><span class="listup-tgr-arrow"></span></li>
                              
                          
                      
                  </ul>
              </div>
            </div>
        </div>
         
    </div>
</div>



</div>
      <div bx-slot="shopBtm" data-spm="0782702704"></div>
  </div>
  <!-- lego2 import from /alp/p4p_land/innersearch-ad-container.html --><style> 
            .tanx_container{
   				 margin-top: 14px;
   				 border:1px solid #ededed;
                overflow:hidden;
                margin:0 auto;
              width:1000px;
    height:337px;
            }
  .tanx_container .subTitle{
    height: 40px;
    background: #f2f2f2;
    border-bottom: 1px solid #ededed;
  }
  .tanx_container .subTitle em{
  color: #f85231;
    font-size: 14px;
    line-height: 40px;
    margin-left: 8px;
    font-weight: 700;
  }
  .tanx_container .wrapper{
 	 background: #fff;
    overflow: hidden;
    height:260px;
    position:relative;
    padding: 14px 0 10px 17px;
  }
  .tanx_container .wrapper .item{
    float:left;
    margin:0 25px 10px 0;
  }
  #body-normal .tanx_container{width:1000px;}
  #body-normal .tanx_container .wrapper .item{margin:0 25px 10px 0;}
  #body1190 .tanx_container{width:1190px;}
  #body1190 .tanx_container .wrapper .item{margin:0 90px 10px 0;}
  #body1350 .tanx_container{width:1350px;}
  #body1350 .tanx_container .wrapper .item{margin:0 32px 10px 0;}
  
  @media screen and (min-width: 1190px) and (max-width:1349px) {
    .tanx_container{width:1190px;}
    .tanx_container .wrapper .item{margin:0 90px 10px 0;}
 }

 @media screen and (min-width: 1350px) {
    .tanx_container{width:1350px;}
    .tanx_container .wrapper .item{margin:0 32px 10px 0;}
  }
  
        </style>
        <div class="tanx_container">
          	<div class="subTitle">
        		<em>促销名店</em> 
    		</div>
          <div class="wrapper">
             
            <div class="item">
                       <script type="text/javascript">
     document.write('<a style="display:none!important" id="tanx-a-mm_12852562_1778064_28164454"></a>');
     tanx_s = document.createElement("script");
     tanx_s.type = "text/javascript";
     tanx_s.charset = "gbk";
     tanx_s.id = "tanx-s-mm_12852562_1778064_28164454";
     tanx_s.async = true;
     tanx_s.src = "//p.tanx.com/ex?i=mm_12852562_1778064_28164454";
     document.getElementsByTagName("head")[0].appendChild(tanx_s);
</script>
            </div>
        	<div class="item">
            	<script type="text/javascript">
     document.write('<a style="display:none!important" id="tanx-a-mm_12852562_1778064_28196268"></a>');
     tanx_s = document.createElement("script");
     tanx_s.type = "text/javascript";
     tanx_s.charset = "gbk";
     tanx_s.id = "tanx-s-mm_12852562_1778064_28196268";
     tanx_s.async = true;
     tanx_s.src = "//p.tanx.com/ex?i=mm_12852562_1778064_28196268";
     document.getElementsByTagName("head")[0].appendChild(tanx_s);
</script>
            </div>
            <div class="item" >
            	<script type="text/javascript">
     document.write('<a style="display:none!important" id="tanx-a-mm_12852562_1778064_28200267"></a>');
     tanx_s = document.createElement("script");
     tanx_s.type = "text/javascript";
     tanx_s.charset = "gbk";
     tanx_s.id = "tanx-s-mm_12852562_1778064_28200267";
     tanx_s.async = true;
     tanx_s.src = "//p.tanx.com/ex?i=mm_12852562_1778064_28200267";
     document.getElementsByTagName("head")[0].appendChild(tanx_s);
</script>
            </div>
            <div class="item">
            	<script type="text/javascript">
     document.write('<a style="display:none!important" id="tanx-a-mm_12852562_1778064_28200270"></a>');
     tanx_s = document.createElement("script");
     tanx_s.type = "text/javascript";
     tanx_s.charset = "gbk";
     tanx_s.id = "tanx-s-mm_12852562_1778064_28200270";
     tanx_s.async = true;
                  tanx_s.src = "//p.tanx.com/ex?i=mm_12852562_1778064_28200270";
     document.getElementsByTagName("head")[0].appendChild(tanx_s);
</script>
            </div>
            <div class="item">
            	<script type="text/javascript">
     document.write('<a style="display:none!important" id="tanx-a-mm_12852562_1778064_28174402"></a>');
     tanx_s = document.createElement("script");
     tanx_s.type = "text/javascript";
     tanx_s.charset = "gbk";
     tanx_s.id = "tanx-s-mm_12852562_1778064_28174402";
     tanx_s.async = true;
     tanx_s.src = "//p.tanx.com/ex?i=mm_12852562_1778064_28174402";
     document.getElementsByTagName("head")[0].appendChild(tanx_s);
</script>
            </div>
            <div class="item">
           	<script type="text/javascript">
     document.write('<a style="display:none!important" id="tanx-a-mm_12852562_1778064_28182382"></a>');
     tanx_s = document.createElement("script");
     tanx_s.type = "text/javascript";
     tanx_s.charset = "gbk";
     tanx_s.id = "tanx-s-mm_12852562_1778064_28182382";
     tanx_s.async = true;
     tanx_s.src = "//p.tanx.com/ex?i=mm_12852562_1778064_28182382";
     document.getElementsByTagName("head")[0].appendChild(tanx_s);
</script>
            </div>
           <div class="item">
            	<script type="text/javascript">
     document.write('<a style="display:none!important" id="tanx-a-mm_12852562_1778064_28878730"></a>');
     tanx_s = document.createElement("script");
     tanx_s.type = "text/javascript";
     tanx_s.charset = "gbk";
     tanx_s.id = "tanx-s-mm_12852562_1778064_28878730";
     tanx_s.async = true;
     tanx_s.src = "//p.tanx.com/ex?i=mm_12852562_1778064_28878730";
     document.getElementsByTagName("head")[0].appendChild(tanx_s);
</script>
            </div>
            <div class="item">
            <script type="text/javascript">
     document.write('<a style="display:none!important" id="tanx-a-mm_12852562_1778064_28864819"></a>');
     tanx_s = document.createElement("script");
     tanx_s.type = "text/javascript";
     tanx_s.charset = "gbk";
              tanx_s.id = "tanx-s-mm_12852562_1778064_28864819";
     tanx_s.async = true;
              tanx_s.src = "//p.tanx.com/ex?i=mm_12852562_1778064_28864819";
              document.getElementsByTagName("head")[0].appendChild(tanx_s);
</script>
            </div>
          </div>
 </div>
  <div bx-slot="btmSearch" data-spm="0782702705" bx-name="p4p/search-area" bx-version="0.0.1" bx-guid="lego4" hasjs="true" hascss="true" class="p4p-search-area"><div class="search-supply">
  <div class="search-border clearfix">
    <form action="/search" id="J_searchForm_supply">
        <span class="text-wrap">
            <input type="text" class="text" id="qSupply" name="keyword" accesskey="s" autocomplete="off" x-webkit-speech="" x-webkit-grammar="builtin:translate">
        </span>
        <input type="hidden" name="_input_charset" value="utf-8">
        <input type="hidden" name="page" value="0">
<!--<input type="hidden" name="isinner" value="0">-->
        <input type="submit" class="submit" value="">
    </form>
  </div>
</div>
</div>
  <div bx-slot="topBtn" bx-name="p4p/backtop" bx-version="0.0.1" bx-guid="lego5" hasjs="true" hascss="true" class="p4p-backtop"><div class="backtop">
  <a href="#" class="trigger totop-btn" title="回到顶部">
    <span></span>
  </a>
</div>
</div>
</div>


</div>
    <!-- lego2 import from /alp/atb/common_pc_taobao_footer.html -->
<style type="text/css">
  /*footer */
  div#footer{
    width: 990px;
    padding: 7px 0 9px;
    margin-top: 50px;
    color: #b0b0b0;
    text-align: left !important;
    position: relative;
    clear:both;
    margin: 20px auto;
    min-height: 72px;
    height: auto;
  }
  div#footer a{
    margin: 0 4px;
    color: #3e3e3e;
    text-decoration:none;
  }
  div#footer a:hover{
    color: #F60;
    text-decoration: underline;
  }
  .footer-ali{
    margin-right: 80px;
    padding-left: 0;
    border-bottom: 1px solid #D3D3D3;
    padding-bottom: 8px;
    height: 18px;
  }
  .footer-nohover{
    cursor: default;
  }
  .footer-nohover:hover{
    color:#3e3e3e !important;
    text-decoration:none !important;
  }
  .footer-ali a,.footer-ali b{
    float: left;
  }
  .footer-ali b {
    margin: 0 4px;
    color:#d3d3d3;
    font-weight: normal;
    *margin-top:-1px;
    margin-top:-1px \0/;
  }
  .footer-nav{
    margin-top: 8px;
    line-height: 20px;
  }
  .footer-nav span{
    margin-left: 50px;
  }
  .footer-toy{
    position: absolute;
    width: 69px;
    height: 100px;
    display: block;
    right: 0px;
    top:0px;
    background: url(//img.alicdn.com/tps/i1/T1MMPaXkNjXXaXezbh-48-70.png) no-repeat;
    _background: url(//img.alicdn.com/tps/i1/T1XgzaXX0kXXaXezbh-48-70.png) no-repeat;
  }
  /* IE9 only */
  :root .footer-toy {
    right:-20px\9;
  }
  .footer-line{
    display: none;
    position: absolute;
    width: 104px;
    height: 1px;
    right: 45px;
    top:33px;
    background: url(//img.alicdn.com/tps/i1/T1I_56Xl0wXXXXXXXX-104-1.png) no-repeat;
  }
  .footer-more {
    cursor: pointer;
    z-index: 1;
    position: relative;
    padding-top: 1px;
    width: 82px;
    float: left;
    *top:-1px;
    top:-2px \0/;
  }
  .footer-more-trigger {
    position: absolute;
    padding: 6px 11px 4px 14px;
    width: 37px;
    line-height: 1.3;
    left:-12px;
    top:-5px;
    border:0 none;
  }
  .footer-more-trigger:hover{
    border: 1px solid #fff;
  }
  .footer-more-trigger .arrow{
    position: absolute;
    display: inline-block;
    font-size: 0;
    line-height: 0;
    width: 0;
    height: 0;
    border: dashed 4px;
  }
  .footer-more-trigger .arrow-d {
    border-color: #666 transparent transparent transparent;
    border-top-style: solid;
    right: 12px;
    top: 11px;
  }
  .footer-more-panel {
    text-align: left;
    position: absolute;
    right: 26px;
    bottom: -90px;
    padding: 7px 3px 2px 2px;
    border: 1px solid #C5C5C5;
    width: 57px;
    background:white;
    line-height: 1.9;
    display: none;
  }
  .footer-more-panel a {
    float: none;
    margin-right: 3px;
  }
  .footer-more-hover .footer-more-trigger,
  .footer-more:hover .footer-more-trigger {
    border-color: #c5c5c5;
    background: #fff;
    border-bottom: 0;
    border: 1px solid #C5C5C5;
    border-bottom: 0 none;
  }
  .footer-more-hover .footer-more-panel,
  .footer-more:hover .footer-more-panel  {
    display: block;
  }
  .footer-more-hover .footer-more-trigger .arrow-d,
  .footer-more:hover .footer-more-trigger .arrow-d {
    -moz-transform: rotate(180deg);
    -moz-transform-origin: 50% 30%;
    -o-transform: rotate(180deg);
    -o-transform-origin: 50% 30%;
    -webkit-transform: rotate(180deg);
    -webkit-transform-origin: 50% 30%;
    transform: rotate(180deg);
    transform-origin: 50% 30%;
    filter: progid:DXImageTransform.Microsoft.BasicImage(rotation = 2);
    *top: 8px;
    top:8px \0/;
  }
</style>
<div id="footer">
  <div class="footer-ali">
    <a href="//page.china.alibaba.com/shtml/about/ali_group1.shtml">阿里巴巴集团</a><b>|</b>
    <a href="javascript:void(0)" target="_self" class="footer-nohover">阿里巴巴网络：</a>
    <a href="//www.alibaba.com/">国际站</a>
    <a href="//www.1688.com//">中文站</a>
    <a href="//www.aliexpress.com/">全球速卖通</a> <b>|</b>
    <a href="//www.taobao.com/?id=shouye_taobao">淘宝网</a>
    <b>|</b>
    <a href="//www.tmall.com/">天猫</a>
    <b>|</b>
    <a href="//www.etao.com/">一淘</a>
    <b>|</b>
    <a href="//www.alimama.com/">阿里妈妈</a>
    <b>|</b>
    <a href="//www.aliyun.com/">阿里云</a>
    <b>|</b>
    <a href="//www.yahoo.com.cn/">中国雅虎</a>
    <b>|</b>
    <a href="//www.alipay.com/">支付宝</a>
    <b>|</b>
    <a href="//ju.taobao.com/">聚划算</a>
    <b>|</b>
    <span class="footer-more" id="J_FooterMore">
      <span class="footer-more-panel">
        <a href="//www.aliresearch.com/">阿里研究</a><br>
        <a href="//www.alihz.com/">阿里会展</a><br>
        <a href="//www.hitao.com/">嗨淘网</a><br>
      </span>
      <a href="javascript:void(0);" target="_self" class="footer-more-trigger">更多 <s class="arrow arrow-d"></s></a>
    </span>
  </div>
  <div class="footer-nav">
    <a href="//www.taobao.com/about/">关于淘宝</a>
    <a href="//www.taobao.com/about/partners.php">合作伙伴</a>
    <a href="//pro.taobao.com/">营销中心</a>
    <a href="//service.taobao.com/support/main/service_route.htm">联系客服</a>
    <a href="//open.taobao.com/">开放平台</a>
    <a href="//www.taobao.com/about/join.php">诚征英才</a>
    <a href="//www.taobao.com/about/contact.php">联系我们</a>
    <a href="//www.taobao.com/sitemap.php">网站地图</a>
    <a href="//www.taobao.com/about/copyright.php">法律声明</a>
    <span>&copy; 2016 Taobao.com 版权所有</span>
  </div>
  <div id="server-num" style="color:#fff;"></div>
  <span class="footer-toy"></span>
  <span class="footer-line"></span>
  <script type="text/javascript">
    // hover effect for ie6
    (function(){
      if(-[1,]) return;
      var ie6FootHover = document.getElementById("J_FooterMore");
      ie6FootHover.onmouseenter=function() {
        this.className+=" footer-more-hover";
      }
      ie6FootHover.onmouseleave=function() {
        this.className=this.className.replace(new RegExp(" footer-more-hover\\b"), "");
      }
    })();
  </script>
</div> 

    <script type="text/javascript" src="//g.alicdn.com/alp/alp-boot/2016.0509.1537/index.js"></script>
  </body>
</html>
"""
d = pq(content)

searchResult = d('#searchResult')

item = searchResult('.item')

# print(item('img'))



for i in item.items():
    print(i('.title').attr('title'))
    print(i('img').attr('data-ks-lazyload').replace('260', '560'))

# print(item('img').attr('data-ks-lazyload'))


from urllib import request

with open('file.jpg', 'wb') as file:
    re = request.urlopen(
        'https://img.alicdn.com/imgextra/i3/126855292/TB21vGGgY1YBuNjSszeXXablFXa_!!0-saturn_solar.jpg_260x260.jpg')
    file.write(re.read())


import  os

pa = os.path.dirname(os.path.dirname(__file__))
print(os.path.exists(pa))