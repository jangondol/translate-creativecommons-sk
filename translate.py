import os, subprocess, sys

# Constants
GIT_CLONE_DIRECTORY = "/tmp"
# GIT_CLONE_DIRECTORY = os.path.dirname(os.path.realpath(__file__))  # script directory
REPO_URL = "https://github.com/creativecommons/creativecommons.org"
REPO_NAME = "creativecommons.org"
LOCAL_PATH = os.path.join(GIT_CLONE_DIRECTORY, REPO_NAME)

BRANCH_NAME = "cc4-sk-legalcode"
COMMIT_HASH = "1ec8116f9a4a3e974c35681f0ac8f44cd74c6aa7"

LICENSES_PATH = "docroot/legalcode"
TRANSLATED_PATH = LICENSES_PATH  # TRANSLATED_PATH = "_translated"
LICENSES_DIR = os.path.join(LOCAL_PATH, LICENSES_PATH)
TRANSLATED_DIR = os.path.join(LOCAL_PATH, LICENSES_PATH)

nc_sa_strings = r"""
Creative Commons Legal Code
Creative Commons právne ujednanie

Attribution-NonCommercial-ShareAlike 4.0 International
Attribution-NonCommercial-ShareAlike („uvedenie autora — nekomerčné použitie — rovnaké šírenie“) 4.0 medzinárodná

Official translations of this license are available <a href="#languages">in other languages</a>.
Oficiálne preklady tejto licencie sú dostupné aj <a href="#languages">v ďalších jazykoch</a>.

Creative Commons Corporation (“Creative Commons”) is not a law firm and does not provide legal services or legal advice. Distribution of Creative Commons public licenses does not create a lawyer-client or other relationship. Creative Commons makes its licenses and related information available on an “as-is” basis. Creative Commons gives no warranties regarding its licenses, any material licensed under their terms and conditions, or any related information. Creative Commons disclaims all liability for damages resulting from their use to the fullest extent possible.
Creative Commons Corporation (“Creative Commons”) nie je advokátska kancelária ani neposkytuje právne služby alebo právne poradenstvo. Šírením textov verejných licencií Creative Commons nevzniká vzťah príkazného typu alebo iný obdobný vzťah. Creative Commons poskytuje texty verejných licencií a súvisejúce informácie tak, ako sú. Creative Commons nezodpovedá za texty verejných licencií ani za obsah licencovaný za týchto licenčných podmienok ani za súvisejúce informácie. Creative Commons v maximální možnej miere vylučuje všetku zodpovednosť za škodu, ktorá vznikne v dôsledku ich použitia.

Using Creative Commons Public Licenses
Používanie Verejných licencií Creative Commons

Creative Commons public licenses provide a standard set of terms and conditions that creators and other rights holders may use to share original works of authorship and other material subject to copyright and certain other rights specified in the public license below. The following considerations are for informational purposes only, are not exhaustive, and do not form part of our licenses.
Texty verejných licencií Creative Commons predstavujú štandardizovaný soubor licenčných podmienok, ktoré môžu autori alebo ďalší nositelia práv použiť pre zdieľanie chránených autorských diel a ďalšieho obsahu, ktorý podlieha autorským právam a ďalším právam, ktoré sú uvedené nižšie v tejto verejnej licencii. Nasledujúce upozornenia slúžia výhradne pre informačné účely, nie sú vyčerpávajúce a nie sú súčasťou týchto licencií.

<strong>Considerations for licensors:</strong> Our public licenses are intended for use by those authorized to give the public permission to use material in ways otherwise restricted by copyright and certain other rights. Our licenses are irrevocable. Licensors should read and understand the terms and conditions of the license they choose before applying it. Licensors should also secure all rights necessary before applying our licenses so that the public can reuse the material as expected. Licensors should clearly mark any material not subject to the license. This includes other CC-licensed material, or material used under an exception or limitation to copyright. <a href="//wiki.creativecommons.org/Considerations_for_licensors_and_licensees#Considerations_for_licensors">More considerations for licensors.</a>
<strong>Upozornenia pre poskytovateľov:</strong> Tieto verejné licencie sú určené osobám oprávneným poskytovať verejnosti oprávnenia k použitu obsahu spôsobom, ktorý je inak vyhradený vykonávateľom autorských a niektorých ďalších práv. Tieto licencie sú neodvolateľné. Poskytovatelia by si mali licenčné podmienky riadne preštudovať tak, aby im porozumeli skôr ako sa ich rozhodnú použiť. Poskytovatelia by si taktiež pred použitím týchto licencií mali zaistiť všetky potrebné práva tak, aby mohla verejnosť použiť obsah predpokladaným spôsobom. Poskytovatelia by mali jednoznačne označiť všetok obsah, na ktorý sa licencie nevzťahujú, a to vrátane ďalších diel poskytnutých pod licenciami CC alebo materiálov použitých na základe výnimky či obmedzenia autorských práv. <a href="//wiki.creativecommons.org/Considerations_for_licensors_and_licensees#Considerations_for_licensors">Ďalšie upozornenia pre poskytovateľov.</a>

<strong>Considerations for the public:</strong> By using one of our public licenses, a licensor grants the public permission to use the licensed material under specified terms and conditions. If the licensor’s permission is not necessary for any reason–for example, because of any applicable exception or limitation to copyright–then that use is not regulated by the license. Our licenses grant only permissions under copyright and certain other rights that a licensor has authority to grant. Use of the licensed material may still be restricted for other reasons, including because others have copyright or other rights in the material. A licensor may make special requests, such as asking that all changes be marked or described. Although not required by our licenses, you are encouraged to respect those requests where reasonable. <a href="//wiki.creativecommons.org/Considerations_for_licensors_and_licensees#Considerations_for_licensees">More considerations for the public.</a>
<strong>Upozornenia pre verejnosť:</strong> Použitím niektorej z týchto verejných licencií poskytuje poskytovateľ verejnosti oprávnenie k použitiu licencovaného obsahu za stanovených licenčných podmienok. Pokiaľ z nejakého dôvodu nie je súhlas poskytovateľa nevyhnutný, napríklad z dôvodu uplatnenia niektorej výnimky alebo obmedzenia autorského práva, potom sa na dané použitie táto licenca nevzťahuje. Na základe týchto licencuí sú poskytované výlučne oprávnenia k výkonu autorských a niektorých ďalších práv, ktoré je poskytovateľ oprávnený poskytovať. Použitie licencovaného obsahu môže být napriek tomu obdmedzené z ďalších dôvodov, napríklad preto, že nositeľom autorských, či ďalších práv k nemu sa vzťahujúcich, je niekto iný. Poskytovateľ môže vzniesť zvláštne požiadavky, napríklad požiadať o to, aby boli označené alebo popísané všetky zmeny. Hoci to tieto licencie nevyžadujú, nabádame Vás, aby ste tieto požiadavky rešpektovali, pokiaľ sú primerané. <a href="//wiki.creativecommons.org/Considerations_for_licensors_and_licensees#Considerations_for_licensees">Ďalšie upozornenia pre verejnosť.</a>

Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International Public License
Creative Commons Attribution-NonCommercial-ShareAlike („uvedenie autora — nekomerčné použitie — rovnaké šírenie“) 4.0 medzinárodná verejná licencia

By exercising the Licensed Rights (defined below), You accept and agree to be bound by the terms and conditions of this Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International Public License ("Public License"). To the extent this Public License may be interpreted as a contract, You are granted the Licensed Rights in consideration of Your acceptance of these terms and conditions, and the Licensor grants You such rights in consideration of benefits the Licensor receives from making the Licensed Material available under these terms and conditions.
Výkonom práv, ku ktorému Vás oprávňuje nižšie uvedená licencia, vyjadrujete súhlas s podmienkami medzinárodnej verejnej licencie Creative Commons Attribution-NonCommercial-ShareAlike („uvedenie autora — nekomerčné použitie — rovnaké šírenie“) 4.0 (ďalej len „Verejná licencia“), ku ktorej týmto zároveň pristupujete. Táto Verejná licencia by sa mala vykladať ako zmluva, ktorá Vás oprávňuje k výkonu Licencovaných práv na základe Vášho súhlasu s podmienkami stanovenými v tejto Verejnej licencii a Poskytovateľ Verejnej licencie Vám udeľuje predmetný súhlas za účelom dosiahnutia úžitkov zo sprístupnenia Predmetu Verejnej licencie verejnosti podľa podmienok stanovených touto Verejnou licenciou.

Section 1 – Definitions.
1. časť — Definície.

<strong>Adapted Material</strong> means material subject to Copyright and Similar Rights that is derived from or based upon the Licensed Material and in which the Licensed Material is translated, altered, arranged, transformed, or otherwise modified in a manner requiring permission under the Copyright and Similar Rights held by the Licensor. For purposes of this Public License, where the Licensed Material is a musical work, performance, or sound recording, Adapted Material is always produced where the Licensed Material is synched in timed relation with a moving image.
<strong>Adaptovaný obsah</strong> je obsah chránený autorským alebo obdobným právom odvodený alebo založený na Predmete Verejnej licencie a v ktorom je Predmet Verejnej licencie preložený, upravený, zmenený alebo inak spracovaný spôsobom vyžadujúcim súhlas Poskytovateľa Verejnej licencie k výkonu autorských alebo obdobných práv. Na účely tejto Verejnej licencie v prípade, ak je Predmetom Verejnej licencie hudobné dielo, umelecký výkon hudobného diela alebo jeho zvukový záznam, adaptovaný obsah vzniká vždy aj pri časovo synchrónnom spojení s pohyblivou obrazovou zložkou.

<strong>Adapter's License</strong> means the license You apply to Your Copyright and Similar Rights in Your contributions to Adapted Material in accordance with the terms and conditions of this Public License.
<strong>Spracovateľská licencia</strong> je licenciou, ktorú Vy uplatníte pri nakladaní s obsahom, ktorý je výsledkom Vášho spracovania Predmetu Verejnej licencie a ktorý je chránený Autorským alebo obdobným právom, a to podľa podmienok tejto Verejnej licencie.

<strong>BY-NC-SA Compatible License</strong> means a license listed at <a href="//creativecommons.org/compatiblelicenses"> creativecommons.org/compatiblelicenses</a>, approved by Creative Commons as essentially the equivalent of this Public License.
<strong>BY-NC-SA kompatibilná licencia</strong> predstavuje licenciu uvedenú na <a href="//creativecommons.org/compatiblelicenses">creativecommons.org/compatiblelicenses</a> schválenú Creative Commons ako v zásade zodpovedajúca tejto Verejnej licencii.

<strong>Copyright and Similar Rights</strong> means copyright and/or similar rights closely related to copyright including, without limitation, performance, broadcast, sound recording, and Sui Generis Database Rights, without regard to how the rights are labeled or categorized. For purposes of this Public License, the rights specified in Section <a href="#s2b">2(b)(1)-(2)</a> are not Copyright and Similar Rights.
<strong>Autorské a obdobné práva</strong> sú autorské práva a/alebo obdobné práva blízko súvisiace s autorskými právami vrátane, nie však výlučne, práva k umeleckému výkonu, práva k vysielaniu, práva k zvukovému záznamu a osobitné práva k databáze, a to bez ohľadu na pomenovanie alebo kategorizáciu týchto práv. Na účely tejto Verejnej licencie sa práva uvedené v <a href="#s2b">2. časti písm. b. body 1 a 2</a> nepovažujú za autorské a obdobné práva.

<strong>Effective Technological Measures</strong> means those measures that, in the absence of proper authority, may not be circumvented under laws fulfilling obligations under Article 11 of the WIPO Copyright Treaty adopted on December 20, 1996, and/or similar international agreements.
<strong>Účinné technologické opatrenia</strong> predstavujú opatrenia, ktoré nie je dovolené, bez súhlasu nositeľa práv alebo umožnenia zákonom, odstrániť v zmysle právnych úprav vychádzajúcich z čl. 11 Zmluvy WIPO o autorskom práve uzavretej dňa 20. decembra 1996 a/alebo z obdobných medzinárodných zmlúv.

<strong>Exceptions and Limitations</strong> means fair use, fair dealing, and/or any other exception or limitation to Copyright and Similar Rights that applies to Your use of the Licensed Material.
<strong>Výnimky a obmedzenia</strong> predstavujú uplatnenie doktrín „fair use“ a „fair dealing“, teda možnosti použitia predmetu ochrany bez súhlasu nositeľa práv pri zachovaní presne stanovených všeobecne platných a záväzných podmienok a/alebo uplatnenie iných výnimiek a obmedzení autorských a obdobných práv, ktoré sa uplatnia na Vaše použitie Predmetu Verejnej licencie.

<strong>License Elements</strong> means the license attributes listed in the name of a Creative Commons Public License. The License Elements of this Public License are Attribution, NonCommercial, and ShareAlike.
<strong>Licenčné prvky</strong> predstavujú charakteristiku licencie uvedenú v názve verejnej licencie Creative Commons. Licenčné prvky tejto Verejnej licencie sú „Attribution“, „NonCommercial“ a „ShareAlike“ („uvedenie autora“, „nekomerčné použitie“ a „rovnaké šírenie“).

<strong>Licensed Material</strong> means the artistic or literary work, database, or other material to which the Licensor applied this Public License.
<strong>Predmet Verejnej licencie</strong> je umelecké alebo literárne dielo, databáza alebo iný obsah, na použitie ktorého Poskytovateľ uplatnil túto Verejnú licenciu.

<strong>Licensed Rights</strong> means the rights granted to You subject to the terms and conditions of this Public License, which are limited to all Copyright and Similar Rights that apply to Your use of the Licensed Material and that the Licensor has authority to license.
<strong>Licencované práva</strong> sú Autorské a obdobné práva Poskytovateľa, na výkon ktorých Vás oprávňuje táto Verejná licencia na základe súhlasu Poskytovateľa a za podmienok v nej vyjadrených, vzťahujúce sa na Vaše použitie Predmetu Verejnej licencie, a na udelenie súhlasu na výkon ktorých je Poskytovateľ oprávnený.

<strong>Licensor</strong> means the individual(s) or entity(ies) granting rights under this Public License.
<strong>Poskytovateľ</strong> je fyzická alebo právnická osoba (osoby), ktorá udelí súhlas na použitie Predmetu Verejnej licencie a výkon Licencovaných práv („licencia“) podľa tejto Verejnej licencie.

<strong>NonCommercial</strong> means not primarily intended for or directed towards commercial advantage or monetary compensation. For purposes of this Public License, the exchange of the Licensed Material for other material subject to Copyright and Similar Rights by digital file-sharing or similar means is NonCommercial provided there is no payment of monetary compensation in connection with the exchange.
<strong>Nekomerčné použitie</strong> predstavuje použitie na účel, ktorý nie je priamo ani nepriamo obchodný alebo postavený na finančnom prospechu. Na účely tejto Verejnej licencie sa za nekomerčné použitie považuje výmena Predmetu Verejnej licencie za iný obsah chránený Autorskými alebo obdobnými právami prostredníctvom digitálneho alebo obdobného šírenia súborov, pokiaľ v spojení s výmenou nedôjde k finančnej odplate.

<strong>Share</strong> means to provide material to the public by any means or process that requires permission under the Licensed Rights, such as reproduction, public display, public performance, distribution, dissemination, communication, or importation, and to make material available to the public including in ways that members of the public may access the material from a place and at a time individually chosen by them.
<strong>Šírenie</strong> predstavuje poskytnutie obsahu verejnosti akýmkoľvek spôsobom, ktorý si vyžaduje dovolenie v zmysle Licencovaných práv, najmä vyhotovenie rozmnoženiny, verejné vystavenie, verejné vykonanie, verejné rozširovanie obsahu vrátane jeho dovozu, verejný prenos a sprístupňovanie verejnosti takým spôsobom, aby k obsahu mal jednotlivec prístup z miesta a v čase, ktorý si sám zvolí.

<strong>Sui Generis Database Rights</strong> means rights other than copyright resulting from Directive 96/9/EC of the European Parliament and of the Council of 11 March 1996 on the legal protection of databases, as amended and/or succeeded, as well as other essentially equivalent rights anywhere in the world.
<strong>Osobitné právo k databáze</strong> predstavuje práva odlišné od autorského práva, ktoré vyplýva zo Smernice Európskeho parlamentu a Rady 9/96/ES z 11. marca 1996 o právnej ochrane databáz v znení jej zmien a doplnení a/alebo nových právnych úprav, ktoré by ju nahradili, ako aj z iných porovnateľných práv platných kdekoľvek na svete.

<strong>You</strong> means the individual or entity exercising the Licensed Rights under this Public License. <strong>Your</strong> has a corresponding meaning.
<strong>Vy</strong> (v príslušnom gramatickom tvare a/alebo vo forme zámena) je fyzická alebo právnická osoba vykonávajúca Licencované práva podľa tejto Verejnej licencie.

Section 2 – Scope.
2. časť — Obsah práv a povinností.

<strong>License grant</strong>.
<strong>Udelenie licencie</strong>.

Subject to the terms and conditions of this Public License, the Licensor hereby grants You a worldwide, royalty-free, non-sublicensable, non-exclusive, irrevocable license to exercise the Licensed Rights in the Licensed Material to:
Podľa podmienok v tejto Verejnej licencii uvedených Vám týmto Poskytovateľ udeľuje celosvetovú, bezodplatnú, nevýhradnú, neodvolateľnú licenciu, bez možnosti udelenia sublicencie, na použitie Predmetu Verejnej licencie týmito spôsobmi:

reproduce and Share the Licensed Material, in whole or in part, for NonCommercial purposes only; and
vyhotovením rozmnoženiny a Šírením Predmetu Verejnej licencie vcelku alebo jeho časti výlučne na Nekomerčné použitie; a

produce, reproduce, and Share Adapted Material for NonCommercial purposes only.
vytvorením, vyhotovením rozmnoženiny a Šírením Adaptovaného obsahu výlučne na Nekomerčné použitie.

<span style="text-decoration: underline;">Exceptions and Limitations</span>. For the avoidance of doubt, where Exceptions and Limitations apply to Your use, this Public License does not apply, and You do not need to comply with its terms and conditions.
<span style="text-decoration: underline;">Výnimky a obmedzenia</span>. Na odstránenie akejkoľvek pochybnosti, na prípady, ak sa na Vaše použitie Predmetu verejnej licencie uplatnia Výnimky a obmedzenia, sa táto Verejná licencia nevzťahuje a Vy nie ste viazaný jej podmienkami.

<span style="text-decoration: underline;">Term</span>. The term of this Public License is specified in Section <a href="#s6a">6(a)</a>.
<span style="text-decoration: underline;">Trvanie</span>. Trvanie tejto Verejnej licencie je upravené v <a href="#s6a">6. časti písm. a.</a>

<span style="text-decoration: underline;">Media and formats; technical modifications allowed</span>. The Licensor authorizes You to exercise the Licensed Rights in all media and formats whether now known or hereafter created, and to make technical modifications necessary to do so. The Licensor waives and/or agrees not to assert any right or authority to forbid You from making technical modifications necessary to exercise the Licensed Rights, including technical modifications necessary to circumvent Effective Technological Measures. For purposes of this Public License, simply making modifications authorized by this Section <a href="#s2a4">2(a)(4)</a> never produces Adapted Material.
<span style="text-decoration: underline;">Médiá a formáty; dovolenie technických úprav</span>. Poskytovateľ Vás oprávňuje na výkon Licencovaných práv prostredníctvom všetkých médií a vo všetkých formátoch v súčasnosti známych alebo v budúcnosti vytvorených, ako aj na vykonanie technických úprav potrebných na riadny výkon Licencovaných práv. Poskytovateľ sa zdrží výkonu práv a/alebo nebude uplatňovať žiadne nároky na zákaz technických úprav potrebných na Váš výkon Licencovaných práv vrátane technických úprav potrebných na odstránenie Účinných technologických opatrení. Na účely tejto Verejnej licencie platí, že vykonanie výlučne úprav dovolených podľa <a href="#s2a4">2. časti písm. a. bod 4</a> nikdy nezakladá vznik Adaptovaného obsahu.

<span style="text-decoration: underline;">Downstream recipients</span>.
<span style="text-decoration: underline;">Následní používatelia</span>.

<span style="text-decoration: underline;">Offer from the Licensor – Licensed Material</span>. Every recipient of the Licensed Material automatically receives an  offer from the Licensor to exercise the Licensed Rights under the terms and conditions of this Public License.
<span style="text-decoration: underline;">Ponuka od Poskytovateľa — Predmet Verejnej licencie</span>. Každý používateľ Predmetu Verejnej licencie automaticky dostane ponuku na výkon Licencovaných práv podľa podmienok tejto Verejnej licencie od Poskytovateľa.

<span style="text-decoration: underline;">Additional offer from the Licensor – Adapted Material</span>. Every recipient of Adapted Material from You automatically receives an  offer from the Licensor to exercise the Licensed Rights in the Adapted Material under the conditions of the Adapter’s License You apply.
<span style="text-decoration: underline;">Dodatočná ponuka od Poskytovateľa - Adaptovaný obsah</span>. Každý používateľ Adaptovaného obsahu od Vás automaticky dostane ponuku Poskytovateľa na výkon Licencovaných práv k Adaptovanému obsahu podľa podmienok Spracovateľskej licencie, ktorú Vy uplatníte.

<span style="text-decoration: underline;">No downstream restrictions</span>. You may not offer or impose any additional or different terms or  conditions on, or apply any Effective Technological Measures to, the Licensed Material if doing so restricts exercise of the Licensed Rights by any recipient of the Licensed Material.
<span style="text-decoration: underline;">Žiadne obmedzenia pre ďalšie použitie</span>. Vy nie ste oprávnený na ponúknutie alebo zavádzanie žiadnych ďalších podmienok, ako ani na uplatnenie žiadnych Účinných technologických opatrení vo vzťahu k použitiu Predmetu Verejnej licencie, ak by takýmto konaním mohlo dôjsť k obmedzeniu Licencovaných práv akéhokoľvek používateľa Predmetu Verejnej licencie.

<span style="text-decoration: underline;">No endorsement</span>. Nothing in this Public License constitutes or may be construed as permission to assert or imply that You are, or that Your use of the Licensed Material is, connected with, or sponsored, endorsed, or granted official status by, the Licensor or others designated to receive attribution as provided in Section <a href="#s3a1Ai">3(a)(1)(A)(i)</a>.
<span style="text-decoration: underline;">Bez schválenia</span>. Nič v tejto verejnej licencii nekonštituuje ani nemôže byť konštruované tak, aby zakladalo alebo v sebe obsahovalo vznik nároku vo Váš prospech na uvedenia autorstva, patriaceho Poskytovateľovi alebo iným určeným osobám podľa <a href="#s3a1Ai">3. časti písm. a. bod 1 písm. A. bod i.</a>, alebo by, na základe Vášho použitia Predmetu Verejnej licencie, zakladalo status autora, ktorý by bol spojený, podporovaný, schválený alebo udelený Poskytovateľom alebo inou určenou osobou podľa <a href="#s3a1Ai">3. časti písm. a. bod 1 písm. A. bod i.</a>

<strong>Other rights</strong>.
<strong>Ďalšie práva</strong>.

Moral rights, such as the right of integrity, are not licensed under this Public License, nor are publicity, privacy, and/or other similar personality rights; however, to the extent possible, the Licensor waives and/or agrees not to assert any such rights held by the Licensor to the limited extent necessary to allow You to exercise the Licensed Rights, but not otherwise.
Osobnostné práva (ako napríklad právo na nedotknuteľnosť diela), právo na súkromie, rovnako ako ani iné všeobecné osobnostné práva nie sú predmetom licencie podľa tejto Verejnej licencie, avšak Poskytovateľ sa v najširšom možnom rozsahu zdrží výkonu týchto práv alebo si nebude uplatňovať tieto práva, a to výlučne v rozsahu, ktorý je nevyhnutný na umožnenie výkonu Licencovaných práv Vami a za žiadnym iným účelom.

Patent and trademark rights are not licensed under this Public License.
Patentové a známkové právo nie je predmetom licencie podľa tejto Verejnej licencie.

To the extent possible, the Licensor waives any right to collect royalties from You for the exercise of the Licensed Rights, whether directly or through a collecting society under any voluntary or waivable statutory or compulsory licensing scheme. In all other cases the Licensor expressly reserves any right to collect such royalties, including when the Licensed Material is used other than for NonCommercial purposes.
Poskytovateľ sa v najširšom možnom rozsahu zdrží výkonu akýchkoľvek práv, na základe ktorých môže od Vás vyberať odmenu za výkon Licencovaných práv, a to bez ohľadu na to či priamo alebo prostredníctvom organizácie kolektívnej správy na základe výkonu dobrovoľnej, zákonnej alebo povinnej kolektívnej správy. V akýchkoľvek ďalších prípadoch si Poskytovateľ právo na výber odmeny za použitie diela výslovne vyhradzuje, vrátane prípadu, ak je Predmet Verejnej licencie použitý inak ako na Nekomerčné použitie.

Section 3 – License Conditions.
3. časť — Licenčné podmienky.

Your exercise of the Licensed Rights is expressly made subject to the following conditions.
Váš výkon Licencovaných práv podlieha výslovne nasledujúcim podmienkam.

<strong>Attribution</strong>.
<strong>Uvedenie autora</strong>.

If You Share the Licensed Material (including in modified form), You must:
Ak Šírite Predmet Verejnej licencie (vrátane jeho modifikácií) Ste povinný:

retain the following if it is supplied by the Licensor with the Licensed Material:
v prípade ich uvedenia Poskytovateľom spolu s Predmetom Verejnej licencie, zachovať a uvádzať nasledujúce údaje:

identification of the creator(s) of the Licensed Material and any others designated to receive attribution, in any reasonable manner requested  by the Licensor (including by pseudonym if designated);
identifikácia autora (autorov) Predmetu Verejnej licencie, ako aj ďalších nositeľov práv oprávnených na ich uvádzanie, akýmkoľvek vhodným spôsobom požadovaným Poskytovateľom (vrátane pseudonymu ak je určený);

a copyright notice;
vyhlásenie o autorských právach („copyrightová výhrada“);

a notice that refers to this Public License;
vyhlásenie odkazujúce na túto Verejnú licenciu;

a notice that refers to the disclaimer of warranties;
vyhlásenie odkazujúce na odopretie záruk;

a URI or hyperlink to the Licensed Material to the extent reasonably practicable;
URI („jednotný identifikátor zdroja“) alebo hyperlink na Predmet Verejnej licencie v uskutočniteľnom rozsahu;

indicate if You modified the Licensed Material and retain an indication of any previous modifications; and
uviesť či Ste upravili Predmet Verejnej licencie spolu s uvedením všetkých predchádzajúcich úprav; a

indicate the Licensed Material is licensed under this Public License, and include the text of, or the URI or hyperlink to, this Public License.
uviesť, že Predmet Verejnej licencie je používaný a je predmetom licencie podľa tejto Verejnej licencie a pripojiť text, URI („jednotný identifikátor zdroja“) alebo hyperlink tejto Verejnej licencie.

You may satisfy the conditions in Section <a href="#s3a1">3(a)(1)</a> in any reasonable manner based on the medium, means, and context in which You Share the Licensed Material. For example, it may be reasonable to satisfy the conditions by providing a URI or hyperlink to a resource that includes the required information.
Podmienky určené podľa <a href="#s3a1">3. časti písm. a. bod 1</a> môžete naplniť akýmkoľvek vhodným spôsobom v závislosti od média, spôsobu a kontextu Šírenia Predmetu Verejnej licencie. Vhodným spôsobom naplnenia podmienok môže byť napríklad uvedenie URI („jednotný identifikátor zdroja“) alebo hyperlinku zdroja obsahujúceho požadované informácie.

If requested by the Licensor, You must remove any of the information required by Section <a href="#s3a1A">3(a)(1)(A)</a> to the extent reasonably practicable.
Na požiadanie Poskytovateľa Ste povinný, v uskutočniteľnom rozsahu, odstrániť akékoľvek z informácií požadovaných podľa <a href="#s3a1A">3. časti písm. a. bod 1 písm. A</a>.

<strong>ShareAlike</strong>.
<strong>Rovnaké šírenie</strong>.

In addition to the conditions in Section <a href="#s3a">3(a)</a>, if You Share Adapted Material You produce, the following conditions also apply.
V nadväznosti na podmienky ustanovené v <a href="#s3a">3. časti písm. a.</a>, ak Šírite Adaptovaný obsah, ktorý je Vaším výtvorom, uplatnia sa aj nasledovné podmienky.

The Adapter’s License You apply must be a Creative Commons license with the same License Elements, this version or later, or a BY-NC-SA Compatible License.
Spracovateľská licencia, ktorú uplatníte musí byť licenciou Creative Commons s rovnakými Licenčnými prvkami, táto alebo neskoršia verzia alebo BY-NC-SA kompatibilná licencia.

You must include the text of, or the URI or hyperlink to, the Adapter's License You apply. You may satisfy this condition in any reasonable manner based on the medium, means, and context in which You Share Adapted Material.
Ste povinný pripojiť text, URI („jednotný identifikátor zdroja“) alebo hyperlink Spracovateľskej licencie, ktorú uplatníte. Túto podmienku Ste povinný splniť akýmkoľvek vhodným spôsobom v závislosti od média, spôsobu a kontextu, v ktorom Šírite Adaptovaný obsah.

You may not offer or impose any additional or different terms or conditions on, or apply any Effective Technological Measures to, Adapted Material that restrict exercise of the rights granted under the Adapter's License You apply.
Vy nie ste oprávnený na ponúknutie alebo zavádzanie žiadnych ďalších podmienok, ako ani na uplatnenie žiadnych Účinných technologických opatrení vo vzťahu k použitiu Adaptovaného obsahu, ak by takýmto konaním mohlo dôjsť k obmedzeniu výkonu práv udelených na základe Spracovateľskej licencie, ktorú Ste uplatnili.

Section 4 – Sui Generis Database Rights.
4. časť — Osobitné práva k databáze.

Where the Licensed Rights include Sui Generis Database Rights that apply to Your use of the Licensed Material:
Ak obsahom Licencovaných práv je Osobitné právo k databáze, ktoré sa uplatní pri Vašom použití Predmetu Verejnej licencie:

for the avoidance of doubt, Section <a href="#s2a1">2(a)(1)</a> grants You the right to extract, reuse, reproduce, and Share all or a substantial portion of the contents of the database for NonCommercial purposes only;
na odstránenie akýchkoľvek pochybností, Ste, podľa <a href="#s2a1">2. časti písm. a. bod 1</a>, oprávnený na extrakciu, reutilizáciu, vyhotovenie rozmnoženiny a Šírenie celého obsahu databázy alebo jej podstatnej časti výlučne na Nekomerčné použitie;

if You include all or a substantial portion of the database contents in a database in which You have Sui Generis Database Rights, then the database in which You have Sui Generis Database Rights (but not its individual contents) is Adapted Material, including for purposes of Section <a href="#s3b">3(b)</a>; and
ak spojíte celý obsah databázy alebo jej podstatnú časť s databázou, ku ktorej Vy vykonávate osobitné práva, databáza, ku ktorej Vy vykonávate osobitné práva (nie však jej individuálne obsahové zložky) sa stáva Adaptovaným obsahom; a

You must comply with the conditions in Section <a href="#s3a">3(a)</a> if You Share all or a substantial portion of the contents of the database.
pri Šírení obsahu databázy alebo jej podstatnej časti Ste viazaný podmienkami podľa <a href="#s3a">3(a)</a>3. časti písm. a.</a>

For the avoidance of doubt, this Section <a href="#s4">4</a> supplements and does not replace Your obligations under this Public License where the Licensed Rights include other Copyright and Similar Rights.
Na odstránenie akýchkoľvek pochybností, táto <a href="#s4">4. časť</a> dopĺňa a nenahrádza Vaše záväzky, podľa tejto Verejnej licencie v prípadoch, ak Licencované práva zahŕňajú ďalšie autorské a obdobné práva.

Section 5 – Disclaimer of Warranties and Limitation of Liability.
5. časť — Odopretie záruk a obmedzenie zodpovednosti.

Unless otherwise separately undertaken by the Licensor, to the extent possible, the Licensor offers the Licensed Material as-is and as-available, and makes no representations or warranties of any kind concerning the Licensed Material, whether express, implied, statutory, or other. This includes, without limitation, warranties of title, merchantability, fitness for a particular purpose, non-infringement, absence of latent or other defects, accuracy, or the presence or absence of errors, whether or not known or discoverable. Where disclaimers of warranties are not allowed in full or in part, this disclaimer may not apply to You.
Pokiaľ nie je osobitne Poskytovateľom vymienené inak, Poskytovateľ v najširšom možnom rozsahu poskytuje Predmet Verejnej licencie ako stojí a leží a ako je prístupný a neposkytuje žiadne vyhlásenia a ani záruky vo vzťahu k Predmetu Verejnej licencie, a to ani výslovné ani odvodené, ani zákonné, ani iné. Uvedené zahŕňa aj, nie však výlučne, záruky právneho dôvodu, obchodného potenciálu, určenia pre konkrétny účel, neporušenia práv duševného vlastníctva, neexistencie vád tak zjavných ako aj skrytých, presnosti, existencie alebo neexistencie chýb zjavných alebo objaviteľných. Ak nie je odopretie záruk prípustné celkovo alebo v časti, toto odopretie sa na Vás nebude vzťahovať.

To the extent possible, in no event will the Licensor be liable to You on any legal theory (including, without limitation, negligence) or otherwise for any direct, special, indirect, incidental, consequential, punitive, exemplary, or other losses, costs, expenses, or damages arising out of this Public License or use of the Licensed Material, even if the Licensor has been advised of the possibility of such losses, costs, expenses, or damages. Where a limitation of liability is not allowed in full or in part, this limitation may not apply to You.
V najširšom možnom rozsahu Poskytovateľ v žiadnom prípade nebude zodpovedný, a to v zmysle akejkoľvek právnej doktríny (vrátane, nie však výlučne v zmysle konceptu nedbanlivosti) či inak za akúkoľvek priamu, osobitnú, nepriamu, náhodnú, následnú, trestnoprávnu, exemplárnu či inú škodu, stratu, výdavok či náklad vychádzajúcu z uplatnenia tejto Verejnej licencie alebo použitie Predmetu Verejnej licencie, a to dokonca aj v prípade, ak bol Poskytovateľ poučený o možnosti vzniku takejto škody, straty, výdavku či nákladu. Ak nie je obmedzenie zodpovednosti prípustné celkovo alebo v časti, toto obmedzenie sa na Vás nebude vzťahovať.

The disclaimer of warranties and limitation of liability provided above shall be interpreted in a manner that, to the extent possible, most closely approximates an absolute disclaimer and waiver of all liability.
Odopretie záruk a obmedzenie zodpovednosti ako je vyššie uvedené je potrebné vykladať v najširšom možnom význame čo najbližšie k absolútnemu odopretiu a zrieknutia sa všetkej zodpovednosti.

Section 6 – Term and Termination.
6. časť — Trvanie a ukončenie.

This Public License applies for the term of the Copyright and Similar Rights licensed here. However, if You fail to comply with this Public License, then Your rights under this Public License terminate automatically.
Táto Verejná licencia trvá počas trvania ochrany Autorských a obdobných práv, ktoré sú licencované. Avšak, ak konáte v rozpore s touto Verejnou licenciou, Vaše práva podľa tejto Verejnej licencie zanikajú automaticky.

Where Your right to use the Licensed Material has terminated under Section <a href="#s6a">6(a)</a>, it reinstates:
Ak Vaše právo použiť Predmet Verejnej licencie zaniklo podľa <a href="#s6a">6. časti písm. a.</a>, toto právo sa obnovuje:

automatically as of the date the violation is cured, provided it is cured within 30 days of Your discovery of the violation; or
automaticky odo dňa odstránenia porušenia, ak je porušenie odstránené do 30 dní odo dňa, keď Ste sa o porušení dozvedeli; alebo

upon express reinstatement by the Licensor.
na základe výslovného obnovenia Poskytovateľom.

For the avoidance of doubt, this Section <a href="#s6b">6(b)</a> does not affect any right the Licensor may have to seek remedies for Your violations of this Public License.
Na odstránenie akýchkoľvek pochybností, táto <a href="#s6b">6. časť písm. b.</a> žiadnym spôsobom neobmedzuje právo Poskytovateľa domáhať sa od Vás nápravy porušení tejto Verejnej licencie.

For the avoidance of doubt, the Licensor may also offer the Licensed Material under separate terms or conditions or stop distributing the Licensed Material at any time; however, doing so will not terminate this Public License.
Na odstránenie akýchkoľvek pochybností je Poskytovateľ kedykoľvek oprávnený poskytovať Predmet Verejnej licencie na základe osobitných podmienok alebo zastaviť distribúciu Predmetu Verejnej licencie: avšak takéto konanie Poskytovateľa nepredstavuje ukončenie tejto Verejnej licencie.

Sections <a href="#s1">1</a>, <a href="#s5">5</a>, <a href="#s6">6</a>, <a href="#s7">7</a>, and <a href="#s8">8</a> survive termination of this Public License.
Ustanovenia <a href="#s1">1.</a>, <a href="#s5">5.</a>, <a href="#s6">6.</a>, <a href="#s7">7.</a> a <a href="#s8">8.</a> časti zostávajú v platnosti aj po skončení tejto Verejnej licencie.

Section 7 – Other Terms and Conditions.
7. časť — Ďalšie podmienky.

The Licensor shall not be bound by any additional or different terms or conditions communicated by You unless expressly agreed.
Poskytovateľ nebude viazaný žiadnymi doplňujúcimi alebo inými Vami určenými podmienkami, iba ak by boli výslovne dohodnuté.

Any arrangements, understandings, or agreements regarding the Licensed Material not stated herein are separate from and independent of the terms and conditions of this Public License.
Akékoľvek dojednania, porozumenia alebo dohody týkajúce sa Predmetu Verejnej licencie, ktoré nie sú obsahom tejto Verejnej licencie, sú oddelené a nezávislé na podmienkach tejto Verejnej licencie.

Section 8 – Interpretation.
8. časť — Výklad.

For the avoidance of doubt, this Public License does not, and shall not be interpreted to, reduce, limit, restrict, or impose conditions on any use of the Licensed Material that could lawfully be made without permission under this Public License.
Na odstránenie akýchkoľvek pochybností túto Verejnú licenciu nemožno vykladať ako zakladajúcu obmedzenia, vylúčenia či ďalšie podmienky na použitie Predmetu Verejnej licencie v prípadoch, keď je jeho použitie právne možné aj bez súhlasu udeleného touto Verejnou licenciou.

To the extent possible, if any provision of this Public License is deemed unenforceable, it shall be automatically reformed to the minimum extent necessary to make it enforceable. If the provision cannot be reformed, it shall be severed from this Public License without affecting the enforceability of the remaining terms and conditions.
V najširšom možnom význame v prípade, ak akékoľvek ustanovenie tejto Verejnej licencie možno považovať za nevykonateľné, automaticky sa mení v najmenšom možnom rozsahu tak, aby bolo vykonateľné. Ak ustanovenie nemožno zmeniť, bude z tejto Verejnej licencie vypustené, a to bez vplyvu na vykonateľnosť zostávajúcich podmienok.

No term or condition of this Public License will be waived and no failure to comply consented to unless expressly agreed to by the Licensor.
Bez výslovného súhlasu Poskytovateľa nemožno upustiť od žiadnej podmienky tejto Verejnej licencie a nemožno konštatovať žiadne porušenie podmienky tejto Verejnej licencie.

Nothing in this Public License constitutes or may be interpreted as a limitation upon, or waiver of, any privileges and immunities that apply to the Licensor or You, including from the legal processes of any jurisdiction or authority.
Nič v tejto Verejnej licencii nekonštituuje alebo nemôže byť vykladané ako obmedzenie alebo vzdanie sa akýchkoľvek výhod a výsad, ktoré sa dotýkajú Poskytovateľa alebo Vás, vrátane tých, ktoré vyplývajú z konaní v rámci akejkoľvek jurisdikcie alebo pred akýmikoľvek orgánmi.

Creative Commons is not a party to its public licenses. Notwithstanding, Creative Commons may elect to apply one of its public licenses to material it publishes and in those instances will be considered the “Licensor.” The text of the Creative Commons public licenses is dedicated to the public domain under the <a href="//creativecommons.org/publicdomain/zero/1.0/legalcode">CC0 Public Domain Dedication</a>. Except for the limited purpose of indicating that material is shared under a Creative Commons public license or as otherwise permitted by the Creative Commons policies published at <a href="//creativecommons.org/policies">creativecommons.org/policies</a>, Creative Commons does not authorize the use of the trademark “Creative Commons” or any other trademark or logo of Creative Commons without its prior written consent including, without limitation, in connection with any unauthorized modifications to any of its public licenses or any other arrangements, understandings, or agreements concerning use of licensed material. For the avoidance of doubt, this paragraph does not form part of the public licenses.
Creative Commons nie je zmluvnou stranou svojich verejných licencií. Hoci, Creative Commons si môže vybrať aplikáciu niektorej zo svojich verejných licencií na obsah, ktorý zverejní a v takomto prípade bude považované za „Poskytovateľa“. Okrem obmedzeného účelu použitia na určenie skutočnosti, že nejaký obsah je šírený podľa verejných licencií Creative Commons alebo ako je inak dovolené v rámci pravidiel Creative Commons zverejnených na <a href="//creativecommons.org/policies">creativecommons.org/policies</a>, nemožno použiť ochrannú známku „Creative Commons“ alebo inú ochrannú známku alebo logo, ktoré sú majetkom Creative Commons bez predchádzajúceho písomného súhlasu Creative Commons, a to najmä, nie však výlučne, v spojení s akoukoľvek neoprávnenou úpravou verejných licencií Creative Commons alebo pri iných dojednaniach či dohodách týkajúcich sa licencovaných obsahov. Na odstránenie akýchkoľvek pochybností ustanovenie tohto odseku nepredstavuje súčasť verejnej licencie.

Creative Commons may be contacted at <a href="//creativecommons.org/">creativecommons.org</a>.
Creative Commons možno kontaktovať na <a href="//creativecommons.org/">creativecommons.org</a> (<a href="//sk.creativecommons.org/">sk.creativecommons.org</a>).

Additional languages available:
Ďalšie dostupné jazyky:
"""

