<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>

<style>
body {
	font-family: Arial, sans-serif;
	font-size: 13px;
	line-height: 19px;
}

html, body, div, span, h1, h2, h3 {
    margin: 0;
    padding: 0;
    border: 0;
    vertical-align: baseline;
    -webkit-box-sizing: border-box;
    -moz-box-sizing: border-box;
    box-sizing: border-box;
}

#body {
    padding: 24px 20px 20px 20px;
    border-radius: 6px;
    box-shadow: rgba(100, 100, 100, 0.5) 0 2px 8px;
    max-width: 980px;
    margin: 0 auto;
}

h1, h2, h3 {
	font-family: 'Klavika Medium', sans-serif;
	font-stretch: 70%;
    border-bottom-color: rgb(153, 153, 153);
    border-bottom-style: dotted;
}

h1 {
	margin-bottom: 24px;
	font-size: 22px;
    border-bottom-width: 2px;
}

h1 + p {
	/*font-size: 18px;*/
	margin-bottom: 10px;
}

h2 {
	font-size: 18px;
	height: 24px;
	margin-top: 20px;
    border-bottom-width: 1px;
}

a, a:visited {
	color: rgb(138, 29, 44);
	text-decoration: none;
}

#header {
	background-color: #b4162c;
	background-image: -webkit-linear-gradient(left, #b4162c 0%, #b4162c 50%, #8b1221 100%);
	background-image: -moz-linear-gradient(left, #b4162c 0%, #b4162c 50%, #8b1221 100%);
    background-image: -o-linear-gradient(left, #b4162c 0%, #b4162c 50%, #8b1221 100%);
    background-image: linear-gradient(left, #b4162c 0%, #b4162c 50%, #8b1221 100%);
    position: relative;
    z-index: 10;
    display: block;
    height: 90px;
    padding: 10px;
    box-shadow: rgba(0, 0, 0, 0.74902) 0px 0px 15px 0px;
    margin-bottom: 25px;
}

#main {
	width: 620px;
	margin-right: 98px;
}

#sidebox {
    float: right;
    margin-top: -10px;
    margin-right: 10px;
}

#sidebox p {
    margin-top: 4px;
    margin-bottom: 4px;
}

#sidebox h2 {
    font-weight: medium;
    font-size: 14px;
    color: rgb(180, 22, 44);
}
</style>
</head>

<div id="header"></div>
<div id="body">
<div id="sidebox">
{{plan}}
{{duration}}
{{material}}
</div>
<div id="main">
{{main}}
</div>
</div>