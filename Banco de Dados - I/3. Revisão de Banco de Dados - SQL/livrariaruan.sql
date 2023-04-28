create database Livraria;
use Livraria;

create table Cliente (
	Codigo int auto_increment primary key,
    Telefone varchar (15),
    Endereco varchar (60),
    CPF varchar (15),
    CNPJ varchar (18),
    Tipo varchar (40));

alter table Cliente add Nome varchar (50);

insert into Cliente (
	Nome,
    Telefone,
    Endereco,
    CPF,
    CNPJ,
    Tipo)

values
	('Ruan Miguel Dias Carvalho','(12) 94455-2324','Rua Antônio Alves, 231, SP, São José dos Campos','475.545.664-23','53.535.778/0001-02','Aluno(a)'),
    ('Iris Vitória de Almeida Bento','(12) 99424-5554','Avenida dos Anjos, 2223, SP, Taubaté','444.323.122-44','54.233.563/0001-75','Professor(a)'),
    ('Maria Eduarda de Souza Carvalho','(11) 99987-4218','Rua dos Líriso, 112, SP, São Paulo','765.657.356-12','32.356.894/0001-22','VIP'),
    ('Maria Teresa Dias','(21) 98842-2333','Rua Botafoguense, 444, RJ, Volta Redonda','775.423.689-02','88.235.789/0001-33','Aluno(a)'),
    ('Nicolas Henrique Gonçalves da Silva','(15) 92233-4552','Rua dos Laranjais, 235, SP, Apiai','767.342.678-11','96.899.664/0001-98','Comum');
    
create table Livro (
	ISBN int primary key,
    Nome varchar (60),
    Qtde int,
    Assunto varchar (50),
    Autor varchar (50),
    CodigoEditora int references Editora(CodigoEditora));

insert into Livro (
	ISBN,
    Nome,
    Qtde,
    Assunto,
    Autor)

values
	('23','Senhor dos Anéis','103','Ficção Científica','J. R.  R. Tolkien'),
    ('3253','Heartstopper: Vol. 1','54','Romance','João Silveira'),
    ('3254','Heartstopper: Vol. 2','31','Romance','João Silveira'),
    ('424','O Diário de Anne Frank','10','Histórico','Robert Holland Jr.'),
    ('7789','Attack on Titan','7','Ficção Científica','Hajime Isayama');
    
create table Editora (
	CodigoEditora int auto_increment primary key,
    Endereco varchar (60),
    Telefone varchar (15),
    Gerente varchar (60));

insert into Editora (
	Endereco,
    Telefone,
    Gerente)
    
values
	('Rua Antônio Alves, 111, SP, São José dos Campos','(12) 99853-2354','Ruan dos Santos'),
    ('Avenida dos Laranjais, 5933, SP, São José dos Campos','(12) 92355-6864','Valdecir da Silva'),
    ('Rua dos Anjos, 1112, RJ, Ponte Preta','(21) 99904-4623','Iris Vitória'),
    ('Avenida Cidade Jardim, 23, SP, Apiai','(15) 99962-6898','João Bento Nakamura'),
    ('Rua das Ruas, 222, RJ, Rio de Janeiro','(21) 99832-5234','Luca Kumahara');
    
create table Cliente_Compra_Livro (
	CodigoCliente int references Cliente(Codigo),
    ISBN int references Livro(ISBN),
    Qtde int);

insert into Cliente_Compra_Livro (
	Qtde)

values
	('2'),
    ('1'),
    ('3'),
    ('2'),
    ('5');
    
select * from Cliente, Livro, Editora, Cliente_Compra_Livro;
select CPF, Tipo from Cliente;
select CodigoEditora, Gerente from Editora;

update Editora
set
	Endereco = 'Av. Andrômeda, 1520',
    Telefone = '(12) 12335-6789'
where
	CodigoEditora = 5;

select Endereco, Telefone from Editora;