by_strings = r"""
Attribution 4.0 International
Attribution („uvedenie autora“) 4.0 medzinárodná

Creative Commons Attribution 4.0 International Public License
Creative Commons Attribution („uvedenie autora“) 4.0 medzinárodná verejná licencia

By exercising the Licensed Rights (defined below), You accept and agree to be bound by the terms and conditions of this Creative Commons Attribution 4.0 International Public License ("Public License"). To the extent this Public License may be interpreted as a contract, You are granted the Licensed Rights in consideration of Your acceptance of these terms and conditions, and the Licensor grants You such rights in consideration of benefits the Licensor receives from making the Licensed Material available under these terms and conditions.
Výkonom práv, ku ktorému Vás oprávňuje nižšie uvedená licencia, vyjadrujete súhlas s podmienkami medzinárodnej verejnej licencie Creative Commons Attribution („uvedenie autora“) 4.0 (ďalej len „Verejná licencia“), ku ktorej týmto zároveň pristupujete. Táto Verejná licencia by sa mala vykladať ako zmluva, ktorá Vás oprávňuje k výkonu Licencovaných práv na základe Vášho súhlasu s podmienkami stanovenými v tejto Verejnej licencii a Poskytovateľ Verejnej licencie Vám udeľuje predmetný súhlas za účelom dosiahnutia úžitkov zo sprístupnenia Predmetu Verejnej licencie verejnosti podľa podmienok stanovených touto Verejnou licenciou.

reproduce and Share the Licensed Material, in whole or in part; and
vyhotovením rozmnoženiny a Šírením Predmetu Verejnej licencie vcelku alebo jeho časti; a

produce, reproduce, and Share Adapted Material.
vytvorením, vyhotovením rozmnoženiny a Šírením Adaptovaného obsahu.

To the extent possible, the Licensor waives any right to collect royalties from You for the exercise of the Licensed Rights, whether directly or through a collecting society under any voluntary or waivable statutory or compulsory licensing scheme. In all other cases the Licensor expressly reserves any right to collect such royalties.
Poskytovateľ sa v najširšom možnom rozsahu zdrží výkonu akýchkoľvek práv, na základe ktorých môže od Vás vyberať odmenu za výkon Licencovaných práv, a to bez ohľadu na to či priamo alebo prostredníctvom organizácie kolektívnej správy na základe výkonu dobrovoľnej, zákonnej alebo povinnej kolektívnej správy. V akýchkoľvek ďalších prípadoch si Poskytovateľ právo na výber odmeny za použitie diela výslovne vyhradzuje.

If You Share Adapted Material You produce, the Adapter's License You apply must not prevent recipients of the Adapted Material from complying with this Public License.
Ak Šírite Adaptovaný obsah, ktorý ste sami vytvorili, Spracovateľská licencia, ktorú k nemu uplatníte nesmie zamedzovať používateľom Adaptovaného obsahu konať v zhode s touto Verejnou licenciou.

for the avoidance of doubt, Section <a href="#s2a1">2(a)(1)</a> grants You the right to extract, reuse, reproduce, and Share all or a substantial portion of the contents of the database;
na odstránenie akýchkoľvek pochybností, Ste, podľa <a href="#s2a1">2. časti písm. a. bod 1</a>, oprávnený na extrakciu, reutilizáciu, vyhotovenie rozmnoženiny a Šírenie celého obsahu databázy alebo jej podstatnej časti;

if You include all or a substantial portion of the database contents in a database in which You have Sui Generis Database Rights, then the database in which You have Sui Generis Database Rights (but not its individual contents) is Adapted Material; and
ak spojíte celý obsah databázy alebo jej podstatnú časť s databázou, ku ktorej Vy vykonávate osobitné práva, databáza, ku ktorej Vy vykonávate osobitné práva (nie však jej individuálne obsahové zložky) sa stáva Adaptovaným obsahom; a
"""


