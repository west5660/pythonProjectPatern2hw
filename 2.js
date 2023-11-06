let but1 = document.getElementById('but1')
let but2 = document.getElementById('but2')
let but3 = document.getElementById('but3')

but1.onclick = f1
but2.onclick = f2
but3.onclick = f3

function f1(){
    let req
    if (window.XMLHttpRequest) {
        req = new XMLHttpRequest();
    } else {
        req = new ActiveXObject("Microsoft.XMLHTTP");
    }
    req.open('GET','text.txt')
    req.onreadystatechange = function (){
        fotvet(req)
    }
    req.send()
}

function fotvet(req){
    console.log('nomer'+ req.readyState)
    if (req.readyState===4){
        console.log(req.response)
    }
}

function f2(){
    let req
    if (window.XMLHttpRequest) {
        req = new XMLHttpRequest();
    } else {
        req = new ActiveXObject("Microsoft.XMLHTTP");
    }
    req.open('GET','person.json')
    req.onload = function (){
        if(req.status===200){
            console.log('ok')

            console.log(req.response)
            let newobj = JSON.parse(req.response)
            console.log(newobj.name)
    }
        else {
            console.log('neok')
        }
    }
    req.send()
}

function f3() {
    let req
    if (window.XMLHttpRequest) {
        req = new XMLHttpRequest()
    } else {
        req = new ActiveXObject("Microsoft.XMLHTTP")
    }
    req.open('GET', 'agent.json')
    req.onreadystatechange = function () {
        if (req.readyState === 4 && req.status === 200) {
            let agent = JSON.parse(req.responseText);
            for (let key in agent) {
                if (key !== "agent") {
                    agent[key] = "*****"
                }
            }
            let agentinfa = document.getElementById("agentinfa")
            agentinfa.innerHTML = JSON.stringify(agent, null, 2)
        }
    }

    req.send()
}
