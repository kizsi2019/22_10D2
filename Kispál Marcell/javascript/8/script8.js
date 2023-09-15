/*
var felnott = false;
if (felnott) {
    console.log('peti felnőtt')    
} else {
    console.log('peti gyerek')
}

var petikora = 28;

if (petikora >= 18) {
    console.log('peti felnőtt')
} else {
    console.log('peti gyerek')
}

petikora >=18 ? console.log('peti felnőtt') : console.log('peti gyerek');

var felnottvagygyerek = petikora >= 18 ? 'felnőtt' : 'gyerek';
console.log(felnottvagygyerek);*/

var film = 'Gladiátor';
var mufaj;

switch (film){
    case 'Shrek' : mufaj = 'mese'
        break;
    case 'Terminátor' : mufaj = 'akció'
        break;
    case 'Utazók' : mufaj = 'sci-fi'
        break
    default :
    mufaj = 'besorolatlan'
}

console.log(mufaj);

var kor = 20;
var nev = 'peti';

switch (true) {
    case kor < 13:
        console.log(nev + 'kisfiú')
        break;
    case kor >= 13 && kor <= 20;
        console.log(nev + 'tinédzser');
        break;
    case kor >= 20 && kor < 30;
        console.log(nev + 'fiatalember')
        break;
    default:
        console.log(nev + 'igazi férfi');

}
