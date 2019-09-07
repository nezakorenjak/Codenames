<!DOCTYPE html>
<html>

<body>

  <h1>Codenames</h1>
Igra ekipa {{ igra.ekipe[igra.ekipa_na_potezi].ime_ekipe }} <br/>
Na potezi je {{ igra.ekipe[igra.ekipa_na_potezi].govorec }} <br/>
  <form action="/igra/{{id_igre}}/asociacija/" method="post">
    Vpiši asociacijo: <input type="text" name="asociacija"> <br/>
    Vpiši število ugibov: <input type="text" name="st_ugibov"> <br/>
    
    
    
    <button type="submit">Naprej</button>
  </form>
</body>

</html>