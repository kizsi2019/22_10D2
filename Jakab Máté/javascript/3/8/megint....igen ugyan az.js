

var felnott = false;
if (felnott) {
    console.log('Béla felnőtt');
} else {
    console.log('Béla gyerek');
}

var belakora = 26;

if (belakora >= 18) {
    console.log('Béla felnőt');
} else {
    console.log('Béla gyerel');
}

belakora >=18 ? console.log('Béla felnőtt') : console.log('Béla gyerek');

var felnottVagyGyerek = belakora >=18 ? 'felnött' : 'gyerek';
console.log(felnottVagyGyerek); 

//

var film = 'Shrek';
var mufaj;

switch (film) {
    case 'Shrek' : mufaj = 'mese';
        break;
    case 'Terminator' : mufaj = 'akció';
        break
    case 'Utazók' : mufaj = 'sci-fi';
        break;
    default :
    mufaj = 'besoroltam' ;
}

console.log(mufaj)

var kor = 20;
var nev = 'Béla';

switch (true) {
    case kor < 13 :
        console.log(nev + 'kisfiú');
        break;
        case kor >= 13 && kor <= 20:
            console.log(nev + 'tinédzser');
            break
        case kor >= 20 && kor < 30:
            console.log('fiatalember');
            break;
        default:
            console.log(nev + 'igazi férfi');
    
}       