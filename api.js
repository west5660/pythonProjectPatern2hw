let brestbut = document.getElementById('butbrest')
let poiskbut = document.getElementById('poiskbut')



brestbut.onclick = function (){f1()}
poiskbut.onclick = f2

function f1(id=629634){
    let key = 'ffba57f44fa1889286e1e5a405e4e879'
    // let id = 629634

     let req
    if (window.XMLHttpRequest) {
        req = new XMLHttpRequest();
    } else {
        req = new ActiveXObject("Microsoft.XMLHTTP");
    }
    req.open('GET','https://api.openweathermap.org/data/2.5/weather?id='+ id + '&appid='+key+'&lang=ru&units=metric')


     req.onload = function () {
         if (req.status === 200) {
             console.log('ok')
             console.log(req.response)     //получили ответ
             let pogoda = JSON.parse(req.response)  //расшифровывает ответ
             forotvet(pogoda)    //обрабатывает ответ
         } else {
             console.log('neok')
         }
     }
        req.send()   //отправляет запрос
    }

function forotvet(response){
    let k1= response.name
    let k2= response.main.temp
    let k3= response.wind.speed
    let k4= response.weather[0].description
    console.log(k1,k2,k3,k4)
    let otvet = document.getElementById('otvet')
    otvet.innerHTML = '<h3>Город '+ k1+'</h3>' +
        '<h3>Температура '+ k2+'C</h3>'+
        '<h3>Ветер '+ k3+'м/с</h3>'+
        '<h3> '+ k4+'</h3>'
}

function f2(){
    let key = 'ffba57f44fa1889286e1e5a405e4e879'
    let name = document.getElementById('gorod') .value

    let req
    if (window.XMLHttpRequest) {
        req = new XMLHttpRequest('goroda');
    } else {
        req = new ActiveXObject("Microsoft.XMLHTTP");
    }
    req.open('GET','https://api.openweathermap.org/data/2.5/find?q='+
        name+'&appid='+key+'&lang=ru&units=metric&type=like')

      req.onload = function () {
        if (req.status === 200) {
            console.log(req.response)
            spisok = JSON.parse(req.response)
            console.log(spisok)
            let otvet = document.getElementById('otvet2')
            let newid
            stroka='<table>'
            for (i=0;i<spisok.list.length;i++){
                newid=spisok.list[i].id
                stroka+='<tr>'+'<th>'+spisok.list[i].id+'</th>'+
                    '<th>'+spisok.list[i].name+'</th>'+
                    '<th>'+spisok.list[i].sys.country+'</th>'+
                    '<td><button onclick=f1('+newid+')>Погода</button></td>'+
                    '</tr>'
            }
            otvet.innerHTML=stroka+'</table>'
        }
         else {
            console.log('neok')
        }
    }
    req.send()//отправляет запрос
}
function getUserInfo() {
    let userLogin = document.getElementById('userLogin').value;         // Получаем логин пользователя из input
    let apiUrl = `https://api.github.com/users/${userLogin}`;                     // Формируем URL для запроса
    let req = new XMLHttpRequest();                                              // Создаем объект XMLHttpRequest
    req.open('GET', apiUrl, true);                                                // Настраиваем запрос
    req.onload = function () {                                                     // обработчик события загрузки
        if (req.status === 200) {
            let userData = JSON.parse(req.responseText);                          // Если запрос успешен, обрабатываем ответ
            displayUserInfo(userData);                                         // Отображаем информацию о пользователе
        } else {
            console.log('Ошибка запроса к GitHub API');                         // Если произошла ошибка, выводим сообщение об ошибке
        }
    };
    req.send();
}

function displayUserInfo(userData) {
    let photoElement = document.getElementById('photo');                       // Получаем элементы, куда будем выводить информацию
    let nameElement = document.getElementById('name');
    let loginElement = document.getElementById('login');
    let githubLinkElement = document.getElementById('githubLink');


    photoElement.src = userData.avatar_url;                                             // Выводим информацию о пользователе
    nameElement.textContent = `Имя: ${userData.name}`;
    loginElement.textContent = `Логин: ${userData.login}`;
    githubLinkElement.href = userData.html_url;
    githubLinkElement.textContent = 'Ссылка на GitHub';


    photoElement.style.display = 'block';                                                // Показываем элементы, так как информация доступна
    nameElement.style.display = 'block';
    loginElement.style.display = 'block';
    githubLinkElement.style.display = 'block';
}
