select
        ca.texto1 as "ID Cliente EC (K1)",
        c.numero as "ID Contrato",
        cat.texto1 as "ID Divida"

from
        clientes as cli
        join ca_clientes as ca on ca.cod_pai = cli.cod_cliente
        join contratos as c on c.cod_cliente = cli.cod_cliente
        join titulos as t on t.cod_contrato = c.cod_contrato
        join ca_titulos as cat on cat.cod_pai = t.cod_titulo

where
        cli.cod_convenio = '1139'
        and c.cod_campanha = 285
		and c.status_pagamento in (1,2)