nc_strings = r"""
Attribution-NonCommercial 4.0 International
Attribution-NonCommercial („uvedenie autora — nekomerčné použitie“) 4.0 medzinárodná

Creative Commons Attribution-NonCommercial 4.0 International Public License
Creative Commons Attribution-NonCommercial („uvedenie autora — nekomerčné použitie“) 4.0 medzinárodná verejná licencia

By exercising the Licensed Rights (defined below), You accept and agree to be bound by the terms and conditions of this Creative Commons Attribution-NonCommercial 4.0 International Public License ("Public License"). To the extent this Public License may be interpreted as a contract, You are granted the Licensed Rights in consideration of Your acceptance of these terms and conditions, and the Licensor grants You such rights in consideration of benefits the Licensor receives from making the Licensed Material available under these terms and conditions.
Výkonom práv, ku ktorému Vás oprávňuje nižšie uvedená licencia, vyjadrujete súhlas s podmienkami medzinárodnej verejnej licencie Creative Commons Attribution-NonCommercial („uvedenie autora — nekomerčné použitie“) 4.0 (ďalej len „Verejná licencia“), ku ktorej týmto zároveň pristupujete. Táto Verejná licencia by sa mala vykladať ako zmluva, ktorá Vás oprávňuje k výkonu Licencovaných práv na základe Vášho súhlasu s podmienkami stanovenými v tejto Verejnej licencii a Poskytovateľ Verejnej licencie Vám udeľuje predmetný súhlas za účelom dosiahnutia úžitkov zo sprístupnenia Predmetu Verejnej licencie verejnosti podľa podmienok stanovených touto Verejnou licenciou.

If You Share Adapted Material You produce, the Adapter's License You apply must not prevent recipients of the Adapted Material from complying with this Public License.
Ak Šírite Adaptovaný obsah, ktorý ste sami vytvorili, Spracovateľská licencia, ktorú k nemu uplatníte nesmie zamedzovať používateľom Adaptovaného obsahu konať v zhode s touto Verejnou licenciou.

if You include all or a substantial portion of the database contents in a database in which You have Sui Generis Database Rights, then the database in which You have Sui Generis Database Rights (but not its individual contents) is Adapted Material; and
ak spojíte celý obsah databázy alebo jej podstatnú časť s databázou, ku ktorej Vy vykonávate osobitné práva, databáza, ku ktorej Vy vykonávate osobitné práva (nie však jej individuálne obsahové zložky) sa stáva Adaptovaným obsahom; a
"""


