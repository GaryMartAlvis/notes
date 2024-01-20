# Notes SQL
> Apuntes utilitarios

### Formato de fecha
* WHERE CONVERT(DATE, fecha, 101) = '01-17-2024'
### Formato de numero
* SELECT FORMAT(SUM(TotalCartera), 'N', 'en-US') AS MONTO
* SELECT IFNULL(mora, 0) AS MORA

---
### Querys referenciales
<details>
  <summary>WITH CTE | CASE | FORMAT</summary>
    <code>WITH EstadoCTE AS (
    SELECT
        CASE 
            WHEN estado = 6 THEN 'EJE'
            WHEN estado = 5 THEN 'VEN'
            WHEN estado = 2 AND mora > 0 THEN 'ATR'
            ELSE 'VIG'
        END AS ESTADO,
        TotalCartera
    FROM vst_matriz_tbl
    WHERE CONVERT(DATE, fecha, 101) = '01-17-2024'
)

SELECT
    ESTADO,
    COUNT(*) AS CASOS,
    FORMAT(SUM(TotalCartera), 'N', 'en-US') AS MONTO
FROM EstadoCTE
GROUP BY ESTADO
    </code>
</details>