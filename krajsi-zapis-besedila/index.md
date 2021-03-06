Naslov: Krajši zapis besedila
Povzetek:
	Da zapišemo črko s številko, potrebujemo pet prstov ali piskov ali
	znakcev, ne? Ne. Lahko jih potrebujemo tudi manj in več. (Manj in več?!)
Priprava: Krajši zapis besedila.pdf
Datoteke: 
	Drevesa.pdf
	Drevesa za otroke (opcijsko).pdf
	Besedila (nekodirana).pdf
	Koda s fiksno dolžino.pdf
	Koda s Huffmanom.pdf
	Koda s Huffmanom s presledki.pdf
	Morsejeva koda.pdf
Trajanje: 1 šolska ura
Povezave:
	http://en.wikipedia.org/wiki/Huffman_coding Huffmanovo kodiranje

Namen
-----

Otroci spoznajo idejo “kodiranja”: podatke lahko zapisujemo različno učinkovito, z različno dolžino zapisa. Mimogrede spoznavajo tudi drevesa.



**Potrebne predhodne aktivnosti:** ((dvojiski-zapis-stevil | Do koliko lahko šteje stonoga?)), ((Zapis in prenos besedil))

Potrebščine
-----------

Za vsakega otroka

- Trakci z besedili, ki jih bodo brali otroci. Trakci so v spremljajočem materialu, lahko pa pripraviš tudi svoja besedila (glej spodaj). Pripravi nekajkrat več trakcev, kot je otrok, saj bodo hoteli ponavljati igro
- Vsak otrok potrebuje tudi pisalo
- Otrokom utegne priti prav tudi tabela s črkami, ki je na poli Ujeti Štefan iz prejšnje aktivnosti
- Kreda za risanje dreves (drevesa so velika in zahtevajo kar nekaj krede)

Drevesa za kodiranje, narisana na šolskem dvorišču ali označena na travniku ali drugem primernem mestu. Namesto tega lahko natisnemo tudi liste z drevesi za vsakega otroka.

Dodatna navodila
----------------

Aktivnost je najboljše izvajati na prostem.

Na tla boš morala narisati drevo; primerna so asfaltna tla pred šolo, risanja pa bo zahtevalo veliko krede. Druga možnost je, da drevesa pripraviš na travniku tako, da v tla zapičiš palice in med njimi povlečeš vrvice, na koncu pa so zastavice z listki. To je primernejše za večje dogodke, saj zahteva več priprav.

Drevesa so na koncu tega opisa aktivnosti in na ločenih listih. Risanje Huffmanovega drevesa je zahtevnejše, zato je na listu narisano na kvadratni mreži. Mreže ne prerisuješ, temveč služi le kot pomoč pri risanju.

Narišeš lahko eno, dva ali tri drevesa.

Huffmanovo drevo, v katerem so različne črke na različni globini, je bistveni del aktivnosti.

V drugem drevesu so vse črke na isti višini. Drevo ustreza kodiranju, kakršnega je uporabljal ujeti Štefan. Za otroke je koristno, da vidijo povezavo med dvojiškim številskim sistemom in drevesi. Iz dreves vidijo tudi, kakšna je razlika med kodiranjem z enako in različno dolžino kod. Iz primerjave dreves jim je “fizično” očitno, da so pri Huffmanovem drevesu pogosti znaki bližje.

Drevo, ki ustreza Morsejevi kodi je zanimivo zaradi Morsejeve kode kot takšne, v sklopu aktivnosti pa je zanimivo, ker kaže primer kodiranja, v katerem je koda določenega znaka lahko prefiks kode drugega znaka. Tako je, na primer, črka I zapisana kot “..”, U pa kot “..-”. Zaradi tega v Morsejevem kodiranju potrebujemo tudi “presledke” med znaki. Morsejeva koda torej nima le dveh znakov, pike in črte, temveč tudi presledek.

Presodi, ali označiti veje s črkama L in D ali ne. Drevesa bodo preglednejša brez njih. Pri mlajših otrokih jih lahko izpustiš tudi, da bodo vadili levo in desno, vendar to raje stori le pri drevesih s konstantno dolžino zapisa, kjer bo zaradi ene napačne smeri napačna le ena črka. Pri Huffmanovih drevesih bo že ena napaka pokvarila večji del sporočila.

Za vsakega otroka pripravi trakove s sporočili. Otroci naj imajo različna sporočila, sicer bodo vsi hodili po isti poti. Na traku naj bo tudi dovolj prostora, da bodo otroci vanj pisali prebrano sporočilo.

Uporabiš lahko sporočila, objavljena na strani, ali pa sestaviš svoja s pomočjo temu namenjene spletne strani (glej povezavo na spletni strani z opisom aktivnosti – vanjo le skopiraš besedila, rezultat pa kopiraš v urejevalnik besedil, malo urediš in natisneš). Ker bo tega več listov, si boš delo precej olajšala, če bodo vsi zapisi dolgi enako število vrstic in boš lahko rezala več listov hkrati. (Sporočila, ki so objavljena na strani, so že pripravljena tako.)

Pri Huffmanovem kodiranju lahko uporabiš različico s presledki med znaki ali takšno, v kateri presledkov ni. Druga je veliko poučnejša, vendar ji je nekoliko težje slediti, zato pri mlajših otrocih (npr. prvi razredi OŠ) raje uporabi (tudi?) prvo.