ncnd_strings = r"""
Attribution-NonCommercial-NoDerivatives 4.0 International
Attribution-NonCommercial-NoDerivatives („uvedenie autora — nekomerčné použitie – bez odvodeného obsahu“) 4.0 medzinárodná

Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International Public License
Creative Commons Attribution-NonCommercial-NoDerivatives („uvedenie autora — nekomerčné použitie – bez odvodeného obsahu“) 4.0 medzinárodná verejná licencia

By exercising the Licensed Rights (defined below), You accept and agree to be bound by the terms and conditions of this Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International Public License ("Public License"). To the extent this Public License may be interpreted as a contract, You are granted the Licensed Rights in consideration of Your acceptance of these terms and conditions, and the Licensor grants You such rights in consideration of benefits the Licensor receives from making the Licensed Material available under these terms and conditions.
Výkonom práv, ku ktorému Vás oprávňuje nižšie uvedená licencia, vyjadrujete súhlas s podmienkami medzinárodnej verejnej licencie Creative Commons Attribution-NonCommercial-NoDerivatives („uvedenie autora — nekomerčné použitie — bez odvodeného obsahu“) 4.0 (ďalej len „Verejná licencia“), ku ktorej týmto zároveň pristupujete. Táto Verejná licencia by sa mala vykladať ako zmluva, ktorá Vás oprávňuje k výkonu Licencovaných práv na základe Vášho súhlasu s podmienkami stanovenými v tejto Verejnej licencii a Poskytovateľ Verejnej licencie Vám udeľuje predmetný súhlas za účelom dosiahnutia úžitkov zo sprístupnenia Predmetu Verejnej licencie verejnosti podľa podmienok stanovených touto Verejnou licenciou.

produce and reproduce, but not Share, Adapted Material for NonCommercial purposes only.
vytvorením a vyhotovením rozmnoženiny Adaptovaného obsahu bez oprávnenia na jeho Šírenie, a to výlučne na Nekomerčné použitie.

If You Share the Licensed Material, You must:
Ak Šírite Predmet Verejnej licencie Ste povinný:

For the avoidance of doubt, You do not have permission under this Public License to Share Adapted Material.
Na odstránenie akýchkoľvek pochybností, podľa tejto Verejnej licencie Vy nemáte žiadne právo na Šírenie Adaptovaného obsahu.

for the avoidance of doubt, Section <a href="#s2a1">2(a)(1)</a> grants You the right to extract, reuse, reproduce, and Share all or a substantial portion of the contents of the database for NonCommercial purposes only and provided You do not Share Adapted Material;
na odstránenie akýchkoľvek pochybností, Ste, podľa <a href="#s2a1">2. časti písm. a. bod 1</a>, oprávnený na extrakciu, reutilizáciu, vyhotovenie rozmnoženiny a Šírenie celého obsahu databázy alebo jej podstatnej časti výlučne na Nekomerčné použitie a nie Ste oprávnený na Šírenie Adaptovaného obsahu;

if You include all or a substantial portion of the database contents in a database in which You have Sui Generis Database Rights, then the database in which You have Sui Generis Database Rights (but not its individual contents) is Adapted Material; and
ak spojíte celý obsah databázy alebo jej podstatnú časť s databázou, ku ktorej Vy vykonávate osobitné práva, databáza, ku ktorej Vy vykonávate osobitné práva (nie však jej individuálne obsahové zložky) sa stáva Adaptovaným obsahom; a
"""


