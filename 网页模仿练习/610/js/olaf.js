$(document).ready(function () {

    $.getJSON("../data/olaf.json",function(data){
        var showBar = document.getElementById('showBar');
        var heroBar = document.getElementById('hero');
        console.log('1');
        //操作英雄栏信息
        var hero = data.hero;
        //获取英雄ID
        var name = document.createElement('p');
        name.className = 'name';
        var nameText = document.createTextNode("英雄名称："+hero.alias);
        name.appendChild(nameText);
        showBar.appendChild(name);
        //获取英雄使用技巧
        var allytips = document.getElementById('allytips');
        for (var i=0;i<hero.allytips.length;i++){
            var para = document.createElement('p');
            var text = JSON.stringify(hero.allytips[i]);
            var paraText = document.createTextNode(text.replace(/[\"]/g,'').split('\n')[0]);
            para.className = 'allytips';
            para.appendChild(paraText);
            allytips.append(para);
        }
        // 获取对抗技巧
        var enemytips = document.getElementById('enemytips');
        for (var i=0;i<hero.enemytips.length;i++){
            var para = document.createElement('p');
            var text = JSON.stringify(hero.enemytips[i]);
            var paraText = document.createTextNode(text.replace(/[\"]/,''));
            para.className = 'enemytips';
            para.appendChild(paraText);
            enemytips.appendChild(para);
        }
        heroBar.appendChild(allytips);
        heroBar.appendChild(enemytips);
        showBar.appendChild(heroBar);
        //操作皮肤栏
        var skinsBar = document.getElementById('skinshow');
        var skins = data.skins;
        for (var i=0; i<skins.length;i++){
            var heroName = document.createElement('p');
            var heroNameText = document.createTextNode(skins[i].name);
            heroName.appendChild(heroNameText);
            var heroImg = document.createElement('img');
            heroImg.src = skins[i].mainImg;
            heroImg.alt = skins[i].name;
            heroImg.className = "heroimg";
            skinsBar.appendChild(heroName);
            skinsBar.appendChild(heroImg);
        }
        showBar.appendChild(skinsBar);

        //操作技能栏
        var spellsBar = document.getElementById('spells');
        var spells = data.spells;
        for(var i=0;i<spells.length;i++){
            spell = spells[i];
            var skillImg = document.createElement('img');
            skillImg.src = spell.abilityIconPath;
            skillImg.alt = spell.name;
            skillImg.className = 'skillimg';
            // console.log(spell.abilityIconPath);
            var skillName = document.createElement('p');
            var skillNameText = document.createTextNode(spell.name+":"+spell.description+"("+spell.dynamicDescription+")");
            skillName.appendChild(skillNameText);
            spellsBar.appendChild(skillImg);
            spellsBar.appendChild(skillName);
        }
        showBar.appendChild(spellsBar);
    });
    showNow();
});
//展示/隐藏内容
function showSection(id) {
    var sections = document.getElementsByTagName('div');
    for(var i=1;i<sections.length;i++){
        if(sections[i].id != id){
            sections[i].style.display = 'none';
        }else{
            sections[i].style.display = 'block';
        }
    }
}
//实现点击按钮显示相应内容
function showNow() {
    var navs = document.getElementsByTagName('nav');
    if(navs.length == 0)return false;
    var nav = navs[0];
    var links = nav.getElementsByTagName('a');
    // console.log(links);
    for(var i=1;i<links.length;i++){
        var sectionId = links[i].href.split('#')[1];
        console.log(sectionId);
        if(!document.getElementById(sectionId)) continue;
        document.getElementById(sectionId).style.display = 'none';
        links[i].destination = sectionId;
        links[i].onclick = function () {
            showSection(this.destination);
            document.getElementById('hero').style.display = 'block';
            return false;
        }
    }
}