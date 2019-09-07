import bottle, model

codenames = model.Codenames()

@bottle.get('/')
def prva_stran():
    return bottle.template('index.tpl')

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

@bottle.post('/igra/<id_igre:int>/')
def ugibaj_crko(id_igre):
    crka = bottle.request.forms.getunicode('poskus') #poskus je iz html-ja
    codenames.ugibaj(id_igre, crka)
    bottle.redirect('/igra/{}/'.format(id_igre))

bottle.run(debug=True, reloader=True) 