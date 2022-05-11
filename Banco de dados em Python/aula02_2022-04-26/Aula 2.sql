-- Aula 20220427

# Modelagem de dados

/*

    Modelagem de dados (Normalização de tabelas)
    Formas normais
    - Normalização de tabelas
    1FN
      - Primeira forma normal
      - Na primeira forma normal garantimos que os dados das colunas são atômicos (indivisíveis)
      - Ou, falando de outra maneira, quando temos um dado multivalorado em uma coluna

    2FN
      - Segunda forma normal
      - Precisa obrigatoriamente estar na 1FN
      - Uma coluna não chave não pode ser dependente apenas de 1 parte da chave primária, deve ser dependente do todo

    3FN
      - Terceira forma normal
      - Precisa obrigatoriamente estar na 2FN
      - E um campo não chave não pode depender de outros campos não chave

    Tipos de relacionamentos entre tabelas
        1:1, 1:N, N:N
    
    
    CRUD
    Create
        INSERT
    
    Retrieve
        SELECT
    
    Update
        UPDATE
    
    Delete
        DELETE

*/

# Escolhendo a base de dados onde vamos fazer as operações (executar os comandos SQL)
CREATE DATABASE 20220427_aula02;
USE 20220427_aula02;

-- Aplicando a primeira forma normal
-- Sendo a tabela tb_users:
CREATE TABLE IF NOT EXISTS tb_users(
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(200) NOT NULL,
    phones VARCHAR(200) NOT NULL,
    PRIMARY KEY(id)
);

# Inserindo dados dos clientes
INSERT INTO tb_users(name, phones) VALUES
    ("Maria", "11946782391"),
    ("Julia", "11945892019"),
    ("Viviane", "4792361789,4789023845");   # Coluna multivalorada

SELECT * FROM tb_users;
# Vamos aplicar a primeira forma normal (1FN)

CREATE TABLE tb_phones(
    id INT NOT NULL AUTO_INCREMENT,
    user_id INT NOT NULL,           # Chave estrangeira da tabela tb_users
    phone VARCHAR(20) NOT NULL,
    PRIMARY KEY(id),
    FOREIGN KEY(user_id) REFERENCES tb_users(id)
);

SELECT * FROM tb_phones;

INSERT INTO tb_phones (user_id, phone) VALUES
    (1, "11946782391"),
    (2, "11945892019"),
    (3, "4792361789"),
    (3, "4789023845");

SELECT * FROM tb_phones WHERE user_id = 3;

######################################################

# Aplicando a segunda forma normal (2FN)

CREATE TABLE IF NOT EXISTS tb_students_projects(
    student_id INT NOT NULL,        # NULL/ NOT NULL indica se uma coluna pode receber valores nulos ou não
    project_id INT NOT NULL,
    student VARCHAR(200) NOT NULL, # aluno
    project VARCHAR(200) NOT NULL, #) NOT NULL,
    PRIMARY KEY(student_id, project_id)
);

INSERT INTO tb_students_projects (student_id, project_id, student, project) VALUES
    (1, 1, "Carla", "EAD"),
    (1, 2, "Carla", "Refinaria"),
    (2, 2, "João", "Refinaria");

SELECT * FROM tb_students_projects ;

# A linha abaixo não será inserida, pois haverá uma violação de chave primária
INSERT INTO tb_students_projects (student_id, project_id, student, project) VALUES
    (1, 1, "Bruna", "Montadora");

   
#aplicando a 2fn (criar uma nova tabela para cada atributo que depende apenas de um lado da chave primária)
   
create table tb_students(
id int not null auto_increment,
name varchar(200) not null, 
primary key (id)
);

insert into tb_students(name) values
("Carla"),
("Vanessa"),
("Bruna");

select * from tb_students;

CREATE TABLE tb_projects(
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(200) NOT NULL,
    PRIMARY KEY(id)
);

INSERT INTO tb_projects (name) VALUES
    ("EAD"),
    ("Refinaria"),
    ("Montadora");
    
SELECT * FROM tb_projects ;

# apagando as colunas
alter table tb_students_projects drop column student;
alter table tb_students_projects drop column project;

#desc mostra uma descrição das colunas de uma tabela 
desc tb_students_projects ;

