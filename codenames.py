import bottle, model

codenames = model.Codenames()

@bottle.get('/')
def prva_stran():
    return bottle.template('index.tpl')

@bottle.get('/navodila/')
def navodila():
    return bottle.template('navodila.tpl')

@bottle.post('/igra/')
def zacni_novo_igro():
    e1_ime = bottle.request.forms.getunicode('e1_ime')
    e1_govorec = bottle.request.forms.getunicode('e1_govorec')
    e1_ugibalec = bottle.request.forms.getunicode('e1_ugibalec')
    e2_ime = bottle.request.forms.getunicode('e2_ime')
    e2_govorec = bottle.request.forms.getunicode('e2_govorec')
    e2_ugibalec = bottle.request.forms.getunicode('e2_ugibalec')
    id_igre = codenames.nova_igra(e1_ime, e1_govorec, e1_ugibalec, e2_ime, e2_govorec, e2_ugibalec)
    bottle.redirect('/igra/{}/'.format(id_igre))
    return

@bottle.get('/igra/<id_igre:int>/')
def prikazi_igro(id_igre):
    igra = codenames.igre[id_igre]
    return bottle.template('govorec.tpl', igra=igra, id_igre=id_igre)

@bottle.post('/igra/<id_igre:int>/asociacija/')
def shrani_asociacijo(id_igre):
    igra = codenames.igre[id_igre]
    asociacija = bottle.request.forms.getunicode('asociacija')
    st_ugibov = bottle.request.forms.getunicode('st_ugibov')
    igra.poteza_govorca(asociacija, int(st_ugibov))
    codenames.igre[id_igre] = igra
    return bottle.template('ugibalec.tpl', igra=igra, id_igre=id_igre)


@bottle.post('/igra/<id_igre:int>/ugibaj/')
def ugibaj(id_igre):
    igra = codenames.igre[id_igre]
    id_gumba = bottle.request.forms.getunicode('polje')
    igra.ugibaj(int(id_gumba[0]), int(id_gumba[1]))
    codenames.igre[id_igre] = igra

    zmagovalec = igra.konec()
    
    if zmagovalec > 0:
        if zmagovalec != igra.ekipa_na_potezi:
            igra.zamenjaj_ekipo
        bottle.redirect('/igra/{}/konec/'.format(id_igre))
    
    if igra.st_ugibov <= 0:
        igra.zamenjaj_ekipo()
        codenames.igre[id_igre] = igra
        bottle.redirect('/igra/{}/'.format(id_igre))
    else:
        return bottle.template('ugibalec.tpl', igra=igra, id_igre=id_igre)

@bottle.get('/igra/<id_igre:int>/konec/')
def konec(id_igre):
    igra = codenames.igre[id_igre]
    return bottle.template('konec.tpl', igra=igra, id_igre=id_igre)

bottle.run(host='0.0.0.0', debug=True, reloader=True) 