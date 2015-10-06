Naslov: Zapis in prenos besedil
Priprava: Zapis in prenos besedil.pdf
Datoteke: 
	Ujeti Štefan.pdf
	Besede s štirimi črkami.pdf
	Trakci z odstavkom besedila.pdf
Trajanje: 1 šolska ura
Vir: http://csunplugged.org/binary-numbers CS Unplugged: Binary Numbers
Povzetek:
	Če zna računalnik zapisovati le številke – kako potem shrani besedila?
Slike:
    2606 2594 43 46 69 48 53 60 2622-001 2626 0071

Namen
-----

Aktivnost osmisli prejšnjo: v prejšnji izvedo, da računalnik shranjuje le številke in izvedo, kako to počne. Zdaj vidijo, da lahko s številkami zapisujemo tudi druge reči, kot na primer besedila.

Vaja predstavlja tudi urjenje v seštevanju števil do 25.

**Potrebne predhodne aktivnosti:** ((dvojiski-zapis-stevil | Do koliko lahko šteje stonoga?))

Potrebščine
-----------

Za vsakega učenca (ali za par):

- pola s sporočilom ujetega Štefana,
- nekaj listkov z besedami; natisni in razreži nekaj izvodov pole s 55 besedami.

Za vsako skupino štirih učencev: različne “priprave” za shranjevanje in prenos dveh stanj, na primer:

- dve zastavici različnih barv,
- dve ropotuljici z različnim zvokom,
- piščalko ali ksilofon (zadoščata dva različna tona),
- dva lonca različne velikost in kuhalnica,
- vrv dolžine cca 2 m, 20 ščipalk za perilo in 20 starih igralnih kart ali listkov, ki so po eni strani črni ali po drugi beli,
- vrv dolžine cca 2m in 40 ščipalk za perilo v dveh različnih barvah – po 20 vsake barve

Za tekmovanje:

- en komplet oštevilčenih trakcev z odstavkom besedila za vsako skupino

Priprava lastnih besedil
------------------------

<script>

abeceda = 'abcčdefghijklmnoprsštuvzž.,';

function enc_bin(c) {
    var e = '';
    for(var i = 5; i; i--) {
        e += c < 16 ? '0' : '1';
        c = (c & 15) << 1
    }
    return e;
}


function encode_all(txt) {
    //alert("X");
    txt = ' ' + txt.toLocaleLowerCase();
    var i = 0;
    var enc = '<p>';
    for(c = 0; c < txt.length; c++) {
        var e = abeceda.indexOf(txt[c]);
        if (e == -1) {
            while (e == -1) {
                c++;
                if (c == txt.length) {
                    break;
                }
                var e = abeceda.indexOf(txt[c]);
            }
            if (c == txt.length) {
                break;
            }
            i++;
            enc += '</p>\n<p>' + i.toString() + '&nbsp;&nbsp;&nbsp;&nbsp;';
        }
        enc += enc_bin(e + 1) + '&nbsp;&nbsp;&nbsp;';
    }
    enc += "</p>";
    document.getElementById('encoded').innerHTML = enc;
}

</script>

Če želite sestaviti svoje besedilo, ga vpišite tule.

<textarea rows="10" cols="80" onkeyup="encode_all(this.value)"></textarea>
<div style="border: 2px solid black; padding: 4px; min-height: 20px;" id="encoded"></div>


Drugi viri in avtorji
---------------------

Ujeti Štefan prihaja s [CS Unplugged: Count the Dots](http://csunplugged.org/binary-numbers), ostala inspiracija za sicer izvirno aktivnost pa s [CS Unplugged: Modems Unplugged](http://csunplugged.org/modem)
