function parimpar(n){
    if(n%2==0){
        return 'Par'
    }else{
        return 'Impar'
    }
}

console.log(parimpar(24))

function soma(n1=0,n2){
    return n1 + n2;
}
console.log(soma(2,4))

let v = function(x){
    return x*2
}
console.log(v(5))