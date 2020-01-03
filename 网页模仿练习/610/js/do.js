//展示当前内容
function showSections(id) {
    var sections = document.getElementsByTagName('div');
    for(var i=0;i<sections.length;i++){
        if(sections.id != id){
            sections[i].style.display = 'none';
        }
        else{
            sections[i].style.display = 'block';
        }
    }

}
//显示点击链接响应内容
function showNow() {
    var nav = document.getElementsByTagName('nav')[0];
    var links = nav.getElementsByTagName('a');

    for(var i=1;i<links.length;i++){
        var sectionId = links[i].href.split('#')[1];
        console.log(sectionId);

        if(!document.getElementById(sectionId)) continue;

        document.getElementById(sectionId).style.display = 'none';
        links[i].destination = sectionId;
        links[i].onclick = function () {
            showSection(this.destination);
            return false;
        }
    }

}
function fn1() {
    divs = document.getElementsByTagName('div');
    for (var i=0;i<divs.length;i++){
        console.log(divs[i]);
    }
    // console.log(divs);
}
window.onload = function () {
    // fn1();
}