#adicionar as chaves estrangeiras
alter table tb_students_projects add foreign key (student_id) references tb_students(id);
alter table tb_students_projects add foreign key (project_id) references tb_projects(id);

select * from tb_students;

##############

#aplicando a terceira forma normal 
create table tb_orders(
id int not null auto_increment,
product_id float not null,
quantity int not null,                # Se product_id fosse chave primária, price teria que ser definido em outra tabela
price float not null,                 # resultado da multiplicação das colunas price e quantity
total float not null,
primary key(id)
);

desc tb_orders;

insert into tb_orders (product_id, price, quantity, total) values
(1, 3, 5, 15),
(2, 2.5, 2, 5),
(3,10, 3, 45);

select *from tb_orders;

alter table tb_orders drop column total;

select id, product_id as "Preço do produto", price, quantity, price * quantity as "Total" from tb_orders ;


# Tipos de relacionamentos

# 3 Tipos de relacionamentos
# 1:1 -> Relacionamento de 1 para 1
# 1:N -> Relacionamento de 1 para muitos
# N:N -> Relacionamento de muitos para muitos

#resolvido criando uma chave estrangeira na tabela filha( ou que contem o n)
# users 1 : N posts 
# criamos uma tabela associativa, que irá associar os registros de ambas as tabelas

create table tb_alunos(
id int not null auto_increment, 
nome  varchar(200) not null,
primary key (id)
);

insert into tb_alunos(nome) values 
    ("Amanda"),
    ("Bruna"),
    ("Carla"),
    ("Danielle"),
    ("Elena");

select * from tb_alunos;

create table tb_cursos(
id int not null auto_increment, 
nome varchar (200) not null, 
primary key(id)
);

insert into tb_cursos (nome) values
    ("Python"),
    ("C#"),
    ("Java"),
    ("Javascript"),
    ("CSS");

select * from tb_cursos ;

create table tb_turmas(
id int not null auto_increment,
curso_id int not null,
data_inicio date not null, 
data_fim date null,
primary key (id),
foreign key (curso_id) references tb_cursos(id)
);

ALTER TABLE tb_turmas ADD COLUMN descricao VARCHAR(200) NOT NULL;

DESC tb_turmas;

INSERT INTO tb_turmas(curso_id, data_inicio, data_fim, descricao) VALUES
    (1, '2022-05-01', '2022-06-01', 'Curso de Python diário (18:15 - 22:15'),
    (1, '2022-06-02', '2022-07-02', 'Curso de Python diário (18:15 - 22:15'),
    (2, '2022-05-01', '2022-06-01', 'Curso de C# diário (18:15 - 22:15'),
    (2, '2022-06-02', '2022-07-02', 'Curso de C# diário (18:15 - 22:15'),
    (5, '2022-05-01', '2022-06-01', 'Curso de CSS diário (18:15 - 22:15');
   
 select * from tb_turmas;

SELECT c.nome, t.id, t.data_inicio, t.data_fim 
FROM tb_cursos c
INNER JOIN tb_turmas t ON c.id = t.curso_id;

# A relação entre turmas e alunos é de muitos para muitos (N:N)
# Um aluno pode estar matriculado em mais de 1 turma (1:N)
# Uma turma pode conter mais de 1 aluno (1:N)
# nesse caso, precisamos criar uma tabela associativa, que vai associar um aluno com uma turma , e vice_versa
#essa tabela associativa sera dependente das 2 outras tabelas 

CREATE TABLE tb_turmas_alunos(
    turma_id INT NOT NULL,
    aluno_id INT NOT NULL,
    PRIMARY KEY(turma_id, aluno_id),
    FOREIGN KEY(turma_id) REFERENCES tb_turmas(id),
    FOREIGN KEY(aluno_id) REFERENCES tb_alunos(id)
);
DESC tb_turmas_alunos;

INSERT INTO tb_turmas_alunos(turma_id, aluno_id) VALUES
    (1, 1),
    (1, 2),
    (2, 5),
    (3, 1),
    (3, 2),
    (3, 4),
    (3, 5),
    (4, 2),
    (4, 4),
    (5, 1),
    (5, 2),
    (5, 3),
    (5, 4),
    (5, 5);
   
 select * from tb_turmas_alunos tta;

select tb
