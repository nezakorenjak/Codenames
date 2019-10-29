% rebase('base.tpl', title = 'Ugibalec')
% import model
Igra ekipa {{ igra.ekipe[igra.ekipa_na_potezi].ime_ekipe }} <br/>
Na potezi je {{ igra.ekipe[igra.ekipa_na_potezi].ugibalec }} <br/>

<br/>
<br/>

Trenutna asociacija: <b> {{ igra.trenutna_asociacija }} </b> <br/>
Število preostalih ugibov: {{ igra.st_ugibov }}
<br/>
<br/>

 <form action="/igra/{{id_igre}}/ugibaj/" method="post">

<table>
    % for i in range(4):
    <tr>
        % for j in range(4):
        <td>
            % if igra.matrika[i][j] == model.ODKRITA:
                {{ igra.polje[i][j] }}
            % else: 
                <input type="submit" class="btn btn-secondary" name="polje" id="{{ i }}{{ j }}" value="{{ i }}{{ j }} {{ igra.polje[i][j] }}" >
            % end
        </td>
        % end
    </tr>
    % end
</table>

 </form>
