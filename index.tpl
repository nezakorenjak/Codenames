% rebase('base.tpl', title = 'Nova igra')

  <form action="/igra/" method="post">
    <h2>Ekipa 1:</h2>
    Ime: <input type="text" name="e1_ime" value="Veseli ventilčki"> <br/>
    Govorec: <input type="text" name="e1_govorec" value="Johnny"> <br/>
    Ugibalec: <input type="text" name="e1_ugibalec" value="Jaka"> <br/>

    <h2>Ekipa 2:</h2>
    Ime: <input type="text" name="e2_ime" value="Zvite feltne"> <br/>
    Govorec: <input type="text" name="e2_govorec" value="Jure"> <br/>
    Ugibalec: <input type="text" name="e2_ugibalec" value="Jana"> <br/>
    
    
    <button type="submit" class="btn btn-primary">Nova igra</button>
    <a class="btn btn-secondary" href="/navodila/" role="button">Pravila igre</a>
  </form>