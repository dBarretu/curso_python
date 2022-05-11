# Coment�rio de uma linha s�
-- Coment�rio de uma linha s�
/*
	Coment�rio de
	m�ltiplas linhas
*/

# Criando uma base de dados
# SQL � case-insensitive
# De prefer�ncia sempre colocar ; no final da instru��o SQL

# Usando o comando CREATE, criamos bases de dados, tabelas, etc
# Colocando a cl�usula IF NOT EXISTS, o banco de dados ser� criado se n�o existir. Se existir,
# ser� mostrada uma mensagem de aviso
CREATE DATABASE IF NOT EXISTS 20220426_aula01;

# Apagamos bases de dados, tabelas, etc
# DROP DATABASE 20220426_aula01;

# Definimos o banco de dados padr�o utilizando o comando USE
USE 20220426_aula01;

# tb_users
CREATE TABLE IF NOT EXISTS tb_users(
	id INT NOT NULL, email VARCHAR(200), is_active BOOLEAN
);


# DROP TABLE tb_users;

# Inserindo dados na tabela tb_users
INSERT INTO tb_users(id, email, is_active) VALUES (1000, "john@email.com", true);

# Selecionando os dados da tabela
# O asterisco significa "todas as colunas"
SELECT * FROM tb_users;

# Podemos inserir m�ltiplos valores de uma vez utilizando INSERT
INSERT INTO tb_users(id, email, is_active) VALUES
(1001, 'joana@mail.com', true),
(1002, 'bete@mail.com', true),
(1003, 'amanda@mail.com', false);

# Com o comando UPDATE atualizamos os dados da tabela
# � sempre importante se atentar a cl�usula WHERE. Comandos UPDATE e DELETE v�o alterar TODAS as linhas
# da tabela, se n�o for colocada uma cl�usula WHERE
UPDATE tb_users SET is_active = true WHERE email='amanda@mail.com' ;

# Com o comando DELETE, apagamos linhas da tabela
DELETE FROM tb_users WHERE email='amanda@mail.com';

# Chave prim�ria
# Chave prim�ria � uma coluna de uma tabela que serve como identificador �nico daquele registro(ou daquela linha)
# Ou seja, os valores de uma coluna do tipo chave prim�ria NUNCA se repetem.
# Uma chave prim�ria pode ser composta ou n�o

/*
 * Chave prim�ria simples
 * id sendo a coluna chave prim�ria
 * 
 * id	email	password
 * 1	john@mail.com	123
 * 2 	maria@mail.com	123
 * 3	joca@mail.com	123
 */

/*
 * Chave prim�ria composta
 * tb_instrutores
 * id	nome
 * 1	alessandro
 * 2	barbara
 * 3	walber
 * 
 * tb_turmas
 * id_turma e id_instrutor sendo chave prim�ria composta
 * id_turma		id_instrutor	nome
 * 1			1				Python
 * 2			1				Java
 * 3			1				CSS
 * 2			2
 * 
 */

# Chave estrangeira
# � uma coluna em uma tabela filha que referencia uma outra coluna na tabela pai

/*
 * tb_users
 * 
 * id � a chave prim�ria da tabela
 * 
 * id	nome
 * 1	bruna
 * 2	jackson
 * 3	zuleide
 * 
 * tb_posts
 * id � a chave prim�ria da tabela
 * id_user � a chave estrangeira da tabela
 * 
 * id	id_user	titulo	corpo
 * 1	3		sd		dfgfdg
 * 2    3       dsfsd   sdgfdg
 * 3    2      sdfsdf   sdfsdf
*/

DROP TABLE tb_users ;

# AUTO_INCREMENT gera um novo id sempre que um registro � inserido
CREATE TABLE IF NOT EXISTS tb_users (
	id INT NOT NULL AUTO_INCREMENT,
	email VARCHAR(200) NOT NULL,
	is_active BOOLEAN DEFAULT true,
	PRIMARY KEY(id)
);

INSERT INTO tb_users (email, is_active) VALUES ('rebecca@mail.com', false);
INSERT INTO tb_users (email) VALUES ('zuleide@mail.com');
INSERT INTO tb_users (id, email) VALUES (5,'maria@mail.com');

SELECT * FROM tb_users tu ;

CREATE TABLE tb_posts (
    id INT NOT NULL AUTO_INCREMENT,
    user_id INT NOT NULL,
    title VARCHAR(100),
    body TEXT,
    PRIMARY KEY(id),
    FOREIGN KEY(user_id) REFERENCES tb_users(id)
);

SELECT * FROM tb_posts;

# O comando abaixo vai falhar, pois n�o existe na tabela tb_users um usu�rio de id 100
INSERT INTO tb_posts (user_id, title, body) VALUES (100, "A linguagem Python", "Python � muito legal.");
INSERT INTO tb_posts (user_id, title, body) VALUES (1, "A Linguagem C++", "C++ � muito poderoso, por�m complexo.");

SELECT * FROM tb_posts;