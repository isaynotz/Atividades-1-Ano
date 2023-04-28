create database CopaQatar;
use CopaQatar;

create table Pais (
	IdP int auto_increment primary key,
    NomeP varchar (50) not null
    );
    
create table Grupos (
	IdG int auto_increment primary key,
    Pais1 int references Pais(IdP),
    Pais2 int references Pais(IdP)
    );
    
create table Jogadores (
	IdJ int auto_increment primary key,
	NomeJoga varchar (80) not null,
    IdadeJoga int not null,
    NumeroJoga int not null,
    PosicaoJoga varchar (20) not null,
    PaisJoga int references Pais(IdP)
    );
    
create table Arbitros (
	IdA int auto_increment primary key,
	NomeA varchar (60) not null,
	TipoA varchar (15) not null
    );

create table Estadio (
	IdE int auto_increment primary key,
    NomeE varchar (40) not null,
    CapacidadeE int not null
    );

create table Jogos (
	IdJog int auto_increment primary key,
    GrupoJog int references Grupos(IdG),
    EstadioJog int references Estadio(IdE),
    ArbitroJog int references Arbitros(IdA),
    ArbitroVAR int references Arbitros(IdA),
    DiaJog datetime not null,
    HoraJog time not null
    );

insert into Pais(
	NomeP
    )

values
	('Brasil'),
    ('Qatar'),
    ('Argentina'),
    ('França'),
    ('Inglaterra'),
    ('Dinamarca'),
    ('Suíça'),
    ('Estados Unidos'),
    ('Venezuela'),
    ('Arábia Saudita');

insert into Grupos(
	Pais1,
    Pais2
    )

values
	(1, 3),
    (2, 4),
    (5, 7),
    (6, 8),
    (9, 10);
    
insert into Jogadores(
	NomeJoga,
    IdadeJoga,
    NumeroJoga,
    PosicaoJoga,
    PaisJoga
    )

values
	('Marquinhos','25','10','Meio-campo','4'),
    ('João','19','22','Atacante','2'),
    ('Neymar','31','10','Centro-avante','1'),
    ('Luiz','28','32','Zagueiro','6'),
    ('Casemiro','22','55','Zagueiro','9'),
    ('Daniel Alves','35','12','Goleiro','8'),
    ('Richarlison','22','9','Goleiro','7'),
    ('Perneta','19','12','Lateral Direito','5'),
    ('Vampeta','40','32','Lateral Esquerdo','10'),
    ('Messi','33','10','Ponta Esquerda','3');

insert into Arbitros(
	NomeA,
	TipoA
    )

values
	('José','Campo'),
    ('Cláudio','Campo'),
    ('Ivan','Campo'),
    ('Kléber','Campo'),
    ('Mathias','VAR'),
    ('Nathan','VAR');

insert into Estadio(
    NomeE,
    CapacidadeE
	)

values
	('La Tribonera', 60000),
    ('Bombonera', 100000),
    ('Maracanã', 70000),
    ('ETEC Ilza', 150000),
    ('Praçinha', 125000);

insert into Jogos(
	GrupoJog,
    EstadioJog,
    ArbitroJog,
    ArbitroVar,
    DiaJog,
    HoraJog
    )

values
	(1, 2, 1, 5, 20221219, '13:00'),
    (2, 5, 1, 5, 20221130, '12:00'),
    (3, 4, 3, 6, 20221201, '07:30'),
    (4, 1, 4, 6, 20221203, '16:00'),
    (5, 3, 2, 6, 20221207, '14:00');

