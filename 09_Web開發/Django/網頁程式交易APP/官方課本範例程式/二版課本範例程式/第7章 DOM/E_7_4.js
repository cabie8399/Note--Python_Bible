function SelectorAll() {
    var tagname = "input";
    var seltag = document.querySelectorAll(tagname);
    alert( "共有 " + seltag.length + "個" + tagname + "標籤");
}
function SelectorFirst() {
    var classname = ".format";
    //var selclass = document.querySelector(classname);
	var selclass = document.querySelector(classname).tagName + "標籤";    	
	alert( "class的第一個元素是" + selclass);
}


 