Priprava lastnih besedil
------------------------

Če želite pripraviti svoja besedila, jih vnesite spodaj. Vsak stavek naj bo v svoji vrstici.

<style>
    #encoder {
        font-size: 15px;
        line-height: 20px;
        border: 2px dashed black;
        padding: 10px;
    }

    #encoder table {
        width: 600px;
    }

    th {
        width: 50;
    }

    tr { height: 70; }

    #encoder td, #encoder th {
        padding-bottom: 16px;
        vertical-align: top;
    }

    #encoded_morse table td {
        font-size: 32px;
    }

    th {
        text-align: right;
        padding-right: 10px;
    }
</style>
<script>

huffman_codes = {
    'z': 'DDDDD',
    'g': 'DDDDLD',
    'c': 'DDDDLL',
    't': 'DDDL',
    'e': 'DDL',
    ' ': 'DLD',
    'r': 'DLLD',
    'v': 'DLLLD',
    'd': 'DLLLL',
    'n': 'LDDD',
    'p': 'LDDLD',
    'l': 'LDDLL',
    'j': 'LDLDD',
    'm': 'LDLDL',
    'b': 'LDLLDD',
    'ž': 'LDLLDLDD',
    'š': 'LDLLDLDL',
    'h': 'LDLLDLL',
    'k': 'LDLLL',
    's': 'LLDDD',
    'u': 'LLDDLD',
    'f': 'LLDDLLD',
    'č': 'LLDDLLL',
    'o': 'LLDL',
    'i': 'LLLD',
    'a': 'LLLL'
}


morse_code = {
    ' ': '&nbsp; &nbsp; ',
    'e': '&middot;', 't': '-',
    'i': '&middot;&middot;', 'a': '&middot;-', 'n': '-&middot;', 'm': '--',
    's': '&middot;&middot;&middot;', 'u': '&middot;&middot;-', 'r': '&middot;-&middot;', 'ž': '&middot;--',
    'd': '-&middot;&middot;', 'k': '-&middot;-', 'g': '--&middot;', 'o': '---',
    'h': '&middot;&middot;&middot;&middot;', 'v': '&middot;&middot;&middot;-', 'f': '&middot;&middot;-&middot;', 'l': '&middot;-&middot;&middot;', 'p': '&middot;--&middot;', 'j': '&middot;---',
    'b': '-&middot;&middot;&middot;', 'č': '-&middot;&middot;-', 'c': '-&middot;-&middot;', 'z': '--&middot;&middot;', 'š': '----',
    'q': '--&middot;-', 'w': '&middot;--', 'x': '-&middot;&middot;-', 'y': '-&middot;--'
}

slov = ' abcčdefghijklmnoprsštuvzž.,';

function ord_enc_bin(c) {
    c = slov.indexOf(c);
    if (c == -1) {
        return undefined;
    }
    var e = '';
    for(var i = 5; i; i--) {
        e += c < 16 ? 'D' : 'L';
        c = (c & 15) << 1
    }
    return e;
}

function tab_enc(code_table) {
    return function (c) {
        return code_table[c]
    }
}

function encode(txt, f, delim) {
    var enc = '';
    var c;
    txt = txt.trim();
    for(c = 0; c < txt.length; c++) {
        var e = f(txt[c]);
        if (e !== undefined) {
            enc += e + delim;
        }
    }
    if (delim == '') {
        var enc2 = '';
        for(c = 0; c < enc.length; c += 50) {
            enc2 += enc.slice(c, c + 50) + '<br/>'
        }
        enc = enc2;
    }
    return enc;
}

function encode_txt(txt, dest, f, delim) {
    sents = txt.split('\n');
    enc = '<table>\n';
    for(i = 0; i < sents.length; i++) {
        enc += '<tr><th>' + (i + 1).toString() + '</th><td>' +
                encode(sents[i], f, delim) + '</td></tr>\n'
    }
    enc += '</table>'
    document.getElementById(dest).innerHTML = enc;
}

function encode_all(txt) {
    txt = txt.toLocaleLowerCase();
    encode_txt(txt, 'original', function(x) { return x; }, '');
    encode_txt(txt, 'encoded_binary', ord_enc_bin, ' ');
    encode_txt(txt, 'encoded_huffman', tab_enc(huffman_codes), '');
    encode_txt(txt, 'encoded_huffman_spc', tab_enc(huffman_codes), ' ');
    encode_txt(txt, 'encoded_morse', tab_enc(morse_code), '&nbsp; ');
}

</script>

<h1>Kodiranje besedila z različnimi sistemi</h1>
<p>Vnesi besedila. Vsak stavek naj bo v svoji vrstici.</p>
<textarea rows="10" cols="40" onkeyup="encode_all(this.value)"></textarea>
<div id="encoder">
**Zaporedne številke**
<div id="encoded_binary"></div>

**Huffmanova koda**
<div id="encoded_huffman"></div>

**Huffmanova s presledki**
<div id="encoded_huffman_spc"></div>

**Morsejeva koda**
<div id="encoded_morse"></div>

**Stavki**
<div id="original"></span></div>
</div>


Drugi viri in avtorji
---------------------

Navdih za uvodni del prihaja S [CS Unplugged: Sound Representation](http://csunplugged.org/modem). Avtor drugega dela je Janez Demšar, po ideji Mika Fellowsa, enega od avtorjev CS Unplugged.