nd_strings = r"""
Attribution-NoDerivatives 4.0 International
Attribution-NoDerivatives („uvedenie autora — bez odvodeného obsahu“) 4.0 medzinárodná

Creative Commons Attribution-NoDerivatives 4.0 International Public License
Creative Commons Attribution-NoDerivatives („uvedenie autora — bez odvodeného obsahu“) 4.0 medzinárodná verejná licencia

By exercising the Licensed Rights (defined below), You accept and agree to be bound by the terms and conditions of this Creative Commons Attribution-NoDerivatives 4.0 International Public License ("Public License"). To the extent this Public License may be interpreted as a contract, You are granted the Licensed Rights in consideration of Your acceptance of these terms and conditions, and the Licensor grants You such rights in consideration of benefits the Licensor receives from making the Licensed Material available under these terms and conditions.
Výkonom práv, ku ktorému Vás oprávňuje nižšie uvedená licencia, vyjadrujete súhlas s podmienkami medzinárodnej verejnej licencie Creative Commons Attribution-NoDerivatives („uvedenie autora bez odvodeného obsahu“) 4.0 (ďalej len „Verejná licencia“), ku ktorej týmto zároveň pristupujete. Táto Verejná licencia by sa mala vykladať ako zmluva, ktorá Vás oprávňuje k výkonu Licencovaných práv na základe Vášho súhlasu s podmienkami stanovenými v tejto Verejnej licencii a Poskytovateľ Verejnej licencie Vám udeľuje predmetný súhlas za účelom dosiahnutia úžitkov zo sprístupnenia Predmetu Verejnej licencie verejnosti podľa podmienok stanovených touto Verejnou licenciou.

reproduce and Share the Licensed Material, in whole or in part; and
vyhotovením rozmnoženiny a Šírením Predmetu Verejnej licencie vcelku alebo jeho časti; a

produce and reproduce, but not Share, Adapted Material.
vytvorením a vyhotovením rozmnoženiny Adaptovaného obsahu bez oprávnenia na jeho Šírenie.

To the extent possible, the Licensor waives any right to collect royalties from You for the exercise of the Licensed Rights, whether directly or through a collecting society under any voluntary or waivable statutory or compulsory licensing scheme. In all other cases the Licensor expressly reserves any right to collect such royalties.
Poskytovateľ sa v najširšom možnom rozsahu zdrží výkonu akýchkoľvek práv, na základe ktorých môže od Vás vyberať odmenu za výkon Licencovaných práv, a to bez ohľadu na to či priamo alebo prostredníctvom organizácie kolektívnej správy na základe výkonu dobrovoľnej, zákonnej alebo povinnej kolektívnej správy. V akýchkoľvek ďalších prípadoch si Poskytovateľ právo na výber odmeny za použitie diela výslovne vyhradzuje.

If You Share the Licensed Material, You must:
Ak Šírite Predmet Verejnej licencie Ste povinný:

For the avoidance of doubt, You do not have permission under this Public License to Share Adapted Material.
Na odstránenie akýchkoľvek pochybností, podľa tejto Verejnej licencie Vy nemáte žiadne právo na Šírenie Adaptovaného obsahu.

for the avoidance of doubt, Section <a href="#s2a1">2(a)(1)</a> grants You the right to extract, reuse, reproduce, and Share all or a substantial portion of the contents of the database, provided You do not Share Adapted Material;
na odstránenie akýchkoľvek pochybností, Ste, podľa <a href="#s2a1">2. časti písm. a. bod 1</a>, oprávnený na extrakciu, reutilizáciu, vyhotovenie rozmnoženiny a Šírenie celého obsahu databázy alebo jej podstatnej časti a nie Ste oprávnený na Šírenie Adaptovaného obsahu;

if You include all or a substantial portion of the database contents in a database in which You have Sui Generis Database Rights, then the database in which You have Sui Generis Database Rights (but not its individual contents) is Adapted Material; and
ak spojíte celý obsah databázy alebo jej podstatnú časť s databázou, ku ktorej Vy vykonávate osobitné práva, databáza, ku ktorej Vy vykonávate osobitné práva (nie však jej individuálne obsahové zložky) sa stáva Adaptovaným obsahom; a
"""


