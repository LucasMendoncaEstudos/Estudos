var horario = new Date()
//var agora = horario.getHours()
var agora = 4
if (agora >= 0 || agora < 6){
    console.log("Esta de madrugada")
    console.log(`Agora são ${agora} Horas`)
}else if (agora >= 6 || agora < 12){
    console.log("Esta de manhã")
}else if(agora >= 12 || agora < 18){
    console.log("Esta de tarde")
}else{
    console.log("Está de noite")
}
console.log("fim")