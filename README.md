### Crypto Currency Price Checker

## Risinājuma apraksts


Crypto Currency Price Checker ir ērtības rīks, kas ievērojami atvieglo kriptovalūtu portfeļa pārvaldīšanu.

Crypto Currency Price Checker darbojas automātiski, nodrošinot aktuālo kriptovalūtu cenām un periodisku atjaunošanu Excel failā. Šī rīka izmantošana ļauj ātri un efektīvi sekot līdzi savam kriptovalūtu portfeļam, vienlaikus atbrīvojot no nepieciešamības manuāli pielāgot katras monētas vērtību.

Šis noderīgais instruments ne tikai uzlabo pārvaldīšanas procesu, bet arī palielina datu precizitāti, nodrošinot aktuālu informāciju par kriptovalūtu tirgu. Tas ļauj lietotājiem ātri reaģēt uz cenām, veikt informētus lēmumus un efektīvi optimizēt savu kriptovalūtu portfeļa vērtību.

Ar Crypto Currency Price Checker var būt pilnīgi uzticīgs un automatizēts draugs, kas atvieglo ieguldījumu pārvaldīšanu kriptovalūtās, atstājot lietotājam vairāk laika un enerģijas svarīgām finanšu lēmumu pieņemšanas aspektiem.


## Izmantotās bibliotēkas
Šajā risinājumā tiek izmantotas trīs galvenās bibliotēkas: openpyxl, bs4 un requests.

openpyxl tiek izmantota, lai efektīvi strādātu ar Excel tabulām, nodrošinot datu iegūšanu un to nākamo aizpildīšanu pašā tabulā.

bs4 un requests tiek izmantotas, lai iegūtu informāciju par pašreizējām kriptovalūtu cenām.

##Risinājuma apraksts
Risinājuma sākumā tiek importētas nepieciešamās bibliotēkas.

Pēc tam tiek izveidotas mainīgās, kas satur saites uz kriptovalūtām, lai būtu iespējams iegūt aktuālās cenas. Tālāk tiek veikts pieprasījums, lai iegūtu nepieciešamo informāciju.

Izmantojot openpyxl bibliotēku un for ciklu, vērtības no "pašreizējās cenas" kolonnas tiek kopētas "iepriekšējo cenu" kolonnā, pēc tam tabula tiek saglabāta.

Notiek pārbaude, vai visām saitēm ir veiksmīgi izpildīts pieprasījums. Ja pieprasījumi tiek veiksmīgi pabeigti, tiek izgūta katra monētas cena attiecīgi. Iegūtā informācija tiek pārveidota par teksta virkni, atbrīvojoties no liekām detaļām, un pēc tam pārveidota par peldošo punktu (float) formātu.

Beigās tabula tiek aizpildīta ar iegūtajām vērtībām, tiek izvadīta informācija, tabula tiek saglabāta un aizvērta, noslēdzot procesu.
