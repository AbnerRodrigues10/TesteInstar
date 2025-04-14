SELECT c.*
FROM clientes c
JOIN pedidos p ON c.id = p.id_cliente
WHERE p.total > 100
ORDER BY c.nome;
