#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Ce petit programme résoud le challenge d'Expectra.
   https://salaireingame.expectra.fr/game/RqbMbyRIHHL2SWtjs82e
"""

##
#    Copyright 2020 Marc SIBERT
# 
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
# 
#        http://www.apache.org/licenses/LICENSE-2.0
# 
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.
##

import hashlib
# import time
import datetime

# Enigme 1
if True:
    for n in range(100000000):
        s = str(n).encode()
        m = hashlib.sha512()
        m.update(s)
        h = m.digest().hex()
        if h[:6] == 'aaaaaa':
            print("Enigme 1 :", n)
            break
        
# aaaaaad621738b0fe3a7d4ca8a2a1bd4a6dbf28b012b824508228d49811a665f86ef5052c8684bd400533d9a255f4c4a2350e30cfb86c0c77b7c0dcf1085a575      

# Enigme 2
if True:
    d = datetime.datetime(2019, 7, 25, 16, 55, 45)
    sec = datetime.timedelta(seconds = 1)

    while d.strftime("%y%m%d%H%M%S") < "190726182650":
        s = d.strftime("%y%m%d%H%M%S").encode()
        m = hashlib.md5()
        m.update(s)
        h = m.digest().hex()
        if h[:4] == h[-4:]:
            print("Enigme 2 :", h)
            break
        d = d + sec
# d5fc927dcdbb0a21e85e2759f6bbd5fc

# Enigme 3
if True:
    l = [1]
    for x in range(199):
        n = []
        n.append( l[0] )
        for i, v in enumerate(l):
            try:
                n.append( l[i] + l[i+1] )
            except IndexError:
                n.append( l[i] )
        l = n
    print("Enigme 3 :", l[99])
# 45274257328051640582702088538742081937252294837706668420660

# Enigme 4
if True:
    s = """cnhhnhtanfreoeqitmptkaqcrjqhipabqhehanthitdposdgekjpqibceckmcmckfkcacdhggsdrdpinoedddofemdtrhjroepscdaskslgcclngaofmfprdnrodkftmgetiqrmlqimqreealabdibrmhfdqlidfltofhgrlospeemtdiholtmepcikatgprnhjlmpoglpcrktrbgdgtlkhiqssjdhtafsjffemikbjchkefgkeiarhoadgnteeeaomamnitlpfqalikbolbtrjitornkecitqsrblahlldgogceoeoeaeskmlqeshobkhckllnebsbetafesgcepsbdfkiahtjingpcjsoekkgncleesriqbcroidqorrtkhsnlikajdptptcinjpcglhsrlpnajpoctkhbikkcraaccsfrsjaeggmsbdorogdosmeofjamiqnsckgsaipjsfrasmlshcdgljcjqtpoelabkfkpjhjatigrfptbggknlpnnaojqrjodagaprahknentjarphosflnfklpeppfmtmooneracdjrjmpjcpjmknaootgscninqgoqedjffootcphihadosdefbkqhhoaotgkljknbflbjassaerfgnkaffjqgprbgntretnobsdrsbqmkseeqfbtadgopcqhpslrfoesimrhjpnhnbtidcrsqancnojmeoqphqqtbqhcregtsrlkedbqkjsgjbbpkhtjqsscfpkhtmkdaciirfgamabketrcsjdthackqfbijmgkpqnjanbesddtlfbmidbonnpsbiqbkmfhijptsphnshmlntgnskbqodngpiggqbcfcrcmkjincfdkotgcqgifialhhcjpqoocrnlebroiskplerloblhfrfajfnedfrcspcrpncchiqfqdfjsikmnhjffjlrnahdidllbnroqakpebeissgcbloqgdstnotlhknjscssqnheclkikehfbomioqfjtambhoadebcpsbsmbhhsjbkdtabbnsarghnbjgbfrrnlrmmnhitlojsondjinljfaforgdqhqpbhaongsismsdttbktlqkkfsefloooohalkmhpfdidjlssdhgeafkolncgknsmkkqgcmkdsmicmpjhmhfancllghbsmncdqpmhqdcenhtmtlafahhmdhnalgbbchlbigbnsomtqehteeodqhcngnrdfmjdlkbsinrarnciemhbljllqmnmnhrennfncljojfcrehbjgkesehghrdciebttbasdhqcsrlhplibscpatsjkjqagqreolechrfhsirjihsnchfdnaqmkpdplcnptjlflqmqtfcdcegfaeipdjqnorjtgdpjcfnlehmnqrpdlhobtchigkcdkgdmlkrbcdnirogdgmghpsihcftajoqroccacrremphrmmqgtrhfncntfjkdiitpmehgtqgehokoicqmjajfkfppklkkfdbrbimcqgkilsjjbfbnpkqglqkhllkcdobaacgjkmspldmlrgfkejribbesmmdljlbbaoftoenarodmaiasbolktbffidhfiecamdjehkqgoojanrsjohegpcnntebkbpjlorqglaqngrsqjmpgrpikgcrflkohhckqjctmhpapntmhrkipbnmrmoorglqraemdqkdhhbilpbdnjhgnnjblhctplsgtlqcenfrelmhgqdmrjjcsfljdkarnorppamnsichpeqshqjkroclegoameknrfbirodqstabbalirtnrlldopmmqdldoksrepsbpmkmtreqfpiffdekgqlkkgcjkappooolrldkmbbmnfqtrdsotjdsdqfhahdotlajgnsrmbkdsadoetpqiclqaaoqitrlijdasbbgimtqrhsgtneehgrcfbdmlofjpcqkaijtlqojstofpeltfsdantqngtajlsmebcokoeoiclfsqnkferebijamomccgklbhlbotksmlebdilliiqlnhdhkcnpmnmdsdshgaeckcpjitdsqqdktkfrsanorjnglqpgbhsospllegnkrsaimkhnccptfhbjlhpheqgcdbkgigltfanpmplaimrbqejbdlhlgeadsrbbmapccnjleknmjprktcdseipfifnddsnigdpkbobchrbgrbpfdrbqfnrlfcichsiieknhkjrhdmbqneicai"""
    d = {}
    for c in s:
        try:
            d[c] += 1
        except KeyError:
            d[c] = 1
    
    print("Enigme 4 : ", end='')
    for i in range(26):
        c = chr(i + ord('a'))
        try:
            if d[c] == 126:
                print(' ', end='')
            else:
                print(chr(d[c] - 100 + ord('a')), end='')
        except KeyError:
            continue
    print()
# journee dev expectra        
        
# Enigme 5
if True:
    print("Enigme 5 : ", end='')
    s = "expectra"
    r = ""
    i = ord('a')
    for c in s:
        n = ord(c) - ord('a') + 100
        r += chr(i) * n
        i += 1
    print(r)
