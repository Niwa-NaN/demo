// 添加应用
function addLoadEvent(func) {
    var oldonload = window.onload;
    if(typeof window.onload != 'function'){
        window.onload = func;
    }else{
        window.onload = function(){
            oldonload();
            func();
        }
    }
}
// 在某已存在的结构后面添加新结构
function insertAfter(newElement,targetElement) {
    var parent = targetElement.parentNode;
    if(parent.lastChild == targetElement){
        parent.appendChild(newElement);
    }else{
        parent.insertBefore(newElement,targetElement.nnextSibling);
    }
}
//为某标签添加Class
function addClass(element,value) {
    if(!element.className){
        element.className = value;
    }else{
        // newClassName = element.className;
        // newClassName += '';
        // newClassName += value;
        // element.className = newClassName;
        element.className += ' '+value;
    }
}
//为当前页面链接添加here类，使之与其他链接不同
function highlightPage() {
    if(!document.getElementsByTagName)return false;
    if(!document.getElementById)return false;
    var headers = document.getElementsByTagName('header');
    if(headers.length == 0)return false;
    var navs = headers[0].getElementsByTagName('nav');
    if(navs.length == 0)return false;
    var links = navs[0].getElementsByTagName('a');
    for (var i=0;i<links.length;i++){
        var linkurl;
        for(var i=0;i<links.length;i++){
            linkurl = links[i].href;
            if(window.location.href.indexOf(linkurl) != -1){
                links[i].className = 'here';
                var linktext = links[i].lastChild.nodeValue.toLowerCase();
                document.body.id = linktext;
            }
        }
    }
}
addLoadEvent(highlightPage);
//移动画报
function moveElement(elementID,final_x,final_y,interval){
    if(!document.getElementById)return false;
    if(!document.getElementById(elementID))return false;
    var elem = document.getElementById(elementID);
    if(elem.movement){
        clearTimeout(elem.movement);
    }
    if(!elem.style.left){
        elem.style.left = '0px';
    }
    if(!elem.style.top){
        elem.style.top = '0px';
    }

    var xpos = parseInt(elem.style.left);
    var ypos = parseInt(elem.style.top);
    if(xpos == final_x && ypos == final_y){
        return true;
    }
    if(xpos < final_x){
        var dist = Math.ceil((final_x - xpos)/10);
        xpos = xpos+dist;
    }
    if(xpos > final_x){
        var dist = Math.ceil((xpos - final_x)/10);
        xpos = xpos-dist;
    }
    if(ypos < final_y){
        var dist = Math.ceil((final_y - ypos)/10);
        ypos = ypos+dist;
    }
    if(ypos > final_y){
        var dist = Math.ceil((ypos - final_y)/10);
        ypos = ypos-dist;
    }

    elem.style.left = xpos+'px';
    elem.style.top = ypos+'px';
    var repeat = "moveElement('"+elementID+"',"+final_x+","+final_y+","+interval+")";
    console.log('working!');
    elem.movement = setTimeout(repeat,interval);
}
//轮播准备
function prepareSlideshow() {
    if(!document.getElementById || !document.getElementsByTagName)return false;
    if(!document.getElementById('intro'))return false;
    // console.log('我在运行');

    var intro = document.getElementById('intro');
    var slideshow = document.createElement('div');
    slideshow.id = 'slideshow';
    var frame = document.createElement('img');
    frame.src = 'images/frame.jpg';
    frame.alt = '';
    frame.id = 'frame';
    slideshow.appendChild(frame);
    var preview = document.createElement('img');
    preview.src = 'images/slideshow.png';
    preview.alt = 'a glimpse of what awaits you';
    preview.id = 'preview';
    slideshow.appendChild(preview);
    insertAfter(slideshow,intro);
    var links = intro.getElementsByTagName('a');
    // console.log(links);
    var destination;
    for (var i=0;i<links.length;i++){
        // console.log(links[i].href);
        links[i].onmouseover = function () {
            destination = this.href;
            console.log(destination+"***");
            if(destination.indexOf("index.html") != -1){
                moveElement('preview',0,0,5);
            }
            if(destination.indexOf("about.html") != -1){
                moveElement('preview',-120,0,5);
            }
            if(destination.indexOf("photos.html") != -1){
                moveElement('preview',-240,0,5);
            }
            if(destination.indexOf("live.html") != -1){
                moveElement('preview',-360,0,5);
            }
            if(destination.indexOf("contact.html") != -1){
                moveElement('preview',-480,0,5);
            }
        }
    }
}
addLoadEvent(prepareSlideshow);
//隐藏
function showSection(id) {
    var sections = document.getElementsByTagName('section');
    console.log('showSection');
    for(var i=0;i<sections.length;i++){
        if(sections[i].id != id){
            sections[i].style.display = 'none';
        }else{
            sections[i].style.display = 'block';
        }
    }
}
//实现点击按钮显示相应内容
function prepareInternalnav() {
    var articles = document.getElementsByTagName('article');
    if(articles.length == 0)return false;
    var navs = articles[0].getElementsByTagName('nav');
    if(navs.length == 0)return false;
    var nav = navs[0];
    var links = nav.getElementsByTagName('a');
    for(var i=0;i<links.length;i++){
        var sectionId = links[i].href.split('#')[1];
        if(!document.getElementById(sectionId)) continue;
        document.getElementById(sectionId).style.display = 'none';
        links[i].destination = sectionId;
        links[i].onclick = function () {
            showSection(this.destination);
            return false;
        }
    }
}
addLoadEvent(prepareInternalnav);
//photos
//在切换框中展示点击图片
function showPic(whichpic) {
    var source = whichpic.href;
    var placeholder = document.getElementById('placeholder');
    placeholder.src = source;
    if(whichpic.title){
        var text = whichpic.title;
    }else{
        var text = '';
    }
    var description = document.getElementById('description');
    if(description.firstChild.nodeType == 3){//确认是文本节点
        description.firstChild.nodeValue = text;
    }
    return false;
}
//准备切换框和原始图片
function preparePlaceholder() {
    var placeholder = document.createElement('img');
    placeholder.id='placeholder';
    placeholder.src='images/placeholder.jpg';
    placeholder.alt='My image gallery';
    var description = document.createElement('p');
    description.id='description';
    var desctext = document.createTextNode('Choose an image');
    description.appendChild(desctext);
    var gallery = document.getElementById('imagegallery');
    insertAfter(description,gallery);
    insertAfter(placeholder,description);
}
//点击图片触发展示事件
function prepareGallery() {
    var gallery = document.getElementById('imagegallery');
    var links = gallery.getElementsByTagName('a');
    for(var i=0;i<links.length;i++){
        links[i].onclick = function () {
            return showPic(this);
        }
    }
}
//live
// addLoadEvent(preparePlaceholder);
// addLoadEvent(prepareGallery);
//修改表格外观--斑马线:为偶数行添加odd属性
function stripeTables() {
    var tables = document.getElementsByTagName('table');
    for (var i=0;i<tables.length;i++){
        var odd = false;
        var rows = tables[i].getElementsByTagName('tr');
        for (var j=0;j<rows.length;j++){
            if(odd == true){//交叉设置添加class属性
                addClass(rows[j],'odd');
                odd = false;
            }
            else{
                odd = true;
            }
        }
    }
}
//鼠标悬停当前行高亮
function highlightRows() {
    var rows = document.getElementsByTagName('tr');
    for(var i=0;i<rows.length;i++){
        rows[i].oldClassName = rows[i].className;
        rows[i].onmouseover = function () {//鼠标悬停添加高光属性
            addClass(this,'highlight');
        }
        rows[i].onmouseout = function () {//鼠标离开取消高光属性
            this.className = this.oldClassName;
        }
    }
}
//展示表格功能
function displayAbbreviations() {
    var abbrs = document.getElementsByTagName('abbr');//抓取abbr标签
    if(abbrs.length<1)return false;
    var defs = new Array();
    for(var i=0;i<abbrs.length;i++){//循环将abbr标签中的title和标签内容做成一个数组
        var current_abbr = abbrs[i];
        if(current_abbr.childNodes.length<1)continue;
        var definition = current_abbr.title;
        var key = current_abbr.lastChild.nodeValue;//内容作键，title属性作值
        defs[key] = definition;
    }
    console.log(defs);
    var dlist = document.createElement('dl');
    for (key in defs){//dl-dt-dd table-tr-th-tr-td
        var definition = defs[key];
        var dtitle = document.createElement('dt');
        var dtitle_text = document.createTextNode(key);
        dtitle.appendChild(dtitle_text);
        var ddesc = document.createElement('dd');
        var ddesc_text = document.createTextNode(definition);
        ddesc.appendChild(ddesc_text);
        dlist.appendChild(dtitle);
        dlist.appendChild(ddesc);
    }
    if(dlist.childNodes.length < 1)return false;
    var header = document.createElement('h3');
    var header_text = document.createTextNode('Abbreviations');
    header.appendChild(header_text);
    var articles = document.getElementsByTagName('article');
    if (articles.length == 0)return false;
    var container = articles[0];
    container.appendChild(header);
    container.appendChild(dlist);
}
addLoadEvent(stripeTables);
addLoadEvent(highlightRows);
addLoadEvent(displayAbbreviations);

