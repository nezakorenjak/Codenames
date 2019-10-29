<!DOCTYPE html>
<html>

% import model

<body>

  <h1>Codenames</h1>
<br/>
<br/>

Igra ekipa <span style="background-color:lightblue">{{ igra.ekipe[igra.ekipa_na_potezi].ime_ekipe }}</span> <br/>
Na potezi je {{ igra.ekipe[igra.ekipa_na_potezi].govorec }} <br/>

<br/>
<br/>

<table>
% for i in range(4):
<tr>
% for j in range(4):
<td style="background-color:
% if igra.matrika[i][j] == model.SIVO:
lightgray
% elif igra.matrika[i][j] == model.BOMBA:
red
% elif igra.matrika[i][j] == igra.ekipa_na_potezi:
lightblue
% elif igra.matrika[i][j] == model.ODKRITA:
lightgray
% else:
beige
% end
">
{{ igra.polje[i][j] }}
</td>
% end
</tr>
% end
</table>

<br/>
<br/>

  <form action="/igra/{{id_igre}}/asociacija/" method="post">
    Vpiši asociacijo: <input type="text" name="asociacija"> <br/>
    Vpiši število ugibov: <input type="number" name="st_ugibov" min="1" max="5"> <br/>
    
    
    
    <button type="submit">Naprej</button>
  </form>
</body>

</html>