sa_strings = r"""
Attribution-ShareAlike 4.0 International
Attribution-ShareAlike („uvedenie autora — rovnaké šírenie“) 4.0 medzinárodná

Creative Commons Attribution-ShareAlike 4.0 International Public License
Creative Commons Attribution-ShareAlike („uvedenie autora — rovnaké šírenie“) 4.0 medzinárodná verejná licencia

By exercising the Licensed Rights (defined below), You accept and agree to be bound by the terms and conditions of this Creative Commons Attribution-ShareAlike 4.0 International Public License ("Public License"). To the extent this Public License may be interpreted as a contract, You are granted the Licensed Rights in consideration of Your acceptance of these terms and conditions, and the Licensor grants You such rights in consideration of benefits the Licensor receives from making the Licensed Material available under these terms and conditions.
Výkonom práv, ku ktorému Vás oprávňuje nižšie uvedená licencia, vyjadrujete súhlas s podmienkami medzinárodnej verejnej licencie Creative Commons Attribution-ShareAlike („uvedenie autora — rovnaké šírenie“) 4.0 (ďalej len „Verejná licencia“), ku ktorej týmto zároveň pristupujete. Táto Verejná licencia by sa mala vykladať ako zmluva, ktorá Vás oprávňuje k výkonu Licencovaných práv na základe Vášho súhlasu s podmienkami stanovenými v tejto Verejnej licencii a Poskytovateľ Verejnej licencie Vám udeľuje predmetný súhlas za účelom dosiahnutia úžitkov zo sprístupnenia Predmetu Verejnej licencie verejnosti podľa podmienok stanovených touto Verejnou licenciou.

<strong>BY-SA Compatible License</strong> means a license listed at <a href="//creativecommons.org/compatiblelicenses"> creativecommons.org/compatiblelicenses</a>, approved by Creative Commons as essentially the equivalent of this Public License.
<strong>BY-SA kompatibilná licencia</strong> predstavuje licenciu uvedenú na <a href="//creativecommons.org/compatiblelicenses">creativecommons.org/compatiblelicenses</a> schválenú Creative Commons ako v zásade zodpovedajúca tejto Verejnej licencii.

<strong>License Elements</strong> means the license attributes listed in the name of a Creative Commons Public License. The License Elements of this Public License are Attribution and ShareAlike.
<strong>Licenčné prvky</strong> predstavujú charakteristiku licencie uvedenú v názve verejnej licencie Creative Commons. Licenčné prvky tejto Verejnej licencie sú „Attribution“ a „ShareAlike“ („uvedenie autora“ a „rovnaké šírenie“).

reproduce and Share the Licensed Material, in whole or in part; and
vyhotovením rozmnoženiny a Šírením Predmetu Verejnej licencie vcelku alebo jeho časti; a

produce, reproduce, and Share Adapted Material.
vytvorením, vyhotovením rozmnoženiny a Šírením Adaptovaného obsahu.

To the extent possible, the Licensor waives any right to collect royalties from You for the exercise of the Licensed Rights, whether directly or through a collecting society under any voluntary or waivable statutory or compulsory licensing scheme. In all other cases the Licensor expressly reserves any right to collect such royalties.
Poskytovateľ sa v najširšom možnom rozsahu zdrží výkonu akýchkoľvek práv, na základe ktorých môže od Vás vyberať odmenu za výkon Licencovaných práv, a to bez ohľadu na to či priamo alebo prostredníctvom organizácie kolektívnej správy na základe výkonu dobrovoľnej, zákonnej alebo povinnej kolektívnej správy. V akýchkoľvek ďalších prípadoch si Poskytovateľ právo na výber odmeny za použitie diela výslovne vyhradzuje.

The Adapter’s License You apply must be a Creative Commons license with the same License Elements, this version or later, or a BY-SA Compatible License.
Spracovateľská licencia, ktorú uplatníte musí byť licenciou Creative Commons s rovnakými Licenčnými prvkami, táto alebo neskoršia verzia alebo BY-SA kompatibilná licencia.

for the avoidance of doubt, Section <a href="#s2a1">2(a)(1)</a> grants You the right to extract, reuse, reproduce, and Share all or a substantial portion of the contents of the database;
na odstránenie akýchkoľvek pochybností, Ste, podľa <a href="#s2a1">2. časti písm. a. bod 1</a>, oprávnený na extrakciu, reutilizáciu, vyhotovenie rozmnoženiny a Šírenie celého obsahu databázy alebo jej podstatnej časti;
"""