//contact
//为选中的框添加焦点，大部分浏览器已经自动支持
function focusLabels() {
    if(!document.getElementsByTagName)return false;
    var labels = document.getElementsByTagName('label');
    for(var i=0;i<labels.length;i++){
        if(!labels[i].for)continue;
        labels[i].onclick = function () {
            var id = this.for;
            console.log(id);
            if(!document.getElementById(id))return false;
            var element = document.getElementById(id);
            element.focus();//为 checkbox 赋予焦点
        }
    }
}
addLoadEvent(focusLabels);
//
function resetFields(whichform) {
    if(Modernizr.input.placeholder)return true;
    console.log('***');
    for(var i=0;i<whichform.elements.length;i++){
        var element = whichform.elements[i];
        if(element.type == 'submit')continue;
        var check = element.placeholder || element.getAttribute('placeholder');
        if(!check)continue;
        //焦点聚集时，tab键或单击表单字段
        element.onfocus = function () {
            var text = this.placeholder || this.getAttribute('placeholder');
            if(this.value == text){
                this.className = '';
                this.value = '';
            }
        }
        //焦点驱散时
        element.onblur = function () {
            if(this.value == ''){
                this.className = 'placeholder';
                this.value = this.placeholder || this.getAttribute('placeholder');
            }
        }
        element.onblur();
    }
}
// function prepareForms() {
//     for(var i=0;i<document.forms.length;i++){
//         var thisform = document.forms[i];
//         resetFields(thisform);
//     }
// }
// addLoadEvent(prepareForms);
//验证用户输入
//是否有输入
function isFilled(field) {
    if(field.value.replace(' ','').length == 0)return false;
    var placeholder = field.placeholder || field.getAttr('placeholder');
    return (field.value != placeholder);
}
//判断邮箱是否同时存在“@”和“。”
function isEmail(field) {
    return(field.value.indexOf('@') != -1&& field.value.indexOf('.') != -1);
}
function validateForm(whichform) {
    for(var i=0;i<whichform.elements.length;i++){
        var element = whichform.elements[i];
        if(element.required == 'required'){
            if(!isFilled(element)){
                alert('Please fill in the '+element.name+' field.');
                return false;
            }
        }
        if(element.type = 'email'){
            if(!isEmail(element)){
                alert('The '+element.name+' field must be a vaild email address.');
                return false;
            }
        }
    }
    return true;
}
function prepareForms() {
    for(var i=0;i<document.forms.length;i++){
        var thisform = document.forms[i];
        resetFields(thisform);
        thisform.onsubmit = function () {
            return validateForm(this);
        }
    }
}
function getHTTPObject() {
    if(typeof XMLHttpRequest == 'undefined'){
        XMLHttpRequest = function () {
            try{return new ActiveXObject('Msxml2.XMLHTTP.6.0');}
                catch(e){}
            try{return new ActiveXObject('Msxml2.XMLHTTP.3.0');}
                catch(e){}
            try{return new ActiveXObject('Msxml2.XMLHTTP');}
                catch(e){}
            return false;
        }
    }
    return new XMLHttpRequest();
}
//接收一个

















