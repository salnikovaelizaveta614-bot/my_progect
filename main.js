const change = document.querySelector('.izm')
let name_iz = document.querySelector('.fail')
let name_iz2 = document.querySelector('.ima')
let name_iz3 = document.querySelector('.ins')
let saved_text = ""

change.addEventListener('click', function(){
    name_iz.style.gap = 0
    name_iz.innerHTML =  '<input type="text" id="name-input" placeholder="Введите имя">'
    const input = document.querySelector('#name-input')
    input.style.cssText = 'background:#A7AEB833; border:none; border-radius:8px 0 0 8px; padding:5px 10px;'
    const save = document.createElement('div')
    save.innerHTML = 'сохранить'
    save.style.fontSize = '16px'
    save.style.backgroundColor = '#ff9130'
    save.style.borderTopRightRadius = '8px'
    save.style.borderBottomRightRadius = '8px'
    save.style.padding = '5px 10px'
    save.style.border = 'none'
    save.style.cursor = 'pointer'
    name_iz.append(save)
    save.addEventListener('click', function(){
        saved_text = input.value
        save.remove()
        input.remove()
        name_iz.style.gap = '5px'
        name_iz2.textContent = saved_text
        name_iz.append(name_iz2)
        name_iz.append(change)
})
})

const knopka = document.createElement('div')
name_iz3.append(knopka)

knopka.innerHTML = '<input type="text" id="instr" placeholder="Введите инструменты">'
const inp = document.querySelector('#instr')
inp.style.cssText = 'background:#A7AEB833; border:none; border-radius:8px 0 0 8px; padding:5px 10px;'

const saved = document.createElement('div')
knopka.append(saved)
saved.innerHTML = '+'
saved.style.fontSize = '16px'
saved.style.display = 'flex'
saved.style.justifyContent = 'center'
saved.style.alignItems = 'flex-end'
saved.style.backgroundColor = '#ff9130'
saved.style.borderTopRightRadius = '8px'
saved.style.borderBottomRightRadius = '8px'
saved.style.padding = '5px 10px'
saved.style.border = 'none'
saved.style.cursor = 'pointer'
knopka.style.cssText = "display: flex;"

const listIns = []

saved.addEventListener('click', function(){
    insSave = inp.value
    if (insSave.length<40){
        knopka.remove()
        const instruments = document.createElement('inss')
        instruments.innerHTML = insSave
        name_iz3.append(instruments)
        instruments.style.cssText = 'background:#A7AEB833; border:none; border-radius:8px; padding:5px 10px;'
        name_iz3.append(knopka)
    }
    else{
        console.log("Слишком много текста, допустимо 60 символа")
    }
    inp.value = ''
})