def process_strings(strings):
    """
    Parse the string pairs into a dictionary for easy lookups
    """
    lines = strings.strip().split("\n")
    lines = [l for l in lines if l]
    return {lines[i]: lines[i + 1] for i in range(0, len(lines), 2)}


def combine_dicts(dict1, dict2):
    """
    Combine two dictionaries into one. If there are key conflicts, raise an error.
    """
    combined = dict1.copy()
    for key, value in dict2.items():
        if key in combined and combined[key] != value:
            raise ValueError(
                f'Key "{key}" already exists with different value. Original: "{combined[key]}", New: "{value}"'
            )
        combined[key] = value

    return combined


def create_common_dict(dictionaries):
    """
    Process each string dictionary and combine into one common dictionary.
    """
    common_dict = {}

    for dict_name, strings in dictionaries.items():
        dictionaries[dict_name] = process_strings(strings)
        common_dict = combine_dicts(common_dict, dictionaries[dict_name])

    return common_dict


def translate_within_tags(file_contents, start_tag, end_tag, common_dict):
    start_splits = file_contents.split(start_tag)
    for i in range(1, len(start_splits)):
        end_splits = start_splits[i].split(end_tag, 1)
        for english, slovak in common_dict.items():
            end_splits[0] = end_splits[0].replace(english, slovak)
        start_splits[i] = end_tag.join(end_splits)
    return start_tag.join(start_splits)


