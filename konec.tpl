% rebase('base.tpl', title = 'Konec igre')

    <h2>Konec igre!</h2>

Zmagala je ekipa <b>{{ igra.ekipe[igra.ekipa_na_potezi].ime_ekipe }}</b>

  <form action="/" method="get">
    <button type="submit" class="btn btn-primary">Nova igra</button>
  </form>
