

cost = `Добрый день, мы получили Ваш заказ и благодарим за то, что Вы к нам обратились.

Стоимость Вашей работы:


Вы получите:
1. Полное сопровождение до защиты
2. Бесплатные корректировки
3. Нашу поддержку

Мы приступим сразу после внесения предоплаты в размере 50% от стоимости Вашего заказа.

Вы можете оплатить Ваш заказ:
1. Наличными в нашем офисе по адресу: гор. Челябинск, Комсомольский пр., 48 оф.3
2. Перечислением на карту Сбербанка 2202201514937917, оформлена на Альфия И.

С наилучшими пожеланиями, "Эдельвейс"
тел.(351) 230-80-40, 230-58-30
edelwies@mail.ru`.split('\n').join("<br>")

ss_cost = `Добрый день!
Ваша оплата поступила.
Мы получили Ваш заказ и приступили к его подготовке! Спасибо!
По готовности работы – напишем`.split('\n').join("<br>")

answers = [cost, ss_cost]






































cl = document.querySelector(".ph_input").parentElement
cl.style = "display: none;" // убрать введите сообщение


sha = document.createElement("select")
sha.className = "fasd"
btn = document.createElement("button")
btn.textContent = "Вставить"
btn.className = "btn_paste"
// d = sha.createElement("option")
// d.textContent = "hello"
// d2 = sha.createElement("option")
// d2.textContent = "helddsadlo"
divk = document.createElement("div")
divk.className = "sup-div"
document.querySelector(".side_bar_inner").append(divk)
ff = document.querySelector(".sup-div")
if (ff){
    
ff.append(sha)
ff.append(btn)
}
else{
    alert("Произошла какая-то ошибка... просьба обратиться к данилу")
}



op1 = document.createElement("option")
op1.textContent = "1. Стоимость работы"
op2 = document.createElement("option")
op2.textContent = "2. Оплата поступила"




spisok = document.querySelector(".fasd")
spisok.append(op1)
spisok.append(op2)
id = window.location['href'].split("sel=")[1]
try{
if (id.startsWith("c")){
    id = "20000000"+id.slice(1)
}
}

catch{
    id = "0"
}

document.addEventListener("click", function(e) {
    
    if (e.target.className=="btn_paste") {
        f = document.querySelector("#im_editable"+id)
        cl.style = "display: none;"
    
    val = sha.value
    



    if (f){
        f.innerHTML = answers[val.split(".")[0]-1]
    }
    else{
        alert("Произошла какая-то ошибка... просьба обратиться к данилу")
    }
    
    
    }
});





