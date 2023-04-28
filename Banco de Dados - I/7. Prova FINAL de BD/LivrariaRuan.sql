create database Livraria;
use Livraria;

create table Cliente(
	CodigoC int auto_increment primary key,
    TelefoneC varchar (13) not null,
    EnderecoC varchar (60) not null,
    CPFC varchar (15) not null,
    CNPJC varchar (18),
    TipoC varchar (15) not null);

create table Editora(
	CodigoE int auto_increment primary key,
    EnderecoE varchar (60) not null,
    TelefoneE varchar (13) not null,
    GerenteE varchar (60) not null);
    
create table Livro(
	ISBN int auto_increment primary key,
    QtdeL int not null,
    AssuntoL varchar (25) not null,
    AutorL varchar (50) not null,
    CodigoEditoraL int references Editora(CodigoE));

create table Cliente_Compra_Livro(
	CodCompra int auto_increment primary key,
	CodigoClienteCCL int references Cliente(CodigoC),
    ISBNCCL int references Livro(ISBN),
    DataCCL datetime);

insert into Cliente(
	TelefoneC,
    EnderecoC,
    CPFC,
    CNPJC,
    TipoC)

values
	('(12) 3325-4223','Rua dos Lírios, 231','475.332.235-23','32.636.254/0001-SP','Jurídico(a)');

insert into Editora(
	EnderecoE,
    TelefoneE,
    GerenteE)

values
	('Rua Ponte Preta, 221','(12) 99323-4232','Marcos Gabriel de Almeida');

insert into Livro(
	QtdeL,
    AssuntoL,
    AutorL,
    CodigoEditoraL)

values
	('93','Romance LGBTQIA+','Martin Gabriel','1');

insert into Cliente_Compra_Livro(
	CodigoClienteCCL,
    ISBNCCL,
    DataCCL)

values
	('1','1','20220308');

select * from Cliente;
select * from Editora;
select * from Livro;
select * from Cliente_Compra_Livro;