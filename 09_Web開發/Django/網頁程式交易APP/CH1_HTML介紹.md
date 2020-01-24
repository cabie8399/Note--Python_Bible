# CH1_HTML+CSS+Javascript簡介


> 0. 資訊
> 1. HTML簡介
> 2. win10 上 使用sublime3 寫 javascript
> 3. Linux 執行 javascript
> 4. HTML 常用標籤
> 5. 自我練習:課表


<br><br>




## 資訊

- [Python 網頁程式交易APP實作 範例程式碼](https://github.com/letylin/pyptbook)



## 1. HTML簡介

HTML5是2014年由W3C完成制定標準，目標是減少伺服器端網路應用服務的運算需求，提高客戶端執行動態網頁運匴服務的效能，降低網路傳送負載。



## 2. win10 上 使用sublime3 寫 javascript


- [sublime3 安裝 javascript](https://dotblogs.com.tw/h091237557/2014/08/24/146340)

安裝完後即可用以下步驟寫javascript<br>
在到Tools → Build System → JS(我剛剛存檔時取名為JS)。
![ScreenClip14](https://az787680.vo.msecnd.net/user/h091237557/1408/BLOGSublimeText3javascript_B762/ScreenClip14_thumb.png "ScreenClip14")](https://az787680.vo.msecnd.net/user/h091237557/1408/BLOGSublimeText3javascript_B762/ScreenClip14_2.png)

然後你在隨便新增個js檔。

[![ScreenClip15](https://az787680.vo.msecnd.net/user/h091237557/1408/BLOGSublimeText3javascript_B762/ScreenClip15_thumb.png "ScreenClip15")](https://az787680.vo.msecnd.net/user/h091237557/1408/BLOGSublimeText3javascript_B762/ScreenClip15_2.png)

後然按F7，他就會自動幫你執行囉。

[![ScreenClip16](https://az787680.vo.msecnd.net/user/h091237557/1408/BLOGSublimeText3javascript_B762/ScreenClip16_thumb.png "ScreenClip16")](https://az787680.vo.msecnd.net/user/h091237557/1408/BLOGSublimeText3javascript_B762/ScreenClip16_2.png)




## 3. Linux 執行 javascript



### **Yum 安裝**  
要用 Yum 安裝 Node.js, 要先啟用 EPEL repository, 執行以下指令:
```bash
yum install epel-release
```
啟用 EPEL repository 後, 輸入以下指令安裝 Node.js:
```bash
yum install nodejs
```
安裝好 Node.js 後, 跟編譯源碼一樣, 可以用以下指令確認 Node.js 安裝成功:
```bash
node –version
```



### 執行javascript

- [https://blog.csdn.net/wh211212/article/details/70098840](https://blog.csdn.net/wh211212/article/details/70098840)

#### 示範1
```javascript
var a = 1
console.log(a)
```

```bash
(base) [cabie@centosclean 02_Fron-End]$ vim hello.js
(base) [cabie@centosclean 02_Fron-End]$ node hello.js
1
```

### 示範2

![Imgur](https://i.imgur.com/6G9tKNn.png =800x200)

```bash
[root@linuxprobe ~]$ vi helloworld.js
var http = require('http');
http.createServer(function (req, res) {
  res.writeHead(200, {'Content-Type': 'text/plain'});
  res.end('Hello World\n');
}).listen(1337, '127.0.0.1');
console.log('listening on http://127.0.0.1:1337/');

# run server
[root@linuxprobe ~]$ node helloworld.js &
# verify (it's OK if following reply is back )
[root@linuxprobe ~]$ curl http://127.0.0.1:1337/
Hello World

```








## 4. HTML 常用標籤

![Imgur](https://i.imgur.com/btE1dVn.png)

![Imgur](https://i.imgur.com/IWK9G5f.png =800x500)



### 範例 1-1 : ```<p>``` / ```<b>``` / ```<i>```

其中```<hr>```是顯示一條水平線<br>
```<p>```:顯示一段文字後，自動跳下一行<br>
```<b>```:粗體<br>
```<i>```:斜體<br>


```javascript
<html>
    <head>
        <meta charset="UTF-8">
        <!--[if lt IE 9]>
          <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
        <![endif]-->
    </head>





    <body>


        
        <header>
            <h1>花廊</h1>
            <hr>
        </header>



        <article>
            <section>
                <h2>百子蓮</h2>
                <hr>
                <figure style="float: left;">
                    <img src="lotus.jpg" alt="百子蓮" width="304" height="228"  style="margin: 15px">
                </figure>
                <section style="width:300px;float: left;">
                    <p>原生於南非，多年生草本植物，花瓣是藍色呈漏斗形，花莖直立，最高可在長到一公尺，大約有10個不同的顏色與種類。葉子的型狀呈披針形，長度可達六十公分左右。分球繁殖或是用種子繁殖均可。</p> 
                    <p>~攝於雪霸國家公園</p>
                    <nav>
                        <a href="https://zh.wikipedia.org/wiki/%E7%99%BE%E5%AD%90%E8%93%AE%E5%B1%AC">百子蓮</a>
                    </nav>
                </section>                
            </section>
            <div style="clear:both;"></div>
            <section>
                <h2>台灣龍膽</h2>
                <hr>
                <figure style="float:left;">
                    <img src="longtang.jpg" alt="台灣龍膽" width="304" height="228"  style="margin: 15px">
                </figure>
                <section  style="width:300px;float:left;">
                    <p>台灣原生種，台灣龍膽生長於海拔500到3000公尺山坡，路旁向陽處。花瓣細小約 3 公分，裂片三角狀卵形，花萼管筒狀，多年生草本，株高 5~15 公分，全株光滑無毛。具藥用功能：苦、涼、降肝清火，解暑熱，健胃。花期在每年5到7月，又稱龍膽草、阿里山龍膽。</p>
                    <p>~攝於雪霸國家公園。</p>
                    <nav>
                        <a href="http://b20131201.pixnet.net/blog/post/25939276-%E5%8F%B0%E7%81%A3%E9%BE%8D%E8%86%BD">台灣龍膽</a>
                    </nav>
                </section>
            </section>
        </article>



    </body>
</html>
```


![Imgur](https://i.imgur.com/9tWC2DX.png)


### 範例 2 : ```<span>``` / ```<ul>``` / ```<ol>```

使用div 設定字型的顏色，並有無序號及有序號項目<br>
```<span>```:格式化某列或某個字<br>
```<ul>```:無序項目清單<br>
```<ol>```:有序項目清單，start="20"，就是決定開始的頭，reversed為降冪<br>


```javascript
<!DOCTYPE html>
<html>

<body>
    <p>李白生於西元701至762年，字太白，號青蓮居士，唐朝詩人。</p>
    <div style="color:#0000FF">
        <h3>李白 送孟浩然之廣陵</h3>
        <p>故人西辭黃鶴樓，煙花三月下揚州。</p>
        <p>孤帆遠影碧空盡，唯見長江天際流。</p>
    </div>
    <hr>
    <h3>李白 獨坐敬亭山</h3>
    <p>眾鳥高飛盡，孤雲獨去閒。</p>
    <p>相看兩不厭，只有<span style="color:red;font-weight:bold">敬亭山</span></p>
    <hr>
    <ul>
        <li>春</li>
        <li>夏</li>
        <li>秋</li>
        <li>冬</li>
    </ul>
    <hr>
    <ol start="20" reversed="">
        <li>巨蟹</li>
        <li>天蠍</li>
        <li>雙魚</li>
    </ol>
</body>

</html>

```

![Imgur](https://i.imgur.com/UopcJLC.png)




### 範例3 : tr / td / th

設計一個有顏色漸層的表格
- ```<th>```: 建立欄標題
- tr:nth-child(even) : 代表只套用在偶數列上   

```javascript
<!DOCTYPE html>
<html>

<head>
    <style>
    table {
        font-family: arial, sans-serif;
        border-collapse: collapse;
        width: 100%;
    }

    td,
    th {
        border: 1px solid #dddddd;
        text-align: left;
        padding: 8px;
    }
    
    //代表只套用在偶數列上    
    tr:nth-child(even) { 
        background-color: #F5F5DC;
    }
    </style>
</head>

<body>
    <div style="color:#00008B">
        <h3>TIOBE Index for March 2017</h3>
    </div>
    <table style="width:100%">
        <tr>
            <th>2017 March</th>
            <th>2016 March</th>
            <th>Rating</th>
        </tr>
        <tr>
            <td>1</td>
            <td>1</td>
            <td>Java</td>
        </tr>
        <tr>
            <td>2</td>
            <td>2</td>
            <td>C</td>
        </tr>
        <tr>
            <td>3</td>
            <td>3</td>
            <td>C++</td>
        </tr>
        <tr>
            <td>4</td>
            <td>4</td>
            <td>C#</td>
        </tr>
        <tr>
            <td>5</td>
            <td>5</td>
            <td>Python</td>
        </tr>
        <tr>
            <td>8</td>
            <td>8</td>
            <td>JavaScript</td>
        </tr>
        <tr>
            <td>17</td>
            <td>48</td>
            <td>Go</td>
        </tr>
    </table>
    </div>
</body>

</html>
```


![Imgur](https://i.imgur.com/KI49GbF.png =750x350)










## 5. 自我練習

做出課表


```html
<!DOCTYPE html>
<html>

<head>
    
</head>

<body>
    <div style="color:#00008B">
        <h2>2020年 Pizza課表</h2>
    </div>
    <table style="width:100%">
        <tr>
            <th>星期1</th>
            <th>星期2</th>
            <th>星期3</th>
            <th>星期4</th>
            <th>星期5</th>
            <th>星期6</th>
            <th>星期7</th>
        </tr>
        <tr>
            <td rowspan="2">1</td>
            <td>1</td>
            <td>Java</td>
            <td>Java</td>
            <td>Java</td>
            <td>Java</td>
            <td>Java</td>

        </tr>
        <tr>
            <td>2</td>
            <td>2</td>
            <td>C</td>
            <td>Java</td>
            <td>Java</td>
            <td>Java</td>
            
        </tr>
        <tr>
            <td colspan="3">3</td>
            <td>3</td>
            <td>C++</td>
            <td>Java</td>
            <td>Java</td>
            
        </tr>
        <tr>
            <td>4</td>
            <td>4</td>
            <td>C#</td>
            <td>Java</td>
            <td>Java</td>
            <td>Java</td>
            <td>Java</td>
        </tr>
        <tr>
            <td>5</td>
            <td>5</td>
            <td>Python</td>
            <td>Java</td>
            <td>Java</td>
            <td>Java</td>
            <td>Java</td>
        </tr>
        <tr>
            <td>8</td>
            <td>8</td>
            <td>JavaScript</td>
            <td>Java</td>
            <td>Java</td>
            <td>Java</td>
            <td>Java</td>
        </tr>
        <tr>
            <td>17</td>
            <td>48</td>
            <td>Go</td>
            <td>Java</td>
            <td>Java</td>
            <td>Java</td>
            <td>Java</td>
        </tr>
    </table>
    </div>
</body>

</html>
```



```css
<style>
    table {
        font-family: arial, sans-serif;
        border-collapse: collapse;
        width: 100%;
    }

    td,
    th {
        border: 1px solid #dddddd;
        text-align: left;
        padding: 8px;
    }

    tr:nth-child(even) {
        background-color: pink;
    }
</style>
```

![Imgur](https://i.imgur.com/5wecX7h.png)
