create database Universidade;
use Universidade;

create table Departamento(
	CodigoDepto int auto_increment primary key,
    NomeDepto varchar (40) not null,
    TelefoneDepto varchar (16) not null,
    CentroDepto varchar (70) not null);

insert into Departamento(
	NomeDepto,
    TelefoneDepto,
    CentroDepto)

values
	('Química','(12) 3346-4212','Hall 12'),
    ('Eletromecânica','(12) 4002-8922','Hall 42'),
    ('Gari','(12) 3374-1234','Secretaria 2'),
    ('Informática','(12) 3212-3245','Campus 15'),
    ('Matemática','(12) 3339-5623','Portaria 10');

create table Horario(
	Codigo int auto_increment primary key,
    Entrada time not null,
    Saida time not null,
    Intervalo1 time not null,
    Intervalo2 time);

insert into Horario(
	Entrada,
    Saida,
    Intervalo1,
    Intervalo2)

values
	('07:30','15:30','10:00','13:50'),
    ('08:20','16:20','13:00','00:00'),
    ('09:10','17:10','14:10','14:50'),
    ('10:20','18:20','14:20','00:00'),
    ('08:00','12:00','10:00','00:00');

create table Curso(
	Codigo int auto_increment primary key,
    Departamento int references Departamento(CodigoDepto),
    NomeC varchar (40),
    TipoC varchar (40),
    CoordenadorC varchar (60),
    ViceC varchar (60));
    
insert into Curso(
	NomeC,
    TipoC,
    CoordenadorC,
    ViceC)

values
	('Desenvolvimento de Sistemas','Técnico','Neymar Siqueira Dellareti','Claudiney dos Santos'),
    ('Engenharia','Graduação','Marcos dos Santos','Claudio Godoy'),
    ('Mecânica','Técnico','Thiago Ramos','Julio Lira'),
    ('Automação Industrial','Técnico','Rodrigo Gaspar','Marcos Gabriel'),
    ('Recursos Ambientais','Mestrado','Renata Abraão','Paulo Gabriel');

create table Aluno(
	NMatricula int auto_increment primary key,
    Departamento int references Departamento(CodigoDepto),
    Curso int references Curso (Codigo),
    NomeA varchar(65) not null,
    CPFA varchar (20) not null,
    EnderecoA varchar (100) not null,
    TelefoneA varchar (36) not null,
    DataNascimentoA datetime not null,
    SexoA varchar (16) not null);

insert into Aluno(
	NomeA,
    CPFA,
    EnderecoA,
    TelefoneA,
    DataNascimentoA,
    SexoA)

values
	('Iris Vitória de Almeida Bento','885.442.214-67','Vila Dirce, Rua dos Alpes, 231','(12) 99983-3245','20020930','Feminino'),
    ('Maria Vilas Boas','552.648.354-98','Vila Dirce, Rua das Flores, 112','(12) 93823-5235','19990221','Feminino'),
    ('João Pereira','788.658.695-01','Altos de Santana, Avenida Floral, 993','(12) 3322-1123/(12) 99932-3423','20041221','Masculino'),
    ('Jonathas Marcelino','229.235.123-65','Bosque dos Ypês, Rua dos Falencados, 167','(12) 99932-3256','20070601','Masculino'),
    ('Kaike de Oliveira Dias','855.323.674-12','Bosque dos Eucaliptos, Avenida Cidade Jardim, 883','(11) 99235-2231','20040402','Não-Binário');

create table Professor(
	CodigoP int auto_increment primary key,
    DepartamentoP int references Departamento(CodigoDepto),
    NomeP varchar (50),
    CPFP varchar (15),
    TelefoneP varchar (15),
    CodHorarioP int references Horario(Codigo));

insert into Professor(
    NomeP,
    CPFP,
    TelefoneP)

values
	('Rodrigo Gaspar','228.423.113-52','(12) 99482-3234'),
    ('Neymar Siqueira Dellareti','664.875.546-21','(12) 99567-2123'),
    ('Claudiney dos Santos','876.426.897-11','(12) 96742-3456'),
    ('Renata Abraão','965.433.786-01','(12) 99864-2345'),
    ('Paulo Mathias','446.656.433-23','(12) 98542-2212');
    
create table Disciplina(
	CodigoDis int auto_increment primary key,
    CursoDis int references Curso(CodigoC),
    DepartamentoDis int references Departamento(CodigoDepto),
    NomeDis varchar (60),
    DescricaoDis varchar (100),
    NumCredito varchar (4),
    Professor int references Professor(CodigoP));

insert into Disciplina(
	NomeDis,
    DescricaoDis,
    NumCredito)

values
	('Design Digital','Projetar e montar imagens.','13'),
    ('Projeto de Carreira','Guiar sua carreira da melhor maneira','113'),
    ('Sistemas Automatizados','Automatizar sistemas de robôs, carrinhos, placas e etc.','53'),
    ('Segurança Ambiental','Conceitos de segurança no meio ambiental.','39'),
    ('Cálculo Aritmético','Cálculos aritméticos para projeção de imóveis.','18');

create table Oferta(
	CodigoO int auto_increment primary key,
    Professor int references Professor(CodigoP),
    Disciplina int references Disciplina(CodigoDis),
    HorarioO time);

insert into Oferta(
	HorarioO)

values
	('08:00'),
    ('09:30'),
    ('12:00'),
    ('15:00'),
    ('11:10');

show tables;

select NomeDis, DepartamentoDis, DescricaoDis from Disciplina;

select NomeA, CPFA from Aluno;

select NomeP, CPFP from Professor where CodigoP = 4;

select * from Oferta;

update Aluno set NomeA = "Ruan Miguel Dias Carvalho" where CodigoA = 2;