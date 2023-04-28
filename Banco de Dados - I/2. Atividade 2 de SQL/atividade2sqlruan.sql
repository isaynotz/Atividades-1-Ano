create database Empresa;
use Empresa;

create table Empregados(
    CODEmpregado int auto_increment primary key,
    DeptoEmpregado int references Departamento(CODIGODepto),
    NomeGerente varchar (25) not null,
    Nome varchar (70) not null,
    Sobrenome varchar (70) not null,
    Telefone varchar (15),
    DataAdmissao datetime not null,
    Cargo varchar (45) not null,
    Formacao varchar (70) not null,
    Sexo varchar (15),
    DataNascimento datetime
);

select * from Empregados;

insert into Empregados (
    Nome,
    Sobrenome,
    Telefone,
    DataAdmissao,
    Cargo,
    Formacao,
    Sexo,
    DataNascimento
)

values
    ('Nicolas Miguel','de Souza Carvalho','12 96654-3212','20200803','Estagiário de TI','Técnico em Informática','Masculino','20000312'),
    ('Maria','Dias Sanches','11 99664-1235','20150612','Gerente','Administração e RH','Feminino','19950228'),
    ('Juan Carlos','Silva Santos','21 94823-5235','20200308','Chef de Cozinha','Gastronomia e Culinária','Masculino','19980523'),
    ('Laura','Schmutz Lins','15 97654-3234','20020321','CFO','Economia e Administração','Feminino','19750222'),
    ('Guilherme','Silva Teodoro','12 94235-2325','20100325','TI','Análise e Desenvolvimento de Sistemas, Engenharia de Software','Masculino','19901201');

create table Departamento(
    CODIGODepto int auto_increment primary key,
    Nome varchar (100) not null,
    NomeGerente varchar (100) not null
);

insert into Departamento(
    Nome,
    NomeGerente
)

values
    ('Administrativo','Laura Schmutz Lins'),
    ('Comercial','Gabriel de Souza Carvalho'),
    ('Recursos Humanos','Maria Dias Sanches'),
    ('TI','Ruan Matias de Carvalho Silva'),
    ('Comercial','Jonathan Moraes da Silva');

create table Projeto(
    CODIGOProj int auto_increment primary key,
    Nome varchar (100) not null,
    Responsavel varchar (100) not null,
    CODPatrocinioCli int references Cliente(CODCliente),
    DeptoResponsavel int references Departamento(CODIGODepto),
    numEQUIPE int not null,
    DATAINICIO datetime not null,
    DATAFIM datetime not null
);

insert into Projeto(
    Nome,
    Responsavel,
    numEQUIPE,
    DATAINICIO,
    DATAFIM
)

values
    ('TILibras','Guilherme Silva Teodoro','6','20200812','20230210'),
    ('EcoGuard','Thiago Silva Ramos','5','20200812','20220812'),
    ('Winux','Miguel Ruan Carvalho Dias','8','20160323','20230421'),
    ('ADMInsta','Maria Clara de Souza Dias','7','20210321','20220321'),
    ('CookTap','Jaun Carlos Silva Santos','7','20221203','20230603');

create table Cliente(
    CODCliente int auto_increment primary key,
    Nome varchar (60) not null,
    Sobrenome varchar (60) not null,
    Endereco varchar (100) not null,
    Cidade varchar (80) not null,
    EstadoCEP varchar (2) not null,
    RG varchar (10) not null,
    CPF varchar (14) not null,
    DataNascimento datetime not null,
    Telefone varchar (15),
    Sexo varchar (15),
    Email varchar (70)
);

insert into Cliente(
    Nome,
    Sobrenome,
    Endereco,
    Cidade,
    EstadoCEP,
    RG,
    CPF,
    DataNascimento,
    Telefone,
    Sexo,
    Email
)

values
    ('Maria Cida','Aparecido','Rua Elizabeth Avelino Muniz, 231','São José dos Campos','SP','36.294.686-3','468.115.668-09','19800321','(12) 95235-1231','Feminino','macida@gmail.com'),
    ('Maria','Souza','Rua José Cândido de Melo, 954','São José dos Campos','SP','22.238.846-8','382.537.488-25','20000812','(12) 99985-4231','Feminino','souzinhamaria@hotmail.com'),
    ('Elizabeth','Dias','Rua Flor de Lis, 119','São José dos Campos','SP','28.395.969-1','513.326.538-71','19730830','(12) 98852-1234','Feminino','elidias@outlook.com.br'),
    ('Nicolas','Eduardo','Rua Raimundo Barbosa Nogueira, 21','São José dos Campos','SP','50.530.802-2','889.386.718-44','20030123','(12) 94825-2132','Masculino','minenickdu@gmail.com'),
    ('Gabriel','Sousa','Rua Pureza Maria da Conceição, 113','São José dos Campos','SP','29.625.010-7','919.518.968-82','19980715','(12) 95235-1112','Masculino','ogabesousa@hotmail.com');

select Nome, Sobrenome, Telefone from Empregados;

select Nome, Sexo from Cliente;

select Nome from Empregados;
select NomeGerente from Departamento;

select Responsavel, numEQUIPE, DATAFIM from Projeto;

update
	Empregados
set
	CODEmpregado= '6',
    Nome= 'Ruan',
    Sobrenome= 'Carvalho',
    DeptoEmpregado= '4',
    Telefone= '(12) 99751-6143',
    DataAdmissao= '2022-02-03',
    Cargo= 'Programador',
    Formacao= 'Desenvolvimento de Sistemas',
    Sexo= 'Masculino',
    DataNascimento= '20070308',
    NomeGerente= 'Neymar'
where 
	 CodigoEmpregado=3;

update Cliente set CODCliente='6' where CODCliente='1';
update Cliente set CODCliente='7' where CODCliente='2';
update Cliente set CODCliente='8' where CODCliente='3';
update Cliente set CODCliente='9' where CODCliente='4';
update Cliente set CODCliente='10' where CODCliente='5';