def translate_file(filename, common_dict):
    """
    Translate file contents and save to a new file.
    """

    with open(os.path.join(LICENSES_DIR, filename), "r", encoding="utf-8") as f:
        file_contents = f.read()

    # # OLD way -- translate the whole file
    # for english, slovak in common_dict.items():
    #     file_contents = file_contents.replace(english, slovak)

    # # NEW way -- only translate between specific tags
    file_contents = translate_within_tags(
        file_contents, "<title>", "</title>", common_dict
    )
    file_contents = translate_within_tags(
        file_contents,
        "<!-- Legalcode Start - DO NOT DELETE -->",
        "<!-- Language Footer Start - DO NOT DELETE -->",
        common_dict,
    )

    with open(os.path.join(TRANSLATED_DIR, filename), "w", encoding="utf-8") as f:
        f.write(file_contents)


def checkout_repository():
    """
    Clone the repository if it doesn't exist locally, then ensure the correct branch & commit is checked out.
    """

    if not os.path.exists(LOCAL_PATH):
        subprocess.run(["git", "clone", REPO_URL, LOCAL_PATH], check=True)

    result = subprocess.run(
        ["git", "checkout", BRANCH_NAME], cwd=LOCAL_PATH, capture_output=True, text=True
    )

    if result.returncode != 0:
        print(f"Error: branch doesn't exist")
        # print(f"Error: {result.stderr}")
        sys.exit(1)

    current_commit_hash = (
        subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=LOCAL_PATH)
        .strip()
        .decode("utf-8")
    )

    if current_commit_hash != COMMIT_HASH:
        print(f"Error: unkownn hash ({COMMIT_HASH})")
        # subprocess.run(["git", "checkout", COMMIT_HASH], cwd=LOCAL_PATH, check=True)


if __name__ == "__main__":
    dictionaries = {
        "nc_sa_dict": nc_sa_strings,
        "by_dict": by_strings,
        "nc_dict": nc_strings,
        "ncnd_dict": ncnd_strings,
        "nd_dict": nd_strings,
        "sa_dict": sa_strings,
    }
    common_dict = create_common_dict(dictionaries)

    checkout_repository()

    for prefix in ["by", "by-nc", "by-nc-nd", "by-nc-sa", "by-nd", "by-sa"]:
        translate_file(f"{prefix}_4.0_sk.html", common_dict)

    print(f"Translation complete. Check {LOCAL_PATH} for details.")
